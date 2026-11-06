# Audit — ten-days-out (chapters 01–18, 38,688 words)

Source: `docs/ai-fiction-tells.md` Parts 2, 3, 5 and `docs/postmortem-boring.md` C. Counts are regex and approximate; judge flagged items by function. FLAG means over cap.

## 1. Repetition

### Motif list (bible caps, whole book)

| Motif | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | Total | Cap | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| "Dollar says" (Dane's bet) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 3 | 4 |  |
| "I don't bet" (Beth's answer) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "Different ocean" (Ch 01) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "The right boots" (Ch 18) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |  |
| Fudge (the boot store) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "The government" as a person (three uses of the bit; Ch 01's exchange is one use with three hits) | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 6 |  |
| "Keeping count" | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Forty-one" | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Ice cube with opinions" | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "I jumped" | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "Fell toward the boat" | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Disappointing kit" | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "Good till next August" | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |  |
| "Four seventy-nine" | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| Receipt | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Load-bearing" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "This is medical" | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Best medical" | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| The ham (tin, eleven pounds, Thanksgiving) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 7 | 9 |  |
| "Eleven pounds" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 2 |  |
| "Ask me in five days" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Ask me again in ten days" (Ch 01) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "Tess doesn't count" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |  |
| "Who'd I tell" (Russ) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "Ask for ID" (Tess) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |  |
| "You're the other one" (Ch 15) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "Till then you bail" (Ch 18) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |  |
| "Here's how this goes" (Dane) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Talk to me" (Dane) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 | 5 |  |
| "Ms. Calloway" (Dane, first night and angry) | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 8 |  |
| "Okay" (Dane, at most once a chapter; Beth never as a pivot) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 18 |  |
| "Bethie" (Ned only) | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 9 | 10 |  |
| "Your marshal" (Ned, Tess) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 3 |  |
| Ned looks back | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 8 |  |
| Gloves off | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 5 |  |
| Bare-handed | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 6 |  |
| The boy she taught to row | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 5 |  |
| Split lip (the kid) | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |  |
| Good coat (the lawyer) | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 5 |  |
| Reading glasses | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Somebody told him" | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "You came down" (Ch 16 payoff) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |
| "You stopped talking" (Ch 16 payoff) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |  |
| "Ten days" (title phrase) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 6 |  |
| "Her eyes are the case" | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Open sand" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  |
| "Good blanket" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |  |
| "Says he walks" / "Cole walks" (the clock) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |  |
| "Emergency protection" | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |  |

### Frequent 3–5 word n-grams (4+ uses, whole book)

- 19× “the harbor road”
- 15× “the kid's phone”
- 12× “his boss said”
- 12× “the town office”
- 11× “on the harbor road”
- 10× “a long time”
- 10× “the north beach”
- 9× “the white water”
- 9× “the harbor mouth”
- 8× “the whole way”
- 8× “i'm going to”
- 8× “her coat pocket”
- 8× “the big boat”
- 7× “she had never”
- 7× “had never once”
- 7× “and said nothing”
- 7× “the grand jury”
- 7× “came up through”
- 7× “dane took the”
- 7× “the coast guard”
- 6× “voice came out”
- 6× “in both hands”
- 6× “against his chest”
- 6× “the man had”
- 6× “beth said and”
- 6× “the car deck”
- 6× “dane said and”
- 6× “he could see”
- 6× “her left hand”
- 6× “the east road”
- 6× “the north-side house”
- 6× “the kid had”
- 5× “her voice came”
- 5× “with both hands”
- 5× “both hands on”
- 5× “she thought about”
- 5× “through the snow”
- 5× “put his hand”
- 5× “let go of”
- 5× “took her hand”

### Body-reaction words per 1,000 (tells 4.3; cluster matters, not any one)

- jaw: 5 (0.1/1k)
- knuckles?: 1 (0.0/1k)
- throat: 7 (0.2/1k)
- reath: 23 (0.6/1k)
- pulse: 2 (0.1/1k)
- chest: 23 (0.6/1k)
- hands? (stopped|stilled|went still|flat): 8 (0.2/1k)
- shoulders?: 47 (1.2/1k)
- gaze: 0 (0.0/1k)
- tightened: 1 (0.0/1k)
- swallowed: 0 (0.0/1k)

## 2. Ear (read-aloud check)

| Ch | Words | Mean sent. | SD | ≤5-word share | Codes/1k | Numerals/1k | ALLCAPS/1k | Max opener run | Flags |
|---|---|---|---|---|---|---|---|---|---|
| 01 | 2,506 | 11.8 | 9.3 | 34% | 0.0 | 0.4 | 0.0 | 3 | mean short |
| 02 | 2,242 | 10.8 | 7.1 | 26% | 0.0 | 0.0 | 0.0 | 3 | mean short |
| 03 | 2,112 | 12.8 | 9.8 | 25% | 0.0 | 0.0 | 0.0 | 2 | mean short |
| 04 | 2,507 | 11.2 | 7.6 | 27% | 0.0 | 0.0 | 0.0 | 2 | mean short |
| 05 | 1,854 | 12.0 | 7.6 | 22% | 0.0 | 0.0 | 0.0 | 3 | mean short |
| 06 | 1,854 | 13.0 | 7.4 | 15% | 0.0 | 0.0 | 0.0 | 3 | mean |
| 07 | 2,371 | 11.9 | 8.4 | 26% | 0.0 | 0.0 | 0.0 | 3 | mean short |
| 08 | 1,953 | 13.9 | 10.3 | 19% | 0.0 | 0.0 | 0.0 | 2 | short |
| 09 | 2,092 | 14.1 | 10.2 | 20% | 0.0 | 0.0 | 0.0 | 4 | short openers |
| 10 | 2,466 | 14.3 | 10.4 | 15% | 0.0 | 0.4 | 0.0 | 3 |  |
| 11 | 1,992 | 13.0 | 9.0 | 18% | 0.0 | 0.0 | 0.0 | 3 | short |
| 12 | 2,096 | 12.4 | 8.3 | 23% | 0.0 | 0.0 | 0.0 | 4 | mean short openers |
| 13 | 2,031 | 11.9 | 8.4 | 24% | 0.0 | 0.0 | 0.0 | 2 | mean short |
| 14 | 2,048 | 13.4 | 7.8 | 18% | 0.0 | 0.0 | 0.0 | 2 | short |
| 15 | 1,987 | 12.4 | 8.6 | 22% | 0.0 | 0.0 | 0.0 | 2 | mean short |
| 16 | 2,310 | 11.5 | 8.2 | 25% | 0.0 | 0.0 | 0.0 | 4 | mean short openers |
| 17 | 2,185 | 13.2 | 10.0 | 19% | 0.0 | 0.0 | 0.0 | 3 | short |
| 18 | 2,082 | 12.5 | 7.5 | 19% | 0.0 | 0.0 | 0.0 | 3 | mean short |

Targets: mean 13–18 with real spread; ≤5-word sentences under 15%; codes under 2/1k; numerals under 12/1k; all-caps under 6/1k; no four sentences in a row with the same opener.

## 3. AI-fiction tells

### Hard bans (remove outright)

- none

### Mood words per 1,000 (count; flag a cluster, not a word)

- quiet: 20 (0.5/1k)
- humm?(ing|ed)?: 2 (0.1/1k)
- softly?: 0 (0.0/1k)
- still(ness)?: 87 (2.2/1k)
- ghost(ly)?: 0 (0.0/1k)
- echo(ed|es)?: 0 (0.0/1k)
- shadow: 1 (0.0/1k)
- whisper: 1 (0.0/1k)
- shimmer: 0 (0.0/1k)
- flicker: 0 (0.0/1k)
- glint: 0 (0.0/1k)
- spectral: 0 (0.0/1k)
- fragile: 0 (0.0/1k)

### Phrases (count, whole book; any 3+ is worth a look)

- 5× for the first time

### Constructions against Part 3 caps

| Construction | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | Total | /1k | Cap | |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| as if / as though | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 9 | 0.2 | 1.0/1k |  |
| the way (a|the|people|someone) ... | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0.1 | 1/ch |  |
| the kind of ... that | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 2/ch |  |
| with the (precision|care...) of someone who | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| not because ... but because | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0 | 1/ch |  |
| contrast construction (not X but Y / wasn't X. It was Y) | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 0.2 | 0.0/1k | FLAG |
| sentence-initial And/But/And yet | 5 | 3 | 1 | 1 | 2 | 1 | 0 | 3 | 1 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 1 | 1 | 24 | 0.6 | 3.0/1k |  |
| em dashes | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 10 | 0.3 | 2.0/1k |  |
| semicolons | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0.1 | 2.0/1k |  |
| perception filter (she noticed / could hear) | 0 | 0 | 1 | 3 | 1 | 3 | 0 | 0 | 2 | 3 | 1 | 0 | 0 | 0 | 1 | 4 | 1 | 0 | 20 | 0.5 | 1.0/1k |  |
| one-sentence paragraph | 16 | 27 | 35 | 34 | 20 | 14 | 40 | 20 | 27 | 36 | 41 | 22 | 19 | 23 | 27 | 30 | 25 | 28 | 484 | 12.5 | report |  |

### Scene cluster check (3+ tell groups in one scene → rewrite the scene, not the sentence)


## 4. Jargon (words a reader with no boat, court, police or trade experience won't know)

Caps: at most 2 distinct terms in the book's first 1,000 words; at most 6 distinct terms and 3 uses per 1,000 words in any chapter. A term the page explains in plain words the first time can be removed in the book's `jargon.txt` with a leading `-`. The plot-critical facts (what was found, who is in danger, what happens if they fail) must be in plain words whatever this count says.

- First 1,000 words: 0 distinct (none) 

| Ch | Distinct | Uses | /1k | Top terms | |
|---|---|---|---|---|---|
| 01 | 1 | 1 | 0.4 | grand jury 1 |  |
| 02 | 2 | 5 | 2.2 | skiff 3, grand jury 2 |  |
| 03 | 1 | 2 | 0.9 | choke 2 |  |
| 04 | 0 | 0 | 0.0 |  |  |
| 05 | 0 | 0 | 0.0 |  |  |
| 06 | 0 | 0 | 0.0 |  |  |
| 07 | 2 | 2 | 0.8 | ledges? 1, grand jury 1 |  |
| 08 | 3 | 5 | 2.6 | hatch 2, grand jury 2, ledges? 1 |  |
| 09 | 0 | 0 | 0.0 |  |  |
| 10 | 2 | 7 | 2.8 | skiff 6, ledges? 1 |  |
| 11 | 1 | 2 | 1.0 | skiff 2 |  |
| 12 | 0 | 0 | 0.0 |  |  |
| 13 | 1 | 1 | 0.5 | ledges? 1 |  |
| 14 | 2 | 2 | 1.0 | stern(man)? 1, hatch 1 |  |
| 15 | 2 | 5 | 2.5 | ledges? 3, hatch 2 |  |
| 16 | 2 | 5 | 2.2 | ledges? 4, grand jury 1 |  |
| 17 | 1 | 1 | 0.5 | grand jury 1 |  |
| 18 | 0 | 0 | 0.0 |  |  |
