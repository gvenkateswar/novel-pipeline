#!/usr/bin/env python3
"""Whole-manuscript audit: repetition, ear, and AI-fiction tells.

Usage:
    python3 tools/audit.py books/<slug> [--through NN] [--out reviews/audit-chNN.md]

Reads books/<slug>/chapters/chapter-XX/final.md in order (through chapter NN
if given; otherwise every chapter present). Edit logs after a line of '---'
followed by '## Edit log' are stripped. Reports, per chapter and whole-book:

  1. Repetition: motifs from the bible's MOTIF LIST table (| name | pattern | cap |)
     plus any 3-5 word n-gram used 4+ times; adjectives and body-reaction words
     that recur beyond expectation.
  2. Ear: mean sentence length and spread, share of sentences <= 5 words,
     codes / numerals / all-caps strings per 1,000 words, runs of identical
     sentence openers.
  3. Tells (docs/ai-fiction-tells.md Part 5): hard-ban hits, mood-word counts,
     phrase counts, construction counts per 1,000 words against the Part 3 caps,
     and a per-scene cluster check (3+ tell groups in one scene).

Anything over cap is flagged FLAG. The tool reports; it changes nothing.
"""
import sys, re, os, glob, collections, argparse, statistics

# ---------- tells lint (from docs/ai-fiction-tells.md, Parts 2, 3, 5) ----------
HARD_BAN_WORDS = [r"\bliminal\b", r"\btapestry\b", r"\bsymphony of\b", r"\bkaleidoscope\b",
    r"\bcacophony\b", r"\blabyrinthine\b", r"\bministrations\b", r"\btestament to\b",
    r"\bunbeknownst\b", r"\blittle did\b", r"\bfor what felt like\b", r"\bthe rest, as they say\b"]
HARD_BAN_NAMES = [r"\bElara\b", r"\bElias\b", r"\bKael(en)?\b", r"\bLyra\b", r"\bSeraphina\b",
    r"\bAris\b", r"\bAmara\b", r"\bThorne\b", r"\bVance\b", r"\bVoss\b", r"\bVex\b",
    r"\bBlackwood\b", r"\bAshwood\b", r"\bAshford\b", r"\bEldoria\b", r"\bElena Vasquez\b",
    r"\bMarcus Chen\b", r"\bLena Petrova\b", r"\bAmara Okafor\b"]
ARTIFACTS = [r"<[a-zA-Z/][^>]*>", r"\bAs an AI\b", r"^Certainly[,.]", r"^Here is\b", r"font-claude"]
MOOD = ["quiet", r"humm?(ing|ed)?", r"softly?", r"still(ness)?", r"ghost(ly)?", r"echo(ed|es)?",
    "shadow", "whisper", "shimmer", "flicker", "glint", "spectral", "fragile"]
PHRASES = ["the air was thick with", "the air crackled", "hung in the air", "dust motes", "dimly lit",
    "casting long shadows", "dipped below the horizon", r"heart (hammered|pounded|thundered|pounding|hammering)",
    r"breath (she|he) (didn't|did not) know", "breath hitched", "took a deep breath", "let out a breath",
    r"shiver (ran|traced) down", "barely above a whisper", "voice trembling", "devoid of emotion", "stammered",
    "eyes never leaving", "sparkling with mischief", r"didn't reach (her|his) eyes", "something flickered",
    "something unreadable", "jaw tightened", r"knuckles (whitened|white)", "white-knuckled", "swallowed hard",
    "adam's apple", "a mix of", "profound sense of", "couldn't help but", "something shifted", "something like",
    "almost like", "not quite", "for the first time", "washed over", "crashed over", "for now, that was enough",
    "face whatever lay ahead", "only just beginning", "together, they", "calculating gaze", "predator stalking",
    "she realized", "he realized", "found herself", "found himself", "in that moment", "a wave of"]
# constructions: (name, regex, cap per 1000 words or None, per_chapter_cap or None)
CONSTRUCTIONS = [
    ("as if / as though", r"\bas (if|though)\b", 1.0, None),
    ("the way (a|the|people|someone) ...", r"\bthe way (a|an|the|people|someone|you|we)\b", None, 1),
    ("the kind of ... that", r"\bthe (kind|sort) of \w+ (that|who|which)\b", None, 2),
    ("with the (precision|care...) of someone who", r"\bwith the (precision|care|economy|deliberateness|ease|calm) of (someone|a \w+) who\b", None, 1),
    ("not because ... but because", r"\bnot because\b[^.]{0,80}\bbut because\b", None, 1),
    ("contrast construction (not X but Y / wasn't X. It was Y)", r"\b(not|wasn't|was not|isn't|is not|didn't|did not|never)\b[^.;:!?]{1,60}[,.;]\s*(but|it was|it's|it is|he was|she was)\b", 0.0, 0),
    ("sentence-initial And/But/And yet", r"(?:^|[.!?][\"”']?\s+)(And|But|And yet)\b", 3.0, None),
    ("em dashes", r"—|--", 2.0, None),
    ("semicolons", r";", 2.0, None),
    ("perception filter (she noticed / could hear)", r"\b(she|he) (noticed|could hear|could see|could feel|felt the|watched as)\b", 1.0, None),
    ("one-sentence paragraph", r"(?m)^[^\n]{1,80}[.!?]\s*$", None, None),
]
BODY_WORDS = [r"\bjaw\b", r"\bknuckles?\b", r"\bthroat\b", r"\bbreath\b", r"\bpulse\b", r"\bchest\b",
    r"\bhands? (stopped|stilled|went still|flat)\b", r"\bshoulders?\b", r"\bgaze\b", r"\btightened\b", r"\bswallowed\b"]
STOP = set("the a an and or but of to in on at for with from by as is was were be been it its he she they him her his their them this that these those i you we me my our your not no so if then than there here when where which who what how all any some one two up out into over off down back just only also very more most".split())

def strip_editlog(t):
    m = re.search(r"\n---\s*\n## Edit log", t)
    if m: t = t[:m.start()]
    m = re.search(r"\n## Edit log", t)
    if m: t = t[:m.start()]
    return t

def sentences(t):
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[\"'“”A-Z])", t) if s.strip()]

def words(t): return re.findall(r"[A-Za-z][A-Za-z'’-]*", t)

def count(pat, t, flags=re.I): return len(re.findall(pat, t, flags))

def per_k(n, w): return (n / w * 1000) if w else 0.0

def load_motifs(book):
    p = os.path.join(book, "story-bible.md")
    rows = []
    if not os.path.exists(p): return rows
    t = open(p, encoding="utf-8").read()
    m = re.search(r"## MOTIF LIST(.*?)(?:\n## |\Z)", t, re.S)
    if not m: return rows
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0].lower() not in ("name", "motif", "") and not set(cells[0]) <= set("-: "):
            try: cap = int(re.findall(r"\d+", cells[2])[0])
            except Exception: cap = 3
            rows.append((cells[0], cells[1], cap))
    return rows

def scenes_of(t):
    parts = re.split(r"\n\s*(?:\*\s*\*\s*\*|#{1,3} [^\n]*|—{3,}|-{3,}|\* \* \*)\s*\n", t)
    return [p for p in parts if len(words(p)) > 150] or [t]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book"); ap.add_argument("--through", type=int, default=None); ap.add_argument("--out", default=None)
    a = ap.parse_args()
    book = a.book.rstrip("/")
    files = sorted(glob.glob(os.path.join(book, "chapters", "chapter-*", "final.md")))
    if a.through: files = [f for f in files if int(re.search(r"chapter-(\d+)", f).group(1)) <= a.through]
    if not files: sys.exit("no final.md files found under " + book)
    chapters = []
    for f in files:
        n = re.search(r"chapter-(\d+)", f).group(1)
        chapters.append((n, strip_editlog(open(f, encoding="utf-8").read())))
    whole = "\n\n".join(t for _, t in chapters)
    W = len(words(whole))
    motifs = load_motifs(book)
    out = []
    P = out.append
    P(f"# Audit — {os.path.basename(book)} (chapters {chapters[0][0]}–{chapters[-1][0]}, {W:,} words)\n")
    P("Source: `docs/ai-fiction-tells.md` Parts 2, 3, 5 and `docs/postmortem-boring.md` C. Counts are regex and approximate; judge flagged items by function. FLAG means over cap.\n")

    # ---------- 1. Repetition ----------
    P("## 1. Repetition\n")
    if motifs:
        P("### Motif list (bible caps, whole book)\n")
        P("| Motif | " + " | ".join(n for n, _ in chapters) + " | Total | Cap | |")
        P("|---|" + "---|" * (len(chapters) + 3))
        for name, pat, cap in motifs:
            per = [count(pat, t) for _, t in chapters]; tot = sum(per)
            P(f"| {name} | " + " | ".join(str(x) for x in per) + f" | {tot} | {cap} | {'FLAG' if tot > cap else ''} |")
        P("")
    else:
        P("_No `## MOTIF LIST` table in story-bible.md; motif caps skipped. Add one (| name | regex | cap |) so this section can run._\n")
    P("### Frequent 3–5 word n-grams (4+ uses, whole book)\n")
    wl = [w.lower() for w in words(whole)]
    grams = collections.Counter()
    for n in (3, 4, 5):
        for i in range(len(wl) - n):
            g = wl[i:i + n]
            if g[0] in STOP and g[-1] in STOP: continue
            if sum(1 for x in g if x in STOP) >= n - 1: continue
            grams[" ".join(g)] += 1
    rows = [(g, c) for g, c in grams.most_common(400) if c >= 4]
    # drop sub-grams of longer grams with the same count
    keep = []
    for g, c in rows:
        if any(g != h and g in h and c == d for h, d in rows): continue
        keep.append((g, c))
    for g, c in keep[:40]: P(f"- {c}× “{g}”")
    if not keep: P("- none")
    P("")
    P("### Body-reaction words per 1,000 (tells 4.3; cluster matters, not any one)\n")
    for pat in BODY_WORDS:
        c = count(pat, whole); P(f"- {pat.strip(chr(92)+'b')}: {c} ({per_k(c, W):.1f}/1k)")
    P("")

    # ---------- 2. Ear ----------
    P("## 2. Ear (read-aloud check)\n")
    P("| Ch | Words | Mean sent. | SD | ≤5-word share | Codes/1k | Numerals/1k | ALLCAPS/1k | Max opener run | Flags |")
    P("|---|---|---|---|---|---|---|---|---|---|")
    for n, t in chapters:
        ss = sentences(t); lens = [len(words(s)) for s in ss] or [0]
        w = len(words(t)); mean = statistics.mean(lens); sd = statistics.pstdev(lens) if len(lens) > 1 else 0
        short = sum(1 for L in lens if L <= 5) / len(lens)
        codes = count(r"\b[A-Z0-9]{1,6}\s*/\s*[A-Z0-9]{1,6}(\s*/\s*[A-Z0-9]{1,6})*", t, 0)
        nums = count(r"\b\d[\d,.:]*\b", t, 0)
        caps = count(r"\b[A-Z]{3,}\b", t, 0)
        openers = [(words(s) or [""])[0].lower() for s in ss]
        run = best = 1
        for i in range(1, len(openers)):
            run = run + 1 if openers[i] == openers[i - 1] else 1; best = max(best, run)
        flags = []
        if not (13 <= mean <= 18): flags.append("mean")
        if short > 0.15: flags.append("short")
        if per_k(codes, w) > 2: flags.append("codes")
        if per_k(nums, w) > 12: flags.append("numerals")
        if per_k(caps, w) > 6: flags.append("caps")
        if best >= 4: flags.append("openers")
        P(f"| {n} | {w:,} | {mean:.1f} | {sd:.1f} | {short:.0%} | {per_k(codes, w):.1f} | {per_k(nums, w):.1f} | {per_k(caps, w):.1f} | {best} | {' '.join(flags) or ''} |")
    P("\nTargets: mean 13–18 with real spread; ≤5-word sentences under 15%; codes under 2/1k; numerals under 12/1k; all-caps under 6/1k; no four sentences in a row with the same opener.\n")

    # ---------- 3. Tells ----------
    P("## 3. AI-fiction tells\n")
    P("### Hard bans (remove outright)\n")
    hits = []
    for pat in HARD_BAN_WORDS + HARD_BAN_NAMES + ARTIFACTS:
        for n, t in chapters:
            for m in re.finditer(pat, t, re.I | re.M):
                s = t[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
                hits.append(f"- Ch {n}: `{m.group(0)}` … {s.strip()}")
    P("\n".join(hits[:60]) if hits else "- none")
    P("")
    P("### Mood words per 1,000 (count; flag a cluster, not a word)\n")
    for pat in MOOD:
        c = count(r"\b" + pat + r"\b", whole); P(f"- {pat}: {c} ({per_k(c, W):.1f}/1k)")
    P("")
    P("### Phrases (count, whole book; any 3+ is worth a look)\n")
    ph = [(p, count(r"\b" + p + r"\b", whole)) for p in PHRASES]
    for p, c in sorted(ph, key=lambda x: -x[1]):
        if c: P(f"- {c}× {p}")
    P("")
    P("### Constructions against Part 3 caps\n")
    P("| Construction | " + " | ".join(n for n, _ in chapters) + " | Total | /1k | Cap | |")
    P("|---|" + "---|" * (len(chapters) + 4))
    for name, pat, capk, capch in CONSTRUCTIONS:
        per = [count(pat, t) for _, t in chapters]; tot = sum(per); k = per_k(tot, W)
        flag = ""
        if capk is not None and k > capk: flag = "FLAG"
        if capch is not None and any(x > capch for x in per): flag = "FLAG"
        capstr = f"{capk}/1k" if capk is not None else (f"{capch}/ch" if capch is not None else "report")
        P(f"| {name} | " + " | ".join(str(x) for x in per) + f" | {tot} | {k:.1f} | {capstr} | {flag} |")
    P("")
    P("### Scene cluster check (3+ tell groups in one scene → rewrite the scene, not the sentence)\n")
    groups = {"similes": r"\b(as if|as though|like a|like the|the way (a|an|the|someone|people))\b",
              "mood": r"\b(" + "|".join(MOOD) + r")\b",
              "body": "|".join(BODY_WORDS),
              "explain": r"\b(she|he) (realized|understood|knew that|felt a|felt the)\b|\b(something|a kind of|the kind of)\b",
              "phrases": "|".join(PHRASES),
              "contrast": r"\b(not|wasn't|isn't|didn't|never)\b[^.;:!?]{1,60}[,.;]\s*(but|it was|it's)\b"}
    for n, t in chapters:
        for i, sc in enumerate(scenes_of(t), 1):
            w = len(words(sc)); present = []
            for g, pat in groups.items():
                c = count(pat, sc)
                if per_k(c, w) >= 3 or c >= 4: present.append(f"{g}({c})")
            if len(present) >= 3: P(f"- Ch {n} scene {i} ({w} words): FLAG {', '.join(present)}")
    P("")
    text = "\n".join(out)
    outp = a.out or os.path.join(book, "reviews", f"audit-ch{chapters[-1][0]}.md" if a.through else "audit-manuscript.md")
    os.makedirs(os.path.dirname(outp), exist_ok=True)
    open(outp, "w", encoding="utf-8").write(text)
    print(outp)

if __name__ == "__main__":
    main()
