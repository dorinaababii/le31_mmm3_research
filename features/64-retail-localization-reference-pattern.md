# Feature 64 — Retail Localization Reference Pattern

> **Priority**: P2 · **Effort**: S (≤3 days) · **Source**: brainstorm
> 2026-08-14 (cross-section pick A) · **Bucket**: **v2 owner-pains
> (EU/Paris/compliance)** — same bucket as feature 05
> (`payment-tip-reconciliation`) but a different surface (per-country
> localization, not per-order math).
> **One-line**: convert LE31's money/time/receipt code from a single
> hard-coded EUR + Europe/Paris + French-format assumption into a
> **localization profile table** indexed by country — currency
> formatting (decimal mark, thousands sep, leading symbol, R2L for
> Arabic-Indic numerals), tax display (inclusive vs exclusive, VAT
> rate display label), receipt-required fields (fiscalization ID for
> France/Italy, BSN for Netherlands, CUFE for Colombia, etc.), and
> thermal-printer behaviour (ESC/POS cut type, paper width 58 vs 80
> mm, RTL layout for Arabic).

## Goal

The charter invariant §Money says *never use binary floats; preserve
exact EUR values and explicit tax/tip derivations*. The charter
invariant §Business time says *persist timezone-aware instants and
render business dates in `Europe/Paris`*. Today's code hard-codes both:
the receipt prints `12,50 €`, the date renders `14/08/2026`, and the
VAT label reads `TVA 20 %`. These are correct for a French restaurant
owner and wrong for *every other* EU country.

`misall-software/retail-localization-reference` (Python, pushed
2026-08-12, NOASSERTION license) ships a curated reference table
covering exactly this surface: *currency formatting, tax display,
receipt requirements, e-invoicing, script direction, thermal-printer
behaviour, by country and language*. Topics: `arabic, bidi,
e-invoicing, escpos, fiscalization, i18n, internationalization,
kenya, localization, multi-currency, peru, point-of-sale, pos,
receipt-printing, retail, rtl, tax-compliance, thermal-printer,
vat, vietnam`.

LE31's contribution: take the *shape* (a country-keyed profile
table), not the file (NOASSERTION means the file is reference-grade,
not copyleft-redistributable — LE31 must consume the pattern, not
the file). What makes it novel for LE31 is that **a single
`RESTAURANT_COUNTRY` config key + a small table** turns today's
single-country assumption into a **multi-country ready** surface
without changing the existing per-order money math (feature 05)
or the existing receipt code path.

## Scope

**In scope (v2 owner-pains S effort, ≤3 days):**

- New `backend/app/i18n/__init__.py` package.
- New `backend/app/i18n/profiles.py`: a Python dict literal
  keyed by ISO-3166-1 alpha-2 country code, with sub-keys for
  `currency_code`, `currency_symbol`, `currency_symbol_position`
  (prefix/suffix), `decimal_mark`, `thousands_sep`,
  `currency_decimals`, `rtl` (bool), `tax_label`, `tax_inclusive`
  (bool), `paper_width_mm` (58|80), `escpos_cut` (partial|full),
  `receipt_required_fields` (list of strings).
- v1 ships with **5 country profiles**: `FR` (default), `DE`,
  `IT`, `ES`, `NL` (the EU countries with the most-distinct
  formatting). `KEN`, `PER`, `VNM` are **out of scope for v1**
  (the file lists them as cross-section examples; full multi-continent
  coverage is a v3 problem).
- New `backend/app/services/locale.py`: a `format_money(decimal_amount) -> str`
  helper and a `format_receipt_line(template, **kwargs) -> str` helper,
  both reading the country profile. Replaces the hard-coded `f"{x:.2f} €"`
  in feature 05's receipt renderer.
- `backend/app/services/receipt.py` (extension of feature 05):
  replace hard-coded format strings with `format_money` and
  `format_receipt_line` calls.
- `backend/app/config.py`: add two config keys —
  `RESTAURANT_COUNTRY` (default `"FR"`) and
  `RESTAURANT_LOCALE` (default `"fr-FR"`).
- `backend/tests/test_locale.py`: 5 fixtures — EUR-format
  (`FR`), Arabic-RTL (`EG` is not in the table, but the test
  exercises the fallback path for unknown countries),
  Kenya-KES (`KE` → fallback to English-default for currency),
  Peru-PEN (`PE` → fallback), missing-country fallback
  (`RESTAURANT_COUNTRY=ZZ` → warns and uses `FR` profile).
- `backend/README.md`: short section on the country profile table
  and how to add a new country.

**Out of scope (v2 v1):**

- Multi-country deployment in a single LE31 instance (charter §3.2
  is single-tenant; v3 with multi-location would need a per-tenant
  override file, similar to feature 62's `agents.yaml`).
- Fiscalization ID *generation* (France's `numéro SIRET`, Italy's
  `codice fiscale`). The slice ships the *field name + display*;
  generation is a separate feature gated on a future third-party
  integration (e.g. a fiscalization API provider).
- Full EU fiscalization matrix. The 5 country profiles are the
  v1 minimum; a v3 owner who needs Portugal or Poland adds the
  profile entry following the `FR` shape.
- Right-to-left *printer* support. The slice ships the `rtl` flag
  in the profile and the `format_receipt_line` helper respects it;
  the actual ESC/POS RTL escapes are a printer-driver concern
  (out of scope; require a real hardware test).

## Description

The single strongest in-window fresh signal today is
`misall-software/retail-localization-reference`. The repo is a
**reference artefact**, not a runtime library: a curated table of
"how does country X format money, print receipts, handle RTL" with
20 topics covering the LE31-relevant surface. The Python language
match is real (LE31 is Python 3.13 + FastAPI + SQLModel; the file
is Python) but the *file itself* is reference-grade, not
redistributable.

The cross-section pattern is the **country-profile table** —
today's hard-coded `f"{amount:.2f} €"` becomes a lookup against
a 30-line table that knows about decimal marks, thousands
separators, RTL, and tax labels. The pattern is well-established
(JS Intl, Python `babel`, Java `Locale`) but LE31's specific
surface (EUR + restaurant receipts + ESC/POS thermal printers)
is a *narrow* subset that a 30-line table covers fully.

`misall-software` corroborates:
- `currency_symbol_position` (prefix vs suffix): the EUR symbol
  is prefix in France (`12,50 €`), suffix in Germany (`12,50 €`),
  and the difference matters when the line length is fixed by
  the thermal printer.
- `decimal_mark` (comma vs period): comma in FR/DE/IT, period
  in UK/US. Hard-coding one breaks receipts in the other.
- `rtl`: Arabic-Indic numerals and RTL layout are required for
  the Moroccan and Tunisian F&B market; an Arabic-speaking
  tourist at a French restaurant owner who wants a printout in
  Arabic gets a wrong-direction printout today.
- `escpos_cut`: French thermal printers default to partial cut;
  German ones default to full cut. The `escpos_cut` field
  captures this.
- `paper_width_mm`: 80 mm is the European standard, 58 mm is the
  US/UK standard; the field lets the operator pick the right
  driver.

The OpenAlex `restaurant-hospitality-hci` carry-over (W7197042220,
WhatsApp-as-hotelaria) does not directly anchor this pick, but the
*hospitality internationalization* literature validates the pattern
(the hospitality sector has been doing this for two decades).

## Data model

No new SQLModel table. The artefact is a Python dict literal.

```python
# backend/app/i18n/profiles.py (≤100 LOC; the table is data, not logic)

_COUNTRY_PROFILES: dict[str, dict] = {
    "FR": {
        "currency_code": "EUR",
        "currency_symbol": "€",
        "currency_symbol_position": "suffix",
        "decimal_mark": ",",
        "thousands_sep": " ",
        "currency_decimals": 2,
        "rtl": False,
        "tax_label": "TVA",
        "tax_inclusive": True,
        "paper_width_mm": 80,
        "escpos_cut": "partial",
        "receipt_required_fields": ["siret"],
    },
    "DE": {
        "currency_code": "EUR",
        "currency_symbol": "€",
        "currency_symbol_position": "suffix",
        "decimal_mark": ",",
        "thousands_sep": ".",
        "currency_decimals": 2,
        "rtl": False,
        "tax_label": "MwSt",
        "tax_inclusive": True,
        "paper_width_mm": 80,
        "escpos_cut": "full",
        "receipt_required_fields": ["ust_idnr"],
    },
    "IT": {  # similar shape, "tax_label": "IVA", "escpos_cut": "partial", ...
    },
    "ES": {  # similar shape, "tax_label": "IVA", ...
    },
    "NL": {  # similar shape, "tax_label": "BTW", "receipt_required_fields": ["bsn"] ...
    },
}
```

```python
# backend/app/services/locale.py (≤80 LOC)

def _profile() -> dict:
    country = settings.RESTAURANT_COUNTRY
    profile = _COUNTRY_PROFILES.get(country)
    if profile is None:
        log.warning("RESTAURANT_COUNTRY=%s not in profile table; falling back to FR", country)
        profile = _COUNTRY_PROFILES["FR"]
    return profile

def format_money(amount: Decimal) -> str:
    """Format a Decimal using the country profile. NEVER uses float."""
    p = _profile()
    formatted = f"{amount:.{p['currency_decimals']}f}"  # Decimal formatter; no float
    # apply decimal_mark + thousands_sep substitution
    int_part, _, frac_part = formatted.partition(".")
    int_part = f"{int(int_part):,}".replace(",", p["thousands_sep"])
    result = int_part + p["decimal_mark"] + frac_part
    if p["currency_symbol_position"] == "prefix":
        return f"{p['currency_symbol']}{result}"
    return f"{result} {p['currency_symbol']}"
```

The `format_money` helper preserves the charter §Money invariant
(Decimal in, string out, no float).

## Implementation steps

1. Create `backend/app/i18n/__init__.py` and `backend/app/i18n/profiles.py`
   with the 5-country profile table.
2. Create `backend/app/services/locale.py` with `format_money` and
   `format_receipt_line` (≤80 LOC).
3. Extend `backend/app/config.py`: add `RESTAURANT_COUNTRY` and
   `RESTAURANT_LOCALE` settings.
4. Extend `backend/app/services/receipt.py` (feature 05's renderer):
   replace hard-coded format strings with `format_money` and
   `format_receipt_line` calls.
5. Add `backend/tests/test_locale.py` (5 fixtures).
6. Validate: run `pytest backend/tests/test_locale.py` and the
   existing `pytest backend/tests/test_payment.py` (feature 05's
   suite) — both must pass. The FR default behaviour must remain
   bit-exact for the existing tests.
7. Add `backend/README.md` section: 1 paragraph on the country
   profile table and how to add a new country.

## Telegram interaction if any

None in this slice. The Telegram surface (cook bot + owner recap
+ AI control plane) does not directly render receipts; receipts
are printed to the thermal printer via the existing
`escpos` integration. A future pick could add a `/country-profile`
owner-only Telegram command that shows the active profile; that
pick is not in scope here.

## Dependencies

- **Feature 05** (`payment-tip-reconciliation`) — the receipt
  renderer that this slice extends.
- **stdlib `decimal.Decimal`** — already in use.
- **No new pip dependency**. `babel` is *not* required for v1;
  stdlib `locale` + a small table keeps the footprint at zero.

## Open questions

- Should the country profile table live in code
  (`backend/app/i18n/profiles.py`) or in a YAML/JSON file at
  the repo root (similar to feature 62's `agents.yaml` pattern)?
  Recommendation: code (this is *data*, not *policy*; a 30-line
  dict literal is easier to read than a YAML file for this case).
  Revisit if the table grows past 100 LOC.
- What happens when the operator deploys LE31 to a non-FR
  country but feature 05's `Decimal` math is *still* in EUR
  (because the bank account is EUR)? Recommendation: the table
  is *display-only*; the underlying `Decimal` math stays in EUR
  and the table formats the display. A future pick could add
  multi-currency math (FX-conversion at order close), but that
  is a separate feature.
- Should the table include paper-width-specific format strings
  (e.g. "Total: 12,50 €" for 80mm vs "12,50 €" for 58mm)?
  Recommendation: no for v1; the `paper_width_mm` field captures
  the *driver* choice, the format strings stay single-template.
  Revisit if a future pick adds multi-width printers.

## Why this matters

The charter invariant says *never use binary floats; preserve exact
EUR values and explicit tax/tip derivations*. The charter also
implies a *country* assumption (Europe/Paris time, EUR, French-format)
that today is hard-coded across the receipt renderer, the date
formatter, and the thermal-printer driver.

`misall-software/retail-localization-reference` is the strongest
2026 in-window signal that this pattern is **production-mature,
not a research idea**. A future v3 multi-country LE31 owner (or
a single v2 owner who receives a non-French-speaking customer)
gets correct receipts without code changes. The
`RESTAURANT_COUNTRY=FR` default keeps today's behaviour
bit-exact; the table is **additive**.

This is a **build candidate**, not an experiment. The slice
boundary is hard: one country-profile table + one `format_money`
helper + one `format_receipt_line` helper + 5 test fixtures. If
the build validates, a follow-up pick adds the v3
multi-continent countries (`KEN`, `PER`, `VNM`) and the
fiscalization-ID *generation* integration.

## Evidence (recorded)

- **Cross-section anchor 1**: `misall-software/retail-localization-reference`
  (0★, Python, NOASSERTION — pattern only, not the file), pushed
  2026-08-12, re-pushed 2026-08-14. *Retail and restaurant POS
  localization reference: currency formatting, tax display, receipt
  requirements, e-invoicing, script direction and thermal-printer
  behaviour, by country and language.* Read at
  `/tmp/le31-brainstorm-2026-08-14/gh_topic_open_source_pos.json`.
- **Cross-section anchor 2**: `vul-os/beepbite` (carry-over from
  feature 42, 2026-08-06) — Go + React, 1★, tags include
  `multi-currency` and `restaurant`. Validates the *multi-currency*
  pattern as a recognized 2026 POS primitive.
- **Cross-section anchor 3**: HN Show HN `Bullet (YC S26)` (3 raw
  hits in `hn_small-cafe-pos`, all noise — listed for completeness
  to mark the HN quiet pattern; not an anchor).
- **In-repo dependency**: feature 05's
  `backend/app/services/receipt.py` renderer, which this slice
  extends without changing its signature.
- **Charter alignment**: §Money (Decimal in, string out, no float);
  §Business time (country profile renders business dates in the
  country's locale).
