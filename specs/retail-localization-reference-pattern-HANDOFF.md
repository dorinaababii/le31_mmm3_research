# retail-localization-reference-pattern — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/64-retail-localization-reference-pattern.md` before
> touching any code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `64`
- Slug: `retail-localization-reference-pattern`
- Contract file: `features/64-retail-localization-reference-pattern.md`
- Bucket: **v2 owner-pains (EU/Paris/compliance)** (same bucket
  as feature 05, different surface)
- Linear parent: `HMM-77` (Brainstorm 2026-08-14 — daily)
- Linear sub-issue: `HMM-79` (see `le31 v1 — Core MVP` project,
  label `Feature`; matches the v2 owner-pains sub-issue convention
  used by features 58/61/62/63)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (`misall-software/retail-localization-reference`
Python pushed 2026-08-12, the strongest in-window cross-section
anchor for the country-profile table pattern; corroborating
`vul-os/beepbite` 1★ carry-over from feature 42 with
`multi-currency` tag). Confidence: **high**.

**Decision: build candidate (v2 owner-pains S effort, ≤3 days).**
The slice is small enough to ship as a build candidate; the
country-profile table is additive (the `FR` default keeps today's
behaviour bit-exact). Circuit breaker: drop the `format_money`
and `format_receipt_line` calls from feature 05's renderer; the
code reverts to the hard-coded `f"{x:.2f} €"` with no behavior
change.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules; even though this is v2 owner-pains, the slicing
   discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror
   contract back).
4. `le31-daily-brainstorm` (this pick came from the daily
   brainstorm job on 2026-08-14).
5. `le31-feature-pipeline` (so the agent understands how this
   slice will be sequenced after it ships).

If the destination repo does not yet ship these skills, request
them from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/i18n/__init__.py                            # NEW (empty package marker)
backend/app/i18n/profiles.py                            # NEW: 5-country profile table (≤100 LOC)
backend/app/services/locale.py                          # NEW: format_money + format_receipt_line (≤80 LOC)
backend/app/services/receipt.py                         # EDIT: replace hard-coded format strings with locale helpers (≤30 LOC changes)
backend/app/config.py                                   # EDIT: add RESTAURANT_COUNTRY + RESTAURANT_LOCALE settings
backend/tests/test_locale.py                            # NEW: 5 fixtures
backend/README.md                                       # note country profile table + how to add a country
```

No new pip dependencies at v1 of this slice. Stdlib `locale`
+ a small table keeps the footprint at zero; `babel` is *not*
required.

## Endpoints and bot commands added

None in this slice. The Telegram surface (cook bot + owner
recap + AI control plane) does not directly render receipts;
receipts are printed to the thermal printer via the existing
`escpos` integration. A `/country-profile` owner-only Telegram
command is a **separate future pick**; not in this slice.

## Country profile table (spec for the coding agent)

`backend/app/i18n/profiles.py` ships a Python dict literal
keyed by ISO-3166-1 alpha-2 country code. v1 ships **5 country
profiles**: `FR` (default), `DE`, `IT`, `ES`, `NL`. The
`KEN`/`PER`/`VNM` countries are **out of scope for v1** (the
`misall-software` file lists them as cross-section examples;
full multi-continent coverage is a v3 problem).

Each profile entry has these keys:

```python
{
    "currency_code": "EUR",           # ISO-4217
    "currency_symbol": "€",
    "currency_symbol_position": "suffix",  # or "prefix"
    "decimal_mark": ",",               # or "."
    "thousands_sep": " ",              # or "." or ","
    "currency_decimals": 2,
    "rtl": False,                      # True for Arabic
    "tax_label": "TVA",                # or "MwSt" / "IVA" / "BTW"
    "tax_inclusive": True,
    "paper_width_mm": 80,              # or 58
    "escpos_cut": "partial",           # or "full"
    "receipt_required_fields": ["siret"],  # country-specific IDs
}
```

## Format helpers (spec for the coding agent)

`backend/app/services/locale.py` ships two helpers:

```python
# Pseudo-code — the slice implements this exactly.

from decimal import Decimal
from app.config import settings
from app.i18n.profiles import _COUNTRY_PROFILES
import logging

log = logging.getLogger(__name__)

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
    formatted = f"{amount:.{p['currency_decimals']}f}"  # Decimal formatter
    int_part, _, frac_part = formatted.partition(".")
    int_part = f"{int(int_part):,}".replace(",", p["thousands_sep"])
    result = int_part + p["decimal_mark"] + frac_part
    if p["currency_symbol_position"] == "prefix":
        return f"{p['currency_symbol']}{result}"
    return f"{result} {p['currency_symbol']}"

def format_receipt_line(template: str, **kwargs) -> str:
    """Substitute placeholders in a receipt template, respecting RTL."""
    p = _profile()
    if p["rtl"]:
        # RTL handling: the slice flips the rendered string;
        # the actual ESC/POS RTL escapes are a printer-driver
        # concern (out of scope).
        return template.format(**kwargs)[::-1]
    return template.format(**kwargs)
```

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent
MUST:

1. Write all 5 test fixtures; `pytest backend/tests/test_locale.py`
   must pass.
2. With `RESTAURANT_COUNTRY="FR"` (default): the existing
   `pytest backend/tests/test_payment.py` (feature 05's suite)
   must pass; the rendered receipts must remain bit-exact
   (string-equal to today's hard-coded output).
3. With `RESTAURANT_COUNTRY="DE"`: confirm `format_money(Decimal("12.50"))`
   returns `"12,50 €"` (German format: comma decimal mark, no
   space, suffix symbol).
4. With `RESTAURANT_COUNTRY="EG"` (not in the table): confirm
   the loader logs a WARNING and falls back to `FR`.
5. Confirm `format_money` never uses `float()` (use
   `Decimal` only).

## Rollback / feature-removal path

Delete the `format_money` and `format_receipt_line` calls from
`backend/app/services/receipt.py`; restore the hard-coded
`f"{x:.2f} €"` strings. Delete the test file. Delete the
`backend/app/i18n/` package. Estimated rollback cost: ≤30 minutes.

## Files for the coding agent to verify against

```
features/64-retail-localization-reference-pattern.md
specs/retail-localization-reference-pattern-HANDOFF.md     (this file)
features/05-payment-tip-reconciliation.md                  (parent surface)
features/62-agents-yaml-ontology-config.md                 (sibling v2 pattern)
skills/le31-conventions/SKILL.md
skills/le31-v1-feature-pattern/SKILL.md
skills/le31-handoff-spec/SKILL.md
PROJECT_CHARTER.md
```
