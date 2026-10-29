# Pipeline changelog

The pipeline's own history. A lesson learned on a book is committed here and to the agents, never only to that book's files. Each entry: what happened, what it taught, what changed.

## 2026-10-28 (evening) — The judge panel and the first tournament

**Why:** the author's goal is a series factory with as few human gates as possible. Every human gate can only go once something else predicts his verdict, and nothing did: both books passed every simulated read and bored him. So the pipeline stops asking one agent to score one draft and starts asking several agents to compare several drafts.

**Added:** `.claude/agents/judge.md` (blind pairwise, forced choice, three personas, quotes the line where each text lost it); `docs/judging.md` (tournaments: three variants from one beat sheet, 18 blind comparisons, plus the current final as a fourth entrant); `docs/calibration.md` (every real human verdict, with the judges' agreement against it); `docs/factory-plan.md` (the trust ladder); `books/_series-template/`. The human gate on autopilot became a 48-hour veto window. Pull-gate failures now trigger a tournament, never line edits.

**First results.** Judges on the calibration pair (v1 Ch 01, which bored the author, against v2 Ch 01, which he liked): 6 of 6 agreed with him, and all six named the same stop line. First tournament, *The Last Frame* Ch 02: three variants were close (7–6–5, mostly medium confidence), and the winner then beat the pre-tournament chapter 6–0 at high confidence. All six judges named the same line where the old chapter lost them, the same passage the sample reader had scored 2. Two things to carry forward: comparison works where scoring did not, and the beat change (keep the couple in the room, never recite the contract) did more than any lead instruction. Skimmer judges and craft judges pull in opposite directions (skimmers punish long interior paragraphs; craft judges reward distinct voices), so neither persona alone should decide.

**Audit tool fixes (same evening).** Three bugs found when the audit ran on the tournament winner: the bible's motif patterns are written in backticks and the tool was matching the backticks (every motif count had been zero since v2); the escaped scene break `\* \* \*` was not recognized, so every chapter counted as one scene and the cluster check never fired; and once scenes split correctly, the cluster check flagged any group with two hits in a short scene. Now: backticks stripped, escaped breaks recognized, a group needs at least three hits to count toward a cluster. Audits run before this on v2 chapters under-reported; the next full run covers them.

## 2026-10-28 — Version 2: the combined repo and the rebuilt system

### What happened

Two novellas went through version 1 in October 2026, in separate repos with identical agents: *The Last Frame* (clean small-town romance, `books/the-last-frame/`) and *Ten Days Out* (open-door romantic suspense, `books/ten-days-out/`). Each had three drafts and three outside AI review rounds. Both reached "ready to publish" scores (8–8.5/10; 4.2/5). Then the author listened to *The Last Frame* on text-to-speech and stopped at 29%: "really boring."

Every fix along the way had been written into one-off files (revision briefs, voice quotas, a repetition script, synthesis "pipeline lessons" sections). None of it reached the agents. Book 2 started with the same agents that produced Book 1's 3.0–3.3 first draft, and Book 1's CLAUDE.md had gained an external-review stage that Book 2's never got.

### What the two books taught

**Accuracy (from the review syntheses):**
- Nobody checked the bible against the world. Book 1 got NH right of first refusal wrong, booked raffle income unlawfully, used tenpin terms in a candlepin book, set a covenant with $600 of headroom. Book 2 overstated federal procedure. The continuity checker propagated every error because the bible said so.
- Arithmetic nobody recomputed: tape sums, lane counts.
- Payoffs with no plant (names first appearing in Ch 9; a vacation week on a tape).
- The writer misses word targets by ~10% either way and compresses high-emotion scenes (Ray's final in one sentence; sex scenes at 300–400 words against a longer brief).
- Both leads sound alike; the voice editor flattened them toward one style reference.
- Motifs strip-mined into tics (room-counting 19×, the rag smear 25×, "squared" 23×).
- A fix in one chapter breaks a later one (the Ch 4 generator line broke Ch 5; clarifying a denial raised a character's culpability later).
- The cold reader grades a third of a point to a full point above outside panels.
- Outside reviewers miscount words and quote stale drafts; the review prompt itself had a wrong fact (four kisses; the book had three).
- "Never a stupid choice in danger" removed the useful mistakes.
- The reader guessed the leak by Ch 3 and was certain by Ch 6; no agent could see what the page had revealed.

**Pleasure (from `docs/postmortem-boring.md`):**
- The signals were there ("too quiet," "I'd keep reading, but not by much," "a metronome") and the orchestrator filed them as small fixes under a one-revision cap.
- Simulated readers cannot get bored; none was asked a forced-choice buying question.
- Every editing stage subtracted; none added. 23 world rules, nearly all prohibitions. Mean sentence 12 words, 23% at five words or fewer, the same rhythm everywhere.
- No agent owned "is this entertaining." First kiss at 48%.
- Texture became the content: 34 slash-codes in Ch 1–3; the chapter everyone liked had 3.
- The review prompt anchored reviewers on our design intent and on "AI experiment," and later rounds became checklist verification.
- The human read came last.

**Machine tells (from `docs/ai-fiction-tells.md`):**
- "Show, don't tell" applied as "convert every feeling to a symptom" is itself a measured tell; that is the gesture-then-explanation pattern every panel flagged.
- The Claude row of the model-drift table (flat escalation, quiet endings, too many similes) is the postmortem restated.
- Word lists are a hygiene pass; structure (Part 7) is the real work.

### What changed

**Repo.** One repo. Pipeline at the root, books under `books/<slug>/`, blanks in `books/_template/`. Book 2 merged in with its history (`git subtree`). Each book has a `book-brief.md`. Per-book pipeline settings that used to live in a book's CLAUDE.md now live in its brief.

**Gates (apply on autopilot):** human gate (Ch 01, sample mark, Ch 03, in the format readers use); pull gate (sample reader); logic gate (plot auditor on the outline).

**New agents:** `character-designer` (the people before the world; split out of bible-builder because the bible spent its attention on money tables and calendars and the leads came out thin), `dialogue-doctor` (a pass between the continuity revision and the voice edit that rewrites every exchange for tactics, subtext, banter and two voices, and may add lines), `plot-auditor` (the skeptic; outline and manuscript modes; owns the tells Part 7 story-level audit), `sample-reader` (the reader who can quit; forced-choice outputs; prediction section), `domain-checker` (web-enabled; bible and manuscript modes).

**New tool:** `tools/audit.py` combines Book 2's repetition script, the postmortem's ear check and the tells lint (Parts 2, 3, 5). Runs after every voice edit on all chapters so far; reports scene clusters.

**Rewritten agents:**
- `story-architect`: genre map; turn/longing/laugh/cost/plants/ending type per chapter; the ordinary scene; the four-beat repair; an unresolved subplot; a condemnable choice; tonal contrast; mystery-fairness clue list; writes the sample synopsis.
- `plot-architect`: want per scene; texture budget; POV per scene; word floors; assigned ending types; plant list; numbers used.
- `bible-builder`: syntax profiles per POV; motif list with caps; numbers ledger; world-rule ceiling of 20 with paired positives; heat rules; samples at both temperatures; name selection with a stated source.
- `prose-writer`: positive rules first (want, rhythm range, turn/longing/laugh, two voices, texture budget, emotion as choice, assigned endings, floors); hard bans only from tells Part 2; "default to short sentences" removed; one signal plus one interior line per beat; Commitments notes after revisions.
- `voice-editor`: may add life (dialogue, interiority, long sentences, sensory pleasure); edits per POV profile; judgment tests (tells Part 6) on audit flags; floors are hard; no new prohibition without its pair.
- `cold-reader`: pull score; prediction section (the reader-knowledge tracker); listener pass; romance check; knows its score is a floor.
- `continuity-checker`: numbers ledger and plant list checks; manuscript mode on Opus; commitments mode after revisions.

**Genre map:** `genre-maps/romance.md` with positions (Act 1 ≤ 20%, first kiss ≤ 35%, hook inside the sample), per-chapter requirements, heat and texture rules, lead rules, the default sample-reader persona.

**External review:** `reviews/prompt-blind.md`, two messages. Blind buyer read first (stop line, buy, boredom ledger, pull curve, comparison, audio test, enjoyment score), design intent second (generated from the bible), editorial panel with craft and publishability scored separately and publishability capped at enjoyment. Later rounds blind, no fix list. Two rounds, then humans.

**Orchestrator:** word check after every draft; one internal revision round before going outside; boredom flags above scores; lessons committed to the pipeline.

### Calibration (added 2026-10-28, same day)

The new sample reader, run on both finished books, finished both samples and said "buy: yes" (pull 4 and 7 of 10). The author found both excruciating. Both reader agents now carry that verdict as a calibration anchor, the pull gate tightened (any scene ≤ 2, sample average under 3.5 of 5, any chapter ≤ 5 of 10), and the simulated readers are labelled a smoke test: a pass means nothing until the author has read it.

### Not changed

The research phase, the per-chapter order, the clean-manuscript build, commit-after-every-step, and the rule keeping readers away from planning files.

### Open for the author

- *The Last Frame*: structural pass on the opening (not line edits), or leave as a lesson.
- *Ten Days Out*: with beta readers; no text changes until they report.
- Pen names and KDP accounts for both.

## 2026-10-26 — Version 1

Ten agents (market-analyst, niche-spotter, comp-reader, story-architect, bible-builder, plot-architect, prose-writer, continuity-checker, voice-editor, cold-reader), a generate → check → revise → edit → cold-read loop per chapter, autopilot mode, one repo per book. Added during Book 1: the external review stage (seven-role editorial panel).

## Oct 29, 2026 — Ten Days Out: sample reader contamination
- The sample-mark re-read was started with no persona. The agent built one from `book-brief.md` as its definition allowed, and the brief's approvals named the leak. Its suspect read was thrown away and the read was rerun clean (`reviews/sample-read-sample-mark-r2-contaminated.md` kept for the record).
- Fix (`.claude/agents/sample-reader.md`): with no persona, build it from `research/chosen-angle.md` only; never open the brief, bible, outline or reviews. Pair: the orchestrator always passes the persona line from the book's first sample read.

## Oct 29, 2026 — Ten Days Out: a scene the gate could not clear
- The Ch 03 store scene scored 2 with the sample reader on six reads running. Nothing moved it: two scene tournaments (11–5–2, 10–4–4), thinning five clues to two, moving the seal-tag clue to Ch 04 (author decision), or cutting the scene to a 690-word bridge (author decision). Over the same reads the sample average rose from 3.15 to 3.7, and the shed scene went from 4 to 5.
- The author then chose to stop gating on that scene, log it as calibration anchor A6 and go on to Ch 04 under the veto window.
- Lesson for the pipeline: after two tournaments on one scene with no change in its score, stop and ask the author before a third pass. A scene the simulated reader marks at 2 no matter what goes into it may be the reader's blind spot (island ensemble scenes with four or more named people), not the scene's. Pair: when that happens, cut the number of named people on the page to three or fewer before anything else, because that was the one complaint the reader repeated every time.
- Also logged: the reader's Ned suspicion rose to 45% as the store scene thinned. The thinner the scene, the more Ned's own beats (the key, "me and God") stood out. Ch 04 has to spread the suspicion again.

## Oct 29, 2026 — The Last Frame: Ch 09 and Ch 10 tournaments
- Ch 09: "the ask" lead (four asks, built to the daughter's call) won 9–6–3 and 6–0 over the first run. Round 1 split 3–3 twice by persona: Buyer took "couple in the room", Craft took "the ask". The cold reader rescored the winner 4/10 with no stop line; its complaints were outline-level (romance settled; stake a bank number). Logged in `docs/calibration.md`.
- Ch 10 (last chapter): the first run scored 4/10 and "would not recommend": every prediction the reader made after Ch 09 came true; the committee result arrived offstage as "It funded"; two reversals (Dale, the treasurer) happened off the page; the pole scene was a curtain call; ten spoken callbacks in the last third. Beats rebuilt and a tournament run. Three lessons from the rebuild, now rules for the plot architect:
  - A last chapter needs its final external stake on the page, in the POV character's presence, with a price paid before it lands. An answer delivered offstage scored 4/10.
  - Payoffs for side characters belong where those characters already are. Moving them to the final set piece produces a curtain call.
  - In a closing chapter, cap spoken callbacks at about five, each doing work in its own scene. Echoes carried by action do not count. (Pair: every scene still gets one thing the reader did not predict.)
- Tournament lead choice, five tournaments in: "couple in the room" wins when the beats keep the leads apart (Ch 02, 04) and loses when they are already together (Ch 06, 09); "pace" wins when the scenes lack a clock (Ch 06, 08) and loses when the clock is on the page (Ch 09); giving the extra words to the scene the cold reader said was missing something wins (Ch 09, the daughter). The architect now states, in the beat sheet, why each lead was chosen against these beats and which were passed over.
