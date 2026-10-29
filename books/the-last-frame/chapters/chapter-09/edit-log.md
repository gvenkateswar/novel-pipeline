---
## Edit log

Draft edited: `draft-dialogue.md` (prose ends before "## Revision notes"), October 29, 2026. Voice pass against Ellen's syntax profile and the bible's quiet and high registers. Read for voice: Ch 07 `final.md` (Ellen as last written), the bible's Ellen profile, motif list, forbidden phrases, `docs/ai-fiction-tells.md` Parts 3, 4.3, 4.4, 6.

**Word count (`wc -w final.md`, heading included): 2,995.** The draft was 2,957; the ceiling is 3,024. By scene, counted from `final.md` (heading excluded from s1): s1 about 930 (floor 800), s2 706, s3 1,022 (floor 700), s4 323. The scene counts run higher than the earlier estimates in the dialogue doctor's notes because those were estimated by delta.

Audit (`tools/audit.py --through 09`): Ch 09 is clean on the motif caps (D-side 3 of 3, quarter past five 1, chop suey 1, readback 1, read it back 1, pilot 1, scale of one to ten 1), contrast constructions 0, "the way" 0, "as if" 0, perception filter 0, hard bans none, mean sentence 17.1 words (SD 14.6), numerals 0.3/1k, codes 0. One flag remains: the share of sentences of five words or fewer is 19% against a 15% target. Almost all of it is dialogue: the protected D-side and readback lines, the briefing's item headings, Denise's "It is not.", Kate's interruptions and the "Ask." exchange. I merged the narration shorts I could. Cutting more would mean touching protected lines or Denise's and Kate's shapes. Flagged for the orchestrator, not for the writer.

### Protected lines: checked word for word against `draft-dialogue.md`
- The briefing, the D-side definition, "I keep the position. I want you on it with me. Today, and after today, whatever Monday says.", "Read it back to me. I want to hear it in your voice.", Ray's full readback, "And I'm on it with you. Today, and after today, whatever Monday says.", "And you haven't sat down since Hollis called.", "Readback correct."
- "Seventeen hundred and fifteen dollars under thirty thousand. Sunday can't bring that much."
- "Ask." / "Ask who?"
- "Scale of one to ten." / "Ten."
- "Then do it. And call me first next time. Like this."
- "What do you make the second night?" / "That one."
- The knee exchange, "I'll allow it." and "By one minute." are also untouched.

### Added life
- **s1, the hands (interior passage 1):** the sentence now carries a new detail, "a black crescent under one nail that no soap had got out", and runs long before it lands on "She went on looking." It replaces "nicked white across the knuckles", which sat too near Ch 07's nicked fingers and the "red across the knuckles" detail. It is one sentence, with no list collapse and no remark on order.
- **s1, the lamp:** "out of long habit" replaces "out of thirty years' habit", because "thirty years" was already in the paragraph above.
- **s2, interior passage 2:** the closing line is now "She had given briefings all her working life, and at the treasurer she would have liked another item." It is Ellen's literal humor turned on her own briefing, and it carries the want without announcing it. It replaces "She had never wanted one to go on", which labelled the feeling.
- **s3, the room:** one sensory line added where the scene had none, "the whole room smelling of wet wool and road salt over the fryer" (the beat sheet's anchor).
- **s3, the envelopes (interior passage 3):** the interior now runs faster under the courtesy. "Under it she was taking each one off a number she had carried all month, this one and this one, with Monday two days off and the bar sitting where the bank had set it, and she heard herself wish the fifth captain a safe drive in exactly the voice she had used on the first." The gap between voice and interior is shown by the voice being identical for the fifth captain. No dollar figure, and no repeat of the cushion (Ch 08 had already spent it).
- **s3, the auger man:** Ellen's answer is now the literal one to the question as asked. "Which one of you's got my auger?" / "Neither of us. It is by the shoe cubbies, with the bow on." This is her deadpan literalism from the profile. It also pays the "by the shoe cubbies" set up two paragraphs earlier.

### Voice
- s3, the auger answer: "The counter has it. It is the one thing in this building today nobody has asked to have back." → "Neither of us. It is by the shoe cubbies, with the bow on." The old line said nobody had asked for anything back, and the man standing in front of her had just asked. It also made Ellen's wit a comment, where the profile makes it an answer.
- s3 PA: "pulled the gooseneck down and keyed it" → "bent the gooseneck to her and keyed it". Ch 07 used the first form, and the hum-first PA.
- s2: Ray's "didn't move" → "did not move". Ellen's narration carries no contractions in the procedure scene, and none were earned there.
- s1: Ellen's contractions stay only where the dialogue doctor placed them (the supper line, "can't" in the protected D-side definition, "I'll" in s1, free in s4).

### Tells (`docs/ai-fiction-tells.md` item numbers)
- **#62/#37 (contrast, gloss):** s2 "never been sorry to reach the end of one. She was sorry when he got to the treasurer." was a contrast pair and also a feeling label. It is now the "another item" line above (see Added life).
- **#42 (perception filters):** s3 "She could hear that it did not." restated the sentence before it and used a filter → folded into "and she listened the whole way for it to." s4 "long enough for Ellen to hear the refrigerator in Manchester" → "long enough that the refrigerator in Manchester came through the line."
- **Motif regex catch:** s1 "before her knuckle reached the glass" would have scored as the Ray knuckle-on-glass motif (cap 3, one spent in Ch 1) → "before her hand came down to the glass".
- **#66 (rhythm, openers):** s1 had three consecutive paragraphs opening "He had" → "The invitation had come in pencil", "Ray ducked the lamp", "Two bowls that did not match waited on the table".
- **#37 (gesture, decode):** none of the decoded gestures remain. "Denise looked past them at the trophy case, and put the fryer basket down on the counter." and "Ray put his hand on the lid of the cash box and closed it, and kept his hand there." are left undecoded.
- **Logic repair, s4:** "She could have wired the money Monday and told Kate on Sunday night, in order, after." put the telling before the wiring but said "after". It is now "She could have waited for Sunday at seven and told Kate in order, after." This matches Kate's "You call Sundays. At seven." and Ellen's "Then you'll get your call on Sunday at seven."
- **Geometry, s1 ending:** the radio sits on top of the refrigerator, and Ray was seated, so "his arm long enough for it" would not reach. He now stands with her bowl in one hand and reaches up with the other. The ending stays mid-action on the dial.
- **s2 "by ten" removed:** "She had come along the catwalk from the steel door by ten" read as lane ten or as the hour. Now "from the steel door".
- **s3 "red from the lot":** ambiguous between jacket and face → "red in the face from the lot".

### Carried over: dialogue doctor's revision notes (still true unless marked)
- Issue 1 (s2): Ray's readback reads "And I'm on it with you." "D-side" is 3 (title, Ellen's definition, Ray's s3 line). ATC phrases: s2 five (relief briefing, item headings, D-side, read it back, readback correct), s3 one, total six.
- Issue 2 (s2): "Three's been coming round slow since your party Saturday, and I let that ride." Three stays an "it/three" there, so the readback is the first place he calls three "she".
- Issue 3 (s1): "Six years she's cooked for one."
- Issue 4 (s2): "Read it back" tagged as Ellen's; the readback opens on Ray's beat with the beam.
- Issue 5 (s1): Doc Marchand.
- Issue 6 (s3): "Aunt Judy from the bank was coming at two to watch me. She'll have to come Sunday at one, then."
- Issue 7 (s3): Ellen's line is "Thirty-three in December. Today, this room, and a boiler that quits when the power does." The room count is spent in s2.
- Issue 8 (s1): bible-sample lifts removed. The details left are the radio on the refrigerator and the pot. The radio reads heating oil to the tenth of a cent. The supper beat is "heard whose word that was, and did not take it back."
- Issue 9 (s2): "can't" in the D-side definition stays, since it is inside the protected model line.
- Issue 10 (s3): "Arlene's room is on it."
- Issue 11 (s3): "His crew's out plowing till morning." / "Dale's team".
- Issue 12 (s2): "each item arriving where she had put it" is cut.
- Issue 13 (s1): she sits at the place he points to; he says nothing.

### Commitments (for the continuity log and Ch 10)
- **Machine three, said aloud:** Ray has told Ellen that three has run slow since the party Saturday (Dec 19) and that he let it ride.
- **Judy Ostrowski:** was going to watch her nephew (Legion) at the Memorial at two on Saturday, and is now coming Sunday at one. Ch 10 s1 has to have her in the building.
- **The Highway crew plows until Sunday morning** (Dale via Hollis); Dale's team misses Saturday and comes in off a night of plowing in Ch 10 s1.
- **Doc Marchand:** Ray's former doctor, now in Florida, who gave the "vary what he eats" advice about fifteen years ago. Keep it from sounding like Fortier, Normand or Normie.
- **The pot has cooked for one for six years**, which matches Linda's death. Ray's "thirty years" of the same supper still stands.
- **Ray has seen Ellen sit to eat at his table** (Wed Feb 24). Neither said so.
- **The room count is spent in s2** (the bible's three: Ch 1, Ch 3, Ch 9 s2).
- **The radio reads heating oil prices to the tenth of a cent** on Ray's kitchen radio. One-off, not a motif.
- **New, from this pass:** the raffle winner asks for his auger and Ellen answers "Neither of us. It is by the shoe cubbies, with the bow on." He leaves with it on his shoulder toward a lake that is closed. The auger is gone from the building and cannot come back in Ch 10.
- **Motifs spent this chapter:** "D-side" 3 of 3 (Ch 10 gets zero); "read it back" and "readback" each once; "a quarter past five" once; "chop suey" once; "pilot" once; "Scale of one to ten" once (2 of 3 in the book); "supper" in Ellen's mouth once.
- **The Open's evening cup:** still open for Ch 10. Nothing on the page here.
- **For the Ch 10 architect, repeated from the beat sheet:** with the corrected chain Sunday has to bring about $615 for $28,900 / $8,800 / $5,200 to stand. Ch 09 states no Sunday figure.

### Tag-strip test
Pass. Ellen: full stops, exact numbers, imperatives under fear ("Draw it now.", "Nobody comes back up that drive tonight."), literal answers ("Neither of us."), items. Ray: and-chains with the weight last, the pot and the machine as "she", teasing her exactness, dating time by what broke (the dock). Hollis: measurements and a closing question. Denise: run-ons that answer themselves, and she is the only one who does it. Kate: fast, clinical, interrupts herself. The treasurer, the Legion boy and the auger man are one line each in their own registers.

### Flagged for writer
- Nothing at plot level. The only structural flag is the ≤5-word share (19%), which is carried by protected and voice-bearing dialogue (see above).

### Pairs for the pipeline
- Stop: writing a motif's regex pattern into an unrelated action (a knuckle reaching the door glass). Do instead: grep the motif list against a new scene's props before the draft goes to the voice editor.
- Stop: a stage direction that puts a seated man's reach above head height (the radio on the refrigerator). Do instead: put the character on his feet before the mid-action ending.
