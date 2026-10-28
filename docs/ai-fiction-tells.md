# AI Fiction Tells: Master Reference for Agentic Writing Systems

Version 1.0 — October 2026. Merged from "The 50 Fiction-Specific AI Writing Tells" (research survey) and "50 AI Fiction-Writing Tells: Sentence Patterns, Examples, and Editing Tests" (editorial checklist).

## 0. How to use this document

This file serves two roles in a writing pipeline:

1. **Drafting constraints.** The writer agent treats Parts 2–4 as rules. Items marked **HARD BAN** are never produced. Items marked **LIMIT** have a density cap. Items marked **TEST** are allowed but must pass the revision tests in Part 6.
2. **Revision checklist.** The editor agent runs Part 5 (lint list) as a mechanical pass, then Part 6 (judgment tests) as a reading pass, then Part 7 (story-level audit) on the whole manuscript.

Core principle: **a single tell proves nothing; a cluster does.** Any phrase here can appear in good human writing. What marks a text as machine-written is three or more groups of tells on the same page, repeated chapter after chapter, with no variation. The goal of these rules is to kill the cluster, never to sterilize the prose.

Evidence tiers used below:
- **Measured** — a corpus or frequency study counted it (Antislop; Cornell "Elias in the Lighthouse"; StoryScope; "The Ghost Couple"; Spinner's 300,000-word comparison; Foreverse).
- **Documented** — editors or critics quoted real examples.
- **Lore** — widely repeated in reader communities, no study found.

Reliability tiers:
- **Strong** — rarely appears in human writing at this density.
- **Medium** — depends on density and context.
- **Weak alone** — common in human genre fiction; only matters inside a cluster.

## 1. The near-certain tells (fix these first)

If the manuscript shows any of these, the editor agent flags it before anything else.

| # | Tell | Why it ranks here |
|---|------|-------------------|
| A | Stock character names (Elara, Elias Thorne, Kael, Lyra, Seraphina, Elena Vasquez, Marcus Chen, Aris Thorne) | "Elara" at 85,513× the human rate (Antislop). 11 words appear in 88.3% of bare-prompt AI stories (Cornell). |
| B | Pretty similes that mean nothing when pictured ("her laugh is bright as zinc") | Documented in the Commonwealth Prize case; critics call it the best single tell. |
| C | The quiet / hum / ghost / echo / liminal mood cluster in a story that has no ghosts | One 759-word ChatGPT essay used "quiet" 10 times. |
| D | The same word, image, or reaction repeated chapter after chapter with no rest | Human writers, even bad ones, notice and stop. Models do not. |
| E | Story explains its own meaning; one tidy plot line; soft hopeful close on every scene | StoryScope separated human from AI fiction at 93.2% macro-F1 on story structure alone. |
| F | Leftover machine artifacts (prompt text in the manuscript, `font-claude-response-body` HTML, impossible output pace) | Direct physical evidence. |
| G | GPT-5 "whimsical bureaucrat" style (fake-precise wry asides: "apologized for the century") | Strong for recent ChatGPT output. |

## 2. Hard bans

The writer agent never produces these. The editor agent removes them without a judgment call.

### 2.1 Name blocklist

**First names:** Elara, Elena (when paired with Vasquez), Elias, Eira, Kael, Kaelen, Lyra, Lena (when paired with Petrova), Mara, Maeve, Seraphina, Aris, Amara, Marcus (when paired with Chen), Echo.

**Surnames:** Thorne, Vance, Voss, Vex, Blackwood, Ashwood, Ashford, Windsor, Wellington, Mayfield, Maynard, Grey, Vasquez (paired), Chen (paired), Okafor (paired), Petrova (paired).

**Place and project names:** Eldoria, Blackmire Forest, Project Erebus, any capitalized abstract force ("the Veil," "the Shadow," "the Void").

**Default settings and professions** when the prompt did not call for them: lighthouse keeper, clockmaker, librarian, baker, the village with a mayor, "The Lighthouse Keeper's Secret" and variants.

Rule: names come from a deliberate source — the setting's culture, period, and class — and are chosen by the writer, never generated as a default. Real people carry some of these names; the ban applies to invented characters only. Model defaults shift with each release, so regenerate this list when a new model enters the pipeline.

### 2.2 Narrator winks and time fillers
"Little did she know," "Unbeknownst to them," "for what felt like an eternity," "the rest, as they say." Zero tolerance.

### 2.3 Vocabulary with no human-rate equivalent
Never: "ozone" (as a smell unless a storm or electrical fault is literally present), "tapestry" (figurative), "symphony of," "kaleidoscope of," "cacophony," "labyrinthine," "ministrations," "testament to," "a democracy of ghosts" and similar abstract-plural constructions.

### 2.4 The theme paragraph
No paragraph, line of dialogue, or closing sentence that states what the story means. No portable maxims about human nature ("There are losses that teach the heart a new language"). If a sentence could sit on a greeting card, delete it.

### 2.5 Machine artifacts
No prompt text, instruction fragments, model self-reference, or pasted HTML in delivered prose. Every delivered draft is plain text or clean markdown.

## 3. Limits (density caps)

These devices are legitimate. The problem is frequency. Caps are per 1,000 words unless stated.

| Device | Cap | Notes |
|--------|-----|-------|
| "as if" / "as though" clauses | 1 | ChatGPT baseline is 5.7 per 1,000. Human literary baseline is well under 1. |
| Trailing "the way a ___ does ___" similes | 1 per chapter | Only when the narrator would plausibly think it. See Test 3. |
| Similes and metaphors of any kind | 2–3 | Never two for the same beat. Never stacked. |
| "Not X, but Y" / "It wasn't X. It was Y." / "Not X. Not Y. Z." | 1 per chapter | ChatGPT uses this 3–4× as often as other models. EQ-Bench weights it at 25% of its slop score. |
| Lists of three | 2 | Vary list length deliberately: use two, use four. |
| Em dashes | 2 | Weak evidence as a tell, but readers now hunt for them. Newer models swap in semicolons with the same sentence shape, which is also a tell. Vary the punctuation and the sentence shape. |
| One-line paragraphs / fragment chains | 1 per scene | Reserve for a genuine beat. Never before a hook as a reflex. |
| Sentences starting with "And" / "But" / "And yet" | 3 | Human writers do this freely; the issue is reflexive use. |
| Scene closes on a soft hopeful beat | 0 in a row; max 1 in 4 scenes | "For now, that was enough" and relatives. See Part 7. |
| Body-language reaction per line of dialogue | not every line | See 4.5. |
| Aphoristic dialogue line | 1 per chapter, and only from a character established as the type | See 4.6. |

## 4. The catalog of tells

Each entry: the tell, an example (all examples here are newly written illustrations, none quoted from a published text unless noted), the rule for the writer, and tiers.

### 4.1 Similes and comparison templates

**1. The explanatory "the way" simile.** *"She folded the letter the way a surgeon closes an incision."* The comparison interprets an ordinary action for the reader. Rule: cut unless the comparison comes from the viewpoint character's own world and adds a fact the reader did not have. Documented. Strong when vague ("the way people do when…"), weak alone otherwise.

**2. The tacked-on "like" or "as if" clause.** *"The sea stayed silent, as if holding its own breath to listen."* Rule: see cap in Part 3. When kept, the "as if" must propose something the character could actually believe. Measured (small study). Medium.

**3. "With the [quality] of someone who…"** *"He set down the glass with the precision of someone who had learned noise had consequences."* A gesture acquires a compressed biography. Rule: show how this particular person moves instead. Documented. Medium.

**4. "The kind/sort of X that…"** *"It was the kind of smile that asked you not to look too closely."* The narrator sorts the moment into a familiar category. Rule: describe the particular features of this smile. Documented. Medium.

**5. "Not because X, but because Y."** *"He stayed not because he believed her, but because leaving would make it real."* Motive solved immediately after action. Rule: let motive stay unresolved for at least a scene. Documented. Medium.

**6. Abstract-plus-physical mashups.** *"The kitchen smelled of burnt toast and old disappointments."* One term is perceptible, the other is mood. Rule: the sense word stays physical. If an abstraction is wanted, give it its own sentence and earn it. Documented across models. Strong in clusters.

**7. Pretty nonsense.** *"The envelope weighed like mornings."* Rule: every comparison must survive the picture test — if the reader cannot imagine it, cut it. Documented. **Strong. Top-tier tell.**

**8. Orphan metaphors.** A comparison appears once, from outside the narrator's world, and is never built on. *"The girl smiled like sunrise over a sink."* Rule: a metaphor either recurs with development or is replaced by one native to the narrator. Documented. Medium to strong.

**9. Stacked similes.** *"The news struck like a hammer, split the floor beneath her, and left her drowning."* Rule: one image per beat. Documented. Medium.

**10. Colliding metaphors.** *"Her grief was an anchor that opened a door inside him."* Rule: the physical logic of the image must work. Documented. Medium.

**11. Metaphor outside the viewpoint.** *"The shepherd assessed their quarrel like a barrister reviewing testimony."* Rule: the comparison must be available to the character's knowledge, trade, and vocabulary. This is a viewpoint test, not a ban on sophistication. Documented. Medium.

### 4.2 Sensory and atmosphere clichés

**12. Everything is quiet or humming.** Rule: audit "quiet," "hum," "soft," "still" per scene. Loud scenes are loud. Measured in samples. Strong in clusters.

**13. Ghosts, echoes, shadows, whispers.** Rule: spectral vocabulary only in a story with actual ghosts. Documented and counted. Strong in clusters.

**14. Liminal and threshold language.** *"Thursday — that liminal day that tastes of almost-Friday."* Rule: ban "liminal." Thresholds are physical doorways only. Documented. Strong.

**15. Shimmering, flickering, glinting.** "Shimmered" at 2,882× human rate. Rule: light does something specific (the bulb buzzes, the sun is on the left wall). Measured. Medium.

**16. Stock atmosphere kit.** "The air was thick with," "the air crackled with tension," "words hung in the air," "dust motes dancing," "dimly lit," "casting long shadows," "the sun dipped below the horizon." Rule: replace with a detail only this room has. Community lists. Weak alone — decades-old genre clichés.

**17. The prefabricated sensory opening.** *"The air smelled of rain, old paper, and something metallic."* An inventory that could open dozens of unrelated scenes. Rule: a scene opens with what the character needs or fears, and the senses follow from that purpose. Measured (StoryScope). Medium.

**18. Environment performs the emotions.** *"The hallway resented her footsteps."* Rule: characters carry the feeling; the building stays a building, except as a deliberate sustained device. Documented. Medium.

**19. Silence as a solid object.** *"The silence settled between them, heavy and sharp-edged."* Rule: say what each person does during the pause. Documented. Medium.

**20. Words as objects in the air.** *"His answer hung between them like a blade."* Rule: replace with the other person's concrete response. Documented. Medium.

**21. Time or the world stops.** *"For a moment, the room forgot how to move."* Rule: at most once per book, at the actual climax. Documented. Medium.

**22. Generic specificity.** *"She entered the little café on the narrow street, where an old song played."* Descriptive slots with no identifying content. Rule: which café, which song, and why does this character notice it. Measured. Medium.

### 4.3 Body language and emotional shorthand

StoryScope: AI fiction overwhelmingly renders emotion as physical sensation. "Show, don't tell" does not mean "convert every feeling to a symptom."

**23. The hammering heart.** "Heart hammered ribs" at 1,192× human rate. Measured. Weak alone, strong in clusters.

**24. The breath she didn't know she was holding** (also "breath hitched," "took a deep breath," "let out a breath"). Measured. Weak alone — thirty-year romance staple.

**25. Shivers down the spine.** All four variant forms. Measured. Weak alone.

**26. The barely-there voice.** "A voice barely above a whisper," "voice trembling slightly" (731×), "voice devoid of emotion" (693×), "stammered" (2,043×). Measured. Medium to strong.

**27. Eyes doing the work.** "Eyes never leaving his" (102 times in 96 prompts from one model), "sparkling with mischief," "a smile that didn't reach her eyes," "something flickered behind his eyes," "something unreadable in his gaze." Measured. Medium.

**28. Tight jaws, white knuckles, swallowing hard, Adam's apples bobbing.** "Tightened," "mouth," "gaze" were ChatGPT's top fiction words. Measured. Weak alone.

**29. The body-language stack.** *"Her jaw tightened, her fists clenched, her shoulders went rigid."* Three signals for one beat. Rule: one signal, or none and a thought instead. Documented. Medium.

**30. The humorless laugh.** *"She gave a short laugh with no amusement in it."* Documented. Medium.

**31. The adjective-loaded voice.** *"His voice was low, rough, and threaded with something dangerous."* Rule: the line itself must carry the effect. Documented. Medium.

**32. Emotions as weather or water.** *"Relief washed over him, followed by a cold tide of dread."* Rule: a feeling produces a perception, a thought, or a choice. Documented. Medium.

**33. Micro-reactions.** *"One corner of his mouth lifted a fraction."* Rule: restraint is a trait of one character, never the house style. Documented. Medium.

**34. Named emotions and the vague "something."** "Felt a profound sense of" (550×), "a mix of anticipation and dread," "couldn't help but," "something shifted," "something that felt almost like." Rule: name the thought or decision, or leave it unnamed and show behavior. Measured for "profound sense." Medium.

**35. "Almost," "not quite," "something like," and the delayed label.** *"Relief, perhaps. Or something close enough to pass for it."* Rule: commit, or make the uncertainty matter to the plot. Documented. Medium.

Rule for the whole section: for any paragraph with two or more items from 23–35, rewrite with at most one physical signal and one interior line.

### 4.4 Narration that explains

**36. Show, then label.** *"She pushed his plate into the bin. She was furious."* Rule: delete the label. Measured. Strong at manuscript level.

**37. Gesture, then psychological translation.** *"He turned the handle twice, needing one small thing he could control."* Rule: delete the decoding clause. Documented. Medium.

**38. The expression containing an emotion list.** *"Her face held grief, defiance, and a fragile thread of hope."* Documented. Medium.

**39. The universal observation.** See 2.4. Measured. Strong.

**40. The narrator states the theme.** See 2.4. Measured. **Strong, especially with 56–58.**

**41. The unearned "for the first time."** *"For the first time in years, she felt truly seen."* Rule: only after the preceding scenes have tested the change. Documented. Medium.

**42. Perception filters on repeat.** "She noticed," "she could hear," "she felt the cold." Rule: cut the filter; present the thing. Documented. Medium.

**43. Decision announced, prepared, executed.** *"She knew she had to leave. Taking a breath, she prepared to go. Then she turned toward the door."* Rule: one beat, one sentence. Measured. Medium.

**44. Backstory at the first opportunity.** *"He disliked hospitals; ever since his mother's death…"* Rule: no origin story in the same paragraph as the preference. Measured. Medium.

**45. Symbols that explain themselves.** *"The repaired bowl sat between them, its gold seams proof that broken things could become beautiful."* Rule: the object stays; the explanation goes. Measured. Strong.

### 4.5 Dialogue

**46. Characters debate the theme out loud.** Measured (StoryScope). Strong at story level.

**47. Clipped lines ending on hooks.** *"'No,' she said, voice low. 'Something promising.'"* Every exchange a mini-cliffhanger, tagged "voice low." Documented. Medium.

**48. Everyone sounds the same.** "An undifferentiated Everyprotagonist." Rule: strip the tags and read; if speakers are indistinguishable, rewrite. Documented. Medium.

**49. Feelings stated with no subtext.** *"I'm angry because you chose your reputation over our friendship."* Rule: characters evade, bargain, insult, joke, lie, or pursue an aim; they almost never explain. Measured. Weak alone, because beginners do this too.

**50. Therapist language without a reason.** *"I need you to acknowledge the harm before we can begin rebuilding trust."* Allowed only for a character whose period, class, and personality support it. Lore. Weak alone.

**51. Aphorisms in every mouth.** *"Some doors only open after you've stopped calling them walls."* Documented. Medium.

**52. No real jokes, banter, or flirting.** Humor goes literal; banter goes flat; slow burn collapses. Rule: a joke must be a joke a specific person would make at a specific target. Documented. Medium.

**53. An action beat after every line.** *"'You knew.' She looked away. 'I suspected.' He rubbed his neck."* Rule: gestures appear when tactics change. Documented. Medium.

**54. The gaze-choreography loop.** *"He searched her face. She held his gaze. He looked away. She studied him."* Rule: delete; the talk itself must move. Documented. Medium.

### 4.6 Structure, pacing, endings

**55. One tidy plot line.** Few subplots, clean cause-and-effect, protagonist solves everything personally. Rule: at least one subplot that the protagonist does not resolve; at least one broken timeline or flashback where the genre allows. Measured. **Strong across a manuscript.**

**56. Flat stakes.** Tension never escalates; conflict stays mild. Claude shows "notably flat event escalation." Rule: each act must raise the cost of the protagonist's goal. Measured. Medium.

**57. The soft hopeful close.** "For now, that was enough." "They would face it together." "It was only just beginning." "Ready to face whatever lay ahead." "Nothing was fixed. But for tonight, it was enough." Rule: a scene ends on a consequence, a reversal, a question, or a cut — and the ending type varies. Measured. Medium to strong.

**58. The last paragraph spells out the moral.** Measured. Strong with 55–57.

**59. The same moves, never rested.** Repeated word, image, or reaction across chapters (the *Shy Girl* "sharp" tally). Rule: editor runs a frequency count of adjectives, body reactions, and images across chapters; anything above expectation is varied or cut. Documented, partly measured. **Strong. Many critics call this the single best tell.**

**60. The repeated fragment crescendo.** *"He would return. Not tonight. Not alone. But soon."* Documented. Medium.

**61. Backward-looking frames and dream sequences** (GPT habit). Rule: no dream sequences unless the prompt requires one. Measured. Medium.

### 4.7 Rhythm and sentence shape

**62. "Not X, but Y" family.** See cap in Part 3. Measured. Medium to strong at density.

**63. Everything in threes.** See cap. Documented. Weak alone.

**64. One-line paragraphs and fragment chains.** See cap. Documented. Medium.

**65. Proverb-shaped declaratives with weak verbs.** *"Ambiguity was not weakness. It was survival."* Documented. Medium.

**66. Every sentence auditions as the best sentence.** *"The afternoon bruised toward evening. The windows hoarded gold."* Rule: plain connective sentences are required. Aim for most sentences to be unremarkable so the strong ones land. Documented. Medium.

**67. Dashes where no pause belongs, and the semicolon swap.** Weak as evidence, but vary the punctuation anyway. Conflicting evidence. Weak.

### 4.8 Tone

**68. Fake depth.** *"He knew her face first as a question and then as a name."* Rule: paraphrase the line in plain words; if nothing survives, cut it. Documented. Strong.

**69. One hollow emotional note.** Competent, earnest, flat. Rule: give each scene a tonal contrast with the one before it. Documented. Medium (gut-level judgment).

**70. Safe, sanitized, morally clean.** Villains lack menace; the protagonist's choices are clearly right; ugliness is rushed. Rule: the protagonist makes at least one choice a reasonable reader would condemn. Measured for moral ambiguity. Medium.

### 4.9 Worldbuilding (fantasy, sci-fi)

**71. Cosmic abstraction instead of a concrete world.** Voids, "the fabric of reality," "older than law and time," rogue AIs, no physical setting. Rule: every scene has a floor, a light source, a temperature, and an object that could be picked up. Documented. Medium.

**72. Default settings and stock place names.** See 2.1. Measured for settings. Medium.

### 4.10 Romance-specific

**73. Cliché heat vocabulary and mechanical sex.** "Tangled in the sheets," "ministrations," hammering hearts. Rule: maintain an ick list; write the scene from the character's specific history and shame. Documented. Medium.

**74. No slow burn.** The draft rushes past longing; the love interest has no interior life between tropes; personalities flip without cause. Rule: the point of no return comes no earlier than the 60% mark unless the subgenre dictates otherwise; the love interest wants something apart from the protagonist. Documented. Medium.

### 4.11 Newer tells (2025–2026)

**75. GPT-5 whimsical bureaucrat.** Odd objects plus fake-precise wry asides: *"a potted plant that had repotted itself into the shape of the light."* Rule: wit belongs to a character with a reason for it. Documented. Strong for recent ChatGPT.

**76. Roleplay-era additions.** "Calculating gaze," "like a predator stalking its prey," "a testament to." Measured (Foreverse). Medium.

**77. Machine artifacts.** See 2.5. Direct. Near-certain.

## 5. Lint list (mechanical pass)

The editor agent greps the draft for the following and reports count per 1,000 words. Anything flagged ★ is removed outright; the rest is reported against the caps in Part 3.

**Names ★:** see 2.1.

**Words ★:** liminal, ozone (figurative), tapestry (figurative), symphony of, kaleidoscope, cacophony, labyrinthine, ministrations, testament to, unbeknownst, little did.

**Mood words (count):** quiet, hum/humming/hummed, soft/softly, still/stillness, ghost/ghostly, echo/echoed, shadow (figurative), whisper (figurative), shimmer, flicker, glint, spectral, fragile.

**Phrases (count):** the air was thick with; the air crackled; hung in the air; dust motes; dimly lit; casting long shadows; dipped below the horizon; heart hammered / pounded / thundered; breath (she didn't know) she was holding; breath hitched; took a deep breath; let out a breath; shiver (ran|traced) down; barely above a whisper; voice trembling; devoid of emotion; stammered; eyes never leaving; sparkling with mischief; didn't reach (her|his) eyes; something flickered; something unreadable; jaw tightened; knuckles whitened / white-knuckled; swallowed hard; Adam's apple; a mix of; profound sense of; couldn't help but; something shifted; something like; almost like; not quite; for the first time (in); washed over; crashed over; for what felt like; for now, that was enough; face whatever lay ahead; only just beginning; together, they; calculating gaze; predator stalking.

**Constructions (count):** `as if` / `as though`; `the way (a|an|the|people|someone)`; `the kind of ... that`; `with the (precision|care|economy|deliberateness) of someone who`; `not because ... but because`; `(wasn't|was not|isn't|is not) ... (It was|It's)`; `Not X. Not Y.` fragment sequences; sentence-initial And / But / And yet; em dashes; semicolons; lists of exactly three; paragraphs of one sentence; `(she|he) (noticed|could hear|could see|felt)`.

**Artifacts ★:** any HTML tag, any text resembling an instruction to a model, "Certainly," "Here is," "As an AI."

## 6. Judgment tests (reading pass)

For each flagged sentence, the editor applies these in order and keeps the sentence only if it passes all five.

1. **Density.** How many other flagged items sit within the same scene? Three or more groups means rewrite the scene, not the sentence.
2. **Specificity.** Could this sentence move unchanged into an unrelated novel? If yes, cut or rewrite.
3. **Viewpoint.** Would this character or narrator choose this comparison, detail, or word? If the metaphor comes from a world the narrator does not know, replace it.
4. **Added value.** Delete the explanatory clause. Does the sentence lose information? If it loses only emphasis, leave it deleted.
5. **Consequence.** What changes in the scene besides the narrator announcing a feeling or insight? If nothing, the beat needs an action or a cut.

Worked example from the source material:

- Template-heavy: *"She checked the lock the way a sailor checks a knot before a storm."*
- Character-specific: *"She pulled the door twice. Then she went upstairs and came back to pull it again."*

The first is acceptable only if the viewpoint character is a sailor. The second shows behavior and leaves interpretation to the reader.

## 7. Story-level audit (whole-manuscript pass)

Run after the lint and reading passes. These outlast vocabulary tells, which frontier models now often avoid.

- [ ] Count subplots. Fewer than two, or all resolved by the protagonist personally → add or restructure.
- [ ] Map the escalation. Does each act cost the protagonist more than the last? Flat curve → raise stakes.
- [ ] List every scene ending. Classify each (consequence / reversal / question / cut / soft hopeful beat). More than one in four soft beats, or any two in a row → rewrite.
- [ ] Find every sentence that states the theme or a general truth about people. Delete all of them. If the theme no longer comes through, the problem is in the scenes, not the missing sentence.
- [ ] Find every moral choice. If none would be condemned by a reasonable reader, add one.
- [ ] Strip dialogue tags from one full scene per chapter. If speakers are not distinguishable, rewrite voices.
- [ ] Run a cross-chapter frequency count of adjectives, physical reactions, and images. Anything that recurs beyond expectation gets varied or rested.
- [ ] Check the timeline. Strictly linear with no flashback, ellipsis, or disorder → consider whether the genre allows more.
- [ ] Check for dream sequences, backward-looking frames, and "the way I remember it" openings. Remove unless required.
- [ ] Check humor. Zero jokes that land as jokes → add banter that a specific character would produce.

## 8. Model-specific drift

Each model has its own accent. The editor agent weights the audit by which model drafted the text.

| Model family | Known habits | Extra attention |
|---|---|---|
| ChatGPT / GPT-5.x | Body-focused ("tightened," "mouth," "gaze"); "as if" at 5.7/1k; heaviest "not X but Y"; dream sequences; whimsical-bureaucrat asides; psychological escalation | 4.3, 4.7, 4.11 |
| Claude | Flat event escalation; quieter endings; tells more than shows; "retreats into absence"; historical default cast Elena Vasquez / Marcus Chen / Amara Okafor (reported gone in newer versions); straight quotes; too many similes | 4.6 (56, 57), 4.4, 4.1 |
| Gemini | External character description; tidy endings and long denouements; physical horror reactions; default cast Aris Thorne / Lena Petrova / Lyra Blackwood / Kaelen Ashwood | 4.3, 4.6 (57), 2.1 |

Prompting alone does not erase these instincts (AIStoryHub tests). Ick lists fix vocabulary and never fix structure. Budget revision time for Part 7 regardless of how clean the lint pass comes back.

## 9. Calibration and caveats

- Word lists are losing power. In Foreverse's July 2026 test, the two strongest models scored zero slop-phrase hits, while the best human-written samples averaged 0.07. Treat Part 5 as a hygiene pass and Part 7 as the real work.
- Many tells are weak alone: items 16, 23–25, 28, 49, 50, 63, 67. Human genre writers use them freely. Do not treat a clean draft as human, and do not treat a single hit as machine.
- Never use this document to accuse a named person. Pangram-style detectors have strong published accuracy and documented false positives on human work. The *Shy Girl* and *Daggermouth* authors both deny using AI.
- Several key studies are preprints (StoryScope, "Elias in the Lighthouse," "The Ghost Couple"). Antislop measured mostly open models. Spinner's study is small. Some sources sell a product (AIStoryHub, Foreverse, Pangram, Coral Hart's courses).
- Lore with no source found: "I know. I know." in dialogue, "a beat," "searching his face," therapy-speak, chapters of identical length, "Ashford." Apply them with the lowest weight.
- Tells move fast. Names drop out of new model versions; em dashes have been trained away; semicolons replaced them. Review this document whenever the pipeline's model changes.

## 10. Sources

Corpus and frequency studies:
- Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models — https://arxiv.org/html/2510.15061v2
- Hamilton & Mimno, "Elias in the Lighthouse, Again? Diagnosing Low Diversity in LLM Stories" — https://arxiv.org/abs/2605.26492
- Russell et al., "StoryScope: Investigating idiosyncrasies in AI fiction" — https://arxiv.org/abs/2604.03136
- Brzozowski & Chung, "The Ghost Couple" — arXiv 2606.02184
- Karen Spinner, 300,000-word ChatGPT/Claude/Gemini comparison — https://wonderingaboutai.substack.com/p/i-prompted-chatgpt-claude-and-gemini
- Foreverse, AI Roleplay Slop Words list — https://foreverse.app/blog/ai-roleplay-slop-words-list
- "Can AI writing be salvaged? Mitigating Idiosyncrasies" — https://arxiv.org/html/2409.14509v2
- "Art or Artifice? LLMs and the False Promise of Creativity" — https://dl.acm.org/doi/10.1145/3613904.3642731
- AIStoryHub, "Why AI Writing Sounds Like AI" — https://aistoryhub.co/blog/why-ai-writing-sounds-like-ai-and-what-actually-fixes-it

Criticism and editorial:
- nostalgebraist, "hydrogen jukeboxes" — https://www.tumblr.com/nostalgebraist/778041178124926976/hydrogen-jukeboxes
- nostalgebraist, "the improvised bureaucracy of wonder" — https://nostalgebraist.tumblr.com/post/792464928029163520/the-improvised-bureaucracy-of-wonder
- Sam Kriss, NYT Magazine (Dec 2025), via https://maxread.substack.com/p/will-ai-writing-ever-be-good and http://benedante.blogspot.com/2025/12/sam-kriss-on-ai-writing.html
- Kelsey Piper, "The literary world is sleepwalking into an AI disaster" — https://www.theargumentmag.com/p/the-literary-world-is-sleepwalking
- Makin, "How to Identify AI-Written Web Fiction" — https://recordcrash.substack.com/p/how-to-identify-ai-written-web-fiction
- Carrie Jones, "What Makes a Story 'Look' Like AI Wrote It?" — https://livinghappy.substack.com/p/what-makes-a-story-look-like-ai-wrote
- Dramatica, "The AI Tells Are in the Story" — https://dramatica.com/blog/the-ai-tells-are-in-the-story
- Justis Mills, "AI Can't Write Good Fiction" — https://justismills.substack.com/p/ai-cant-write-good-fiction
- Daria Gavrilova, "Why does AI write… like this?" — https://mistressprompt.substack.com/p/why-does-ai-write-like-this
- A.I. Freeman, "Top 10 Ways to Recognize AI-Generated Writing" — https://aifreeman.substack.com/p/top-10-ways-to-recognize-ai-generated
- jlevy, practical-prose AI-prose corrections — https://github.com/jlevy/practical-prose/blob/main/docs/ai-prose-corrections.md
- Storycraft (lanternkey) — https://storycraft.lanternkey.fyi/
- Fix Your Fiction humanizer notes — https://fixyourfiction.com/tools/humanizer.html
- WebProWorld, "How to Prompt AI So Your Novel Doesn't Read Like a Machine Wrote It" — https://www.webproworld.com/artificial-intelligence/how-to-prompt-ai-so-your-novel-doesn-t-read-like-a-machine-wrote-it/
- Max Read, "Who is Elara Voss?" — https://maxread.substack.com/p/who-is-elara-voss
- TomLikesRobots, name blocklist — https://x.com/TomLikesRobots/article/2074504762448339243
- Chris Thomas, "The Elara problem" — https://microblog.christhomas.co.uk/blog/the-elara-bias
- Rachel Neumeier's blog — https://www.goodreads.com/author/show/1407193.Rachel_Neumeier/blog?page=46
- Jo Michaels's blog — https://www.goodreads.com/author/show/5833874.Jo_Michaels/blog?page=4
- AO3 detection guide — https://awesomefringey.blog/post/828940674448670720/how-to-detect-ai-in-fanfiction
- Monster Romance Reviews, "Romance has an AI Problem" — https://monsterromancereviews.substack.com/p/romance-has-an-ai-problem
- Paprika Lynn, "If You Have to Hide the AI…" — https://jessicasbookrecs.substack.com/p/if-you-have-to-hide-the-ai-the-book

Cases and reporting:
- Slate on *Shy Girl* — https://slate.com/culture/2026/03/shy-girl-mia-ballard-novel-a-i-book-horror-reddit-hachette-canceled.html
- Locus on *Shy Girl* — https://locusmag.com/2026/03/hachette-pulls-shy-girl-over-suspected-ai-use/
- Pangram, "AI is Writing Prize-Winning Fiction" — https://www.pangram.com/blog/ai-is-writing-prize-winning-fiction
- Mother Jones, "I Asked AI to Write a Novel" — https://www.motherjones.com/politics/2026/08/artificial-intelligence-ai-claude-write-novel-anthropic-copyright-manuscript/
- NYT, "The New Fabio Is Claude" (Feb 2026), via https://dnyuz.com/2026/02/08/the-new-fabio-is-claude/ and https://the-decoder.com/human-writers-face-an-impossible-race-against-chatbots-that-finish-a-book-before-lunch/
- IBM Think on Elias Thorne — https://www.ibm.com/think/news/why-every-ai-writes-the-same-story-elias-thorne
- ArtReview on the Altman story — https://artreview.com/sam-altman-ai-short-story-review-michelle-santiago-cortes/
- Gizmodo on the Altman story — https://gizmodo.com/openais-sam-altman-thinks-this-chatgpt-short-story-is-beautiful-but-its-just-trash-2000574939
- Fast Company / AI and You on prompts left in published books — https://aiandyou.org/news/fantasy_and_romance_writers_address_ai_controversies_after_readers_discover_prompts_in_published_books/
- IBTimes UK on the AO3 Claude-HTML dispute — https://www.ibtimes.co.uk/hidden-claude-code-ao3-ai-dispute-1822141
- Whitney A. Foster on the AO3 PDF — https://whitneyafoster.substack.com/p/ao3-ai-fanfiction-heated-rivalry-detection
- Katharine English, "Pangram Flagged My Own Writing as AI" — https://writerkatharine.substack.com/p/pangram-flagged-my-own-writing-as
- Goodreads list, "Elara" in AI-generated books — https://www.goodreads.com/list/show/225617._Elara_in_AI_generated_books
- Google AI forum, Gemini name repetition — https://discuss.ai.google.dev/t/gemini-cannot-come-up-with-unique-name-for-characters/94830
