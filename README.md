# Kleos — Georgia contractor-taxation page

A self-contained landing page explaining what a contractor in Georgia (the
country) actually keeps, with a live gross-to-net calculator across the three
realistic statuses — plus an interactive "Keeping the 1%" section that scores
the risk of losing Small Business Status. English only. Same design system as
the Belarus, Romania, Spain and Serbia pages in this series.

## Files
- `index.html` — the entire page (HTML + CSS + JS, no build step, no dependencies)
- `app.py` — thin Streamlit wrapper that renders `index.html` full-bleed
- `requirements.txt` — Streamlit dependency for cloud deploy
- `README.md` — this file

## Run it

**Just open it.** `index.html` is standalone — double-click it, or open in any
browser. Nothing to install.

**As a Streamlit app (local):**
```bash
pip install streamlit
streamlit run app.py
```
`app.py` and `index.html` must sit in the same folder.

**On Streamlit Community Cloud:** push all four files to a GitHub repo (root),
then deploy `app.py` at share.streamlit.io. `requirements.txt` must be in the
repo or the build fails with `ModuleNotFoundError`.

## What the calculator models

Currency: shown in **euros** for comparability with the other country pages
and because foreign hiring is priced in EUR — but **Georgian tax is assessed
in lari (GEL)**. Amounts convert at an indicative `GEL_PER_EUR = 2.99`; the
rate moves.

Three statuses (tabs):

1. **Small Business Status (Individual Entrepreneur, "IE")** — **1% of gross
   turnover** up to 500,000 GEL a year, **3% on the excess**, no expense
   deduction. Only covers **Georgian-source** turnover — work performed while
   physically in Georgia — and only for activities not on the excluded list
   (consulting, legal, financial, medical, architectural, audit, licensed
   work, gambling, personnel provision). Cross the 500,000 GEL ceiling for two
   years running and the status is revoked outright the following January.
   Employees are allowed under this status (not under Micro Business). This
   is the default, cheapest route for a solo cross-border contractor — the
   page also surfaces **Micro Business Status** (0% up to 30,000 GEL, no
   employees) as an inline note when the entered amount sits under that
   threshold, since it isn't one of the three calculator tabs.
2. **Standard IE (no special status)** — flat **20% on profit**
   (`invoiced − expenses`). This is the fallback whenever Small Business
   Status doesn't apply: excluded activity, revoked status, or simply never
   applied for.
3. **LLC — Estonian model** — **0% while profit is retained**, **15%
   corporate tax** the moment it's distributed, then a further **5%
   withholding tax** on the dividend paid to an individual shareholder
   (`profit = invoiced − expenses`; assumes full distribution and excludes a
   director's salary). Treaty relief can reduce the 5% leg, sometimes to 0%
   — not modelled.

Both directions work: enter an invoice to see the net, or a target net to
solve for the invoice (60-step binary search) — reframed in the payer's
voice throughout ("the yearly amount you'll pay them" / "the rate you'd need
to agree on"), per the hero's dual-audience framing.

The **"Keeping the 1%"** section (id `risk`) is the main buyer-facing risk
block: an orange section with an interactive checklist scoring six things
that jeopardize Small Business Status — being at or over the 500,000 GEL
ceiling, an excluded/licensed activity, missed monthly rs.ge filings, work
performed abroad (which shifts income out of the Georgian-source base
entirely), a single-client/salary-like arrangement that reads as disguised
employment, and non-business income (rent, dividends, interest, royalties)
that was never covered by the 1% in the first place. Georgian tax authorities
have in practice challenged "service agreements" that were really
employment — the checklist is built around that substance-over-form risk,
matched to the fact that the fallback isn't a proration but the full 20%.

The hero uses the same dual-audience framing carried over from the latest
Belarus page: the contractor pays their own tax, but the rate you agree sets
their net, so the page shows "both of you" the math — and it flags Georgia's
new **1 March 2026 labour-migration reform** (Special Labour Activity Permit
+ matching residence permit/D1 visa for foreign nationals doing paid work in
Georgia, including as an IE) as the second thing that quietly bites, alongside
the source-of-income rule.

## Updating the numbers each year

All tax parameters live in one `TAX` object plus the `GEL_PER_EUR` constant
near the top of the `<script>` in `index.html`. To refresh:

- `GEL_PER_EUR` — indicative exchange rate
- `sbs.rate1` / `rate2` / `thresholdGEL` — Small Business Status (1% / 3% /
  500,000 GEL)
- `micro.thresholdGEL` — Micro Business Status ceiling (30,000 GEL, informational)
- `std.rate` — standard IE / no-status flat rate (0.20)
- `llc.corpRate` / `dividendRate` — Estonian-model CIT + dividend withholding
  (0.15 / 0.05)

You should not need to touch the engine or layout for a yearly figures
refresh.

## Re-verification pass (corrections made)

A follow-up fact-check pass re-verified every rate, threshold, currency
figure, deadline and legal citation against fresh 2026 sources (prioritizing
PwC Worldwide Tax Summaries, the Tax Code/Matsne, and named advisory/law
firms over aggregator sites). Two corrections came out of it and are now
reflected in `index.html`:

1. **Small Business Status effective date.** Previously stated (correctly, at
   the time) that SBS only takes effect from the first day of the month
   *following* application. A Ministry of Finance order (Order №38, published
   6 February 2026, amending Order №999, in force ~30 days later) changed
   this: SBS now takes effect **the same day you apply**. Confirmed via
   Eurofast's dated legal update citing the order directly, and cross-checked
   against ExpatHub.GE's independent write-up of the same change. Fixed in
   the "Day 1" timeline card.
2. **The 2026 labour-permit rule was narrowed six weeks after it started.**
   The original build correctly flagged the 1 March 2026 Special Labour
   Activity Permit requirement, but missed that **Law №1509 (15 April 2026)**
   added an exemption for foreigners doing work for a non-resident client
   tied to that client's business conducted outside Georgia — i.e., almost
   exactly the standard Kleos cross-border contractor scenario. This is
   corroborated by four independent sources (nomosgeorgia.com citing the
   specific sub-clause added to Article 1(4); tkcounsel.com; gegidze.com; and
   a fifth, more recent source describing an implementing decree that further
   operationalizes the exemption). All sources still hedge the exemption as
   fact-specific ("requires careful structuring and documentation"), so the
   page now presents it as a real but conditional carve-out to check, not a
   blanket exemption — updated in the hero, the calculator's Small-Business
   note, the timeline, case 6, and the FAQ.

Everything else in the original fact-check list below was re-checked and
held up without change, including a fresh currency check: multiple
independent live-rate sources (Currency.Wiki, Xe/Forbes Advisor, Pluang, all
dated within the last week) clustered tightly around **2.98–2.99 GEL per
€1**. One aggregator (Investing.com) showed an inconsistent, internally
contradictory figure (~3.15) not corroborated by any other source and was
discounted as likely stale.

## What was fact-checked before writing this (2026)

Verified via web search against multiple current sources (Georgian Revenue
Service–adjacent legal/advisory publishers, PwC, Legal500, and Georgia's
official Matsne legislative portal) as of July 2026:

- **Small Business Status**: 1% of turnover up to 500,000 GEL/year, 3% on the
  excess (marginal, not retroactive), automatic revocation after two
  consecutive years over the ceiling. Available only to Individual
  Entrepreneurs, not companies.
- **Excluded activities** (Resolution №415): licensed/regulated activities,
  medical, architectural, legal/notarial, audit, consulting of any kind
  (including tax consulting), gambling, personnel provision, forex/financial
  intermediation, real estate brokerage. These default straight to 20%.
- **Source-of-income rule**: the 1% (and the 20% fallback) only reaches
  Georgian-source income, which for services generally means work physically
  performed in Georgia — not the client's location, currency or bank. Work
  genuinely performed while the contractor is outside Georgia is foreign-
  source and falls outside the regime; several advisory sources flag this as
  the single most common misunderstanding among remote contractors.
- **Flat 20% personal income tax** — confirmed as the standard-rate fallback
  for salaries, self-employment profit and most other personal income.
- **LLC "Estonian model"**: 0% CIT on retained/reinvested profit since 2017;
  15% CIT triggered on distribution (and certain deemed distributions); a
  further 5% withholding tax on dividends paid to individuals, reducible or
  eliminated under some double-tax treaties (confirmed via PwC Tax Summaries
  and multiple Georgian advisory firms).
- **Micro Business Status**: 0% up to 30,000 GEL/year turnover, no employees
  permitted (Resolution №415), same excluded-activity list as Small Business
  Status.
- **VAT**: 18% standard rate, no reduced rate; mandatory registration at
  100,000 GEL of domestic taxable turnover in any rolling 12 months; exports
  of goods and services (including services billed to non-resident clients,
  under place-of-supply rules) are zero-rated and excluded from that
  threshold.
- **Tax residency**: standard route is 183 days of physical presence in any
  continuous 12-month period; the High-Net-Worth-Individual (HNWI) route
  (Art. 34) allows residency without the day count for those with worldwide
  assets over ~3,000,000 GEL or income over ~200,000 GEL/year for three
  years, plus a Georgian-connection condition. Confirmed across several
  advisory sources; treated in the FAQ as informational rather than
  load-bearing, since Small Business Status itself is a business
  registration, not a personal-residency status.
- **GEL/EUR rate**: ≈2.99 GEL per €1 (≈0.334 €/GEL) as of late July 2026
  across several live-rate sources — used as the page's indicative constant.
- **2026 labour-migration reform**: confirmed via Georgia's government
  Resolution №70 (20 Feb 2026) and the U.S. Embassy in Georgia's public
  notice — a Special Labour Activity Permit became mandatory from 1 March
  2026 for foreign nationals doing paid work, including self-employed IEs,
  with a transition period for those already active. This is genuinely new
  for 2026 and worth flagging prominently to buyers, since it can block a
  contractor from working legally regardless of the tax setup.

**Flagged as genuinely uncertain / fact-specific, not guessed:** whether the
500,000 GEL Small Business Status ceiling is computed only on Georgian-source
turnover or on the IE's total recorded turnover more broadly; the exact
interaction between deemed-distribution rules and ordinary owner-salary
payments in an LLC; and — the biggest moving target on the page — the precise
scope of the 15 April 2026 labour-permit exemption for non-resident-client
work. Every source describing that exemption hedges it as fact-specific and
documentation-heavy, and at least one implementing decree since (refining
turnover tests and required supporting documents) shows the mechanics are
still being operationalized. The copy presents it as a real, well-corroborated
carve-out worth checking, not a guarantee. These are called out as
professional-advice territory rather than stated as settled fact.

(Resolved on re-verification, no longer uncertain: repeated missed monthly
filings do not equate to a "zero declaration" — a February 2026 amendment
made the monthly filing obligation explicit and mandatory even at zero
income, removing what used to be genuine ambiguity here.)

## Honest caveats

- **Small Business Status is conditional, not automatic** — it depends on
  activity, turnover, genuine self-employment and monthly compliance, and it
  can be revoked. The 20% fallback is not a proration.
- **The source-of-income line is fact-specific.** "Georgian-source" turns on
  where the work was physically performed, which is a documentation question
  (travel records, contracts specifying place of work), not a simple
  client-location test.
- **The LLC route excludes a director's salary**, deemed-distribution
  triggers, and treaty-reduced withholding — a real company's take-home can
  differ, sometimes a lot.
- **The 2026 work-permit reform is new and still bedding in** — transition
  deadlines, quotas and exemptions (e.g. for IT specialists) vary by
  category; confirm current status before assuming a contractor is exempt.
- **EUR is indicative.** Georgian tax is assessed in lari; the rate moves.
- This is general information, **not tax, legal or immigration advice.**
  Confirm Small Business Status, VAT registration and the work-permit
  position at rs.ge or with a qualified Georgian adviser before relying on
  any number here.

Figures reflect 2026 Georgian rules as understood as of late July 2026.
