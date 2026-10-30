# External review, v3 r1 — the two messages for the author to send

*Orchestrator, Oct 30, 2026. Filled from `reviews/prompt-blind.md`, `book-brief.md` and `story-bible.md`. The author sends message one to 2–3 outside tools with `manuscript.md` (or the .docx) attached, saves each reply under `reviews/2026-10-30-external/`, and only then sends message two in the same chat. Message one says nothing about design or AI.*

Attach: the clean manuscript, 31,161 words, Chapter 1 through the epilogue (built Oct 30 from the Ch 01–11 finals after internal round 1).

---

## Message one (blind)

```
Attached is a novella titled The Last Frame, about 31,000 words. Genre: clean later-in-life small-town romance.

Read it as a buyer, not an editor. You found it on a Kindle carousel, downloaded the free sample, and you can stop at any time. Please answer in this order, and keep each answer in the form asked:

1. SAMPLE. Read the first 12% (roughly chapter 1 and the first scene of chapter 2). Quote the exact line where you stopped reading, or write "finished the sample." Then: Buy, yes or no? One sentence why.

2. WHOLE BOOK. Now read the rest. If you cannot read all of it, tell me where you stopped before saying anything else.

3. BOREDOM LEDGER. Every place your attention dipped, with its approximate % position and a quoted line. Then name the three most boring passages in the book.

4. PULL CURVE. For each chapter, a number from 1 to 10 for how much you wanted to keep going at its end. One line per chapter on what you wanted to happen next, or "nothing."

5. THE COUPLE. By which chapter did you want them together? Quote the first moment you felt it. Did anyone make you laugh? Quote it or say no.

6. WHAT YOU WORKED OUT. What did you guess, when, and from which line? (Any secret, any twist, any outcome.)

7. COMPARISON. Compare chapter 1 with the opening of a current bestseller in this sub-genre that you know well. Name it. Which would you keep reading, and why, in one paragraph?

8. AUDIO. Read chapter 1 again as if a text-to-speech voice were narrating it. List everything that does not work aloud: codes, numbers, lists, unclear speakers, runs of the same sentence shape.

9. ENJOYMENT SCORE, 1 to 10, as a reader. This is a separate number from anything you say later about craft.

Do not comment on craft, prose, structure or marketability in this message. That comes next.
```

## Message two (only after the reply to message one is saved)

```
Thank you. Now the editorial pass. Here is what the book was trying to do:

Niche and reader: a clean, later-in-life small-town romance for the Kindle Unlimited reader who buys three or four of these a month, is over fifty herself, and is tired of heroines written older than their stated age, of an age gap used as the obstacle, of misunderstandings one honest talk would fix, of couples who have already fallen before page one, and of endings resolved off the page. Categories: Clean & Wholesome; Later in Life. A novella, read in one or two sittings. Winter in a New Hampshire lake town, December through April: candlepin bowling, ice fishing, plowing. No beaches, inns, bookshops or bakeries.

The leads. Ellen Daly, 58, retired by federal statute after thirty-one years as an air-traffic controller, buys a failing ten-lane 1958 candlepin alley and owes the former owner a quarter of a million dollars on March 1; she holds every position alone and lies only with true sentences. Ray Gagnon, 61, widowed, runs the hardware store his father built and has coached the alley's winter league for thirty years; he lost the building to her by eight days, is the only man who can keep her pinsetters running, and under a backup contract buys the building at appraisal if her refinance has not funded by March 1. Both have adult children: her daughter Kate, an ER nurse; his son Danny, who takes over the store.

What the book set out to do: a hard deadline with real money and no villain; two leads whose wants conflict (she needs the winter to clear a bank line; he will not put his late wife's name on a cup strangers bowl for money); the courtship on the page from chapter 1, with the first kiss by a third of the way in; a rupture that is a real cruelty, not a misunderstanding; a repair that costs the one who did it; the last stake paid in a scene with both leads present; an epilogue that is a scene, not a summary. Both points of view: her chapters and his alternate.

Heat: clean, closed door, three kisses, no profanity. Length: about 31,000 words, ten chapters and an epilogue. Series: book 1 of a town series; each book a complete love story with a new couple; no cliffhanger.

Run a panel. Play each role in turn as a separate person who has not read the others' notes. Stay in role and quote the text for every major point.

1. Acquisitions editor at a digital-first romance imprint: would you buy this, and at what revision cost?
2. Developmental editor: the three structural changes that would most raise the reader's enjoyment score from message one. Changes to events and options, not more explanation.
3. Line editor: the prose habits that mark it, with counts where you can.
4. Fact and continuity reader: what does not add up (timeline, money, law, trade, terminology), with the lines.
5. Market strategist: category, price, label, blurb line, and whether the sample sells the book.

Then two numbers: CRAFT, 1 to 10, and PUBLISHABILITY, 1 to 10. Publishability may not be higher than the enjoyment score from message one. If you think it should be, say why in one sentence and leave the number capped.
```

## Facts checked against the bible before sending

- Ellen 58, Ray 61 (bible, Characters). Thirty-one years ATC; retired by statute. The alley: ten lanes, 1958, candlepin. The note: a quarter of a million on March 1 (bible, Premise). Three kisses on the page (Ch 03; Ch 10 twice). Both POVs: Ellen Ch 01, 03, 05, 07, 09, epilogue; Ray Ch 02, 04, 06, 08, 10. Word count 31,161 by `wc -w`. Kate: ER nurse, Manchester. Danny: takes the store March 1.
- Nothing in message one names the design, the pipeline, or AI. Message two states facts only and makes no claim about quality.

## After the replies

Save each reply as `reviews/2026-10-30-external/review-<tool>-m1.md` and `-m2.md`. Then `Run external review synthesis for the-last-frame`: the orchestrator writes `synthesis.md` with the reliability column, verifies every claim against the text, scores enjoyment and craft separately, and writes `revision-brief-v3-2.md` for the one targeted round the external stage allows before the hard stop.
