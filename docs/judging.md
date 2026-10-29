# Judging: tournaments and calibration

Why: AI readers grade badly on a scale ("rate this 1–10") and much better in comparison ("which of these two would you keep reading"). So the pipeline never asks one agent to score one draft when it can ask several agents to compare several drafts.

## When a tournament runs

- The opening chapter (Ch 01) of every book.
- The sample-mark chapter(s) if the sample reader fails the pull gate.
- Any scene a reader scores ≤ 2, or a chapter the whole-book read scores ≤ 5.
- Any time the orchestrator must choose between two approaches it can't settle (two beat sheets, two endings).

## Procedure

1. **Variants.** The plot architect writes the beats once. The prose writer is run **three times in parallel** on the same beats, each with a different lead instruction, for example:
   - V1: "Lead with the couple. Every scene has both of them in it or one of them thinking about the other."
   - V2: "Lead with pace. Enter every scene late, leave early, cut the logistics, keep the jokes."
   - V3: "Lead with voice. Let the POV character's humor and interior run; longer sentences allowed."
   The orchestrator chooses the three instructions from the reader notes that triggered the tournament. Save as `chapters/chapter-XX/variants/v1.md`, `v2.md`, `v3.md`.
2. **Judges.** `.claude/agents/judge.md`, run on each **pair** (V1 vs V2, V1 vs V3, V2 vs V3), with three personas each (buyer, skimmer, craft) and across two models (opus and sonnet). That is 3 pairs × 3 personas × 2 models = 18 blind comparisons. Variants are presented in random order and labeled A and B, never by number, so judges can't learn a slot.
3. **Scoring.** Each comparison yields one winner. The variant with the most wins takes the round. Ties go to the buyer persona's wins. Record every verdict in `chapters/chapter-XX/variants/tournament.md` with the one-line reason each judge gave.
4. **Winner** goes through the normal pipeline from the continuity check onward. The losers stay in `variants/` for calibration.
5. If every variant loses to the previous draft (the orchestrator always includes the current `final.md` as a fourth entrant when one exists), the beats are the problem: back to the plot architect.

## Calibration mode

Run the judge on the anchor texts in `docs/calibration.md`, paired against each other (for example A1 Ch 01 vs A3 Ch 01). The judge is right when it prefers the text the human preferred. Log the agreement rate. This is how we find out which persona and model to trust, and when a human gate can be retired.

## Cost control

A full tournament is about 18 judge calls plus 3 writer calls. Run it only at the trigger points above. For a scene-level trigger, run variants of the scene, not the chapter.
