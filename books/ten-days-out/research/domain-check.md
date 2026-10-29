# Ten Days Out: Domain check (setup mode, scoped to v2 facts)

*Domain-checker, October 28, 2026. Scope: only the new facts that outline revision 3.1 and "Settled after logic gate round 4" depend on. Three earlier outside rounds already checked the v1 facts in `story-bible-v1.md` (tides, ferry layout, radio rules, Maine EMD law, federal write-arounds), so this file doesn't re-check them. Verdicts: **OK** (confirmed against the sources listed), **adjust** (the core holds but a detail or word is wrong or unsupported), **wrong** (it would fail a reader in the trade). Anything I couldn't source is marked "unclear", never OK.*

## Summary

| # | Item | Verdict | One-line fix |
|---|---|---|---|
| 1 | Casualty and the no-passengers hold until a CG inspection | **OK** (wording adjust) | Keep Ned's line. Add one line saying the inspector was booked on the Day 7 boat that never came |
| 2 | No non-SAR CG flight; LifeFlight declines for icing and ceiling | **adjust** | The CG flight is a refusal, not a rule. Use "Northeast District", not "First District" |
| 3 | Beth can refuse a deputy's protection | **OK** | Never call her a "material witness" on the page |
| 4 | Cash over the slip: credit by count, flag, SAR not CTR | **OK** | Optional: a seal number beside "red" |
| 5 | Minimum crew; sailing short | **OK if** the COI minimum is master + one deckhand | Put the COI manning tiers in the bible |
| 6 | Beth's 100-ton license on the *North Reach* | **wrong** as specced (a 128-ft, 18-car ferry is about 300+ GRT) | Either shrink the boat to under 100 GT, or have Ned stand master while Beth has the wheel |
| 7 | A used Holland 34 for $31,000 | **wrong** (no Holland 34 exists; a Holland 32 costs far more) | "A '66 Webbers Cove 34 with a rebuilt Cat", firm at 31 |
| 8 | Iridium texts; calling an Iridium from a cell on the booster | **OK** (adjust the screen) | One message open on screen; the broker's is the next line in the inbox |
| 9 | Maine shorts law; Ned thinking the reefer carries shorts | **OK** (adjust the tell) | "The count ran high for the weight", not "the weights didn't match" |

---

## 1. Storm damage to the bow: must the ferry stop carrying passengers until the Coast Guard inspects?

**Claim (outline, Ch 2 s3, Logic holes):** The transfer bridge comes down on the bow and cracks the forepeak. Ned: "She's not carrying anybody till somebody from the Coast Guard has his hand on that." The inspector comes on Day 9. Day 10 the boat runs ("Take her across tomorrow").

**Verdict: OK, with one adjustment to the timing.**

**What is actually the case:**
- **Immediate notice.** Damage "materially and adversely affecting the vessel's seaworthiness or fitness for service or route" (flooding is a listed example) requires notice to the nearest Coast Guard unit "immediately after addressing resultant safety concerns" (46 CFR 4.05-1). Ned would call it in on Day 1 night, by VHF or landline, to Sector Northern New England (South Portland).
- **Written report.** Form **CG-2692, Report of Marine Casualty**, is due within **5 days** (46 CFR 4.05-10). Ned filling it in at the mess table on Day 3 or 4 is good texture. The trade calls it "the 2692."
- **Repairs need the OCMI.** Repairs affecting safety may not be made without the knowledge or approval of the Officer in Charge, Marine Inspection (46 CFR 71.55-1 for vessels of 100 GT or more; 46 CFR 176.700 for Subchapter T boats under 100 GT). Emergency repairs are allowed if the OCMI is told as soon as practicable afterward. The OCMI may require an inspection after a repair (176.700). The general rule is 46 CFR 2.01-15, and a move to a shipyard needs a CG-948 "Permit to Proceed to Another Port for Repairs."
- **Precedent for the hold.** In November the Steamship Authority's ferry *Iyanough* was taken out of service for a hull crack and returned "following inspection by the U.S. Coast Guard" (Marine Log). Ned's line matches practice.
- **How long.** No source gives a standard wait. In practice an inspector comes on the first transport the sea allows. In this book that could be the Day 6–7 window, which makes a Day 9 inspector look slow unless the page explains it. *Unclear; this is from working knowledge, not a source.*
- **Separate constraint.** With the transfer bridge down, no vehicles can load at the island slip anyway, whatever the inspection says. The Day 10 run needs the temporary ramp or barge already in v1 research note 5 ("foot traffic and pickups only").

**Smallest change:**
- Keep Ned's line as written.
- Add one line, in Ch 6 or Ch 7, saying the inspector was booked on the Day 7 first-light boat, the same window that was shot out. Then Day 9 follows from the weather and needs no explanation.
- Optional texture: the 2692 on the mess table, and "Sector" as the word Ned uses.
- On Day 9 the inspector accepts a temporary repair to the forepeak and clears limited service. The Day 10 run stays foot traffic and pickups, as v1 note 5 already says.

**Sources:**
- [46 CFR 4.05-1 (Cornell LII)](https://www.law.cornell.edu/cfr/text/46/4.05-1)
- [46 CFR 4.05-10 (Cornell LII)](https://www.law.cornell.edu/cfr/text/46/4.05-10)
- [CG-2692 form (USCG)](https://www.dco.uscg.mil/Portals/9/DCO%20Documents/5p/CG-5PC/INV/docs/CG_2692.pdf)
- [46 CFR 71.55-1](https://federal-regs.com/title/46/part-71/71.55-1/)
- [46 CFR 176.700 (Cornell LII)](https://www.law.cornell.edu/cfr/text/46/176.700)
- [46 CFR 2.01-15 (Cornell LII)](https://www.law.cornell.edu/cfr/text/46/2.01-15)
- [Marine Log: *Iyanough* back in service after hull-crack repair](https://www.marinelog.com/passenger/ferries/steamship-authority-fast-ferry-iyanough-back-in-service-after-repair-to-hull-crack/)
- [USCG Sector Northern New England](https://www.atlanticarea.uscg.mil/Our-Organization/Northeast-District/Units/Sector-Northern-New-England/)

---

## 2. Would the Coast Guard fly a non-SAR federal witness transport? Would LifeFlight decline for icing or a low ceiling?

**Claim (outline, Logic holes; Ch 3, Ch 6):** Mrs. Dyer: LifeFlight won't fly on Day 2. Day 6: "no non-SAR flight and the helicopter offshore." Day 7: a Coast Guard lifeboat is timed for first light. Day 8: the gale.

**Verdict: adjust (Coast Guard wording); OK (LifeFlight).**

**What is actually the case:**
- **Coast Guard.** No rule bars the Coast Guard from moving a federal witness. 14 U.S.C. § 701(a) lets it, "when so requested by proper authority," use its personnel and facilities "to assist any Federal agency." So a lifeboat run for the Marshals on Day 7 is supported. A helicopter for a non-emergency transfer is a discretionary call on scarce aircraft, and the district would refuse it while its helicopter is on a case offshore. That refusal is believable, but it is a decision, not a rule. *I found no source on how often the Coast Guard flies witness moves; unclear.*
- **Name of the command.** The Coast Guard's own site now files Sector Northern New England under the "Northeast District" (the old First District). If anyone names the district in 2026, use "Northeast District." Safest is to say "the district" or "Sector."
- **LifeFlight.** LifeFlight says its aircraft "will remain on the ground if the weather is deemed unsafe for flight," judged on conditions at origin, destination and along the route. It names "visibility and ceiling (the altitude of the clouds)" as the limits. A LifeFlight pilot told NEWS CENTER Maine that crews start watching temperatures "below 4 degrees Celsius" and that "wet snow and freezing rain can be really dangerous to a helicopter" (icing). Two sources, both close to primary. A November nor'easter grounding the helicopter for Mrs. Dyer is accurate. LifeFlight also has a fixed-wing plane for wider weather, but Cutter has no airstrip, so only the helicopter matters.

**Smallest change:**
- Pike's Day 6 line becomes a refusal with a reason, for example: "District won't put a helicopter on a non-emergency move, and the one they've got is offshore on a case."
- Keep "Coast Guard will lift you" for the lifeboat.
- Never write "First District."

**Sources:**
- [14 U.S.C. § 701 (Cornell LII)](https://www.law.cornell.edu/uscode/text/14/701)
- [LifeFlight of Maine, "Rain and Fog: Summer 2023 in Review"](https://lifeflightmaine.org/rain-and-fog-summer-2023-in-review/)
- [NEWS CENTER Maine, "When LifeFlight can't come to the rescue"](https://newscentermaine.com/article/life/when-lifeflight-cant-come-to-the-rescue/97-343dfed2-0ff5-4f19-8e5f-a8ada3bf1c01)
- [USCG Northeast District / Sector Northern New England](https://www.atlanticarea.uscg.mil/Our-Organization/Northeast-District/Units/Sector-Northern-New-England/)

---

## 3. Voluntary protection for a witness who isn't in WITSEC: can she refuse a deputy marshal?

**Claim:** Beth is on an emergency protective transport pending a WITSEC decision ("the waiting room for the program"). She argues with Dane, refuses the safe house on Day 1 and works the boat anyway.

**Verdict: OK.**

**What is actually the case:**
- **WITSEC is by agreement.** Before WITSEC protection begins, the Attorney General must enter a memorandum of understanding with the person, and an adult signs it personally (18 U.S.C. § 3521(d)(1)–(2)). Temporary protection may start before the memorandum, which must then follow "without undue delay" (§ 3521(e)). That matches Dane's "waiting room."
- **Other programs.** There is a Marshals-run **Short-Term Protection Program**: relocation and subsistence with no new identity, overseen by the Criminal Division's Office of Enforcement Operations. There is also the U.S. Attorneys' **Emergency Witness Assistance Program**, which pays for temporary housing and transport but "does not include any protective services" (DOJ OIG). Either could sit behind Dane's line.
- **She can refuse.** Nothing in these programs compels a witness to accept a protector. What compels her is the **grand jury subpoena** (she must appear on Day 11). In the extreme, a judge can order a **material witness** arrested if her testimony is material and a subpoena may not secure her presence (18 U.S.C. § 3144). That is detention, and nobody would use it on a cooperating witness who calls in her own sighting.
- **What Dane can do if she refuses.** Stay close, report it to Pike, and document it. He can't make her go to the safe site.

**Smallest change:**
- No plot change.
- **Terminology:** never call Beth a "material witness" on the page. To a lawyer reader that means a § 3144 arrest. Use "witness," "your witness" or "the protectee."
- If Dane needs a name for her status, "short-term protection" is real.

**Sources:**
- [18 U.S.C. § 3521 (Cornell LII)](https://www.law.cornell.edu/uscode/text/18/3521)
- [DOJ OIG report, Appendix (Short-Term Protection Program)](https://oig.justice.gov/archives/reports/EOUSA/e0102/app2.htm)
- [DOJ OIG report, Introduction (EWAP)](https://oig.justice.gov/archives/reports/EOUSA/e0102/intro.htm)
- [18 U.S.C. § 3144 (govinfo)](https://www.govinfo.gov/content/pkg/USCODE-2023-title18/html/USCODE-2023-title18-partII-chap207-sec3144.htm)
- [USMS WITSEC](https://usmarshals.gov/witsec)

---

## 4. The credit union and a courier pouch holding more cash than the deposit slip

**Claim (outline; R4-1):** Ned adds $9,000 in hundreds to Beth's envelope (her slip shows only the paycheck). The credit union credits by count and flags it. The BSA officer calls on Day 2. The written report on Day 5 reads "Pouch: two bags. Seal noted: red."

**Verdict: OK. One optional realism detail.**

**What is actually the case:**
- **Credit by count.** Federal deposit-reconciliation guidance uses exactly this case: a customer deposits $110 but writes $100 on the slip. It calls that a "credit discrepancy" that harms the customer "if not appropriately reconciled." So the credit union credits the counted amount to the member's account (FFIEC agencies' guidance; NCUA issued it to credit unions as 16-CU-04).
- **The member is told.** The member normally gets a deposit-adjustment notice by mail or online banking. *The notice is standard practice, but I found no source for it; unclear.* That is fine for the plot: the mail stops with the ferry and the grid fails at 9 p.m. on Day 1. **Watch item:** if Beth has phone banking, she could have seen the $9,000 on Day 1 afternoon. Either give her no mobile banking (she banks by envelope, which is in character) or keep her phone dead or off all day.
- **No CTR.** A Currency Transaction Report is required for cash over $10,000 in one business day by or on behalf of one person; multiple transactions are aggregated only if they are for the same person (31 CFR 1010.313). $9,000 to Beth's account is under the limit, and the other envelopes are other members. The paycheck is a check, not cash.
- **A SAR is possible.** The threshold is $5,000 when a suspect can be identified, and the filing deadline is 30 days (12 CFR 21.11 for banks; credit unions follow the same scheme under 12 CFR 748.1). For an ongoing violation the institution "shall immediately notify, by telephone, an appropriate law enforcement authority." That supports the BSA officer phoning on Day 2.
- **SAR secrecy.** A SAR and anything revealing it are confidential. The credit union may not tell Beth or Tess that one exists, which fits Dane's "do not disclose to witness."
- **Who could see it.** The teller and a second staffer if bags are opened under dual control (*standard practice; unclear, no source*), the head teller or vault, the BSA officer and compliance, then the AUSA and HSI through the grand jury subpoena. Tess and the ferry district would see nothing unless called.
- **The seal note.** Tamper-evident bag seals are sold numbered and colored, and banks log them (seals.com; vendor listings for red and yellow numbered pull-tight seals). A discrepancy note naming the seal of the bag the envelope came from ("Seal noted: red") is plausible. A real log would usually give the seal **number** too. *Unclear: I found no source on teller wording.*

**Smallest change:**
- None required.
- Optional: "Pouch: two bags. Seal noted: red, no. 0417." The number doesn't break fairness unless someone traces the series, so make sure nobody on the page does.
- Keep "credited and flagged" in the notebook. It is the right phrase.

**Sources:**
- [Interagency Guidance on Deposit Reconciliation (Federal Reserve copy)](https://www.federalreserve.gov/supervisionreg/caletters/CA_16-2_Attachment_Interagency_Guidance_on_Deposit_Reconciliation.pdf)
- [NCUA Letter 16-CU-04](https://ncua.gov/regulation-supervision/letters-credit-unions-other-guidance/member-account-deposit-reconciliation-practices)
- [31 CFR 1010.313 (Cornell LII)](https://www.law.cornell.edu/cfr/text/31/1010.313)
- [12 CFR 21.11 (Cornell LII)](https://www.law.cornell.edu/cfr/text/12/21.11)
- [Seals.com, "Five top uses of security seals by banks"](https://seals.com/security-seals-blog/five-top-uses-of-security-seals-by-banks/)
- [Red numbered pull-tight seals (vendor)](https://wellbefore.com/products/red-consecutively-numbered-pull-tight-seals-case-of-100)

---

## 5. Minimum crew on a small Maine island car ferry; can the captain sail short-handed?

**Claim (outline Ch 1; bible):** Winter crew is captain, mate/engineer (off-island this week) and deckhand (Beth, with Kenny as second deckhand). On Day 0 Ned tries to send Beth home and "work it short", "against the manning rule she will cite at Pruett." On Day 1: "Kenny's puking and there's no relief on a storm Friday."

**Verdict: OK, provided the bible fixes the COI minimum at master plus one deckhand for the winter tier.**

**What is actually the case:**
- **The COI sets the crew.** The certificate of inspection states the required complement, and a vessel "may not be operated without having in its service the complement required in the certificate of inspection" (46 U.S.C. § 8101(a), (d)). The owner's civil penalty is $10,000 (§ 8101(f)).
- **Sailing short.** The master may sail short only when a crew member is lost *without the consent, fault or collusion* of the master, no credentialed replacement can be found, and the master judges the vessel "sufficiently manned for the voyage." He must report in writing to the OCMI within 12 hours of arrival (46 U.S.C. § 8101(e); 46 CFR 15.725).
  - Kenny being sick is a vacancy that qualifies.
  - **Ned sending Beth home is his own consent**, so he can't sail short on that ground. Beth is right at Pruett. This is the strongest version of the scene.
- **Real Maine practice.** MaineDOT says it takes "four-to-five trained and credentialed seamen" to run each state vessel (Maine Public). The largest state boat "requires an additional one to two crew hands" under Coast Guard rules, and when crew is short a smaller boat substitutes at lower capacity (MaineDOT). So manning is tied to passenger capacity. MaineDOT's 2024 fleet list shows the 130-ft *Captain Henry Lee* class at 60 passengers, against 250 at build, which fits a reduced-crew tier. A three-person winter crew on a small district ferry is plausible only if the COI has a low-passenger winter tier. *The exact tiers are unclear; COIs are vessel-specific and not public.*

**Smallest change (for the bible):**
- *North Reach* COI manning:
  - Winter tier (up to 49 passengers): master + one deckhand.
  - Up to 149 passengers: master + engineer + two deckhands.
- On Day 0, with the mate/engineer away and Kenny sick, Ned and Beth are the legal minimum. Without her the boat cannot sail.
- Beth's line at Pruett can be: "Master and one deck. That's the certificate. Without me she doesn't leave the slip."

**Sources:**
- [46 U.S.C. § 8101 (Cornell LII)](https://www.law.cornell.edu/uscode/text/46/8101)
- [46 CFR 15.725 (ecfr.io)](https://ecfr.io/Title-46/Section-15.725)
- [WHOI "Sailing Short" procedure (an operator's application of 15.725)](https://www.whoi.edu/wp-content/uploads/2021/12/SMM-Sailing-Short-092821.pdf)
- [MaineDOT, "Maine State Ferry Service adjusts capacity"](https://www.maine.gov/dot/news/maine-state-ferry-service-adjusts-capacity)
- [Maine Public, staffing shortages and cancellations (2022)](https://www.mainepublic.org/business-and-economy/2022-07-26/staffing-shortages-spark-dozens-of-state-ferry-cancellations)
- [MaineDOT MSFS presentation, Dec 2024 (fleet table)](https://www.maine.gov/dot/sites/maine.gov.dot/files/inline-files/Maine%20State%20Ferry%20Service%20Presentation%2012.11.24.pdf)

---

## 6. License tonnage: does Beth's 100-ton master's license cover the *North Reach*?

**Claim (outline, author decision 8):** "Beth's license covers the *North Reach*. Default: yes. Fallback: a relief master." The bible's *North Reach*: steel, 128 ft, bow-loading, built 1989, 149 passengers, about 18 cars or two tractor-trailers plus six cars. Beth holds a 100-ton master's license and takes the wheel on Day 10 with Ned standing master.

**Verdict: wrong as specced.**

**What is actually the case:**
- **A comparable ferry is far over 100 tons.** The *Captain Henry Lee*, a 130-ft Maine state car ferry carrying 17 vehicles, is **325 gross register tons** (Maritime Reporter, Jan 1993; MaineDOT fleet table). A 128-ft, 18-car ferry would measure about 300 GRT. A master's endorsement for "less than 100 GRT" doesn't cover it.
- **The state's own standard.** MaineDOT's ferry-captain posting requires a Coast Guard master's license "for the tonnage of largest vessel operated by the State" (500 GRT).
- **Beth can't simply upgrade.** A near-coastal master's endorsement under 500 GRT needs two years as master or mate while holding an officer endorsement (46 CFR 11.418). Beth has been a deckhand, so she couldn't qualify. *Partly blocked: Cornell's 11.418 and 11.426 pages didn't load; checked via federal-regs.com.*
- **The other way round works.** MaineDOT's new 104-ft *Charles Norman Shay* carries 149 passengers and up to 8 cars, or one tractor-trailer plus four light trucks, and is **under 100 GT** (Subchapter T). A boat of that size is one a 100-ton master can command.

**Smallest change: two options. The author or architect chooses.**
- **A (keeps the payoff literal; bible numbers change, no plot change):** make the *North Reach* about 104 ft and under 100 gross tons (Subchapter T). Certificated for 149 passengers and about 8 cars, or one tractor-trailer plus four light trucks.
  - Everything the plot uses still fits: the dealer's reefer on Day 0, the two storm-bound trucks on deck for the Ch 9 alley, the 149 passengers that keep the boat outside MTSA, and the layout.
  - Beth's 100-ton license then covers her. Day 10 stands as written.
  - Repair rules become 46 CFR 176.700 rather than 71.55-1.
  - Watch items: change "two tractor-trailers plus six cars" and "about 18 cars" in the bible, and check Ch 1 for a truck count over capacity.
- **B (keeps the boat):** Ned is master of record in the wheelhouse and Beth has the wheel and makes the landing. That is legal, because the master is aboard and in charge. *Unclear: from working knowledge, no source fetched.*
  - Decision 8 becomes "Beth takes the wheel under Ned's license."
  - One line in Ch 10 can pay the gap: "Start logging your mate time" from Ned.
  - Drop the claim that her license covers the boat.
  - The relief-master fallback isn't needed.

**Recommendation:** A, if the author wants "her license" to be the payoff; B, if the 128-ft boat matters more.

**Sources:**
- [Maritime Reporter, Jan 1993, p. 45 (*Captain Henry Lee*: 130 ft, 325 GRT, 250 passengers, 17 vehicles)](https://magazines.marinelink.com/Magazines/MaritimeReporter/199301/page/47)
- [MaineDOT MSFS presentation, Dec 2024](https://www.maine.gov/dot/sites/maine.gov.dot/files/inline-files/Maine%20State%20Ferry%20Service%20Presentation%2012.11.24.pdf)
- [MaineDOT ferry captain posting, Maine JobLink](https://joblink.maine.gov/jobs/1054818)
- [46 CFR 11.418 (federal-regs.com)](https://federal-regs.com/title/46/part-11/11.418/)
- [46 CFR Part 11 Subpart D index (Cornell LII)](https://www.law.cornell.edu/cfr/text/46/part-11/subpart-D)
- [Baird Maritime: *Charles Norman Shay* review (104 ft, 149 pax, under 100 GT, Subchapter T)](https://www.bairdmaritime.com/amp/story/passenger/ro-pax/vessel-review-charles-norman-shay-maine-transport-department-welcomes-new-lifeline-ferry-into-service)

---

## 7. Price of a used Holland 34 lobster boat in Maine, 2026

**Claim (outline):** "A used Holland 34 in a Pruett Harbor yard, 'firm at 31, Saturday noon'"; "a Holland 34 with a rebuilt Cat"; "thirty-one thousand dollars."

**Verdict: wrong, twice.**

**What is actually the case:**
- **There is no Holland 34.** Holland's Boat Shop (Belfast, Maine) built the Holland 30 (1973), 32 (from 1978), 38 (from 1986) and 14, plus a 38 stretched to 41 (Fishermen's Voice). Boat Trader lists only the 32, 38 and 14. A Maine boat reader will catch "Holland 34."
- **A Holland 32 is far above $31,000.** Current listings:
  - A 1980 working Holland 32 in Steuben, ME, at $85,000 (Cummins, 5,000 hours).
  - A 1987 at $139,900.
  - A 2015 in Rockport at $225,000.
  - The Holland 32 has largely become a picnic and commuter boat (Gamage Shipyard). That fits Beth's father's boat but not Dane's budget.
- **An old 34-footer can be near the number.** A **1966 Webbers Cove 34 with a Caterpillar 3304 diesel** is listed in Camden at **$44,995**. Other old working lobster boats list at about $40,000–68,000. $31,000 "firm" for a sixty-year-old hull in November, with the yard wanting it gone before storage, is believable. *The haggled figure is fiction and unclear, but it's in range.*

**Smallest change:** "a '66 Webbers Cove 34 with a rebuilt Cat," firm at 31. "Thirty-one," "34" and "rebuilt Cat" all stand, and only the make changes. In Ch 1 s3: "What's a Webbers Cove 34 with a rebuilt Cat worth?" If the author wants to keep "Holland," it must be a Holland 32, and the price goes to about 85, which breaks "thirty-one" in Ch 1–3.

**Sources:**
- [Fishermen's Voice, "Holland Boat" (models)](https://fishermensvoice.com/archives/201502HollandBoat.html)
- [Boat Trader, Holland make page](https://resources.boattrader.com/boats/make-holland)
- [1980 Holland 32, Steuben ME, $85,000 (boats.com)](https://ca.boats.com/power-boats/1980-holland-32-9823692)
- [1987 Holland 32, $139,900 (boats.com)](https://au.boats.com/power-boats/1987-holland-32-9909015)
- [2015 Holland 32, Rockport ME, $225,000 (boats.com)](https://www.boats.com/power-boats/2015-holland-32-9940430)
- [Gamage Shipyard, Holland 32](https://gamageshipyard.com/project/holland-32-for-sale/)
- [1966 Webbers Cove 34, Cat 3304, Camden ME, $44,995 (Boatzon)](https://boatzon.com/boat-detail/used-webbers-cove-34-1966-44-bayview-street-camden-me-04843-camden-me-us-1788260272496)
- [1986 Crusader 35 lobster boat, $68,000 (Ocean Marine)](https://www.oceanmarine.com/vessels/15911/pdf/view)

---

## 8. Iridium: texts on screen; can a cell phone on the store's booster call an Iridium number?

**Claim (outline Ch 3 s1; "Get right"):** Iridium texts arrive only under sky and stay on screen. Dane sets the sat phone down with the screen lit: "Pike: Q's request approved. Log daily. Do not disclose to witness." Under it, the broker's line. Ned's cell works only inside the store's booster and calls the *Margaret Ann*'s Iridium.

**Verdict: OK, with one adjustment to the screen.**

**What is actually the case:**
- **Sky view.** Iridium handsets "must be outside, with a clear view of the sky," and buildings interrupt the signal (Satellite Phone Store FAQ). Iridium's own messaging FAQ says line of sight to the satellites improves delivery and most messages arrive within 7 minutes.
- **Held until delivered.** Iridium SMS are "stored until delivered, up to 8 days" (MailASail). Texts sent while Dane is indoors land the next time he steps out.
- **Message length.** 160 characters; longer messages are truncated. Pike's line fits.
- **Sending to an Iridium.** Email to number@msg.iridium.com, the Iridium web form, or a text from a cell, which "is very operator dependent" (MailASail).
  - Pike would plausibly email from the office.
  - The yard broker texting from a cell is plausible with most US carriers.
- **The inbox.** Received texts sit in the handset's inbox. *Unclear (from the guides, not a manufacturer page):* the 9575's small monochrome screen shows one message open at a time, or a list.
- **Calling an Iridium from a cell.** Yes. A booster only amplifies the outside signal, so Ned's phone behaves like any cell phone on one bar. Dialing the 12-digit +8816 number directly is billed at the caller's carrier's satellite rates, which are "extremely high." The cheap route is **two-stage dialing**: call the Arizona gateway (+1-480-768-2500) as an ordinary US call, then enter the satellite number (GSAT). Either way the *Margaret Ann*'s set must be on and under sky. A dragger normally has an installed Iridium with a mast antenna, so it rings in the wheelhouse.

**Smallest change:**
- Ch 3 s1: Pike's message is open on the screen and the broker's is the next line in the inbox, or Beth presses the arrow once. Two full messages stacked on one 9575 screen would bother a reader who has used one.
- Optional texture for Ned's call: he dials the Arizona number first.

**Sources:**
- [Satellite Phone Store, Iridium FAQ](https://support.satellitephonestore.com/hc/en-us/articles/360054333432-Iridium-Satellite-Phone-FAQ-Frequently-Asked-Questions)
- [Iridium Messaging FAQ](https://messaging.iridium.com/faq/)
- [MailASail, Iridium SMS features and limitations](https://www.mailasail.com/Support/Send-Iridium-SMS)
- [BlueCosmo, Iridium Extreme SMS how-to](https://support.bluecosmo.com/hc/en-us/articles/4838219626516-Iridium-Extreme-How-To-Send-a-Text-SMS-Messages)
- [GSAT, two-stage dialing vs +1 access](https://www.gsat.us/node/266)

---

## 9. Maine "shorts" law; would Ned plausibly think the reefer moves undersized lobster?

**Claim (outline):** For a year Ned signed for the dealer's Thursday reefer "knowing something was wrong. The unit always ran, but the weights didn't match the manifest and the sternman was from away. He thought it was shorts." In Ch 6 he confesses to shorts, which is "true and smaller."

**Verdict: OK on the law; adjust the tell.**

**What is actually the case:**
- **The law.** Maine's legal size is 3 1/4 to 5 inches, measured with a certified gauge from the rear of the eye socket to the rear of the body shell. It is unlawful to "buy, sell, give away, transport, ship, or possess" a lobster outside those limits (12 M.R.S. § 6431(1)–(3)).
- **The penalty.** A **Class D crime**: a mandatory $500 per violation, plus $100 per lobster for the first five and **$200 per lobster after that**. If the count can't be determined, $1,000–5,000 (§ 6431(7)). A reefer load of shorts is a ruinous fine for the dealer and the end of his license.
- **Sealed imports.** Live imported lobsters moved between licensed dealers or shipped out of state in containers sealed under the commissioner's rules are exempt (§ 6431(6)). That makes a sealed reefer of "Canadian" product a cover a dealer might claim. Optional texture.
- **The gauge.** The ASMFC gauge increase (Addendum XXVII, to 3 5/16 in) was **repealed by Addendum XXXII in 2025**. The minimum is still 3 1/4 in. Don't mention a gauge change.
- **Enforcement.** The Maine Marine Patrol brings these cases, for example a Stonington lobsterman charged over 269 shorts and facing more than $100,000 in fines (National Fisherman).
- **The tell is the problem.** Shorts don't make the weight disagree with a manifest kept in pounds. They make the **count per crate run high for the weight**. Bricks of pills under the lobsters would make the boxes **heavier** than the manifest. As written, "the weights didn't match" points at the drugs, which is fine as a latent clue, but it isn't what would make a ferry captain think "shorts."
- **Ned's exposure.** The ferry is a carrier, not a dealer. Ned's own criminal exposure for a dealer's shorts is thin. His real fear, losing the contract that keeps the winter boat running, is what the outline already uses. Keep it that way.

**Smallest change:** make Ned's "something wrong" two things. First, the crates he saw opened ran small and many for the weight ("too many pieces to the crate"), which is shorts. Second, the boxes rode heavy, which the reader can later set against the pills. Keep "the unit always ran" and "the sternman was from away." Use "shorts" (islander word) and "the gauge" (Marine Patrol word). Never write "undersized lobsters" in Beth's or Ned's mouth.

**Sources:**
- [12 M.R.S. § 6431 (Maine Legislature)](https://legislature.maine.gov/statutes/12/title12sec6431.html)
- [SeafoodSource, ASMFC repeals gauge and vent changes (Addendum 32)](https://www.seafoodsource.com/news/supply-trade/asmfc-repeals-lobster-gauge-and-vent-size-changes)
- [ASMFC Addendum XXXII, May 2025](https://asmfc.org/wp-content/uploads/2025/05/AmLobsterAddendumXXXII_May2025.pdf)
- [National Fisherman, Stonington lobsterman charged](https://www.nationalfisherman.com/northeast/lobsterman-charged-with-possessing-undersized-lobsters)

---

## Things the bible does not say but the plot will need

*Facts a writer will have to invent in a scene, which a reader in the trade would check. Verified items have a source above; the rest are marked unclear.*

1. **The casualty paperwork.**
   - "Calling it in to Sector" on Day 1 night (VHF 16, then a working channel, or landline while it lasts).
   - The **CG-2692** within five days.
   - The inspector is "the marine inspector" or "the inspector from Sector," never "the Coast Guard guy from the district."
   - Clearing a temporary repair is the OCMI's call. (Sources: §1.)
2. **The COI manning tiers.** Pin them in the bible (§5) so Ch 1's fight and Ch 10's crossing count the same people.
3. **The sailing-short report.** If Ned ever sails short (Kenny sick, Beth aboard counts), he owes the OCMI a written report within 12 hours of arrival. That's one line of texture, or leave it unsaid. (§5.)
4. **The tonnage on Beth's credential.**
   - The words on a modern MMC are "Master of Self-Propelled Vessels of Less Than 100 GRT," upon near coastal waters. Islanders say "my hundred-ton."
   - Pick option A or B in §6 before Ch 4 plants "the license."
5. **The deposit-adjustment notice** the credit union would send Beth, and why she never sees it. The mail stops with the ferry, and she banks by envelope, not by app. *Unclear (practice, not a cited rule).* (§4.)
6. **The courier.** Who carries the pouch from the Pruett ramp to the credit union (an armored service, a credit-union runner, or a local courier on contract) and what the pouch is called ("the courier bag" or "the night bag"). *Unclear; no source.* The outline uses "pouch"; keep one word.
7. **How the Iridium is billed and dialed.** Two-stage dialing through the Arizona gateway is the realistic way an islander's cell reaches the dragger. (§8.)
8. **The dragger's Iridium.** An installed unit with a mast antenna that rings in the wheelhouse, so it works aboard with the deck lights on. *Unclear (standard fit-out, no source fetched).*
9. **LifeFlight's decision.** The pilot declines on weather (icing, ceiling, visibility), and the island's EMT stays with Mrs. Dyer. The book shouldn't have dispatch "cancel" it; it's the pilot's call. (§2.)
10. **The witness-program vocabulary.** "Protectee," "short-term protection," "the program." Never "material witness." (§3.)
11. **Lobster trade words.** "Shorts," "the gauge," "a lobster transportation license" (the dealer's truck needs one: § 6431(6-A) names lobster transportation license holders), "Marine Patrol." (§9.)

## Blocked or unfetched

- Cornell LII pages for 18 U.S.C. § 3144, 46 CFR 11.418 and 46 CFR 11.426 were blocked by the permission system. I used the govinfo and federal-regs.com copies instead. 46 CFR 11.426 (master under 200 GRT, near coastal) was not checked.
