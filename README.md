# Kleos — Georgia contractor guide

Country page for the Kleos contractor-of-record series. Single self-contained
HTML file: markup, stylesheet and calculator in one document, no build step.

**Audience:** a foreign company paying a contractor based in Georgia (the
country). Not the contractor, and not an employer-of-record buyer.

**Status:** structurally complete, pending legal sign-off. Do not publish before
the items in [Needs legal review](#needs-legal-review) are cleared.

---

## Files

| File | Purpose |
|---|---|
| `index.html` | The page. Markup + `<style>` + calculator script. |
| `README.md` | This file. Current state, verified facts, open items. |
| `CHANGELOG.md` | Revision history and the reasoning behind each change. |
| `streamlit_app.py` | Local preview harness, fixed at 1440px. |
| `requirements.txt` | Preview dependencies. |
| `.gitignore` | Standard Python and editor excludes. |

## Preview

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

The page is laid out for a fixed 1440px canvas, matching the Figma frame. The
harness pins that width so what you see matches the design; resizing the browser
will not reflow it, because the stylesheet has no breakpoints.

---

## Structure

Eight sections, derived from the Armenia revision of the shared template. Figma
node ids are preserved in `data-node-id` for round-tripping via html.to.design.

| # | Section | id | Notes |
|---|---|---|---|
| 1 | `hero` | `top` | Georgian flag SVG is a simplified placeholder |
| 2 | `dark` | `calculator` | Three regime tabs, USD input |
| 3 | `lowflat` | `taxes` | Three dark cards, no info-tile row |
| 4 | `yearlife` | `deadlines` | Four timeline beats |
| 5 | `employee` | `misclassification` | Ten-signal checklist, live scoring |
| 6 | `cases` | `what-to-ask` | Four cards |
| 7 | `faq` | `faq` | Nine items |
| 8 | `ctacard` | `demo` | Footer disclaimer lives here |

### Deliberate departures from the reference pages

Each of these was a decision, not an omission. Do not "restore" them without
reading the reason.

- **Three calculator tabs, not four.** Georgia has four legally distinct
  arrangements, but Micro Business Status caps at GEL 30,000 and cannot fit a
  professional engagement, so it is a note under the calculator rather than a
  tab. `.calc__tab` is `width: 409px` against a 1260px inner: three tabs fit at
  1259px, four overflow.
- **No VAT card.** Services to a non-resident business are outside Georgian VAT
  and excluded from the GEL 100,000 registration threshold, so VAT is a
  non-event for a contractor billing abroad. The third card carries the
  activity restriction instead, which is the page's central thesis. VAT is not
  mentioned anywhere on the page.
- **No LLC or company route**, consistent with the series. Virtual Zone and
  International Company appear only as a caveat in `cases`, framed as "your
  contractor may invoice through a company".
- **Contributions card carries one number, not three.** Georgia has no
  social-insurance and no mandatory medical contribution. The section is short
  because there is nothing there; it has not been padded for parity with Armenia.
- **No info-tile row** under `taxes` (removed; the figures live in the card chips).
- **No `screen` section.** Removed, so the page has one mid-page product
  mention fewer than Armenia. `.employee + .cases { margin-top: 0 }` in the
  stylesheet already handles the resulting adjacency.
- **No dedicated right-to-work section.** Built, then removed: the regime was
  amended six weeks after it commenced and the exemption now covers this page's
  primary use case. The facts live in `cases` card 4 and FAQ 4, where a future
  amendment is a one-paragraph edit rather than a two-screen rewrite.
- **No EAEU or CIS reasoning.** Georgia is not an EAEU member and left the CIS
  in 2009. Mobility and mutual-recognition arguments used on other pages in the
  series do not transfer here.
- **No EU accession framing.** Candidate status has been shelved by the Georgian
  government until end-2028 and the 2026 labour-migration reform moved away from
  open-market policy, so the "regulatory alignment" argument points the wrong way.

---

## Editing constraints

**The `<style>` block is never modified.** It is 34,739 characters and
byte-identical to the Armenia reference. Verify after any edit:

```bash
python3 - <<'EOF'
import io, hashlib
css = io.open('index.html', encoding='utf-8').read().split('<style>')[1].split('</style>')[0]
assert len(css) == 34739, len(css)
assert hashlib.sha256(css.encode()).hexdigest().startswith('d90ba6727a31632d'), 'CSS CHANGED'
print('CSS intact')
EOF
```

Layout overrides go inline on the element, following the pattern already used
for the calculator bar widths.

### Container budgets

These are hard limits in the stylesheet. Copy that exceeds them is silently
clipped, because the parents are `overflow: hidden`.

| Element | Budget | Why |
|---|---|---|
| `.calc__note` | **4 lines** | `.calc__card` is 485px, note starts at 402px, line-height 17.17px → 83px |
| `.calc__tab` | **3 tabs** | 409px each against a 1260px inner |
| `.yearlife` timeline | **4 beats** | Section is `height: 1299px; overflow: hidden`, card starts at 324px |
| `.testimonial` | 396px fixed | Three cards in `lowflat` |
| `.testimonial__item-text` chips | ~40 chars | Longest current is 40 |
| `.ctacard__title` | ~3.5 lines | 56px font in a 553px usable width |
| `.employee__card`, `.faq__list`, `.cases__grid` | no fixed height | Item counts are free |

The calculator note is the one that bit. `render()` **replaces** the note with
the active regime's text rather than appending to the static copy; appending
could never fit four lines. Keep each model note under ~330 characters.

*Note: the live Armenia page has the same appending bug and clips its note on
every tab. Worth fixing there separately.*

### Calculator

All rates are constants at the top of the script, updatable in one place.
Statutory thresholds are held in lari and converted for display, so the lari
figure remains the one that binds:

```js
var GEL_PER_USD   = 2.60;   // indicative
var SBS_RATE      = 0.01;
var SBS_EXCESS    = 0.03;
var SBS_CEIL_GEL  = 500000;
var MICRO_CEIL_GEL = 30000; // not modelled, shown as a note
var PIT           = 0.20;
```

Default invoice is $36,000/year, matching Armenia so the two pages compare.
The 3% band engages at $192,307.69, i.e. exactly GEL 500,000.

### Checklist scoring

Ten signals. Bands are editorial and claim no legal threshold, because the
criteria are administrative rather than statutory.

| Ticked | Message | Colour |
|---|---|---|
| 0 | genuine services | default |
| 1–2 | still contracting | default |
| 3–6 | mixed | orange text |
| 7–10 | reads as employment | orange block |

The count appears in three places in the script and in the timeline warncard.
Change the number of `.chk` items and all four must move together.

---

## Verified

Multiply sourced against PwC Worldwide Tax Summaries, Andersen Georgia,
TPSolution, Forbes Georgia, matsne.gov.ge and rs.ge.

- Small Business Status: 1% of gross turnover, GEL 500,000 ceiling, 3% on the
  excess from the month of crossing to 31 December; status revoked
  automatically on 1 January of the third year if the ceiling is crossed in two
  consecutive years
- The 1% rate runs only from the first day of the month after the status is
  granted; a separate application from IE registration
- Micro Business Status: 0% up to GEL 30,000, closes on hiring or VAT registration
- Standard rates: 20% PIT, 15% CIT on distributed profit, 18% VAT
- Government Resolution No. 415 of 29 December 2010, Appendix 4: bars
  licensed activities, significant-investment activities, currency exchange,
  **medical, architectural, legal or notarial, auditing, consulting (including
  tax)**, gambling, personnel provision, excise-goods production
- Salary income is excluded from Small Business Status by the Tax Code, which is
  why reclassification moves the money from 1% to 20%
- Withholding: a Georgian payer withholds 20% from a non-entrepreneurial
  individual, nothing from a registered IE; 10% on other Georgian-source income
  to non-residents; 15% to preferential jurisdictions; **a foreign payer with no
  permanent establishment withholds nothing**
- Tax Code art. 104: services physically performed in Georgia are
  Georgian-source; art. 104(2) makes the place of receipt irrelevant
- No general social-insurance system, no mandatory medical contribution, no
  unemployment levy
- Funded pension mandatory for employees at 2% employee + 2% employer; the state
  adds 2% up to GEL 24,000 of annual income, 1% between GEL 24,000 and
  GEL 60,000, nothing above; voluntary for the self-employed at 4%
- Private-sector minimum wage GEL 20/month, Presidential Decree No. 351 of
  4 June 1999, never revised; market floor is roughly GEL 1,000–1,200
- Labour Code: numerus clausus termination grounds; 30 days' notice + one
  month's severance, or 3 days' notice + two months'; 6-month probation;
  40-hour week; 24 working days' paid leave; final settlement within 7 days
- No employment-contract state register in Georgia
- Right to work: regime in force 1 March 2026 under Government Resolution
  No. 70 of 20 February 2026; **amendments of 16 April 2026 exempt persons
  providing services for the benefit of a non-resident whose business activity
  is conducted outside Georgia**, remove "partner" from the definition of
  self-employed foreigner, and add a short-term professional activity exemption
  still to be scoped by ordinance
- Georgia is not an EAEU member and left the CIS in 2009; EU candidate status
  granted 14 December 2023, accession shelved by the government on
  28 November 2024

---

## Needs legal review

Escalation point for this page is **not** Gayane — Georgia is outside her
jurisdictions. This needs a Georgian adviser.

### Interpretive

| # | Claim | Issue |
|---|---|---|
| L1 | The page says software development, design and marketing "qualify" for the 1% rate | Resolution 415 lists what is **barred**, not what is permitted. "Not named in the prohibition" is not the same as "qualifies". The boundary between barred consulting and permitted marketing is a matter of practice and of the activity code on the certificate. **The page currently sounds more certain than the source allows.** This is the most likely place for a reviewer to stop. |
| L2 | Small Business Status and VAT registration coexist | Sources directly contradict. Andersen says separate; Tbilisi Expat says VAT registration costs the 1% rate. Following Andersen. Not currently visible on the page (VAT was removed) but it underpins the decision to omit VAT. |
| L3 | Reclassification exposure "lands on your contractor", with the payer's exposure second-order | The tax mechanism is well sourced. The claim that the foreign payer's exposure is limited is an inference from the absence of a positive rule, not from one. |
| L4 | A foreign payer with no PE has no Georgian withholding or filing obligation | Well supported, but it is a categorical statement about another country's tax law on a commercial page. |

### Single-source claims

Each rests on one source, none of it primary. Plausible, unverified.

| # | Claim | Where | Source |
|---|---|---|---|
| S1 | GEL 500 fine for carrying on a prohibited activity (shown as ~$190) | `taxes` chip, FAQ 8 | one accounting blog |
| S2 | No reapplication for the status until the following tax year | FAQ 8 | ExpatHub, March 2026 |
| S3 | Status tax payable only from a Georgian bank account; rs.ge login needs a Georgian phone number | FAQ 6 | ExpatHub |
| S4 | "articles 88 to 90 of the Tax Code" as the basis for Small Business Status | FAQ 5, disclaimer | assembled from three secondary sources, not confirmed against the code |

### Known simplifications

Accepted, flagged so nobody mistakes them for errors.

- **"There is no middle band"** (`taxes` card 1). Fixed Taxpayer Status is a
  third regime, but it covers tone ovens and beauty salons and has no bearing on
  this reader.
- **"No expense deduction" for an unregistered individual** (calculator note).
  True in practice; the statutory position is softer.
- **"$192,000" as a threshold** in the timeline and chips. The binding figure is
  GEL 500,000; the disclaimer says so.

---

## Open items

| # | Item | Owner |
|---|---|---|
| O1 | The Revenue Service questionnaire at `rs.ge/EmployeevsContractor` could not be read: Georgian-only JavaScript app, no server-rendered text. The ten checklist signals are derived from ILO Recommendation No. 198 as adopted in Georgian judicial practice and from Supreme Court decisions ას-1129-1156-2011 and ას-863-825-2014 — that is, from the basis the questionnaire was built on, **not from the questionnaire itself**. An earlier draft claimed "thirty-eight questions"; that number came from one secondary source and has been removed. | Georgian-reading adviser |
| O2 | Whether the checklist should mirror the questionnaire item for item. Depends on O1. | Content, after O1 |
| O3 | The right of disciplinary sanction is the one limb of the subordination principle only implied on the page, via "reviews" in signal 8. If a reviewer rates it higher than we did, it becomes an eleventh signal. | Georgian adviser |
| O4 | Right-to-work scope is still being codified by ordinance. Re-verify at `labourmigration.moh.gov.ge` immediately before publication. The regime moved in June 2025, February 2026, April 2026 and July 2026. | Content, pre-publication |
| O5 | GEL/USD rate is stated as an indicative 2.60 with no date, following the Belarus precedent. If the lari moves materially, the page has no internal signal that the figure is stale. | Content |
| O6 | Two fines appear only in dollars (~$190, ~$770). The lari originals, GEL 500 and GEL 2,000, are no longer anchored anywhere on the page after the disclaimer was trimmed. | Content |
| O7 | The Georgian-language string ინდივიდუალური მეწარმე is no longer on the page. Consider reinstating it once, as a recognition aid for a buyer reading a certificate. | Content |
| O8 | Hero image and CTA background are placeholders, and the CTA placeholder still carries a Russian-language asset filename from the Armenia file. Flag SVG is a simplified placeholder. | Pavel |
| O9 | Gap between `employee` and `cases` computes to zero after the `screen` section was removed. Handled by an existing stylesheet rule, but eyeball it at 1440px. | Pavel |
| O10 | One mid-page product mention and one CTA button were lost with the `screen` section. If a mid-page conversion point is wanted, the timeline warncard is the cheaper place for it. | Content |

## Not done

**Circleback was not searched.** The connector was not callable in the session
that produced this page, so no customer questions, objections, pricing
conversations or demo intelligence are reflected anywhere in this file. Worth a
pass before the page is used for sales enablement.

## Keyword note

Searchable demand for this topic is roughly 150–250 a month, and generic phrasing
is almost entirely contaminated by the US state: a Semrush `phrase_fullsearch`
on "contractors in georgia" returned 40 of 40 results about construction
licensing in Atlanta. Titles, H1s and targets should carry a Georgian-specific
noun — lari, Tbilisi, Revenue Service, individual entrepreneur, Small Business
Status — rather than the bare geographic phrase. This page earns its place as
sales enablement and credibility, not as an organic acquisition asset.
