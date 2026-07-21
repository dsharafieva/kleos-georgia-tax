# Kleos — Georgia contractor-taxation page

A self-contained landing page explaining what a contractor in Georgia actually
keeps, with a live gross-to-net calculator across the three realistic structures
and an interactive check on what can cost you the famous **1% Small Business
Status**. EN / RU toggle. Same design system as the Romania, Spain, Serbia and
Belarus pages in this series.

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

## A note on the second language

The toggle is **EN / ქარ (Georgian)**. Georgian was produced carefully with
correct tax terminology, but — unlike the Russian and Serbian pages in this
series — it has **not** been through a native-speaker review, and Georgian
morphology and idiom leave room for subtle errors. **Have a native Georgian
speaker proofread the `ka` strings in `index.html` before this goes live.** The
full Georgian text was also supplied separately for exactly that vetting. If you'd
rather ship Russian instead (which was native-quality), that version can be
restored on request.

## What the calculator models

Currency: shown in **euros** for comparability with the other country pages —
but **Georgian tax is assessed in lari (GEL)**. Amounts convert at an indicative
`GEL_PER_EUR = 2.95` (so 500,000 GEL ≈ €170k); the rate moves. Say the word and
this can be rebuilt lari-native.

Three structures (tabs):

1. **Small Business Status (1%)** — an individual entrepreneur paying **1% of
   turnover** up to 500,000 GEL, **3% on any excess**, no expense deduction.
   `net = turnover − tax`. Assumes the activity qualifies and the income is
   Georgian-source. The hero regime — dramatically cheaper than the others.
2. **Standard IE (20%)** — Georgia's flat 20% personal income tax on profit
   (`turnover − expenses`). The fallback when Small Business Status doesn't apply
   or is lost.
3. **LLC (Estonian model)** — 0% on retained profit; on full distribution, 15%
   corporate tax then 5% dividend (~19.25% combined). `profit = turnover −
   expenses`. Suits reinvestment/scaling.

Both directions work: enter an invoice to see the net, or a target net to solve
for the invoice (60-step binary search).

The **"Keeping the 1%"** section is the Georgia-specific interactive piece: tick
the flags true of an arrangement (near/over the ceiling, excluded activity,
missed filings, work done abroad, disguised employment, non-business income) and
the verdict escalates from solid → watch → at-risk. It parallels the Serbia
independence-test mechanic.

## Updating the numbers each year

All parameters live in one `TAX` object plus `GEL_PER_EUR` near the top of the
`<script>` in `index.html`:

- `GEL_PER_EUR` — indicative rate (also re-derives the €-shown ceilings)
- `sbs.rate` / `sbs.excessRate` (0.01 / 0.03) and `sbs.ceilingEUR` (from 500,000 GEL)
- `ie.rate` (0.20)
- `llc.citRate` / `dividendRate` (0.15 / 0.05)
- `vatThresholdEUR` (from 100,000 GEL), `microCeilingEUR` (from 30,000 GEL)

You should not need to touch the engine or layout for a yearly figures refresh.

## Honest caveats

- **Small Business Status is conditional and revocable.** The 1% depends on a
  permitted activity, staying under 500,000 GEL, filing monthly on rs.ge, and the
  income being Georgian-source. Lose any of those and income is taxed at 20%. The
  calculator's 1% output assumes the status holds.
- **Source of income is the subtle part.** The 1% applies to Georgian-source
  income — broadly, work performed while physically in Georgia. Genuinely
  foreign-source personal income isn't taxed in Georgia, but claiming the 1% while
  working elsewhere invites a source-and-residency challenge.
- **The "3% on excess" is the common reading;** some interpretations apply 3% more
  broadly once the ceiling is crossed. Either way, two years over revokes the
  status. Contractors are almost always under the ceiling, so this is an edge.
- **The LLC figures are simplified:** full distribution assumed; the exact CIT
  gross-up and any treaty relief on the 5% dividend are excluded, as are a
  director's costs. Retaining profit defers tax (0%).
- **EUR is indicative.** Georgian tax is assessed in lari; the rate moves.
- This is general information, **not tax, legal or accounting advice.** Confirm
  with a qualified Georgian adviser and verify current rules at rs.ge.

Figures reflect the 2026 Georgian rules.
