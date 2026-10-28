# Novel Pipeline

An agentic writing pipeline using Claude Code subagents. One repo holds the pipeline and every book written with it.

```
CLAUDE.md               orchestrator (read first)
.claude/agents/         15 agents, shared by every book
tools/audit.py          repetition, ear and AI-tells audit
genre-maps/             structural defaults per genre (romance.md so far)
reviews/                external review prompts
docs/                   ai-fiction-tells.md · postmortem-boring.md · changelog.md
books/
  _template/            blank files for a new book
  the-last-frame/       Book 1 — clean small-town romance (finished Oct 2026; opening needs a structural pass)
  ten-days-out/         Book 2 — open-door romantic suspense (finished Oct 2026; with beta readers)
```

## How to run

Open a Claude Code session with this repo attached. Every command names a book slug.

| Phase | Command |
|---|---|
| Research | `Run research phase for <slug>` |
| Setup (outline → logic gate → sample synopsis → bible → domain check) | `Run setup phase for <slug> with angle 3` |
| Draft a chapter | `Run chapter 3 pipeline for <slug>` |
| Several chapters | `Run chapters 3 through 6 for <slug>` |
| Audit only | `Run audit for <slug>` (or `python3 tools/audit.py books/<slug>`) |
| After the last chapter | `Run manuscript stage for <slug>` |
| Outside review | `Run external review round for <slug>` |
| Reports without changes | `Report only for <slug>` |

Three gates stop the pipeline even on autopilot: the author's own read of Ch 01, the sample mark and Ch 03; the sample reader's pull gate; the plot auditor's logic gate on the outline. `CLAUDE.md` has the detail.

## Agents

| Agent | Role | Model | Runs |
|---|---|---|---|
| market-analyst | Genre research, reader demand | Sonnet | Once |
| niche-spotter | Story angle proposals | Sonnet | Once |
| comp-reader | Comparable books and their 2–3 star reviews | Sonnet | Per angle |
| story-architect | Outline against the genre map; sample synopsis | Opus | Setup, and when a gate sends work back |
| plot-auditor | The skeptic: who knew, how it travelled, why not the safer option; story-level tells audit | Opus | Outline, manuscript, after revisions |
| sample-reader | The reader who can quit: stop line, buy yes/no, pull per scene | Opus | Synopsis, Ch 01, sample mark, manuscript |
| character-designer | The people first: wants apart from the plot, humor, syntax profiles, friction that is not the story | Opus | Setup |
| bible-builder | The world around those people: locations, rules, motif caps, numbers ledger, both-temperature samples | Opus | Setup |
| domain-checker | Law, money, sport, trade, procedure against the world, with sources | Opus | Bible, manuscript |
| plot-architect | Beat sheet: want, turn, longing, laugh, floors, texture budget, plants, endings | Opus | Per chapter |
| prose-writer | Draft and revision | Opus | Per chapter (twice) |
| continuity-checker | Facts, timeline, ledger, plants; commitments after revisions | Sonnet / Opus | Per chapter; manuscript; after revisions |
| dialogue-doctor | Every exchange for tactics, subtext, banter, two voices; may add lines | Opus | Per chapter |
| voice-editor | Voice per POV, adds life, judgment tests, floors | Sonnet | Per chapter |
| cold-reader | Pull, boredom, prediction, listener pass | Opus | Per chapter; manuscript |

## Your manuscript

The orchestrator builds `books/<slug>/manuscript.md` from the chapter finals. Final assembly for KDP, the pen name, cover and blurb are yours.

## History

`docs/changelog.md`. The short version: version 1 produced two novellas that outside editorial panels scored 8/10 and that the author found boring at 29%. Version 2 adds the readers who can quit, the gates that stop autopilot, the auditor who disbelieves the outline, the checker who looks outside the bible, and an editor allowed to add.
