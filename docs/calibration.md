# Calibration anchors

Every real human verdict on text this pipeline produced, with the text it was about. Judges and readers cite these. Add each new verdict here; re-run the judges on the anchors to measure agreement.

## Human verdicts

| ID | Text | Who | Format | Verdict | Date |
|---|---|---|---|---|---|
| A1 | *The Last Frame* v1, Ch 01–03 (`books/the-last-frame/chapters-v1/chapter-0{1,2,3}/final.md`) | the author | Speechify, text-to-speech | **Stop at 29%.** "So boring, really boring." Later: "excruciating." | Oct 27 |
| A2 | *Ten Days Out*, full manuscript (`books/ten-days-out/manuscript.md`) | the author | listened | **Excruciatingly boring.** | Oct 27 |
| A3 | *The Last Frame* v2, Ch 01 (`books/the-last-frame/chapters/chapter-01/final.md`) | the author | read | **Keep going.** "Already better, more interesting than the last one," "still better" at the end. No drift through the two passages the simulated readers had flagged. | Oct 28 |
| A4 | *The Last Frame* v2, Ch 01–03 sample | the author | — | **Open.** Sent Oct 28; no verdict yet. | — |

## What the simulated readers said about the same texts

| ID | Sample reader (v1 agent) | Sample reader (calibrated v2 agent) | Cold reader | Outside panels |
|---|---|---|---|---|
| A1 | Finished, buy yes, pull 4/10 | — | 4 stars, "I'd keep reading" | 8–8.5/10 |
| A2 | Finished, buy yes, pull 7/10 | — | — | 8/10 |
| A3 | — | Pull 3.25 (gate FAIL) | 5/10 | — |
| A4 | — | Pull 3.42, buy yes, one scene at 2 (gate FAIL) | Ch 02: 5/10 | — |

Reading: the v1 readers were too kind by a wide margin (A1, A2). The calibrated v2 reader is now too harsh on at least one chapter (A3: failed what the author liked). Neither direction is usable as a gate alone. The judge panel is scored against this table.

## Judge agreement log

| Date | Judge config | Anchors tested | Agreement | Notes |
|---|---|---|---|---|
| — | — | — | — | first run pending |

## How to add an anchor

1. Add the row with a stable ID, the exact file(s), who judged, the format, the verdict in their words, the date.
2. Run the judge panel on the same text (`docs/judging.md`, "calibration mode") and fill the second table.
3. Update the agreement log. Report the agreement number in the next milestone message.
