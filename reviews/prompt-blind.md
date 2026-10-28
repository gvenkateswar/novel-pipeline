# External review prompt — blind, two messages

The first review prompt (`prompt-v1-editorial-panel.md`) handed reviewers the design intent, said "AI experiment," and asked an editorial panel for a publishability score. They graded whether we hit our design, and we had. Three rounds scored 8/10 and the author stopped listening at 29%. This prompt is built so the reviewer behaves like a buyer first and an editor second, and never sees our intent until the buyer verdict is on record.

The orchestrator fills the bracketed parts from `book-brief.md` and `story-bible.md` (so the facts are right) and gives the author both messages. The author sends message one to each outside tool with the clean manuscript attached, saves the reply, and only then sends message two in the same chat.

---

## Message one (blind)

```
Attached is a [novella/novel] titled [TITLE], about [WORD COUNT] words. Genre: [ONE-LINE GENRE LABEL, e.g. "clean small-town romance" or "open-door romantic suspense"].

Read it as a buyer, not an editor. You found it on a Kindle carousel, downloaded the free sample, and you can stop at any time. Please answer in this order, and keep each answer in the form asked:

1. SAMPLE. Read the first 12% (roughly the first [N] chapters). Quote the exact line where you stopped reading, or write "finished the sample." Then: Buy, yes or no? One sentence why.

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

## Message two (after the reply to message one is saved)

```
Thank you. Now the editorial pass. Here is what the book was trying to do:

[DESIGN INTENT, generated from the bible: niche and target reader; the reader complaints the book set out to answer, and how; the leads in two lines each; heat level and rules; length and format; series plan. Facts only; no claims about quality. Check kiss counts, ages, figures against the bible before sending.]

Run a panel. Play each role in turn as a separate person who has not read the others' notes. Stay in role and quote the text for every major point.

1. Acquisitions editor at a digital-first romance imprint: would you buy this, and at what revision cost?
2. Developmental editor: the three structural changes that would most raise the reader's enjoyment score from message one. Changes to events and options, not more explanation.
3. Line editor: the prose habits that mark it, with counts where you can.
4. Fact and continuity reader: what does not add up (timeline, money, law, trade, terminology), with the lines.
5. Market strategist: category, price, label, blurb line, and whether the sample sells the book.

Then two numbers: CRAFT, 1 to 10, and PUBLISHABILITY, 1 to 10. Publishability may not be higher than the enjoyment score from message one. If you think it should be, say why in one sentence and leave the number capped.
```

## Later rounds

Send the new draft with message one again, blind, in a fresh chat. Do not send the previous round's notes or a list of what was fixed. Checklist verification belongs to the pipeline's commitments check, not to the reviewer. Compare the enjoyment score and the pull curve round to round; those are the numbers that matter.

## Synthesis format (`reviews/<date>-external/synthesis.md`)

| Panel | Stopped at (sample) | Buy | Enjoyment | Craft | Publishability | Reliability notes |

Then: where all panels agree; where they disagree; the boredom ledger merged by position; the pull curves side by side; findings verified against the text (reviewers miscount words and quote stale drafts); what the pipeline missed and the rule it implies (paired: a thing to stop and a thing to do).
