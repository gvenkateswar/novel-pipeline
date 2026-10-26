# Novel Pipeline — Orchestrator Instructions

You coordinate a writing pipeline for a novel or novella. Read this file first on every session.

## Project files

- `story-bible.md` — source of truth for characters, world, tone, style. Never modify.
- `outline.md` — full chapter breakdown. Never modify unless explicitly asked.
- `continuity-log.md` — running chapter-by-chapter summary. Append after each chapter, never overwrite.
- `chapters/` — all working files. One subfolder per chapter.
- `.claude/agents/` — agent definitions.

## Pipeline: Research phase (run once before writing begins)

Run these in parallel:

1. @market-analyst — identify genre trends, reader complaints, underserved niches on Amazon/Goodreads/Reddit
2. @niche-spotter — takes market-analyst output, proposes 3–5 specific story angles

Output lands in `research/`. Present findings to the user and wait for them to choose a direction before proceeding.

## Pipeline: Setup phase (run once after niche is chosen)

Run in sequence:

1. @story-architect — builds full chapter-by-chapter outline from the chosen niche and any user input, saves to `outline.md`

Review outline with user and get approval before drafting begins.

## Pipeline: Chapter pipeline (run once per chapter)

Run in this exact order:

1. @plot-architect — reads `outline.md` entry for this chapter + `continuity-log.md`, produces beat sheet, saves to `chapters/chapter-XX/beats.md`
2. @prose-writer — reads `beats.md` + `story-bible.md` + previous chapter file, writes draft scene by scene, saves to `chapters/chapter-XX/draft.md`
3. @continuity-checker — reads `draft.md` + `story-bible.md` + `continuity-log.md`, outputs issues list to `chapters/chapter-XX/issues.md`
4. @prose-writer — reads `issues.md`, revises flagged passages only, saves to `chapters/chapter-XX/draft-revised.md`
5. @voice-editor — reads `draft-revised.md` + style reference in `story-bible.md`, runs final pass, saves to `chapters/chapter-XX/final.md`
6. Append a summary entry for the completed chapter to `continuity-log.md`
7. Report to user: final file path, word count, any unresolved flags

## How to invoke

- `"Run research phase"` — fires market-analyst and niche-spotter in parallel
- `"Run setup phase"` — fires story-architect after niche is chosen
- `"Run chapter 3 pipeline"` — runs all five chapter steps in sequence
- `"Run chapters 3 through 6"` — runs the chapter pipeline sequentially for each
- `"Run just the voice edit on chapter 3"` — fires only voice-editor on an existing draft
- `"Check continuity on chapter 5"` — fires only continuity-checker

## Rules

- Never modify `story-bible.md` without explicit user instruction
- Never skip the continuity-checker step
- If an agent flags an unresolvable conflict with the story bible, stop and report to the user before continuing
- Chapter numbering is always zero-padded: chapter-01, chapter-02, etc.
- Never summarize what just happened at the top of a new scene or chapter
