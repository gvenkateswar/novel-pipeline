# Chapter 15 issues (continuity check of draft.md)

Read: chapter-15/draft.md and beats.md, story-bible.md (all), outline.md (all, including the Ch 13-15 carry-forwards, the icing line and the predictability note), continuity-log.md (through Ch 14), book-brief.md "For the author's next bible review", chapter-14/final.md. Outline and log win over the bible. Stale bible items are listed separately at the end.

Checked and clean: Dane swears 0; "Bethie" 0; "your marshal" 0; "I don't bet" 0; "I'm asking" once ("Can I kiss you? I'm asking."); "He wanted her" once; no contrast constructions found; every boat is "it"; no fire; nobody in the water; no forbidden phrases; Ned in Russ's cuffs, then one cuff on the rail; cuff key in Beth's pocket; kid's tie cut and re-tied in front over the jacket; Russ's handheld with Dane; Russ and Tess ashore with the shotgun; icing "Tuesday" matches Ch 14; "two tomorrow", "an hour off", "three hours at best", "thirty years", "eleven pounds", "three of us"/"Four" all match the ledger.

---

**Issue 1**
- Problem: HIGH. Contradicts Ch 09 (and Ch 07). Dane stood on the north beach in Ch 09 while Beth asked Ned for the captain's job out loud and got it ("it's hers in June"). In Ch 07 she asked for him out loud ("I want you. I'm saying it out loud") and got that too. Dane was present for both, and this is his POV.
- Location: "It was the first thing he had ever seen her ask for out loud and get."
- Suggested fix: Cut the sentence. If the beat is kept, narrow it to what is true: the first thing she has asked a board for, in so many words, on her own.

**Issue 2**
- Problem: The scene opens with a past-perfect catch-up block (two paragraphs of "had come / had given / had spent") before the scene has moved. The beat sheet said "one clause each, no past-perfect block." It also gives the Saturday-on-the-rod fact as a stated paragraph instead of letting her failed grip on the ham show it.
- Location: "She had come straight in from the phone on the front-room desk. The ferry board had given her the boat for tonight." and "She had spent all of Saturday at the co-op's vise with the steering rod, straightening it again with those hands while he held the light. Today her hands were paying for it."
- Suggested fix: Fold the board into one simple-past clause attached to her entrance ("She came in from the desk phone with the boat for tonight in her pocket, from a board she'd asked herself"). Give Saturday in one clause at the moment she fails to hold the ham, in simple past.

**Issue 3**
- Problem: Hard to follow aloud, and the narration quotes the earlier line back. "It was the terms for something, and she hadn't said what" has no clear referent for a listener. "She'll go" is re-quoted from Ch 12 inside a run-on that also states the emotion ("it ran through him").
- Location: "He understood her all at once, and it ran through him: it was Wednesday she meant, his own voice saying \"She'll go\" on the speaker with her three feet off, and it was the terms for something, and she hadn't said what."
- Suggested fix: Cut to one short sentence naming Wednesday and the speaker without re-quoting the line, and drop "it ran through him" and "the terms for something".

**Issue 4**
- Problem: Two problems in one line. (a) Beth re-tells what both of them already know and Dane himself said aloud in Ch 14 ("Thursday, on your step. You said you wanted me."): "On Thursday I told you I want you. I meant it, and I'm still not going." (b) Listener hazard: "I said so do we" is the Ch 12 quote "And so do we" with no marking, and it reads as a sentence fragment by ear.
- Location: "On Thursday I told you I want you. I meant it, and I'm still not going. On Wednesday I said so do we. I decided that for both of us, in that room. Same thing I hated you for."
- Suggested fix: Delete the Thursday and "still not going" sentences. Give the Wednesday line as a quote a listener can hear: "On Wednesday I said, 'And so do we.' I decided that for both of us, in that room."

**Issue 5**
- Problem: Narration restates what the dialogue just showed (his view, her refusal), then re-quotes Ch 14's "on the other side" and explains it ("They were still on this one"), which is hard to parse by ear.
- Location: "He still thought the program would keep her breathing. She still wasn't going into it. He had promised her the rest on the other side. They were still on this one."
- Suggested fix: Cut the first two sentences. Keep at most "He had promised her the rest on the other side, and they were not there yet", or cut the paragraph.

**Issue 6**
- Problem: Ledger discrepancy on the two capped bits. The log's own Ch 06 entry records "Dollar says he's at the front door." / "I don't bet on what I can see. Pantry." The Ch 14 log line records "Dollar says" as 1 of 4 and "I don't bet" as 1 of 2, which ignores Ch 06. If Ch 06 final matches its log entry, then with this chapter "Dollar says" is at 3 of 4 (Ch 06, Ch 14, Ch 15), not 2 of 4, and "I don't bet" is already 2 of 2 (Ch 06, Ch 14), so the "one left for Ch 18" is not there. I did not run tools/audit.py or open Ch 06 final to confirm.
- Location: "A dollar says it does."
- Suggested fix: Run `tools/audit.py` and correct the caps lines in the log. If "I don't bet" is spent, Ch 18's blind bet needs other wording (the outline already says to word it another way).

**Issue 7**
- Problem: Motif caps likely tripped by this chapter. `\beleven pounds\b` cap 2: the body has "eleven pounds of pig" and "The ham is eleven pounds", and the chapter heading "Eleven Pounds" is a third hit if the audit reads headings ("eleven-pound ham" does not match). `\bham\b` cap 9 book-wide: this chapter alone has about six ("ham" in the first line, the glaze paragraph, "tried the ham", "The ham slid", "The ham is eleven pounds", "beyond the ham"), on top of Ch 08's tin of ham and its "load-bearing" joke, with Ch 18 still to come.
- Location: "He was holding eleven pounds of pig and he couldn't put it down." and "\"The ham is eleven pounds,\" Dane said, \"and there are three of us.\""
- Suggested fix: Run the audit. If over, swap "ham" for "it" or "the roast" in the narration lines (keep the dialogue lines), and drop "eleven pounds of pig" to "the pig".

**Issue 8**
- Problem: The bet logic undercuts the joke. Dane's "That is not going in that oven" is beaten by Beth's first order, "Take the rack out", which is the first thing he would have tried when "the rack was in the way". The roasting pan Tess carries in is handed to Dane, the beat that justifies it, and then never appears again; the ham goes in with "a soft scrape", as if bare. Nothing says why the pan is wanted or where it goes.
- Location: "Beth held out her wrists for the pan. Tess walked past them and gave it to Dane." / "\"Take the rack out,\" Beth said." / "The ham slid in with a soft scrape."
- Suggested fix: Make the rack fixed ("the rack was welded in", or the rack won't come out), so the fit really needs her orders, or have the ham go in the pan on the oven floor and say so. Either way give the pan one use or cut it.

**Issue 9**
- Problem: Says Dane told nobody in a room where everyone already knows. Beth saw the boat all of Saturday; Russ and Tess were told; Dane reported it on Ch 14's call. "Said nothing about it in this room" implies a secret that doesn't exist. The "past the white water" view is also a near-repeat of the same view 55 lines earlier.
- Location: "He shut the window and said nothing about it in this room." / "Down the harbor, past the white water at the mouth, the big boat lay off the point out of the wind, showing its one light"
- Suggested fix: End the paragraph at "He shut the window." and vary the second description of the view.

**Issue 10**
- Problem: Narration explains what the dialogue is about to show, repeats the Issue 3 point about Wednesday, and carries an implied contrast ("the right way round").
- Location: "He had planned nothing for this afternoon beyond the ham. She had just done in a doorway what he'd done on a speaker on Wednesday, the right way round."
- Suggested fix: Cut the second sentence. Keep "He had planned nothing for this afternoon beyond the ham."

**Issue 11**
- Problem: "Russ's shirt" is the first and only mention of what Dane is wearing, so a listener has no idea whose shirt or why (the shirt he gave up is in Ch 14). The line also puts Russ's shirt into the kiss. Separately "careful of hers" doesn't parse: her hands are up behind his neck and his are at her waist, so there is no way his hands could be rough on hers.
- Location: "The oven was hot at his back, and Russ's shirt rode up his arms when she drew him in." / "He kept his own hands at her waist, careful of hers."
- Suggested fix: Set the borrowed shirt up in Scene 1 in one clause ("in Russ's flannel, short in the arms") and take the shirt out of the kiss. Change the hands clause to "away from hers" or "off her palms".

**Issue 12**
- Problem: Contradicts the calendar and the Ch 13 custody note. The outline's Calendar has Saturday night "aboard at the pier" (and the bible says guarded every night from Ch 13). The draft says the pier was open and the island asleep, which is also the reason given for searching. It is also a past-perfect catch-up clause.
- Location: "This boat had sat at an open pier last night with the island asleep, and something had watched it from off the point since dawn yesterday."
- Suggested fix: Make it true to the calendar: "Nobody had been aboard for the six hours the rod was off at the co-op, and something had watched the boat from off the point since dawn yesterday." Or restate who was aboard Saturday night.

**Issue 13**
- Problem: Custody gap in the search. The kid and Ned are already on the passenger-cabin benches while Dane lies under the trucks and searches the crew room and engine room. Nothing says who walked them down from the town office back room, or who watched two prisoners while he was under a truck. Beth is the only candidate, and she is not placed until "Beth came in." The kid is tied; Ned is cuffed; still unguarded on a boat Dane is searching because it might be compromised.
- Location: "Nothing. He slid out and did the lumber truck, cab and load, then the crew room's two bunks and the engine room." / "At the far end of the passenger cabin, Dane cut the kid's cable tie with Ned's knife"
- Suggested fix: Bring the prisoners aboard after the search ("When the boat was clean he brought them down from the town office") with one clause, or put Beth at the cabin door with them.

**Issue 14**
- Problem: Re-glosses of terms the book already defined. "Car deck" was glossed in Ch 01-02 and used unglossed in Ch 14. "The hatch" is used unglossed in Ch 14. "The ledges" was glossed in Ch 10 ("the rocks just under the water at the harbor mouth"). The predictability note says not to re-gloss defined terms.
- Location: "Dane Reyes lay on his back on the car deck, the open deck where the trucks parked, with his flashlight" / "Beth went out to the hatch, the square lid in the deck over the steering, and knelt." / "At the mouth she slowed again for the ledges, the rocks just under the water on both sides, and white water showed in the deck lights."
- Suggested fix: Drop all three glosses. Keep the new gloss for "the rail".

**Issue 15**
- Problem: Listener cannot tell Tess is on the radio. The radio test is a single line, and "from the couch end" reads as if she were in the room. Nothing says Dane is on the ferry and Tess ashore at the town office.
- Location: "Dane clipped Russ's handheld radio to his coat and keyed it. / \"Here,\" Tess said from the couch end."
- Suggested fix: "Her voice came back out of the radio, small and flat: 'Here.'" and drop "from the couch end".

**Issue 16**
- Problem: A backfill exposition block in the middle of the action, between the radio test and the next beat. It re-states Ch 14's boss paragraph (icing, Tuesday, no flight) in narration, the plan logic, and the custody reason, in "would/couldn't" constructions. "That lawyer" and "that boat's men" have no anchor on the page (the lawyer last appears in Ch 12; "the boat" has not been named as the thing off the point in this scene).
- Location: "The Coast Guard would fly for Russ when the icing cleared, and it wouldn't clear before Tuesday. The same icing kept anything from flying Beth to Portland. So it was this boat, tonight. Russ waited on the couch, his bleeding stopped, with Tess and the shotgun. The prisoners crossed. Tess couldn't guard two men and nurse Russ, and a boy who could name that lawyer, left ashore, would bring that boat's men to Russ."
- Suggested fix: Cut to two sentences max (why Russ waits; why the prisoners cross). Name "Cole's lawyer" and "the big boat" on first use here. Better, put the custody reason in a spoken line, to Beth or Tess.

**Issue 17**
- Problem: Dane's line plus an explaining sentence of narration that repeats it. Also "that lawyer" / "that man" are both unanchored for a listener, and the narration switches to "the boy" for the kid.
- Location: "\"A text from a phone in nobody's name and Ned's word won't arrest that lawyer. The kid's would. And the kid isn't talking.\"" / "The boy had just heard that he was the only one aboard who could put that man in a cell."
- Suggested fix: Delete the narration sentence (the kid turning to the window already shows it). Change "that lawyer" to "Cole's lawyer" in the line. Use "the kid" throughout.

**Issue 18**
- Problem: Near-verbatim repeat of Scene 1, and narration restating a binding fact in the same words. Also slightly wrong: the rod did not skin her palms, the wheel spinning back did (Ch 14), so "the thing that had skinned them" misattributes it.
- Location: "She had spent Saturday at the co-op's vise on it. It was as straight as anyone on this island could make it." / "checking the thing that had skinned them"
- Suggested fix: Show it instead of re-stating: a bright new mark on the rod where the vise held it, or her thumb running along it. Change the clause to "checking the rod that had sent the wheel through her hands."

**Issue 19**
- Problem: Word drift. Ch 14 has Beth say the rod "might stick when the sea's on it", and the narration says "stuck" and "jammed". "Binds" appears nowhere else and is a term a listener would not connect to it.
- Location: "\"If it binds,\" she said, \"I'll feel it first.\""
- Suggested fix: "If it sticks, I'll feel it first."

**Issue 20**
- Problem: A listener has no setup for "the certificate". Ch 14 never says the ferry's certificate needs two aboard (Dane's "Two hands on the ropes" is the nearest setup). The laugh depends on knowing what "two" means. The bible has the fact as a [DC] note, not on the page.
- Location: "\"The certificate says two,\" she said. \"You're the other one.\""
- Suggested fix: Add one clause: "The certificate says the boat needs two aboard. You're the other one." (Keep "you're the other one" as a once-only motif.)

**Issue 21**
- Problem: Narration summarizes the exchange it follows. The dialogue already shows it.
- Location: "He kept his view, and she kept the decision."
- Suggested fix: Cut it.

**Issue 22**
- Problem: Beth's stated reason is weak on the page. (a) Ned did not send the kid; the kid is Cole's, and in Ch 12 Ned's part was the leaks (the outline carry-forward uses "sent" loosely). (b) She argues "He can't swim", but Dane buckled a life jacket on Ned in the previous scene, which takes the point away. (c) "Boy" for the kid is not what anyone else has called him in this scene.
- Location: "\"He can't swim. He's on this boat with me and the boy he sent after me. He won't put it on the rocks.\""
- Suggested fix: Rewrite the reason as one she can hold: "He's on this boat with me and the boy he led to my door. He won't put it on the rocks." Drop "He can't swim" (or make it "He's in a life jacket and he still can't swim").

**Issue 23**
- Problem: Geometry. Beth asks for Ned "at my shoulder", but the rail is "the steel bar along the back wall of the cabin" and the cuff is closed "behind Beth". Then Dane "stood at her shoulder on the side away from Ned", so Ned is somehow both behind her at the back wall and at her shoulder. A listener cannot place anyone. The bible's "rail" is also a different thing (the top of the car-deck side walls).
- Location: "He opened one of Russ's cuffs and closed it on the rail behind Beth, the steel cold under his hand." / "Dane stood at her shoulder on the side away from Ned, with the rifle."
- Suggested fix: Say the rail runs beside the wheel (or Ned is cuffed to it at her left), and drop "behind Beth". Keep Dane on the other side.

**Issue 24**
- Problem: Pronoun and sense. "It" has no antecedent: the previous sentences are about the cuff key, so "it" reads as the sea. "The short way" has no counterpart on the page (the long way is a Ch 16 fact). The line also comes out of nowhere, with no one asking.
- Location: "\"In what's left of the sea it can only crawl,\" Beth said. \"Three hours at best, the short way.\""
- Suggested fix: "In what's left of the sea the ferry can only crawl," and either cut "the short way" or set up the long way here in a clause. Give it a trigger (Dane asking how long, or Ned saying the weather).

**Issue 25**
- Problem: Understated against what both of them know. Dane has watched this boat since Saturday dawn and looked at its light twice in Scene 2, and Beth has seen it. "May be" is false for both.
- Location: "\"There may be a boat out there. Do we go?\""
- Suggested fix: "That boat's still out there. Do we go?" (If the outline's wording is wanted, note it is deliberate understatement.)

**Issue 26**
- Problem: "The rule that said so" has no rule behind it. Nothing in the chapter says wait until Portland. The "they stop" rule was taken back in Scene 1 ("So that part's off too"), and the only rule stated is "ask every time". A listener cannot tell which rule he means, and it contradicts the repair.
- Location: "He wanted her. He couldn't do one thing about it until Portland, and he was glad of the rule that said so."
- Suggested fix: Name the obstacle (the boat, the kid in the next room, the ledges) or cut "and he was glad of the rule that said so".

**Issue 27**
- Problem: Three recap paragraphs in a row in Scene 4 (the deadline, the kid on the bench, Russ on the couch, then the escort), each one re-stating a fact already on the page in full. The two sentences about the kid and Russ quote the chapter's earlier phrases back ("the one who could put that lawyer in a cell"; "with Tess and the shotgun", now the third use); Dane cannot see the town office from the car deck. They also split Dane's longing paragraph from the ropes line it belongs with, and the kid switches to "the boy".
- Location: "Through the lit cabin window he saw the boy on the far bench, the one who could put that lawyer in a cell. Up the dark road, Russ lay on the town office couch waiting for Tuesday's helicopter, with Tess and the shotgun."
- Suggested fix: Cut both sentences. If one restate is wanted, make it a clause of Dane's thought ("Behind him, up the road, the town office window was one yellow square").

**Issue 28**
- Problem: The no-escort paragraph repeats Ch 14's boss speech nearly point for point (Coast Guard "from an hour off", Marine Patrol "had a hole in it") as narration, immediately before the departure, and "a shooting" has not been named as a risk on the page. This is the re-gloss the predictability note warns about.
- Location: "Nobody was coming out with them. The Coast Guard would come by sea only if that boat came at them, and then from an hour off. The Marine Patrol boat on this stretch had a hole in it, and the state wouldn't send another into a shooting."
- Suggested fix: One sentence, or turn it into a line Dane says to Beth at the cabin door with a reason behind it ("Nobody's coming out with us. If it comes at us, the Coast Guard is an hour off.").

**Issue 29**
- Problem: Scene 3 has no time anchor. Scene 2 ends in blue dusk about half past three; Scene 3 opens under a truck with no clock and no "night", and the first cue that hours have passed is "the black window" in the middle of the scene. A listener will place it in the same dusk, with the ham still going in. Scene 4 then says "a little before ten". The chapter is called supper, but nobody eats; the ham goes in and is never mentioned again.
- Location: "Dane Reyes lay on his back on the car deck, the open deck where the trucks parked, with his flashlight on the underside of the bait truck"
- Suggested fix: Open with the time ("By eight the island was dark and Dane Reyes lay on his back on the car deck..."). Give the ham one line in Scene 3 or 4 (the smell on his coat, Tess carving it).

**Issue 30**
- Problem: Chapter 14 and Chapter 15 both end on the same image, the one light off the point. The predictability note (binding on Ch 16-18, and fair to apply here) asks to vary chapter endings and not repeat a single ominous image.
- Location: "Off the point, the one light was moving. It swung in behind them, low on the black water, and under their own engine he heard a bigger one, keeping pace."
- Suggested fix: Keep the turn (it follows them), but end on a different beat: a sound, a line (Beth's one word), or the radio, rather than the same light image.

**Issue 31**
- Problem: Word count. I did not run `wc -w`. A hand count gives about 2,150-2,250 words against the 1,950 target (+10-15%), with Scene 3 at roughly 550 against 450 and Scene 1 about 560 against 500. The orchestrator's ±8% limit looks exceeded.
- Location: whole chapter (Scene 3 most)
- Suggested fix: Run the word check first. If over, the cuts in Issues 2, 5, 10, 16, 17, 27 and 28 take about 200 words.

**Issue 32**
- Problem: Injuries are not carried. Beth kneels at the hatch on the knee laid open in Ch 10 (Ch 14 has "the stiff knee" on the steel stair), and climbs the stair again, with no cost shown. Dane's scalp cut is not mentioned. Her taped palms are carried well; the other two are dropped.
- Location: "Beth went out to the hatch, the square lid in the deck over the steering, and knelt."
- Suggested fix: One clause: she lowers herself onto the bad knee. Optional: Dane's hand goes to his scalp once.

**Issue 33**
- Problem: The phone Beth uses is not established. Her own phone drowned in Ch 07-08, and the bible says landlines worked only through Day 1 night with the power out since. Ch 14 shows Dane's phone on the shelf getting "the harbor's one bar". "The phone on the front-room desk" is a new, unexplained working phone.
- Location: "She had come straight in from the phone on the front-room desk."
- Suggested fix: Say whose phone it is ("Dane's phone"), or add "the desk phone, which the town office kept alive".

**Issue 34**
- Problem: The kid is called "the kid" in narration in Scenes 3-4 and "the boy" in the same paragraphs. For a listener that reads as a second person. "The boy" belongs to Ned and Russ (their word for him), not Dane's narration.
- Location: "The boy had just heard that he was the only one aboard who could put that man in a cell." / "Through the lit cabin window he saw the boy on the far bench"
- Suggested fix: Use "the kid" in Dane's narration throughout.

---

## Stale bible items (outline and log win; the bible is wrong or retired here)

- Crossing length: Weather ("Crossing takes about six hours, slow and wide of the ledges") and Numbers ledger ("Crossing in the window: about six hours"). Now three hours at best, the short way.
- "Rail": Key locations defines it as "a rail along the top of the side walls". The page defines the rail in the captain's cabin (the steel bar Ned is cuffed to). Also Calendar Day 10 "the hand on the rail" and the leak table row 15-16 "The kid waits at the harbor mouth / The hand on the rail" are retired.
- Harbor mouth location note: "Where the kid waits in his skiff (Ch 15)" is retired. Plant ledger: "The kid's skiff... 15-16 (comes aboard from it)" is retired; the kid is caught in Ch 13 and crosses as a prisoner.
- Injuries table: Russ "stretcher on the crossing" (he stays ashore); the kid "shot in the shoulder Ch 14" (he was grazed at the beach and arm-bound; he was caught in Ch 13); Beth and Tess "both hands burned Ch 11" (no burns; Beth's palms were skinned by the wheel in Ch 14, taped through Ch 17). Ledger "Shots Dane fires: at the pier" is stale.
- Ned on the crossing: the bible has Ned "hold the wheel while she handles the lines at Pruett" and "nobody is left ashore to guard him". Outline/log: Ned is cuffed to the rail at her shoulder (Ch 15), the wheel comes to him in Ch 16; Russ and Tess are ashore, but cannot guard two men and nurse Russ.
- Town office: "a back room where Ned is held (Russ guarding)" and the Calendar/leak table events for Day 7-9 (church fire, float, bait text, kid by water) are the old plot. Tess guards with the shotgun; the ham-day scene has Russ on the couch.
- Speaker table / Lines as they now stand: "There may be a boat out there. I'm asking." (outline) is now "Do we go?" per the beats. Dane's tender line 10 ("Can I kiss you? I'm asking. You told me to ask every time...") is trimmed to its first two sentences on the page.
- "She/her" for the ferry in the bible's Key locations ("run her", "painted on her", "with the sea behind her") and Ned's sample line: boats are "it" (book-brief next-review note).
- Where they sleep: Fri-Sat "Aboard the ferry... Guarded every night from here, per Ch 13 s3" conflicts with the draft's open pier (see Issue 12); settle the draft to the Calendar.
