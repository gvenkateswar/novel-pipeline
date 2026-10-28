# Audit — the-last-frame (chapters 01–10, 32,888 words)

Source: `docs/ai-fiction-tells.md` Parts 2, 3, 5 and `docs/postmortem-boring.md` C. Counts are regex and approximate; judge flagged items by function. FLAG means over cap.

## 1. Repetition

_No `## MOTIF LIST` table in story-bible.md; motif caps skipped. Add one (| name | regex | cap |) so this section can run._

### Frequent 3–5 word n-grams (4+ uses, whole book)

- 17× “the snack bar”
- 15× “the highway department”
- 14× “all ten lanes”
- 11× “ellen looked at”
- 11× “the far end”
- 11× “the adding machine”
- 10× “the scorer's table”
- 10× “her vest pocket”
- 10× “the pit door”
- 10× “the drop light”
- 9× “the trophy case”
- 9× “the strip board”
- 9× “ellen looked at the”
- 8× “last saturday in february”
- 7× “gagnon and son”
- 7× “the steel door”
- 7× “ray looked at”
- 7× “the steel desk”
- 7× “at the far end”
- 7× “the end of the counter”
- 6× “the vestibule door”
- 6× “under the register”
- 6× “the lakeview diner”
- 6× “across the deck”
- 6× “linda gagnon memorial”
- 6× “the coffee pot”
- 6× “across the counter”
- 6× “let it go”
- 6× “she had said”
- 6× “by the pit door”
- 5× “in green ink”
- 5× “the counter denise”
- 5× “ellen said the”
- 5× “the sweep came”
- 5× “behind his ear”
- 5× “ellen said and”
- 5× “the counter lights”
- 5× “across the top”
- 5× “behind the register”
- 5× “the pool sheet”

### Body-reaction words per 1,000 (tells 4.3; cluster matters, not any one)

- jaw: 1 (0.0/1k)
- knuckles?: 7 (0.2/1k)
- throat: 0 (0.0/1k)
- reath: 5 (0.2/1k)
- pulse: 0 (0.0/1k)
- chest: 3 (0.1/1k)
- hands? (stopped|stilled|went still|flat): 6 (0.2/1k)
- shoulders?: 16 (0.5/1k)
- gaze: 0 (0.0/1k)
- tightened: 1 (0.0/1k)
- swallowed: 0 (0.0/1k)

## 2. Ear (read-aloud check)

| Ch | Words | Mean sent. | SD | ≤5-word share | Codes/1k | Numerals/1k | ALLCAPS/1k | Max opener run | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 01 | 3,735 | 12.7 | 9.0 | 23% | 0.8 | 14.2 | 9.9 | 3 | mean short numerals caps |
| 02 | 3,210 | 11.7 | 8.0 | 27% | 1.2 | 6.2 | 9.3 | 2 | mean short caps |
| 03 | 3,287 | 12.3 | 9.6 | 28% | 2.7 | 14.0 | 16.1 | 3 | mean short codes numerals caps |
| 04 | 3,352 | 11.9 | 8.2 | 21% | 0.3 | 15.2 | 2.1 | 3 | mean short numerals |
| 05 | 3,016 | 12.3 | 8.1 | 26% | 1.3 | 16.6 | 5.3 | 2 | mean short numerals |
| 06 | 3,616 | 12.2 | 8.7 | 21% | 0.3 | 5.3 | 6.1 | 3 | mean short caps |
| 07 | 3,338 | 11.4 | 7.5 | 24% | 0.0 | 7.2 | 2.4 | 3 | mean short |
| 08 | 3,678 | 13.0 | 8.8 | 21% | 2.2 | 13.6 | 5.7 | 3 | short codes numerals |
| 09 | 3,660 | 12.8 | 8.1 | 18% | 1.9 | 18.9 | 4.1 | 3 | mean short numerals |
| 10 | 1,996 | 11.0 | 8.5 | 27% | 2.5 | 10.0 | 14.0 | 3 | mean short codes caps |

Targets: mean 13–18 with real spread; ≤5-word sentences under 15%; codes under 2/1k; numerals under 12/1k; all-caps under 6/1k; no four sentences in a row with the same opener.

## 3. AI-fiction tells

### Hard bans (remove outright)

- none

### Mood words per 1,000 (count; flag a cluster, not a word)

- quiet: 8 (0.2/1k)
- humm?(ing|ed)?: 10 (0.3/1k)
- softly?: 0 (0.0/1k)
- still(ness)?: 57 (1.7/1k)
- ghost(ly)?: 1 (0.0/1k)
- echo(ed|es)?: 0 (0.0/1k)
- shadow: 0 (0.0/1k)
- whisper: 0 (0.0/1k)
- shimmer: 0 (0.0/1k)
- flicker: 0 (0.0/1k)
- glint: 0 (0.0/1k)
- spectral: 0 (0.0/1k)
- fragile: 0 (0.0/1k)

### Phrases (count, whole book; any 3+ is worth a look)

- 1× for the first time

### Constructions against Part 3 caps

| Construction | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | Total | /1k | Cap | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| as if / as though | 2 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 5 | 0.2 | 1.0/1k |  |
| the way (a|the|people|someone) ... | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0.0 | 1/ch |  |
| the kind of ... that | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 2/ch |  |
| with the (precision|care...) of someone who | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| not because ... but because | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| contrast construction (not X but Y / wasn't X. It was Y) | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0.1 | 0.0/1k | FLAG |
| sentence-initial And/But/And yet | 1 | 2 | 4 | 1 | 0 | 2 | 1 | 3 | 1 | 2 | 17 | 0.5 | 3.0/1k |  |
| em dashes | 1 | 2 | 1 | 0 | 1 | 7 | 5 | 5 | 3 | 1 | 26 | 0.8 | 2.0/1k |  |
| semicolons | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0.0 | 2.0/1k |  |
| perception filter (she noticed / could hear) | 0 | 1 | 2 | 1 | 0 | 3 | 2 | 0 | 0 | 0 | 9 | 0.3 | 1.0/1k |  |
| one-sentence paragraph | 25 | 40 | 27 | 26 | 34 | 48 | 51 | 33 | 36 | 25 | 345 | 10.5 | report |  |

### Scene cluster check (3+ tell groups in one scene → rewrite the scene, not the sentence)

