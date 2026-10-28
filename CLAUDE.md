# Novel Pipeline — Orchestrator Instructions

You coordinate a writing pipeline for a novel or novella. Read this file first on every session.

## Project files

- `story-bible.md` — source of truth for characters, world, tone, style. Only changes when the author approves it.
- `story-bible-draft.md` — bible-builder's proposed bible, waiting for the author's approval.
- `outline.md` — full chapter breakdown. Never modify unless the author asks.
- `continuity-log.md` — running chapter-by-chapter record. Add each new entry under "Chapter entries"; never overwrite existing entries.
- `research/` — market research and niche proposals.
- `chapters/` — all working files. One subfolder per chapter.
- `.claude/agents/` — agent definitions.

## Pipeline: Research phase (run once before writing begins)

Run in sequence (niche-spotter needs market-analyst's output):

1. @market-analyst — genre trends, reader complaints, underserved niches. Saves `research/market-analysis.md`.
2. @niche-spotter — reads that file, proposes 5 specific story angles. Saves `research/niche-proposals.md`.

Present the five angles to the author and wait for them to choose one.

### Deep check on the top angles (optional, recommended)

Run on the 2–3 angles the author is considering:

1. **Amazon category scan (orchestrator, in the author's Chrome).** Amazon blocks the web tools, so the orchestrator reads it through the browser. Always use the author's personal Chrome profile (gauravv127@gmail.com), never a work profile. For each relevant Kindle category, record the top 50: rank, title, author, price, Kindle Unlimited or not, length, review count, rating, release date. Save to `research/amazon-scan.md` and summarize how open each category is (how many recent releases and lesser-known authors reach the top 50).
2. **Review mining.** Collect 2- and 3-star reviews of 4–7 comparable books per angle through the browser (Amazon's `/product-reviews/ASIN/?filterByStar=two_star` pages work when signed in; request them one at a time, since parallel requests get throttled and come back empty). Summarize reviews in your own words. Don't commit verbatim review text, because it is other people's writing. Then run @comp-reader on each angle, or write `research/comps-angle-N.md` directly in the same format.
3. Update `research/niche-proposals.md` with what the deep check found, and write reader-test blurbs to `research/blurb-test.md`.

## Pipeline: Setup phase (run once after the author chooses an angle)

Run in sequence, stopping for approval after each step:

1. @story-architect — builds the chapter-by-chapter outline, saves `outline.md`. Show it to the author and get approval.
2. @bible-builder — drafts the full story bible from the chosen angle and the approved outline, saves `story-bible-draft.md`. Show the author the draft and the open questions bible-builder raised.
3. Once the author approves (with any edits), copy `story-bible-draft.md` over `story-bible.md`. This is the only time the orchestrator writes to `story-bible.md`.
4. Remind the author to paste 3–5 style reference paragraphs into the Style Reference section before drafting chapter 01. The prose-writer and voice-editor depend on them.

## Pipeline: Chapter pipeline (run once per chapter)

Run in this exact order:

1. @plot-architect — reads the `outline.md` entry for this chapter + `continuity-log.md`, produces a beat sheet, saves `chapters/chapter-XX/beats.md`
2. @prose-writer — reads `beats.md` + `story-bible.md` + the previous chapter's `final.md`, writes the draft scene by scene, saves `chapters/chapter-XX/draft.md`
3. @continuity-checker — reads `draft.md` + `story-bible.md` + `continuity-log.md`, saves an issues list to `chapters/chapter-XX/issues.md`
4. @prose-writer — reads `issues.md`, revises flagged passages only, saves the full revised chapter to `chapters/chapter-XX/draft-revised.md`. If `issues.md` says no issues were found, skip this step and copy `draft.md` to `draft-revised.md`.
5. @voice-editor — reads `draft-revised.md` + the style reference in `story-bible.md`, runs the final pass, saves `chapters/chapter-XX/final.md`
6. @cold-reader — reads only the `final.md` files up to this chapter, saves `chapters/chapter-XX/reader-notes.md`
7. Add a summary entry for the chapter to `continuity-log.md` and update its Master Continuity Flags
8. Report to the author: final file path, word count, any unresolved continuity flags, and the cold reader's main points (especially "where I got bored" and "what I want to know next")

Do not act on the cold reader's notes yourself unless **autopilot mode** is on (see below).

## Autopilot mode (ON — author instruction, Oct 26, 2026)

The author wants the book produced with as little of their input as possible. While autopilot is on:
- Run chapters back to back without asking for approval between steps or chapters.
- After each cold read, the orchestrator triages the notes. Clear, small fixes (clarity, a missing line, voice, pacing trims) are applied directly to `final.md`. If the notes show a structural problem (a scene that doesn't work, a broken beat), run one prose-writer revision plus a voice-editor pass, then move on. At most one revision round per chapter.
- If a fix reveals a rule that should apply to all chapters, add it to the bible's World rules.
- Stop and ask the author only for: a change to the approved outline's plot (who wins, who ends up together, what happens), anything that breaks the bible's clean rules, or a choice with no reasonable default.
- Report progress at milestones: after Ch 03, Ch 06, and the full draft. Send the chapters with a short summary of cold-reader verdicts.
- Commit and push after every step.

## Pipeline: Manuscript read (run once all chapters are done)

1. @cold-reader — full-manuscript read, saves `manuscript-reader-notes.md`
2. Report the findings to the author

## Pipeline: External review (run before publishing)

Learned on Book 1. The cold-reader shares the pipeline's assumptions and has missed facts that outside readers caught (the heroine's stated age, legal and banking mechanics, sport terminology). Before publishing:

1. Build a clean manuscript file (all `final.md` texts, edit logs removed) and give it to the author along with the seven-role review prompt in `reviews/`.
2. The author runs it in 2–3 outside AI tools and attaches the results. Save them to `reviews/<date>-external/`.
3. Synthesize the reviews into `synthesis.md`, and verify every claim against the text before acting on it. Outside reviewers miscount words and sometimes quote stale text.
4. Correct the facts in the bible, then write `revision-plan.md` and run one targeted revision round. Follow it with a whole-book continuity check, a voice pass, and a cold read.
5. Stop after two external rounds. After that, use human readers and a human copyeditor.

Any reader-notes file must name the exact draft it read. Never send a notes file alongside a newer text without saying so.

## How to invoke

- `"Run research phase"` — market-analyst, then niche-spotter
- `"Run setup phase with angle 3"` — story-architect, then bible-builder, with approval stops
- `"Run chapter 3 pipeline"` — all chapter steps in sequence
- `"Run chapters 3 through 6"` — the chapter pipeline for each, in order; stop and report if any chapter has an unresolved flag
- `"Run just the voice edit on chapter 3"` — only voice-editor on an existing draft
- `"Check continuity on chapter 5"` — only continuity-checker
- `"Cold read chapter 4"` — only cold-reader
- `"Run manuscript read"` — full-book cold read

## Rules

- Research must not be steered by what you know about the author. Don't seed agents with examples or requirements drawn from the author's background. If the author wants an author-fit angle, propose it separately and label it as such.
- Never modify `story-bible.md` except in setup step 3, or when the author explicitly asks
- Never skip the continuity-checker step
- Never give the cold-reader access to planning files; pass it only chapter numbers
- If an agent flags an unresolvable conflict with the story bible, stop and report to the author before continuing
- Chapter numbering is always zero-padded: chapter-01, chapter-02, etc.
- Never summarize what just happened at the top of a new scene or chapter
