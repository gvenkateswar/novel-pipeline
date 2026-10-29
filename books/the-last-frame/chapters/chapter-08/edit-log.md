# Chapter 8 edit log

## Edit log
Draft edited: draft-dialogue.md, Oct 29, 2026 (voice pass, Ray's POV, warm register). Output: final.md.

Word count (wc -w final.md, heading included): 3,317. Draft-dialogue prose was 3,297; ceiling 3,510. Net +20.
By scene (approximate, from the break markers): s1 about 1,067 (beat target 950), s2 486 (450), s3 697 (750), s4 1,054 (target 1,100, **floor 850: held, 204 over**). s3 is the one scene under its target, and it has no floor.

### Main lines changed

- [Added life, s1, the tenth box]: the passage is now two paragraphs of long sentences that land on short ones. Added one sound (the music still playing overhead because nobody thought to turn it down, and the Highway crew stopping talking on the rail) and one hand-and-wear detail on the third ball (his thumb finds the nearer of the two worn places and sits in it). Both similes are kept ("plank somebody had laid across a ditch" on the first ball; "bundle of shovel handles going over in a back room"). Neither is a motor comparison, and there are no "the way" similes. The tenth box has no rule named and no Ellen in his head.
- [Tells, s1, 4.4 item 37]: "watching to see whether a man who'd be paid for losing would try" -> "and watched." Dale had already said the stake aloud; the clause decoded his gaze. Nothing was moved into narration.
- [Rhythm, s1]: "Ray had seen... Her pencil... Ray opened... He shaved" had two "Ray" openers in four sentences. -> "Then he opened his pocketknife".
- [Tells, s2, interior paragraph]: was six sentences, over the five-sentence cap. Now five. "since Friday" is cut (a weekday where the chapter wants no calendar), and so is "chapped white at the joints" (it repeated the red knuckles two paragraphs up). "The date was at the head of it in the hand on his counter. That hand and the other one lay side by side..." was hard to parse. -> "The date at its head was in the hand that lay on his counter now, with the other beside it a foot from his gloves, and she kept them still." The two-fingers beat and "He kept his hand on the gloves." are untouched. "Knuckles" stays once in the chapter, in a sentence with no "glass".
- [Added life, s3, a Ray joke]: after Arlene's "She takes that corner like it owes her money," Ray, with his mouth full: "Wrecker ought to set up out there and save himself the gas." It is a straight-faced tease, with the joke on the last word, aimed at a third party (his own register, engine (a)). It adds no fact. Arlene's line stays the scene's laugh, and his line is the turn into "I want off the March paper."
- [Tells, s3, the reversal gloss]: "...and he would have to put it in front of her and ask." deleted. It announced what Arlene's last line says two paragraphs later, and the scene ends on her line, with nothing from Ray. What stays: "He had come up her stair for a paper he could carry down it finished, and the last line on it was Ellen's." Ending type unchanged (consequence, said to a third party).
- [Rhythm and plain statement, s4, the door]: "loose in its putty as it always was" added to the rattle. Ray hears and knows the building, and it is not a new fact. "From a room he had not stood in tonight" -> "from a room he had not stood in". "the release in his jacket had its fold against his chest from the door to the counter" -> "he carried the release against his chest, folded, from the door to the counter."
- [Tells, s4, 4.4]: "She took it standing and let it stand, and he let her." -> "She took it standing and said nothing to it, and he let her." The stand/standing/stand echo is gone, and the line now echoes Ch 06 ("She said nothing to it.").
- [Line hygiene, s4]: the 54-word sentence about the hundred and fifteen dollars is split: "A hundred and fifteen dollars was a kids' birthday party on a Saturday with the fryer going, or most of one. He had heard her swear to her daughter, the house and not the rest, and he put the pencil back in her box and his hands in his jacket pockets."
- [Fix + voice, s4, the signing]: "She lifted the pen between the two names" was unclear (she signs once). -> "between her first name and her last". "slower than she wrote anything at her counter" put her at a counter she was standing at -> "slower than he had ever seen her write". "the knuckles of it were still chapped from the cold" -> "red still from the cold" (callback to s2, and no "knuckle"). Five sentences, so under the cap. Her printing "standing separate" stays; the pen scratch audible from the lot stays (sound first).

### The one interior line
"Whatever happened to her number now, he could not buy her building if she put the keys in his hand" is **not in draft-dialogue.md**. The dialogue pass had already cut it (it is in `draft.md` only, issue 15). It does not return. What remains is the plain line "He had not got as far as counting them, and she had." Nothing follows it. If a judge read the sentence twice, they read an earlier draft.

### Checks (run on final.md)
- Word floors: s4 1,054 against 850. Pass.
- Ending types, unchanged: s1 question ("Where'll you be?"); s2 mid-action (her hand going out for the cup); s3 consequence (Arlene's line to her lawyer); s4 question ("Not yet." with the key on her palm, nothing after).
- Counts: "Holy mackerel" 1; "Coffee's on" 1; "Not yet" 1 (last line only); "bare" 1 (s2); "the March paper" 3 (s2, s3, s4); "knuckle" 1, in a sentence with no "glass"; "as though" 1; "the way" 0. Date on the page: the third of February only. No clock openings. "Mrs. Daly" 0. No Normie. No contrast constructions found. No ATC phrases in narration.
- Ray's motor comparisons: 0. Similes in the chapter: 2, both in the tenth, both from Ray's world.
- Longest interior paragraphs: tenth box paragraphs 3 and 3 sentences (the first of the two is 3, the second 3 counting Denise's pencil); s2 interior 5; s4 signing 5. None past five.
- Ellen's one contraction: "won't" in "I won't have you standing at the bottom of my drive as well", in s4 only. Her s2 lines have none.
- Protected, untouched: every bold beat-sheet line, the three terms lines, Hollis's line as Ray's reported speech, "In fries.", the clutch line, the verbatim afraid line, Arlene's window speech (under 75 words), Normand, "First. And none of it stands without hers", the K exchange, "There are thirteen days."
- tools/audit.py ran without error. I did not read its report.

### Voice
- Tag-strip test: same as the dialogue pass. The speakers separate: Gil (long, talks over people), Dale (short, reads the book back), Hollis (measurements), Denise (run-ons with a qualifier), the end stool ("don't" for "doesn't"), Arlene (blunt, "dear", "Raymond"), Ellen (full stops, exact figures, no contractions but one), Ray (and-chains, the joke or the plain word last). The new Ray line in s3 is one and-free tease with the joke last, in the mouth that already teases.
- The hero never echoes the heroine's words as a fragment.

### Flagged for writer
- None at plot level. One for the continuity checker: "the house and not the rest" in s4 relies on Ray having heard both halves of Ellen's oath in Ch 02 (carried from the dialogue pass).
- Pattern for the pipeline: stop writing a narrator clause that tells us what a watcher is waiting to see when a character has already said the stake aloud (the "Dale watched to see whether he would try" kind). Instead end the sentence on the watcher's posture and let the next ball answer it.

---

- Issue 1 (s3): Arlene's answer is now "First. And none of it stands without hers. It's hers to risk as much as mine." Her instruction to the lawyer adds "to stand only if the third name follows". s4's page lets the three go "once the third name was on it", so there is one signing order: Arlene first, Ray under her, Ellen's line last.
- Issue 2 (s4): Ellen's line now ends "…on a hundred and fifteen dollars and a promise I made my daughter." Ray's wallet clause is gone. In its place he remembers hearing her swear to her daughter, "the house and not the rest", so he knows the money is not the point.
- Issue 3 (s4): "Nine teams entered for Linda's cup alone, and wrote her name on the form to say so."
- Issue 4 (s2): the end-stool man is the one who gets as far as "And the—". Later he "left the other two standing" and pours. He is still unnamed.
- Issue 5 (s1): "Had a dollar on Gil's man, Ray."
- Issue 6 (s1): "Dale looked at Ray's own checkbook, laid on the scorer's table."
- Issue 7 (s2): new sentence: her car was at the curb, engine off and dark inside, when he put the first light on.
- Issue 8 (s3): the window speech is cut to 75 words, the cap. "I watched it from that window" and "That paper's mine" are gone, the two-fingers beat moves before the speech, and the engine running stays. The cost speech is split by Ray's "You'd be paid, though, wouldn't you?" and the Normand speech by "He ran it eighteen years." Arlene now has one long speech.
- Issue 9 (s3): "Raymond will carry it to her himself, and he'll ask her."
- Issue 10 (s2): she has taken nothing off an invoice "since these same gloves on the ice, and those she had handed back folded one into the other". This matches Ch 06's return, and I used no month name.
- Issue 11 (s2): "and she had come before it."
- Issue 12 (s1): "the date he had watched her write at her counter, the night he worked her key off his ring." s4's "I watched you put the date on it" is kept.
- Issue 13 (s2): "with her own gloves pushed into her vest pocket and her hands bare." Her bare hands are now her choice. "bare" is used once in the chapter.
- Issue 14 (s4): "the release in his jacket."
- Issue 15 (s4): cut "Whatever happened to her number now…". The line "He had not got as far as counting them, and she had." is kept.
- Issue 16 (s3, s1): Arlene's cupboard door is now the oilcloth split at the corner by his plate "the winter her furnace quit", and he keeps his eyes "on the split in the oilcloth". The s1 tenth-box simile is now "a bundle of shovel handles going over in a back room". The chapter has no cupboard left in it.
- Issue 17: the author's call. No change to the page.

## Commitments

- Ch 08 s4 now says the cost of the release aloud: a hundred and fifteen dollars "and a promise I made my daughter". Ray has silently placed that promise as the oath he heard ("the house and not the rest"). Ch 09 has to show that the oath is what she spends, not the amount. That fits the bible's Ch 09 permission ("Then do it. And call me first next time.") and Ch 10's savings paid out loud.
- The release is drawn to take effect only once all three names are on it, Arlene's first. Since Ellen signs in s4, it is in force from the night of Feb 16.
- The nine refunded teams are the Open entrants who entered for Linda's cup alone and wrote her name on the entry form. The entry form has a place where that could be written. Teams that entered the Open without writing her name stay entered, and no refund is owed to them.
- On Feb 10, before opening, Ellen's car sat at the curb outside Gagnon & Son, engine off and dark, before Ray's first light. That is the morning Arlene saw from her window.
- Feb 10: Ellen had her own gloves in her vest pocket, unworn.
- Arlene's furnace quit one winter, and her kitchen oilcloth is split at the corner from it. The cupboard door stays free for Ray's cribbage tally in Ch 09.
- Ray's line "He ran it eighteen years" puts Normand's 1971–1989 on Ray's tongue as well as Arlene's. It adds no new fact.
- Ray has heard Ellen's oath to Kate ("the house and not the rest"), per Ch 02. Continuity: confirm Ch 02 shows Ray hearing both halves of it.

---
## Dialogue log
- Scene 1: exchange added after Gil's opener. Ray gets a straight-faced tease of his own aimed at Hollis, with the joke on the last words ("I bowl with older every Tuesday, Gil, and he's standing right behind me."), and Hollis answers with a flat measurement ("Five years."). Hollis is now in the room before the lot, and the leads' own humor shows before the stakes start. Everything else in s1 is unchanged: Gil talking over Dale, Dale's lines, the end stool and Denise, the pencil, "Holy mackerel", and the lot.
- Scene 2: no changes. Ray's silence is his tactic there, and the Bench's broken call and "Coffee's on" already carry the scene.
- Scene 3, the cost exchange (judge note): no fact cut. Cut the repeat of the condition ("If she misses and"), which Ray's own question had just asked. Merged the paid-months-on and condo-man sentences into one answer. Arlene now answers Ray's soft question ("You'd be paid, though, wouldn't you?") with "dear" used as a weapon ("Months on, dear, …"), her one profile mark the chapter hadn't used. Trimmed the contract clause by three words and kept every item in it. Ray's afraid line, "Then hold it", the window speech, Normand and the phone line are untouched.
- Scene 4, the terms (judge note): the single 46-word block is now three short lines, the ones the beat sheet asks for. Ellen's "Go ahead." stays. Ellen asks for the third line herself with a new prompt, "And the Open.", so she is pressing for her side's cost; it has no contraction. Hollis's line is now Ray's reported speech, said with a pencil from her cigar box turning in his hands ("Hollis says his committee voted on an Open, and nobody voted on a name."). The pencil goes back in her box in the beat where he offers her nothing, so his hands-in-pockets beat now marks the change of tactic. The apology, "In fries.", the release exchange, the signing, the K, "Not yet" (once) and Ellen's one contraction are unchanged.
- Lines added: 4 (Ray's tease, Hollis's "Five years.", Ellen's "And the Open.", and the third terms line split out as its own line). Lines cut: 0 (one 46-word speech split into three; the cost repeats trimmed inside their lines).
- Prose word count: about 3,297, worked out as the orchestrator's 3,261 plus the net of the edits (+17 s1, −5 s3, +24 s4). Ceiling 3,510. s4 is about 1,130 against its 850 floor. Ending types unchanged: question, mid-action, consequence, question.
- Retired-list and cap checks on new text: no dates or clock times, no contrast constructions, no "bare", no "Mrs. Daly", no Normie, no ATC phrases. "Holy mackerel", "Coffee's on" and "Not yet" stay at 1 each.
- Tag-strip test: pass. s1 has Gil (smug, long, talks over people), Dale (flat, reads things back, short), Hollis (measurement), Denise (run-on with a qualifier), the end stool ("don't" for "doesn't") and Ray (an *and*-chain with the joke last). s2 has Ellen with no contractions, against the Bench's broken call. s3 has Arlene (blunt, "dear", "Raymond") against Ray's chains and tag questions. s4 has Ellen (full stops, exact figures, the prompt "And the Open.") against Ray (clipped NH subjects, *and*, the weight on the last word).

---
## Cold-read triage (voice editor, Oct 29), edits made straight into final.md
Draft edited: final.md (3,317 words before). After: 3,341 words (ceiling 3,510). s4 about 1,145 against its 850 floor. Ending types unchanged: question, mid-action, consequence, question.

1. [Money line, s4] Figure kept. Added to Ellen's speech, same paragraph: "The Open is my whole margin, and the weather owns the Open. Page two refunds every entry in cash if weather stops play, so a hundred and fifteen under with every lane full means one storm takes all of it." Cut Ray's narration "A hundred and fifteen dollars was a kids' birthday party on a Saturday with the fryer going, or most of one." (it was the line that shrank the stake). Fries exchange kept; the laugh now reads "He laughed out loud, once, at something that was not funny, and it went down the dark lanes." No contractions in the new Ellen text.
2. [Cold open, s1] Added after the first sentence, Ray's side: "Ray had called the match himself, three strings to bring Ellen's two walkout teams home from this building, and it was his money on the table."
3. [Attribution, s1] "You anchor Tuesday," Ray said. / "Where'll you be?" Hollis said. Still ends on Hollis's question, unanswered.
4. [End-stool man, s1/s2/lot] Play-by-play voice added to his Pine Ridge line: "And the veteran comes to the line for the third string, folks, with a dollar of mine riding against him. Had it on Gil's man, Ray. Nothing personal. ..." (bible: "And the veteran declines", Saturday broadcast). His s2 "And the—" stays, so the two lines now rhyme. "End stool" count: 4 to 2 (s1 intro, s2 "the one off the end stool"). Lot: "The same man was at Ray's truck". s2 pour: "Then the one who had paid Hollis a dollar in the Pine Ridge lot left the other two standing". Still never "Normie".
5. [Arlene's kitchen, s3] Cut Ray's "Tell me what happens to you if she misses, Arlene, and tell it plain, because I'd rather hear it from you than work it out by myself in the truck." Arlene's answer is now the two new facts only: "If she misses and you aren't standing there, The Pines gives my room to the next name, and I go on the bottom of that list at eighty-four, and I may not live to the top of it." / "Months on, dear, when my lawyer's done selling it out from under her." Cut "nobody buys it" and the condo-man clause. "You'd be paid, though, wouldn't you?" and "I know it." kept.

## Flagged for orchestrator
- Bible Ray line 8 ("Tell me what happens to you if she misses, Arlene, and tell it plain...") and the beat sheet's s3 plant "condo man at land value" are no longer on the page in Ch 08, per this instruction. The beat sheet says Ch 09 s4 and Ch 10 pay these off; the condo man is also known from Ch 01 and Ch 02, so the payoff should still land, but the continuity log should record that Ch 08 no longer restates it. If the author wants line 8 on the page somewhere, move it to a later chapter where the question is new.
- Out of scope, not touched: in s3, "Wrecker ought to set up out there..." and "I want off the March paper..." are consecutive paragraphs both Ray's, with no tag or beat between them. A tag or a one-word beat would fix it.
- Not touched, still on the cold reader's list: unattributed "Holy mackerel." (s1).

## Manuscript revision round 1 (Oct 29)

Brief: `reviews/revision-brief.md`. Prose-writer, targeted. About +185 words (3,341 → about 3,525; +5.5%, inside ±8%). Ending types unchanged: question, mid-action, consequence, question. Ellen still has one contraction in s4.

- §2.6 (s1): Gil's "pick up a four-horse" → "pick up the four horsemen". Ch 10's one use matches.
- §4 match terms / §3 F8 (s1): the terms are now three lines. (1) Gil's opener and both outcomes in one speech. (2) Gil's self-interest, new: "And your name on my Tuesday sheet is worth two more teams to me by April, so don't take me for sociable." (3) Hollis names what Ray put up of Ellen's, new: "That's her third Tuesday team you're putting up," Hollis said. "She know that?" Dale's interruption and Gil's "as though nobody had spoken" are cut, because both terms now sit in Gil's speech.
- §4 kitchen cues (s3): every speaker in Arlene's kitchen is tagged or cued: "Arlene said" on the Pelletier line, "Do you know what you're asking me?", the cost line, "Then hold it", "In nineteen seventy-one" and "First"; "Ray said" on "I know it" and "He ran it eighteen years"; "he said" on "You'd be paid, though" and "Then you'll sign it". Ray's two consecutive paragraphs (the wrecker joke and "I want off the March paper") are now one Ray speech with an action beat between them ("He cut another piece of ham and left it on the fork."), and "Arlene" is added to the ask.
- §4 ("She said nothing to it" variants) (s3): "He ate, and didn't argue it." → "He ate." The s4 "said nothing to it" (the apology) is kept.
- §3 Normand's thirty (s3): Arlene settles it after "He ran it eighteen years": "He never cleared thirty, either, whatever you tell the Bench. Nobody did. You tell that one because you liked him." This is the brief's line, turned to "you" because she is talking to Ray. A beat ("She took her fingers off the page.") comes before "I won't hold you to one you've stopped wanting, Raymond."
- §1 lawyer clause (s3): Arlene answers her lawyer before the drawing instructions: "I know it's on record at the registry in Laconia. Put your notary's line under his name if you want it there." She adds "It won't come back through your office" before "Raymond will carry it to her himself, and he'll ask her." The scene still ends on that line.
- §2.3 margin speech (s4): replaced with the brief's text ("…and that is with every lane of the Open full. Page two refunds the Open in cash if weather stops play, so one storm puts me a good deal further under than that."), plus one sentence for the certain shortfall and how she means to cover it: "I am agreeing to come in short, and I mean to make it up at the snack bar on Linda's day and the derby's Sunday, with nothing of yours in it." No contractions. The fries exchange follows as before, so Ray's "Snack bar might find you some of it" now picks up her plan.
- §1 notary clause (s4, Ray's POV): her reading now stops "under his name, where the lawyer had left a line for a notary and nobody had filled it." Her choice, spoken: "There is a line here for a notary. I will not send this to Concord and back through a lawyer's office with the time I have left. It goes as it stands." Then Ray: "He nodded at it and no more. He had not looked under his own name." That beat says on the page why nobody caught it. "She took the glasses off" now comes before "You have asked…", so the two Ellen lines are split by his beat. "There are thirteen days." is unchanged and is still the first time the number is said.
- §4 ordinals: none printed as a list in Ch 08 (Arlene's "First" is one word, not Ellen's list). No change.

## Dialogue doctor, revision round 1 (Oct 29)

Edited final.md in place, prose only. Word count is an estimate (no shell in this session): 3,549 → about 3,496 (net −53; ceiling 3,510). The orchestrator's `wc -w` governs.

- s1 cold open: "Ray had called the match himself, three strings… and it was his money on the table." → "Ray had called the match to bring Ellen's two walkout teams home." (Gil's "You called me" and Dale's look at the checkbook already carry the caller and the stake; −14.)
- s1 Pine Ridge: cut "under screens nobody in this match looked up at" (Gil's "over my screens" carries them; −9).
- s1 Gil: his two paragraphs are now one speech, cued by "Gil smiled at him." at the front, so the untagged "You called me…" no longer follows Ray's narration uncued. "drove over to watch it and they're" → "is"; "go home to Kettle Lanes on Tuesday" → "go home on Tuesday" (−9).
- s1 Dale: "on the settee behind the table" → "on the settee"; at the tenth, "sat with his bag between his boots and watched" → "sat and watched" (the bag detail was said twice; −9).
- s3 cues (§4): every speaker in Arlene's kitchen is now cued by an action, and each action marks a change of tactic. Ray's question shares a paragraph with his eating (the pleasure sentence moves below the room paragraph to sit next to it). Arlene: "turned the oven down", "sniffed" (Pelletier), lays the contract down and "sat down" before her question and cost (one speech, so she answers her own question before he can), "shrugged" ("Months on, dear": money like weather), "pushed the contract toward him" ("Then hold it"), "waited" (Normand), "raised a finger" ("First"). Ray: "swallowed", "nodded", "looked up" (defends Normand), "reached for it" ("Then you'll sign it"). The window speech, Ray's clutch line and the lawyer call are word for word as before (+14).
- s4 terms (§4): the condition is now Ray's three lines in one paragraph, "He counted them off on his fingers," with Hollis's line after them. Cut Ellen's "And the Open." prompt, the "League bowls…" and "Gets the morning…" fragments, and "with whatever name you like on it". Ellen's "Go ahead." is kept (−16).
- s4: the pencil from her cigar box is gone with the terms it was turned over, so "put the pencil back in her box and his hands" → "put his hands" (−7).
- s4: gaze cut, "Her eyes went down the dark lanes and came back to him." "Agreed." now runs straight into the nine teams (−12).
- s4 notary, Ellen (Issues 2 and 3): "That would be you at a desk at Granite Lakes, with half of Main Street watching you go in. I will not have that. It goes as it stands." Her reason now protects him from the walk Ch 10 makes him take. No contraction (her one s4 contraction is still "won't"). "Concord" is now only the bank (+6).
- s4 notary, Ray (Issue 4): "He nodded. He had heard Arlene order that line at her table, and signed above it without looking." (+3)
- Tag-strip test: pass. Kitchen: Arlene is blunt and short with "dear" and "Raymond", and Ray is sideways with the weight last; every line is cued before or with its words. s4: Ellen's notary line is full stops, no contraction and a refusal; Ray's terms are three plain lines with his hands doing the counting.

## Voice editor, revision round 1 (Oct 29)

Draft edited: `final.md` in place, after the dialogue doctor's round-1 pass. Flagged passages and listener items only. Words 3,496 → 3,472 (net -24; band 2,990–3,510). Scenes: s1 1,089 (incl. heading), s2 473, s3 766, s4 1,137.

- [Commitments Issue 9] s2: "stood with her weight on both feet" → "came to the counter and stood at it" (retires the third "weight on both feet").
- [Listener, s1] Dale/Denise count line: "Nine pins behind, with ten on the deck. He needed every pin, with three balls to get them, and on the settee Dale sat and watched." → "Nine pins behind. Ten stood on the deck, and he needed every one. On the settee Dale sat and watched." (two numbers in one sentence gone; three balls is carried by the ball-by-ball paragraph).
- [Listener, s1] First-ball paragraph: the 55-word opening sentence split at "back wall" ("…carried to the back wall. One pin came down sideways…"); the second-ball sentence split at "plank" ("…looking at that plank. It went by the near end of it, took one of the three, and left two at the back…").
- [Listener, s1] Third-ball paragraph: the 40+ and 65-word chains split into four sentences ("…by other men's palms. His thumb found…"; "…let the ball go easy. It went the whole length…touched it. The pin came up…"). No word changed.
- [Listener, s2] "…folded one into the other, and he was the man the March paper said would buy her building" → two sentences ("…folded one into the other. He was the man…").
- [Silence variants, cap one per chapter] s2: cut "He didn't answer it." before "Inside his jacket the yellow page…". "She took it standing and said nothing to it, and he let her." (s4) is the chapter's one.
- [Listener, s4] Door paragraph: split at "as it always was." and at "vestibule tile." (three sentences became five; no words changed).
- [Listener, s4] Ellen's refund speech: "all nine" twice → "call them… all of them will take it"; "a hundred and fifteen dollars under thirty thousand, and that is with every lane of the Open full" → "a hundred and fifteen dollars under the number, with every lane of the Open full" (one figure per sentence); "further under than that" → "further under"; "I am agreeing to come in short, and I mean to make it up" split into two sentences. Facts unchanged: 115 under, Open full, page-two refund, snack bar and derby's Sunday.
- [Listener, s4] "You have asked an eighty-four-year-old woman to bet her bed on a hundred and fifteen dollars and a promise…" → "…to bet her bed. The stake is a hundred and fifteen dollars and a promise I made my daughter." (age and dollars no longer share a sentence).
- [Listener, s4] The letterhead sentence split at "letterhead." ("It was one sheet on Arlene's lawyer's letterhead. It let the three of them go…, with Arlene's signature at the top, his under hers, and a line left…"). The signing paragraph split at "one before it." ("The pen going over the paper was the one sound…").
- [Cues at the peak, s4] Added action/speech tags where the exchange ran untagged: Ellen's "It did," she said; Ray's "I know what I asked," he said; "I could," he said. (Speakers at the apology and the signing are now cued every time.)
- [Checked, no change] "level" and "in order": none in Ch 08. Ellen's printed ordinals: none (Arlene's "First." at the kitchen table is Arlene's, in speech). Ray's motor comparisons: none. Lane numbers: Ch 08 names none. Minutes quote ("strike that from the minutes"): carries no lane number, so no "behind lane five" needed. Match terms: Gil's terms stay at the three lines the beats asked for.
- [Flagged for orchestrator] Ch 08 s2's Bench sentence ("Then the one who had paid Hollis a dollar…held it out to her across the end of the counter", 47 words) is one subject and one chain; left, because s2 was not in this pass and it reads aloud as a single motion. Split it if the listener pass wants it.
