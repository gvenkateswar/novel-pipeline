# Reader calibration: what published romances teach this pipeline

*Not the same file as `docs/calibration.md`, which holds human verdicts on this pipeline's own text and judge agreement. This file holds what readers rewarded and punished in 40 published books. The genre map, the story architect, the plot auditor, the character designer, the bible-builder and the packaging check cite it. Raw data: the author's `ai-romance-novels/calibration-data.zip`.*

Built 2026-10-29 from 40 published books and 611 scored reader and critic reviews.

## What the data is

- **Structure reads.** Every book was read in full. For each one we recorded:
  - point of view, tense and narrators
  - heat level
  - where the first kiss and first sex fall
  - the dark moment's position and cause, and whether one honest talk would fix it
  - how much of the book follows the climax
  - the heroine's age
  - side cast, tropes and prose tics
- **Reviews.** About 15 per book, spread across 1 to 5 stars where possible. Each review was scored against 26 construction codes (+ praise, − criticism, mixed). Each book's reader reviews were weighted by its real Goodreads star distribution.
- **Lanes:**
  - **A, clean small-town romance:** 12 books.
  - **B, spicy novellas:** 12 books.
  - **C, other contemporary romance:** 9 books.
  - **D, book-club, thriller and historical:** 7 books, used as reference only.

**Limits.**
- The set was chosen to include well-rated and poorly rated books on purpose. Anything that differs between the two groups is a strong hint, not proof.
- Author fan bases are a confound. Debbie Macomber and Carolyn Brown readers rate generously.
- Goodreads and other sites block star-filtered review lists, so 1- and 2-star reviews are under-sampled. Where no star was given, a review was weighted by its verdict.
- With 12 books per lane, treat the differences between groups as directional.

---

## Rules for every book

### 1. The dark moment must survive an honest conversation
- 29 of the 33 romances use a conflict that one talk would fix. Readers punish this more than anything else in the set.

  | Cause of the dark moment | Review comments | Negative |
  |---|---|---|
  | Misunderstanding | 27 | 22 |
  | Secret revealed | 15 | 12 |
  | Pride or values clash | 7 | 6 |
  | Outside obstacle | 4 | 4 |
  | External danger | 1 | 0 |
  | No dark moment | 2 | 0 |

- The 4 romances whose conflict can't be fixed by talking average **4.20** on Goodreads. The 29 that can be fixed average **3.83**.
- Even highly rated books draw this complaint at every star level. *Nora Goes Off Script* (4.04) is an example.
- **Check at the outline stage:** "If the two leads sat down and told each other the whole truth, would the problem go away?" If yes, rebuild the conflict so it rests on:
  - a real clash of goals or values, such as kids, a city or a career that can't both be kept, or
  - an outside force they can't control.
- *Summer Romance* is praised for an obstacle that is visible from chapter 1: her divorce and her kids.

### 2. Avoid sameness
- Formula and predictability is the most negative code in every romance lane:

  | Lane | Raw score | Weighted score |
  |---|---|---|
  | A | −61 | −50 |
  | B | −64 | −43 |
  | C | −64 | −59 |

- Readers notice repeats inside one author's catalogue: "carbon copies," "rinse and repeat."
- **Pipeline:** keep a series ledger of premises, tropes, pet names, set pieces and dark-moment types already used. Have the outline agent avoid repeats.

### 3. The packaging must match the book
- Every packaging or promise mismatch comment was negative: 25 of 28 overall, the other 3 mixed.
- The mismatch goes both ways:
  - more spice than a cozy cover suggests (the Gilmore books)
  - less heat than a kink premise promises (Jacquot)
  - grief under a light rom-com cover (*Beach Read*, *Summer Romance*)
  - a title that promises something the book doesn't deliver (*Sawmill Book Club*, *Pride and Prejudice and Mistletoe*)
  - faith content that isn't disclosed (*Theo of Golden*)
- **Pipeline:** add a packaging check that compares the title, blurb, cover brief and heat label against the manuscript.

### 4. Don't rush the resolution
- Rushed or abrupt endings are criticized across all lanes.
- The share of the book after the climax doesn't separate high and low ratings: books with 8% or more and books with less both average 3.88.
- What readers punish is resolving the conflict off-page or in a few hundred words. *Naughty Boss* is the clearest case: its story ends at 69% of the ebook.
- **Check:** the reconciliation happens on the page, in a scene, with both leads present.

### 5. Spend effort where readers reward it
These are the most praised codes:
- the hook (+79 to +97 weighted)
- the side cast and found family (+70 to +77)
- emotional payoff (+82 to +91)
- humor (spicy lane +97)
- the epilogue (+74 to +77)

### 6. Watch prose tics
- Prose scores negative in lanes B and C (raw −34, −47).
- Repeated complaints:
  - overused pet names and slang
  - stacked metaphors and purple prose
  - repeated phrasing
  - "sparks when hands brushed"
  - statements punctuated as questions
- **Pipeline:** the line editor caps each pet name or catchphrase per chapter, and flags repeated physical-reaction lines and stacked metaphors.

### 7. No one-note villains
Villains score −55 weighted in lane A and −57 in lane C.

---

## Lane A: clean small-town romance

**What readers reward:**

| Element | Weighted score |
|---|---|
| Setting and atmosphere | +91 |
| Emotional payoff | +82 |
| Heat level (closed-door is accepted when promised) | +79 |
| Side cast | +71 |
| Theme | +60 |

**What readers punish:**

| Element | Weighted score |
|---|---|
| Packaging mismatch | −100 |
| Dark moment | −58 |
| Formula | −50 |
| Twists and coincidence | −42 |
| Subplot | −30 |

**Structure norms in the set.** Most books:
- are heroine-only or heroine-led
- use first person present or third person past
- have no explicit scenes
- put the climax at 85–96%
- end with a reward-stacking time-jump epilogue

**Calibration points:**
- **Give the hero chapters.** Books with hero point-of-view chapters average **4.09** (5 books); books without average **3.63** (7 books). The structure readers flagged the missing hero point of view in *Girls of Summer*, *The Holiday Swap* and *Pride and Prejudice and Mistletoe*.
- **Older heroines work, but write her at her real age.**
  - Heroines 38 and older average **3.98** (5 books); younger heroines average **3.72** (7 books). Reviewers welcome middle-aged leads.
  - What they punish is a 49- or 54-year-old written as if she were in her 70s (*The Bucket List*, *Must Love Flowers*).
  - They also punish making the age gap the obstacle and repeating it. That was the top complaint in *Girls of Summer*.
  - **Rule:** state her age once. Give her a current wardrobe, technology, work and desire. Don't use age as the conflict.
- **Show the courtship on the page.** *Alaskan Holiday* opens after the couple has already fallen in love, and that is its main 1–2 star complaint.
- **Chemistry is the weak spot of clean books** (+25 weighted, against +30 to +56 in the other lanes). Closed-door doesn't mean tension-free. Use proximity, near-misses, interruptions and charged conversation. Kissing earlier didn't help: books with a first kiss before 40% average 3.82, and the rest average 3.91. What helps is tension the reader can see.
- **A strong device helps.** The journal entries in *The Family Journal* and the comic premise of *The Bucket List* are both praised. On-the-nose theme statements are criticized.
- **Holiday titles rate lower.** Holiday-themed romances average **3.73**; the others average **3.94**. Seasonal books may draw impulse readers with different expectations.
- **Faith.** Keep it light, or disclose it in the packaging if it's central.

---

## Lane B: spicy novellas (15–50K words)

**What readers reward:**

| Element | Weighted score |
|---|---|
| Humor | +97 |
| Older heroine or age gap | +90 |
| Hook | +79 |
| Narration (dual point of view) | +79 |
| Epilogue | +74 |
| Side cast | +70 |
| Heat level | +59 |

**What readers punish:**

| Element | Score |
|---|---|
| Packaging mismatch | −100 weighted |
| Formula | −43 weighted |
| Prose tics | −34 raw |

**Structure norms in the set:**
- 15–31K words
- often a single day or a compressed timeline
- first person, mostly present tense, dual point of view
- short chapters under about 1.5K words
- the couple already knows each other or is stuck together
- the hero falls first
- the dark moment is small or absent

**Heat placement** falls into one of two patterns:
- front-loaded kink, with 4–6 explicit scenes
- a late slow burn, with the first kiss or first sex at 86–92%

**Calibration points:**
- **Set expectations for a standalone.** Series add-on novellas average **4.22**; standalones average **3.63**. The high ratings come from existing fans. A debut standalone spicy novella should expect a rating in the high 3s.
  - **Strategy:** release the novella next to a full-length book, or as a companion to one, rather than first.
- **Length.** "Wanted more" counts as praise. Readers punish a thin plot or rushed intimacy. Give the relationship at least one real turn, not only sex scenes. *Dipped in Holly* drew criticism for having no arc.
- **Deliver the promised heat.** Spicy readers punish having less than the premise implies.
- **The older-heroine or younger-hero angle is liked.** In *Mother's Day Inn*, every reviewer who mentioned it was positive. Make consent and the hero's intentions clear: one structure reader called *Mother's Day Inn*'s secret scheme borderline.
- **Intimate scenes must handle consent and protection clearly.** This was a recurring complaint about *Under One Roof*.
- **Pet names in sex scenes divide readers** ("mama," "baby girl"). Use them sparingly and on purpose.

---

## Checks to add to the pipeline

1. **Outline:** the one-talk test for the dark moment, and the series-ledger check for repeats.
2. **Outline:** the hero has point-of-view chapters (lane A), and the courtship happens on the page.
3. **Character bible:** the heroine's age, with age-true behavior notes, and the age gap is not used as the obstacle.
4. **Draft:** the reconciliation happens in a scene, and the ending isn't abrupt.
5. **Line edit:** caps on pet names and catchphrases, and flags for metaphor density and repeated reaction lines.
6. **Packaging:** the title, blurb, cover brief, heat label and faith disclosure all match the manuscript.
