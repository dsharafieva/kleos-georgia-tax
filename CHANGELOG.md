# Changelog

Reasoning is kept here; current state is in `README.md`.

---

## 0.1.0 — initial build

Built from the Armenia revision of the shared template rather than
`kleos-landing-countryguide-draft.html`. Both carry a byte-identical stylesheet
and the same `data-node-id` set, but the Armenia file is the newer revision and
already matched the approved section order, so no sections had to be deleted.

83 replacements, every one guarded by an exact match-count assertion so template
drift would fail loudly rather than silently mangle the markup.

**Structural decisions taken at build time**

- Calculator cut from four tabs to three. This is a fix, not a trim:
  `.calc__tab` is `width: 409px` against a 1260px inner, so Armenia's four tabs
  were already overflowing. Three fit at 1259px.
- Micro Business Status demoted from a tab to a note. GEL 30,000 is below any
  professional engagement.
- The third `lowflat` card changed from VAT to the activity restriction.
- Contributions card reduced to one figure, because Georgia has no
  social-insurance and no mandatory medical contribution. Not padded for parity.
- Timeline held at four beats. `.yearlife` is `height: 1299px; overflow: hidden`
  with the card at `top: 324px`, so a fifth beat would have been clipped.
- A right-to-work section was added in the slot Belarus uses for sanctions,
  reusing the `sanctions__*` component, whose classes exist unused in the
  stylesheet, and its real Figma node ids.

---

## 0.2.0 — copy and currency

- H1 reverted to the series line, "Here's where the money actually goes".
- Hero subtext rewritten twice: first from a list of page topics to buyer
  actions, then shortened. Settled on the Armenia construction, "Below it — …
  and what it costs if the arrangement reads as employment".
- **VAT removed entirely.** The card became the activity restriction; two
  surviving clauses in the calculator note and the disclaimer were also
  stripped. Zero VAT references outside the stylesheet.
- **Switched from lari display to US dollars.** Statutory thresholds are held in
  lari and converted for display, following the Armenia pattern, so the lari
  figure remains the one that binds. Rate: an indicative 2.60 GEL/$, from a
  mid-market 0.38439 USD/GEL; the National Bank official rate was 0.3813 on
  6 August 2026, i.e. 2.62.
- `lowflat` heading changed from "Three taxes" to "Three things", since after
  the VAT cut only two of the three cards are taxes. Flagged rather than left
  silent, because it departs from the series wording.

## 0.2.1 — calculator note overflow

Reported as broken text. Two causes, one visible and one not.

The static note ran to 5.1 lines against a budget of 4.83: `.calc__card` is
485px with `overflow: hidden` and `.calc__note` starts at 402px with a 17.17px
line-height.

The larger cause was in the script. `render()` appended the active regime's
explanation to the static copy, so at runtime every tab produced static text
plus a blank line plus three to nine more lines. It was clipped on every tab,
always, which is why the screenshot showed it cut mid-sentence.

Fixed by making the regime note **replace** the static copy rather than append
to it, and trimming every model note to under ~330 characters. All five states
now measure between 1.0 and 3.0 lines.

The contributions paragraph was dropped from the note as a duplicate of the
`lowflat` card and the disclaimer; the micro-business fact moved to FAQ 5.

*The live Armenia page has the same appending bug.*

## 0.2.2 — voice

- Removed meta-commentary about the page itself: "This is the shortest card on
  the page and it is not an omission", "the most common and most avoidable
  mistake on this page", "more here than anywhere else on this page".
- Replaced "Revenue Service" with plain language in four places. The
  institutional name is kept once, in the misclassification intro, where the
  point is that an official body publishes the test, and once in the disclaimer.
- Timeline warncard rewritten to name misclassification and its mechanism
  instead of counting signals abstractly.
- Em-dashes in visible copy reduced from 13 to 4, deliberately via different
  marks — colons, full stops, commas and reordering — so one tic was not traded
  for another. The worst case was FAQ 6, which had two in a single sentence.

## 0.3.0 — sections removed

- **Info-tile row** under `taxes` removed, all three tiles with their wrapper.
- **`screen` section removed.** Cost: one mid-page product mention and one CTA
  button; `btn--primary` now appears once, in the hero. The resulting
  `employee → cases` adjacency is already handled by
  `.employee + .cases { margin-top: 0 }`, a rule written for the draft's
  original order.
- **Right-to-work section removed.** Reasoning matters here, because the section
  was the strongest differentiator found in research.

  Challenged on why it was there, three problems surfaced. Its load-bearing
  sentence claimed "a large share of Georgian individual entrepreneurs are not
  Georgian nationals" — unverified, and Geostat puts foreign-individual-owned
  enterprises at about 101,400 of roughly 921,500, so "large share" was an
  overstatement. The regime was still moving. And the fact was already on the
  page in `cases` card 4.

  Kept the cases card, added a ninth FAQ item with the dates, dropped the
  unverified claim. The section would have been substantially wrong six weeks
  later — see 0.4.0.

## 0.3.1 — checklist audit

Audited all nine inherited signals against ILO Recommendation No. 198 as adopted
in Georgian judicial practice, the three limbs of the subordination principle
(`ქვემდებარეობის პრინციპი`) and Supreme Court decisions ას-1129-1156-2011 and
ას-863-825-2014.

Eight of nine confirmed against a named criterion. Two changes:

- Signal 2 reframed to lead with internal labour regulations, a genuine
  statutory marker under Labour Code art. 13, rather than contract vocabulary.
  Georgian doctrine is explicitly facts-over-labels, which made the original
  the weakest item on the list.
- **Signal 10 added: financial risk of the worker**, ILO Rec. 198 §6.2.2.1.7.
  A named criterion absent from all nine — a gap inherited from Armenia.

Score bands recalculated. A straight "of 9" → "of 10" substitution left the text
saying "reads as employment" at six ticks while the colour escalated at seven;
the text threshold was moved to keep them aligned, preserving the original
proportion.

## 0.3.2 — FAQ and copy trims

Three FAQ answers were outliers. Range tightened from 336–901 to 336–613.

- FAQ 4: dropped the resolution number, transitional dates, the enterprise-count
  figure and the portal URL. The dates concern the contractor, not the buyer.
- FAQ 5: dropped the micro-business paragraph, a duplicate of the calculator note.
- FAQ 9: dropped "by regional standards", "set by decree in 1999" and
  "Different page, different arithmetic".

Misclassification result note cut from 541 to 209 characters. It duplicated
FAQ 8 almost word for word; the widget now gives the conclusion and the FAQ
gives the detail.

---

## 0.4.0 — factual audit

Full pass over every claim. **One material error found, in the item previously
described as the strongest finding of the research.**

### Right to work was rolled back

Amendments passed **16 April 2026** added to the exempted-persons list of the
Law on Labour Migration:

> Persons who carry out labour activity / provision of services for the benefit
> of a non-resident person, where that activity is connected to the
> non-resident's business activities conducted outside the territory of Georgia.

That is this page's primary scenario: a foreign company paying a
Georgia-based contractor for work on that company's own business. The page
asserted in two places that such a contractor needs authorisation. Corrected in
`cases` card 4, FAQ 4, the hero trust line and the disclaimer.

Also in the same amendments: "partner" removed from the definition of
self-employed foreigner; a short-term professional activity exemption
introduced; the GEL 50,000 turnover requirement removed from the work residence
permit provision pending an ordinance.

Confirmed against four sources including links to `info.parliament.ge`.

Vindicates the 0.3.0 decision to cut the dedicated section: it would now be
wrong across two screens rather than two paragraphs.

### Questionnaire question count removed

"Thirty-eight-question test" rested on a single 2024 secondary source and could
not be independently confirmed; searches return only US-state results. Now
"its own questionnaire". The administrative-not-statutory caveat stays, because
it is the legally load-bearing part.

### State pension share corrected

The card read "2% + 2% + 2%" and the disclaimer "2% each from employee, employer
and state". The state share is stepped: 2% up to GEL 24,000 of annual income,
1% between GEL 24,000 and GEL 60,000, nothing above. Only the employee and
employer shares are flat. Card now reads "2% + 2%, plus a state top-up", with the
steps in the disclaimer.

---

## 0.4.1 — disclaimer

Disclaimer shortened from roughly 2,400 to 1,373 characters. Conversion date
dropped in favour of "an indicative 2.60 GEL/$", following the Belarus
precedent, which carries a rate but no date. The rate itself is kept so the
dollar figures on the page remain reproducible.

Two consequences recorded as open items: the state pension steps and the two
statutory fines, GEL 500 and GEL 2,000, are no longer anchored in lari anywhere
on the page.
