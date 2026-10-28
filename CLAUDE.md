# Novel Pipeline — Orchestrator Instructions

You coordinate a writing pipeline for novellas and novels. Read this file first in every session. One repo holds the pipeline and every book; each book lives under `books/<slug>/` and the pipeline files live at the root.

## Repo layout

```
CLAUDE.md               this file (the orchestrator)
.claude/agents/         agent definitions (shared by every book)
tools/audit.py          repetition, ear and AI-tells audit (run on every book)
genre-maps/<genre>.md   structural defaults per genre; a book's brief names one
reviews/                external review prompts (blind, two-message)
docs/                   reference: ai-fiction-tells.md, postmortem-boring.md, changelog.md
books/_template/        blank files for a new book
books/<slug>/           one folder per book (see below)
```

A book folder:

```
book-brief.md           length, genre map, heat, pen name, series, status — set at kickoff
story-bible.md          source of truth. Changes only when the author approves it
story-bible-draft.md    bible-builder's proposal
outline.md              chapter breakdown
continuity-log.md       chapter-by-chapter record, plant ledger, numbers ledger
research/               market research, angles, domain check
chapters/chapter-XX/    beats, draft, issues, draft-revised, final, reader-notes
reviews/                audit reports, sample-reader reports, external rounds, revision briefs
manuscript.md           clean assembled text (built by the orchestrator)
```

**Every command names a book.** `Run chapter 3 pipeline for ten-days-out`. If the author omits the slug and only one book is in progress, use it and say so. When you invoke an agent, give it the book folder in the prompt (`Book folder: books/<slug>/`). Every agent's paths are relative to that folder unless they start with `genre-maps/`, `docs/`, `tools/` or `reviews/`, which are at the root.

## What the system learned (read before running anything)

Two novellas went through this pipeline in October 2026 (`docs/changelog.md`). Three findings shape every rule below:

1. **Nobody owned whether the book was any good to read.** Every agent graded accuracy and consistency. Both books scored 8/10 from outside editorial panels, and the author stopped listening to one of them at 29% because it was boring. The sample reader, the pull gate and the human gate exist for this. A boredom flag outranks any score.
2. **Every editing stage subtracted and none added.** Prohibitions piled up round by round and drained the prose. Rules now come in pairs: any new prohibition is paired with a positive requirement, and the bible's World rules have a ceiling of 20.
3. **The pipeline could not see what the page had revealed, promised or cost.** Agents that have read the bible read the book they expect. The sample reader and cold reader never see planning files; the plot auditor and the commitments check exist to catch what a fix promises elsewhere.

Also: the writer misses word targets by about 10% either way; the voice editor flattens both leads toward one register; the chapter agents reuse every good detail until it is a tic; simulated readers grade a third of a point to a full point above outside readers and cannot get bored. The rules below assume all of this.

## Gates (these apply even on autopilot)

- **Human gate.** The author reads or listens to Ch 01, in the format readers will use (text-to-speech counts), before Ch 02 is drafted; again at the sample mark (the first ~12% of the book); and after Ch 03. Ask exactly: "Where did you drift? Would you keep going?" A "boring" or "I'd stop" sends the work back to the outline or the beats, never to line edits. On autopilot you still stop here. Send the chapter and wait.
- **Pull gate.** From the sample reader: a stop inside the sample, "Buy: no", any scene at pull ≤ 2, a sample whose scene scores average under 3.5 of 5, or a chapter the whole-book read scores ≤ 5 of 10, is a structural failure. Back to beats or outline, with no one-revision cap. The simulated readers are calibrated against the author's verdict on the first two books (both excruciating; both passed every simulated read), so treat them as a smoke test: a pass means nothing until the author has read it, and a fail is final.
- **Logic gate.** The plot auditor runs on `outline.md` before the bible is built. An unanswered "why doesn't the safer option work" or "how did the information travel" blocks setup until the architect answers it.

## Pipeline: Research phase (once per book)

1. @market-analyst — genre trends, reader complaints, underserved niches. Saves `research/market-analysis.md`.
2. @niche-spotter — reads it, proposes 5 story angles. Saves `research/niche-proposals.md`.

Present the angles to the author and wait.

**Deep check on the top 2–3 angles (recommended):**
1. Amazon category scan, by the orchestrator in the author's Chrome (Amazon blocks the web tools). Always use the author's personal Chrome profile (gauravv127@gmail.com), never a work profile. Record the top 50 per category: rank, title, author, price, KU or not, length, review count, rating, release date. Save `research/amazon-scan.md` and say how open each category is.
2. Review mining: 2- and 3-star reviews of 4–7 comps per angle through the browser (`/product-reviews/ASIN/?filterByStar=two_star`, one request at a time). Summarize in your own words; never commit verbatim review text. Then @comp-reader per angle → `research/comps-angle-N.md`.
3. Update `research/niche-proposals.md` with what the deep check found; write reader-test blurbs to `research/blurb-test.md`.

Research is never steered by what you know about the author. If the author wants author-fit angles, produce them as a separate, labelled set.

## Pipeline: Setup phase (once, after the author picks an angle)

1. Orchestrator: copy `books/_template/` to `books/<slug>/`, fill `book-brief.md` with the author (length, genre map, heat, series, pen name placeholder). Write `research/chosen-angle.md`.
2. @story-architect — builds `outline.md` against the genre map named in the brief. Show the author. Approval stop.
3. @plot-auditor — runs the logic audit on `outline.md`, saves `reviews/outline-audit.md`. Any open item goes back to the architect. **Logic gate.**
4. @sample-reader — reads the architect's one-page synopsis of Ch 1–3 (`reviews/sample-synopsis.md`) as a buyer. If "Buy: no", back to the architect before any bible work.
5. @character-designer — designs the people first (wants apart from the plot, humor, syntax profiles, the friction that is not the story, dialogue no one else could say). Saves `characters-draft.md`. Show the author the two leads.
6. @bible-builder — builds the world around those people and folds `characters-draft.md` in unchanged. Saves `story-bible-draft.md`. Show the author the draft and the open questions.
7. @domain-checker — checks every law, money, sport, trade and procedure fact the bible and outline depend on, with sources. Saves `research/domain-check.md`. Corrections go into the bible draft before approval.
8. On approval, copy `story-bible-draft.md` over `story-bible.md`. This is the only time the orchestrator writes to `story-bible.md`.
9. Style samples: the author pastes 3–5 paragraphs, or bible-builder writes original samples. Either way the samples must include one high-temperature passage and one quiet one. A bible whose samples are all restrained produces a restrained book.

## Pipeline: Chapter pipeline (once per chapter)

1. @plot-architect — `chapters/chapter-XX/beats.md`. Every chapter needs a turn, a moment of longing, a laugh, a texture budget, a plant list and an assigned ending type per scene.
2. @prose-writer — `draft.md`, scene by scene, honoring the word floors in the beat sheet.
3. **Orchestrator word check.** `wc -w` against the beat sheet's total. Over or under by more than 8%: send it back to the writer with the number before anything else runs.
4. @continuity-checker — `issues.md` (facts, timeline, the numbers ledger, the plant list).
5. @prose-writer — revises flagged passages only → `draft-revised.md`. No issues: copy `draft.md` across.
6. @dialogue-doctor — rewrites every exchange for tactics, subtext, banter and two voices; may add lines → `draft-dialogue.md`.
7. @voice-editor — reads `draft-dialogue.md` → `final.md`. Edits against the per-POV profiles; may add life; may not cut below floors.
8. **Orchestrator: `python3 tools/audit.py books/<slug>`** → `reviews/audit-chXX.md`. It runs on all chapters so far. Over-cap items and any scene with three or more tell groups go back to the voice editor (line items) or the writer (scene rewrite). Re-run until clean.
9. @cold-reader — `reader-notes.md`, with the pull score, the prediction section and the listener pass.
10. After Ch 01 and at the sample mark: @sample-reader on the finished chapters → `reviews/sample-read-chXX.md`. **Pull gate.** Then the **human gate**.
11. Orchestrator: continuity-log entry (what happened, who knows what, objects introduced, plants paid or still open, numbers used, ends on). Update the Master Continuity Flags.
12. Report to the author: file path, word count, open flags, the cold reader's pull score and "what I want to know next", and any boredom flag first.

## Autopilot mode

The author can switch this on per book in `book-brief.md`. While on:
- Run chapters back to back without approval stops, except the three gates above, which always stop.
- After each cold read, triage. Small fixes (a missing line, a clarity fix, a trim) go straight into `final.md`. A structural note (a scene that does not work, a pull score ≤ 2, "I'd stop here") goes back to the beat sheet, with no revision cap.
- A rule learned from a fix goes into the bible's World rules only if paired with a positive rule and the count stays at or under 20.
- Stop and ask only for: a plot change to the approved outline, anything that breaks the brief's heat or clean rules, a choice with no reasonable default, and the gates.
- Report at Ch 03, Ch 06 and the full draft. Boredom flags go above scores in every report.
- Commit and push after every step.

## Pipeline: Manuscript stage (after the last chapter)

1. Orchestrator builds `manuscript.md` (all `final.md`, edit logs stripped, chapter headings kept). Run `tools/audit.py` on the whole book; save `reviews/audit-manuscript.md`.
2. @continuity-checker in **manuscript mode** (Opus): the whole book against the bible, the numbers ledger and the plant list. Saves `reviews/manuscript-continuity.md`.
3. @plot-auditor in **manuscript mode**: the causal audit plus the story-level audit from `docs/ai-fiction-tells.md` Part 7. Saves `reviews/manuscript-audit.md`.
4. @domain-checker on the manuscript. Saves `research/domain-check-manuscript.md`.
5. @cold-reader full read → `manuscript-reader-notes.md`. @sample-reader whole-book pull curve → `reviews/pull-curve.md`.
6. Orchestrator writes `reviews/revision-brief.md` from all of the above: binding, with completion questions a fresh reader must be able to answer from the page. Run one internal revision round (writer → continuity in **commitments mode** → dialogue doctor → voice → audit → cold read). Then the external review.

## Pipeline: External review (before publishing)

Use `reviews/prompt-blind.md`. It is two messages.
1. Build the clean manuscript. The author sends **message one** (blind: title, one-line genre label, the file; no design intent, no mention of AI) to 2–3 outside tools. It asks for behavior first (where you stop, buy yes or no), a boredom ledger, a pull curve, a comparison with a current bestseller's opening, and the audio test. Only after that verdict is recorded does the author send **message two**, the design intent, generated by the orchestrator from the bible so the facts are right, which asks for the editorial panel.
2. Save results to `reviews/<date>-external/`. Synthesize into `synthesis.md` with a reliability column per panel (reviewers miscount words and quote stale text) and verify every claim against the text before acting.
3. Enjoyment and craft are scored separately. Publishability may not exceed enjoyment.
4. Write `revision-brief-N.md`, run one targeted round (writer → continuity in commitments mode → dialogue doctor → voice → audit → cold read).
5. Later rounds send the new draft blind again with no fix list. Checklist verification belongs to the commitments check.
6. Hard stop after two rounds. Then 3–5 human target readers get the sample with two questions: where did you stop, would you buy. Then a human copyedit.

Any reader-notes or review file names the exact draft it read.

## How to invoke

- `Run research phase for <slug>` (slug may not exist yet; create it from `_template`)
- `Run setup phase for <slug> with angle 3`
- `Run chapter 3 pipeline for <slug>` · `Run chapters 3 through 6 for <slug>`
- `Run just the voice edit on chapter 3 for <slug>` · `Check continuity on chapter 5 for <slug>` · `Cold read chapter 4 for <slug>` · `Sample read <slug>`
- `Run audit for <slug>` · `Run manuscript stage for <slug>` · `Run external review round for <slug>`
- `Report only for <slug>`: audit, plot auditor (manuscript mode), sample reader. Changes nothing; saves reports under `reviews/`.

## Rules

- Never modify `story-bible.md` except in setup step 8 or when the author explicitly asks.
- Never skip the continuity checker or the audit.
- Never give the cold reader or the sample reader a planning file. Pass them chapter numbers only. `final.md` holds prose only; edit logs go in `edit-log.md` beside it.
- An agent that flags an unresolvable conflict with the bible stops the pipeline; report to the author.
- Chapter numbering is zero-padded: chapter-01, chapter-02.
- Never summarize what just happened at the top of a scene or chapter.
- Treat "I'd keep reading, but…" from any reader as a warning. Report it above the score.
- Lessons learned on a book are committed to the pipeline (agents, `docs/changelog.md`, genre map), never only to that book's files.
- Commit and push after every step.
