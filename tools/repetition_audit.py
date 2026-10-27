#!/usr/bin/env python3
"""Whole-manuscript repetition audit.

Counts tracked gestures/phrases and frequent 3-5 word n-grams across all
chapters/chapter-XX/final.md files, with per-chapter counts. Writes a
markdown report. Any tracked item over the cap is flagged.
"""
import re, sys, glob, collections, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = 3

TRACKED = {
    "palm flat": r"\bpalms?\b[^.]{0,30}\bflat\b|\bflat\b[^.]{0,15}\bpalms?\b|\bhands? (?:went |lay |were |stayed )?flat\b",
    "knuckle": r"\bknuckle",
    "barometer": r"\bbarometer|\bthe glass\b",
    "hearing aid": r"hearing aid",
    "rag / smear": r"\bsmear|\brag\b",
    "cap (Russ)": r"\bcap\b",
    "squared": r"\bsquare(?:d)?\b(?! mile)",
    "right side clear": r"right side",
    "put it where": r"put it where|put (?:that|things) where|filed (?:it|that)",
    "longer than X needed": r"longer than [^.]{0,20}need",
    "the way she'd/he'd": r"\bthe way (?:she|he)'d\b",
    "didn't ask": r"didn't ask",
    "He didn't": r"\bHe didn't\b",
    "She didn't": r"\bShe didn't\b",
    "not asking": r"\bnot ask(?:ing|ed)\b",
    "stopped short / hand stopped": r"\b(?:hand|fingers?) (?:stopped|stayed)|stopped short",
    "pulse": r"\bpulse",
    "burnt coffee and wet wool": r"burnt coffee|wet wool",
    "heavier jug": r"heavier jug",
    "counted": r"\bcount(?:ed|ing)\b",
}

def chapters():
    files = sorted(glob.glob(os.path.join(ROOT, "chapters", "chapter-*", "final.md")))
    out = []
    for f in files:
        n = re.search(r"chapter-(\d+)", f).group(1)
        out.append((n, open(f, encoding="utf-8").read()))
    return out

def ngrams(text, n):
    words = re.findall(r"[A-Za-z']+", text.lower())
    return zip(*[words[i:] for i in range(n)])

STOP = set("the a an and of to in on at it he she her his was is that for with as but".split())

def main():
    chs = chapters()
    lines = ["# Repetition audit", "", f"Cap: {CAP} uses per book for a gesture or signature phrase.", ""]
    lines += ["## Tracked gestures and phrases", "", "| Item | Total | Per chapter | Flag |", "|---|---|---|---|"]
    for name, pat in TRACKED.items():
        rx = re.compile(pat, re.I)
        per = [(n, len(rx.findall(t))) for n, t in chs]
        total = sum(c for _, c in per)
        per_s = ", ".join(f"{n}:{c}" for n, c in per if c)
        flag = "OVER" if total > CAP and name not in ("He didn't", "She didn't", "counted") else ""
        lines.append(f"| {name} | {total} | {per_s} | {flag} |")
    lines += ["", "## Most repeated 4-word phrases (excluding pure stopwords)", "", "| Phrase | Count | Chapters |", "|---|---|---|"]
    cnt = collections.Counter(); where = collections.defaultdict(set)
    for n, t in chs:
        for g in ngrams(t, 4):
            if sum(w in STOP for w in g) >= 3: continue
            cnt[g] += 1; where[g].add(n)
    for g, c in cnt.most_common(60):
        if c < 3: break
        lines.append(f"| {' '.join(g)} | {c} | {', '.join(sorted(where[g]))} |")
    lines += ["", "## Scene endings (last sentence of each scene)", ""]
    for n, t in chs:
        body = re.sub(r"^#.*$", "", t, flags=re.M)
        scenes = [s.strip() for s in re.split(r"\n-{3,}\n|\n\*[^*\n]+\*\n", body) if s.strip()]
        for i, s in enumerate(scenes, 1):
            sents = re.split(r"(?<=[.!?\"”])\s+", s.strip())
            last = sents[-1] if sents else ""
            words = len(last.split())
            lines.append(f"- Ch {n} sc {i} ({words}w): {last[:140]}")
    out = os.path.join(ROOT, "reviews", "repetition-audit.md")
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(out)

if __name__ == "__main__":
    main()
