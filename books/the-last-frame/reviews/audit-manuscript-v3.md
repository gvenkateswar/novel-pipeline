# Audit — the-last-frame (chapters 01–11, 32,362 words)

Source: `docs/ai-fiction-tells.md` Parts 2, 3, 5 and `docs/postmortem-boring.md` C. Counts are regex and approximate; judge flagged items by function. FLAG means over cap.

## 1. Repetition

### Motif list (bible caps, whole book)

| Motif | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | Total | Cap | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ellen counting the room (Ch 1, 3, 9 only) | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 3 |  |
| Headcount phrasing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "I'm aware" (anger only) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| "No readback" (Ch 3 thought, Ch 7 spoken) | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |  |
| Readback, the noun | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 4 |  |
| Read (it) back, the verb | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 4 |  |
| The D-side | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 3 | 3 |  |
| Denise's crossword | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| "honey" (Denise, before something hard) | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 4 | 4 |  |
| Denise's "You'll live" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| The sign's buzz | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |  |
| The dead K | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |  |
| Ettle / Ettle's | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| Hollis's cap | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 3 |  |
| Ray's key ring | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |  |
| Holding out the key | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |  |
| "Not yet" (Ch 8's line) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 3 |  |
| "upside down" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "without looking" | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 3 |  |
| "didn't look up" | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| Block capitals | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| Masking tape | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |  |
| "forty minutes" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "thirty-one years" | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 3 |  |
| Thirty-one, every use | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 7 |  |
| Marble cake | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "eight days" | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 3 |  |
| Two in the morning (the 2 a.m. night) | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 4 | 4 |  |
| Separation (incl. Ch 7 title) | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 5 |  |
| "Understood." (Ellen hurt) | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 5 | 4 | FLAG |
| Story about some other fella | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 3 |  |
| "fella," any use | 0 | 2 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 5 | 8 |  |
| Knuckle on the trophy glass | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Mrs. Daly" (once a chapter at most) | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 5 | 10 |  |
| "Linda wouldn't have" (before Ch 7) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "unless the numbers say otherwise" | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 6 |  |
| "The wood stays on the lane" (Ch 4 only) | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| deadwood (never a metaphor) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| Machines sulking | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "a quarter past five" | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 3 | 3 |  |
| American chop suey | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| "Scale of one to ten" | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 3 | 3 |  |
| "The Pines doesn't take half" | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "Voyons donc" | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| Licked thumb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 2 |  |
| Gloves off | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 |  |
| Breath on his wrist | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| Ray's voice, unhurried | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| Pilot (Ray's voice as a 3 a.m. pilot's) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |  |
| "Stay on the step" / the step | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 3 | 3 |  |
| Pencil behind the ear | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| Glasses on the forehead | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 2 |  |
| The pool sheet | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 |  |
| Locker fourteen | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 5 |  |
| Linda's 187 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 |  |
| Crash like wooden spoons | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| Chair dragged (the table's sound) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Traffic, twelve o'clock, one mile" | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "That's the bell" | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Coffee's on" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "Holy mackerel" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |  |
| "Ayuh" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "For Pete's sake" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| Ellen waking at ten to four | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 |  |
| "twenty-eight thousand nine hundred" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |
| "Both words" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | FLAG |

### Frequent 3–5 word n-grams (4+ uses, whole book)

- 9× “the snack bar”
- 9× “the glass block”
- 8× “behind the counter”
- 8× “the scorer's table”
- 7× “in both hands”
- 7× “the first time”
- 7× “all ten lanes”
- 7× “end of the counter”
- 7× “the first of march”
- 6× “the front door”
- 6× “five and six”
- 6× “had an answer”
- 6× “at the far end”
- 6× “last saturday in february”
- 5× “through the glass”
- 5× “the steel door”
- 5× “let go of”
- 5× “under the register”
- 5× “i'd like to”
- 5× “a long time”
- 5× “the highway crew”
- 5× “her vest pocket”
- 5× “the far register”
- 5× “before he could”
- 5× “did not move”
- 5× “he said that's”
- 5× “did not look”
- 5× “she had never”
- 5× “had never once”
- 5× “she had said”
- 5× “did not say”
- 5× “linda's name on”
- 5× “the first night”
- 5× “at a quarter past”
- 5× “at the scorer's table”
- 5× “the end of the counter”
- 5× “the last saturday in february”
- 4× “on march first”
- 4× “the inner door”
- 4× “lane six and”

### Body-reaction words per 1,000 (tells 4.3; cluster matters, not any one)

- jaw: 2 (0.1/1k)
- knuckles?: 11 (0.3/1k)
- throat: 0 (0.0/1k)
- reath: 11 (0.3/1k)
- pulse: 0 (0.0/1k)
- chest: 3 (0.1/1k)
- hands? (stopped|stilled|went still|flat): 5 (0.2/1k)
- shoulders?: 24 (0.7/1k)
- gaze: 0 (0.0/1k)
- tightened: 1 (0.0/1k)
- swallowed: 0 (0.0/1k)

## 2. Ear (read-aloud check)

| Ch | Words | Mean sent. | SD | ≤5-word share | Codes/1k | Numerals/1k | ALLCAPS/1k | Max opener run | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 01 | 3,301 | 20.5 | 19.1 | 17% | 0.0 | 0.6 | 0.0 | 2 | mean short |
| 02 | 2,975 | 18.1 | 13.4 | 18% | 0.0 | 0.3 | 0.7 | 2 | mean short |
| 03 | 3,245 | 17.7 | 14.0 | 14% | 0.0 | 0.3 | 0.0 | 3 |  |
| 04 | 2,980 | 17.5 | 14.0 | 14% | 0.0 | 0.3 | 0.0 | 3 |  |
| 05 | 2,905 | 18.5 | 12.4 | 13% | 0.0 | 0.3 | 0.0 | 4 | mean openers |
| 06 | 3,041 | 17.3 | 11.7 | 14% | 0.0 | 0.3 | 0.0 | 2 |  |
| 07 | 3,193 | 17.0 | 12.3 | 14% | 0.0 | 0.3 | 0.3 | 4 | openers |
| 08 | 3,227 | 16.7 | 11.1 | 16% | 0.0 | 0.3 | 0.0 | 3 | short |
| 09 | 3,115 | 14.2 | 10.0 | 16% | 0.0 | 0.3 | 0.0 | 3 | short |
| 10 | 3,524 | 15.1 | 10.5 | 19% | 0.0 | 0.3 | 0.0 | 3 | short |
| 11 | 856 | 12.2 | 7.8 | 20% | 0.0 | 0.0 | 0.0 | 2 | mean short |

Targets: mean 13–18 with real spread; ≤5-word sentences under 15%; codes under 2/1k; numerals under 12/1k; all-caps under 6/1k; no four sentences in a row with the same opener.

## 3. AI-fiction tells

### Hard bans (remove outright)

- none

### Mood words per 1,000 (count; flag a cluster, not a word)

- quiet: 16 (0.5/1k)
- humm?(ing|ed)?: 3 (0.1/1k)
- softly?: 0 (0.0/1k)
- still(ness)?: 75 (2.3/1k)
- ghost(ly)?: 0 (0.0/1k)
- echo(ed|es)?: 0 (0.0/1k)
- shadow: 0 (0.0/1k)
- whisper: 0 (0.0/1k)
- shimmer: 0 (0.0/1k)
- flicker: 0 (0.0/1k)
- glint: 0 (0.0/1k)
- spectral: 0 (0.0/1k)
- fragile: 0 (0.0/1k)

### Phrases (count, whole book; any 3+ is worth a look)

- 2× for the first time
- 1× not quite

### Constructions against Part 3 caps

| Construction | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | Total | /1k | Cap | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| as if / as though | 0 | 0 | 1 | 0 | 2 | 1 | 3 | 0 | 0 | 0 | 0 | 7 | 0.2 | 1.0/1k |  |
| the way (a|the|people|someone) ... | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| the kind of ... that | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 2/ch |  |
| with the (precision|care...) of someone who | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| not because ... but because | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| contrast construction (not X but Y / wasn't X. It was Y) | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0.0 | 0.0/1k | FLAG |
| sentence-initial And/But/And yet | 2 | 1 | 1 | 1 | 2 | 0 | 2 | 2 | 3 | 1 | 0 | 15 | 0.5 | 3.0/1k |  |
| em dashes | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 3 | 0 | 0 | 7 | 0.2 | 2.0/1k |  |
| semicolons | 3 | 0 | 1 | 1 | 1 | 3 | 1 | 0 | 1 | 0 | 0 | 11 | 0.3 | 2.0/1k |  |
| perception filter (she noticed / could hear) | 1 | 0 | 0 | 1 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 7 | 0.2 | 1.0/1k |  |
| one-sentence paragraph | 6 | 23 | 20 | 18 | 18 | 24 | 15 | 16 | 30 | 33 | 13 | 216 | 6.7 | report |  |

### Scene cluster check (3+ tell groups in one scene → rewrite the scene, not the sentence)

