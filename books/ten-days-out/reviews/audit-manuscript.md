# Audit — ten-days-out (chapters 01–10, 34,470 words)

Source: `docs/ai-fiction-tells.md` Parts 2, 3, 5 and `docs/postmortem-boring.md` C. Counts are regex and approximate; judge flagged items by function. FLAG means over cap.

## 1. Repetition

_No `## MOTIF LIST` table in story-bible.md; motif caps skipped. Add one (| name | regex | cap |) so this section can run._

### Frequent 3–5 word n-grams (4+ uses, whole book)

- 17× “the harbor road”
- 15× “the margaret ann”
- 13× “the north reach”
- 11× “her float coat”
- 9× “the car deck”
- 9× “the cove road”
- 9× “the north road”
- 8× “she could hear”
- 8× “the guest mooring”
- 8× “the ashby place”
- 7× “the outside ladder”
- 7× “the crew mess”
- 7× “her deck lights”
- 7× “by half past”
- 7× “the shore path”
- 7× “under the eave”
- 7× “a long time”
- 6× “the deckhouse door”
- 6× “and said nothing”
- 6× “the store dock”
- 6× “the front door”
- 6× “a quarter past”
- 6× “went through the”
- 6× “let go of”
- 6× “the coast guard”
- 6× “her father had”
- 6× “half past three”
- 6× “the stern gate”
- 6× “the box truck's”
- 6× “on the harbor road”
- 5× “day to day”
- 5× “the transfer bridge”
- 5× “across the harbor”
- 5× “kept her eyes”
- 5× “the cutter island”
- 5× “under the latch”
- 5× “the passenger cabin”
- 5× “the grand jury”
- 5× “i'd like to”
- 5× “standing by one-six”

### Body-reaction words per 1,000 (tells 4.3; cluster matters, not any one)

- jaw: 3 (0.1/1k)
- knuckles?: 3 (0.1/1k)
- throat: 1 (0.0/1k)
- reath: 21 (0.6/1k)
- pulse: 2 (0.1/1k)
- chest: 7 (0.2/1k)
- hands? (stopped|stilled|went still|flat): 1 (0.0/1k)
- shoulders?: 36 (1.0/1k)
- gaze: 0 (0.0/1k)
- tightened: 0 (0.0/1k)
- swallowed: 0 (0.0/1k)

## 2. Ear (read-aloud check)

| Ch | Words | Mean sent. | SD | ≤5-word share | Codes/1k | Numerals/1k | ALLCAPS/1k | Max opener run | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 01 | 2,906 | 11.4 | 8.4 | 32% | 0.0 | 5.8 | 3.1 | 4 | mean short openers |
| 02 | 3,525 | 13.2 | 9.7 | 26% | 0.0 | 3.1 | 1.1 | 4 | short openers |
| 03 | 3,210 | 11.1 | 8.2 | 28% | 0.0 | 2.2 | 0.0 | 2 | mean short |
| 04 | 3,086 | 12.2 | 10.3 | 31% | 0.0 | 1.3 | 0.0 | 3 | mean short |
| 05 | 3,472 | 11.8 | 8.2 | 22% | 0.0 | 1.4 | 0.9 | 2 | mean short |
| 06 | 3,079 | 11.6 | 8.8 | 29% | 0.0 | 4.2 | 0.3 | 3 | mean short |
| 07 | 3,276 | 10.8 | 8.1 | 31% | 0.0 | 5.5 | 2.4 | 5 | mean short openers |
| 08 | 4,555 | 14.2 | 10.5 | 22% | 0.0 | 2.6 | 0.4 | 3 | short |
| 09 | 3,550 | 11.3 | 8.9 | 28% | 0.0 | 2.8 | 0.0 | 3 | mean short |
| 10 | 3,811 | 15.2 | 11.3 | 18% | 0.0 | 2.9 | 0.0 | 3 | short |

Targets: mean 13–18 with real spread; ≤5-word sentences under 15%; codes under 2/1k; numerals under 12/1k; all-caps under 6/1k; no four sentences in a row with the same opener.

## 3. AI-fiction tells

### Hard bans (remove outright)

- none

### Mood words per 1,000 (count; flag a cluster, not a word)

- quiet: 11 (0.3/1k)
- humm?(ing|ed)?: 6 (0.2/1k)
- softly?: 0 (0.0/1k)
- still(ness)?: 62 (1.8/1k)
- ghost(ly)?: 0 (0.0/1k)
- echo(ed|es)?: 0 (0.0/1k)
- shadow: 7 (0.2/1k)
- whisper: 1 (0.0/1k)
- shimmer: 0 (0.0/1k)
- flicker: 0 (0.0/1k)
- glint: 0 (0.0/1k)
- spectral: 0 (0.0/1k)
- fragile: 0 (0.0/1k)

### Phrases (count, whole book; any 3+ is worth a look)

- 1× let out a breath

### Constructions against Part 3 caps

| Construction | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | Total | /1k | Cap | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| as if / as though | 0 | 1 | 1 | 3 | 1 | 2 | 1 | 0 | 0 | 2 | 11 | 0.3 | 1.0/1k |  |
| the way (a|the|people|someone) ... | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 1 | 5 | 0.1 | 1/ch | FLAG |
| the kind of ... that | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 2/ch |  |
| with the (precision|care...) of someone who | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| not because ... but because | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| contrast construction (not X but Y / wasn't X. It was Y) | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 4 | 0.1 | 0.0/1k | FLAG |
| sentence-initial And/But/And yet | 4 | 1 | 4 | 1 | 2 | 0 | 1 | 7 | 1 | 0 | 21 | 0.6 | 3.0/1k |  |
| em dashes | 7 | 8 | 12 | 6 | 9 | 14 | 20 | 10 | 9 | 10 | 105 | 3.0 | 2.0/1k | FLAG |
| semicolons | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 8 | 0.2 | 2.0/1k |  |
| perception filter (she noticed / could hear) | 2 | 3 | 5 | 1 | 3 | 0 | 1 | 1 | 1 | 3 | 20 | 0.6 | 1.0/1k |  |
| one-sentence paragraph | 24 | 27 | 25 | 27 | 37 | 33 | 32 | 37 | 40 | 22 | 304 | 8.8 | report |  |

### Scene cluster check (3+ tell groups in one scene → rewrite the scene, not the sentence)

- Ch 04 scene 5 (333 words): FLAG mood(2), body(1), explain(2)
- Ch 09 scene 2 (327 words): FLAG similes(1), mood(3), body(1)
