# Calibration anchors

Every real human verdict on text this pipeline produced, with the text it was about. Judges and readers cite these. Add each new verdict here; re-run the judges on the anchors to measure agreement.

## Human verdicts

| ID | Text | Who | Format | Verdict | Date |
|---|---|---|---|---|---|
| A1 | *The Last Frame* v1, Ch 01–03 (`books/the-last-frame/chapters-v1/chapter-0{1,2,3}/final.md`) | the author | Speechify, text-to-speech | **Stop at 29%.** "So boring, really boring." Later: "excruciating." | Oct 27 |
| A2 | *Ten Days Out*, full manuscript (`books/ten-days-out/manuscript.md`) | the author | listened | **Excruciatingly boring.** | Oct 27 |
| A3 | *The Last Frame* v2, Ch 01 (`books/the-last-frame/chapters/chapter-01/final.md`) | the author | read | **Keep going.** "Already better, more interesting than the last one," "still better" at the end. No drift through the two passages the simulated readers had flagged. | Oct 28 |
| A5 | *The Last Frame* v2, Ch 01–03 sample with the tournament Ch 02 (`books/the-last-frame/chapters/chapter-0{1,2,3}/final.md`, Oct 28 evening) | the author | veto-window send, Oct 28 late | **Open.** Sent; no verdict yet. | Oct 28 |
| A4 | *The Last Frame* v2, Ch 01–03 sample (`books/the-last-frame/chapters/chapter-0{1,2,3}/final.md`, the pre-tournament Ch 02) | the author | read, other session | **Keep going, mildly.** "The writing is generally more interesting than previously." No stop line given. The sample reader had failed the same text (3.42; Ch 2 scene 3 at 2). | Oct 28 |
| A6 | *Ten Days Out* v2, Ch 01–03 sample (`books/ten-days-out/chapters/chapter-0{1,2,3}/final.md`, Oct 29 late, store cut to a bridge) | the author | pending | **Open.** The author chose to stop gating on the store scene after six simulated fails and to read Ch 01–03 himself. | Oct 29 |


| A7 | *The Last Frame* v2, full draft after revision round 1 (`books/the-last-frame/manuscript.md`, Oct 29, 31,400 words) | author, text-to-speech, veto window | where did you drift / keep going | **pending** (window closes Oct 31) | Oct 29 |## What the simulated readers said about the same texts

| ID | Sample reader (v1 agent) | Sample reader (calibrated v2 agent) | Cold reader | Outside panels |
|---|---|---|---|---|
| A1 | Finished, buy yes, pull 4/10 | — | 4 stars, "I'd keep reading" | 8–8.5/10 |
| A2 | Finished, buy yes, pull 7/10 | — | — | 8/10 |
| A3 | — | Pull 3.25 (gate FAIL) | 5/10 | — |
| A4 | — | Pull 3.42, buy yes, one scene at 2 (gate FAIL) | Ch 02: 5/10 | — |
| A5 (pending) | — | Pull 3.33, buy no, no scene under 3, Ch 02 scenes 3/3/3/4 (gate FAIL) | Ch 02: 5/10, "I'd keep reading, but…" | — |

Reading on A5: the sample reader scored Ch 01 and Ch 03, unchanged text the author passed in A3 and A4, exactly as before, and scored the new Ch 02 with no scene under 3 where the old one had a 2. Its sample fail (3.33) is therefore the same fail it gave A3 and A4, on text the author liked. Logged, not acted on (CLAUDE.md pull-gate exception). The author's verdict on the send decides.

Reading: the v1 readers were too kind by a wide margin (A1, A2). The calibrated v2 reader is now too harsh on at least one chapter (A3: failed what the author liked). Neither direction is usable as a gate alone. The judge panel is scored against this table.
| A6 (pending) | — | Six reads, 3.15 → 3.6 → 3.8 → 3.6 → 3.6 → 3.7, buy yes every time; Ch 03 store scene at 2 on all six across two tournaments, a clue thinning, a clue move and a cut to a bridge (gate FAIL each time) | Ch 03 7/10, store 3 | — |

## Judge agreement log

| Date | Judge config | Anchors tested | Agreement | Notes |
|---|---|---|---|---|
| Oct 28 | 3 personas × 2 models (opus, sonnet), A/B order randomized, blind to this file | A1 Ch 01 vs A3 Ch 01 (author: A3 better) | **6 of 6** picked A3 (4 high, 2 medium) | Every judge named the same stop line in A1: the flight-strip code "04 / 1830 / LG / 4 / —" at ~2–4%. Four judges named the same two weak spots in A3: the room-count "First, the ones moving…" at ~30% and the "First, the ball… Third…" device at ~50%. One pair is not a track record; it is the first point. |
| Oct 28 | same panel, 6 judges | *The Last Frame* v2 Ch 02: tournament winner (v3) vs the pre-tournament final that was part of A4 | **6 of 6** picked v3 (5 high, 1 medium-high) | Not a human-agreement score: the author gave no stop line on A4. All six named the same lost-me line in the old chapter (Ray reciting the contract to the lock, ~35%), the passage the sample reader scored 2. The revised sample is the next veto-window send; the author's verdict on it becomes A5. Full tally in `books/the-last-frame/chapters/chapter-02/variants/tournament.md`. |
| Oct 29 | same panel, 6 judges each, round 2 only | *The Last Frame* v2 Ch 04, 06, 08, 09: tournament winner vs the first finished chapter (cold reader 4/10 each time) | Ch 04 5–1, Ch 06 5–1, Ch 08 6–0, Ch 09 6–0 for the winner | No human verdict yet on any of these (not sent; the next veto-window send is the full draft). The cold reader rescored each winner: Ch 04 5, Ch 06 5, Ch 08 4, Ch 09 4; its remaining complaints on Ch 08–09 are outline-level (stake size; the romance settled early). The judges and the cold reader agree on which lines lose a reader and disagree on whether a chapter whose stake is settled can still pull; the author's verdict on the full draft decides who is calibrated. Round 1 of Ch 09 split 3–3 twice between the "couple in the room" and "the ask" leads, by persona: Buyer took the couple, Craft took the ask. Tallies in each chapter's `variants/tournament.md`. |
| Oct 29 | same panel, 6 judges, round 2 | *The Last Frame* v2 Ch 10 (last chapter): tournament winner vs the first finished chapter (cold reader 4/10, "would not recommend") | 6–0 for the winner (3 high) | Cold reader on the winner: 5/10, still "would not recommend; would not buy the next book blind," no stop line. Logged as a pull-gate fail under the Oct 28 exception (text already through a tournament at ≥ 5 of 6); goes to the author with the full draft as the veto-window send. The judges' reasons and the reader's agree on the two scenes that work (Kate on speaker; the iron step) and on the notary condition reading as paperwork. The reader's complaint that the whole ending was predictable from Ch 09 is one no judge can see, since the panel reads one chapter at a time. |

## How to add an anchor

1. Add the row with a stable ID, the exact file(s), who judged, the format, the verdict in their words, the date.
2. Run the judge panel on the same text (`docs/judging.md`, "calibration mode") and fill the second table.
3. Update the agreement log. Report the agreement number in the next milestone message.
