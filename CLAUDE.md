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

Do not act on the cold reader's notes yourself. They go to the author, who decides what to revise.

## Pipeline: Manuscript read (run once all chapters are done)

1. @cold-reader — full-manuscript read, saves `manuscript-reader-notes.md`
2. Report the findings to the author

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

- Never modify `story-bible.md` except in setup step 3, or when the author explicitly asks
- Never skip the continuity-checker step
- Never give the cold-reader access to planning files; pass it only chapter numbers
- If an agent flags an unresolvable conflict with the story bible, stop and report to the author before continuing
- Chapter numbering is always zero-padded: chapter-01, chapter-02, etc.
- Never summarize what just happened at the top of a new scene or chapter
