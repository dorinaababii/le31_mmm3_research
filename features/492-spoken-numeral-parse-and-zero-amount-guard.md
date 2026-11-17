# Feature 492 — A spoken amount is parsed from numerals AND words, and a zero is never a guess

> **Pick A of Daily Brainstorm 2026-11-17 (106th daily-brainstorm pass).**
> Bucket: **v2-AI** (new bucket — justified below). Verdict: **`experiment`**.
> Evidence class: **OBSERVED** — the mechanism is read verbatim from the in-window
> source's own README; the LE31-side gap is **proved by EXECUTION** against LE31's
> real schema and by a corpus-wide grep, not by reading.
>
> **Source artifact:** `beingmushfiq/Baki-Bondhu` — *"Baki Bondhu (বাকী বন্ধু) — Voice-First
> Smart Credit & Debit Ledger for Bangladeshi Retailers"*.
> MIT licence (permissive — §3.2-compatible on paper), ★0, ⑂0, created **2026-10-24**,
> pushed **2026-11-16** — **in-window by BOTH `created_at` and `pushed_at`**.
> Kotlin / Jetpack Compose / Room (SQLite) / Firebase.
> URL: https://github.com/beingmushfiq/Baki-Bondhu
> Raw README: `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.README.md`
> Raw repo JSON: `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.repo.json`

## Goal

Make one sentence true that LE31 cannot currently say:

> **When a staff member speaks a monetary amount, LE31 either hears an amount or it
> refuses to write one. It never writes a zero it did not hear.**

Two mechanisms, both net-new to LE31:

1. **Spoken-numeral parsing.** A spoken amount is not a string to be echoed — it is a
   *number to be recovered*. The source parses **digits** (`450`, `৪৫০`) **and verbal
   forms** (*one thousand*, *five hundred*, *one and a half thousand*) into a single
   integer amount in minor units.
2. **A zero-amount hallucination guard.** When the utterance contains **no monetary
   value at all**, the source *"never guesses or defaults to zero"* — it alerts the
   merchant and asks for clarification **before** committing to the ledger.

## Scope

**In scope (v2-AI):**

- A **pure, offline, deterministic parser** — `parse_spoken_amount(text: str) -> ParsedAmount | None`
  — that recognises a monetary amount in a free-form utterance, in both digit and
  verbal form, and returns `None` (not `0`) when no amount is present.
- A **word-to-number vocabulary** for the supported language(s): units
  (`ten`, `hundred`, `thousand`, `million`), scales (`half`, `and a half`), and the
  connectors LE31's own surfaces already use (`€`, `euros`, `euro`).
- A **minor-unit integer** as the parser's output type — never a float, never a
  `Decimal` reconstructed from a float literal.
- The **refusal path**: a parser result of `None` must produce a *clarification request*
  to the operator, and **must not** reach the write path. The write path must be
  **unreachable** with an absent amount.
- A **recognition of LE31's own currencies**: LE31 books in **EUR** (charter §3.1);
  the parser's minor unit is **cents**. The source's `paisa` vocabulary is
  Bangladesh-specific and is **not** adopted; only the *shape* of the mechanism is.
- A **non-AI fallback** (charter §3.3): the typed path stays available and is the
  default; the spoken path is opt-in and off by default.

**Out of scope (v2-AI):**

- **Any change to feature 38's cook voice-note flow.** Feature 38 owns the *input
  modality* for the cook's stock `86`; this feature owns only the *amount
  vocabulary* and the *refusal rule*. Feature 38's file is not modified.
- **A speech-to-text engine.** This feature starts at the **text** boundary. A
  transcript arrives from somewhere (feature 38's `transcribe_ogg`, a browser
  `SpeechRecognition`, a human typing the sentence). The transcript-to-amount step
  is the unit under test.
- **Cloud speech-to-text, any new pip dependency, and any new model download.**
- **Voice for the waiter surface.** Feature 38 is the cook's surface; a waiter
  hands-free flow is a separate question (see Open questions).
- **Multi-currency and FX.** One currency, EUR, cents.
- **Any change to `Bill`, `DerivedTip`, `OrderItem` or `StockEntry` schemas.** This
  feature adds **no table and no column**; it is a pure function plus a rule.
- **Anything that writes an amount without the caller having supplied one.**

## Description

### What LE31 has today

**Feature 38 owns voice for the cook's stock reason.** Its own file, read verbatim:

- it writes a `StockEntry` with `qty_delta = -<batch>`, `reason = "86"`,
  `rationale = <transcript>` — **a quantity and a reason, never an amount**;
- the phrase *"the transcript is the new `rationale` value"* — the transcript is
  **text to store**, not a **number to compute**;
- the parse step it does specify is *"the same regex used by the typed `/86`
  command (`/86 <item> <reason>`)"* — a **token splitter**, not a numeral reader.

The parent verified the absence by grepping feature 38's own file:

| pattern in `features/38-cook-voice-note-to-stockentry.md` | hits |
|---|---:|
| `numeral` | **0** |
| `spoken number` | **0** |
| `parse.{0,15}amount` | **0** |
| `zero.{0,10}guard` | **0** |
| `hallucinat` | **0** |
| `cents` | **0** |
| `€` | **0** |
| a money amount written by voice | **False** |

And the corpus-wide sweep over all 525 `features/` contracts and 487 `specs/`
HANDOFFs (`grep -rliE`):

| corpus concept | files |
|---|---:|
| `spoken (numeral\|number)\|verbal (number\|amount)\|numeral pars` | **0** |
| `voice.{0,50}(amount\|price\|total due\|payment)` | **0** |
| `spoken.{0,50}(amount\|price\|total due\|payment)` | **0** |

**Zero files own this mechanism.**

### The executed LE31 probe

Run against LE31's own `backend/app/models.py` (`SQLModel.metadata.create_all` on a
throwaway SQLite DB, then real inserts). Script:
`/opt/data/le31-brainstorm-2026-11-17-scripts/audit_lifecycle.py`.

```
SCHEMA CREATED from LE31's own models.py
TABLES: ['app_user','batch','bill','derived_tip','menu_item','order_item','shift','stock_entry','table_','visit']

--- PICK A: input paths (ANY non-form input surface?) ---
  BaseModel (JSON body schema) occurrences: 0
  routes:
      @app.on_event("startup")
      @app.get("/api/health")
      @app.get("/")
      @router.get("")
      @router.post("/{table_id}/seat")
  shipped index.html: <form>=0  fetch(= 0  <input>=4
  voice/audio tokens in index.html: NONE
```

The backend declares **zero** request-body schemas and exactly **one** non-GET route.
**There is no surface in LE31 today that can accept a spoken amount** — and that is
correct, because there is no surface that can accept a *typed* amount either. The
gap this feature closes is therefore **first** in the parser, not first in the wire.

### Why the zero-amount guard is the sharper half

A numeral parser that returns `0` on failure is worse than no parser: it produces a
**plausible wrong number**, and a plausible wrong number in a money ledger is a
defect that surfaces at closing time, in front of a guest.

The source states the rule explicitly (README, verbatim):

> *"**Zero-Amount Hallucination Guard**: Never guesses or defaults to zero when no
> monetary value is spoken. The app alerts the merchant and prompts for clarification
> before committing to the ledger."*

This is the same class of defect LE31 has already filed twice, in a different place:

- **feature 484** — *"a missing number and a zero amount are different facts, and a
  waiter must not read one as the other"* (the **display** path);
- **feature 457** — *"the row that is documented as computed is a free-standing number"*
  (a **stored** derived value with no constraint).

Feature 484's rule is about *rendering*; this feature's rule is about *ingestion*.
**484 does not own it** — `grep -c` on 484's file finds no parser, no ingestion path,
and no spoken input.

### The two-step shape

The source's guarantee is not "transcribe then commit". It is:

```
utterance ──▶ parse spoken numeral ──▶ amount present? ──┬── yes ──▶ commit
                                                         └── no  ──▶ ASK, do not commit
```

LE31's own surfaces have the second half **inverted** in the one place a number can
go missing. `backend/app/routers/tables.py` and `index.html`'s bill handler both
treat "no amount" as "zero" in the shipped path — which is why feature 484 exists.
This feature applies the same rule at the **input** boundary, one step earlier.

## Data model

**No schema change.** The parser is a pure function over text.

```python
# backend/app/services/spoken_amount.py  (NEW)
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)
class ParsedAmount:
    """A recovered amount. `minor_units` is an INTEGER count of cents.
    `None` is never represented as 0 — absence is absence."""
    minor_units: int          # e.g. 4250 for €42.50
    currency: str             # "EUR"
    source_span: str          # the substring the number was recovered from

def parse_spoken_amount(text: str) -> ParsedAmount | None:
    """Return the monetary amount spoken in `text`, or None.

    None means: no monetary value was heard. Callers MUST treat None as a
    clarification request and MUST NOT write a zero.
    """
    ...
```

**The return type is the contract.** `ParsedAmount | None` — a caller that writes
`minor_units` without narrowing cannot compile. A parser returning `int` would make
`0` indistinguishable from "heard zero".

**Minor units, not `Decimal`.** The source stores amounts as **integer 64-bit paisa**
and states the reason: *"completely eliminating IEEE 754 floating-point drift."*
LE31's charter §7 says *"No `float(qty * price)` anywhere"*; the integer-minor-unit
form is the same rule applied to a spoken number. (The parent probed LE31's own
storage: `order_item.unit_price` is `Decimal(10,2)`, and SQLite stored `25.00` as
**integer `25`** — `typeof(unit_price) == 'integer'`. So LE31's storage is already
minor-unit-safe; the *parser* must not be the step that reintroduces a float.)

**A `VoiceTranscript`-style audit row is NOT added here.** Feature 38 already
specifies `VoiceTranscript` for the cook path. This feature produces **no new
durable row** — it produces a number or `None`.

## Implementation steps

1. **The vocabulary.** A word→value map for the supported language(s): units
   (`ten`…`ninety`, `hundred`, `thousand`, `million`), scales (`half`), and the
   connector words (`and`, `a`). Currency words: `euro`, `euros`, `€`.
   **The language is LE31's, not the source's** — the source's Bengali vocabulary is
   recorded here as evidence, not adopted.
2. **The parser.** Scan the utterance for the first span that resolves to an amount.
   Digit spans (`450`, `1,200`, `€42.50`) are read directly; verbal spans are
   accumulated with the unit/scale rules. Return `ParsedAmount` or `None`.
   **Never return `ParsedAmount(0, ...)` because nothing was found.**
3. **The zero-amount guard.** `parse_spoken_amount` returns `None` for an utterance
   with no monetary value — including an utterance whose only number is a **bare
   count** (*"two coffees"*) and an utterance that is **pure noise**. A unit test
   asserts `None`, not `0`, for each.
4. **The refusal path.** The caller (see Open questions) receives `None` and **must**
   ask for clarification. The write path is reached only with a `ParsedAmount`.
   The call site is written so that `None` cannot be unwrapped into `0` — e.g. by
   requiring the `ParsedAmount` object itself, not its `minor_units`.
5. **The minor-unit conversion.** `ParsedAmount.minor_units` is `int`. Converting to
   EUR for display is `Decimal(minor_units) / 100` — **never** `minor_units / 100`
   in Python (that is a float).
6. **A pure-function test suite**, no network, no model:
   - digit forms → expected cents;
   - verbal forms → expected cents;
   - mixed form → expected cents;
   - **no amount → `None`** (four cases, including the near-misses above);
   - "€0" spoken deliberately → `ParsedAmount(0, ...)` — **a spoken zero is a
     spoken zero**, and is distinguishable from absence by the type, not by the value.
7. **A config flag** `SPOKEN_AMOUNT_ENABLED: bool = False` (default off), and the
   typed path remains the default and always-available fallback (charter §3.3).

## Telegram interaction if any

**None in this feature.** This feature is a parser; it defines no Telegram command,
no keyboard, and no handler. Feature 38 owns the cook bot's voice-note flow and its
confirmation keyboard. A future feature may wire this parser to the **waiter's**
bill flow; that is explicitly out of scope here.

## Dependencies

- **Feature 38** (`features/38-cook-voice-note-to-stockentry.md`) — **upstream, for
  the transcript→text boundary only.** This feature does **not** modify feature 38's
  file and does **not** depend on its `VoiceTranscript` table. Feature 38's
  `transcribe_ogg` is the *one* existing path that could eventually feed this
  parser; the parser is independently testable without it.
- **No new pip dependency.** The parser is pure Python + `decimal` + `re`.
- **No new model download**, no cloud API, no API key.
- **Charter §3.3** (AI may assist staff with observable evidence and a non-AI
  fallback) is satisfied by construction: the typed path is the default and the
  spoken path is opt-in.

## Open questions

- **Which surface consumes the parser first?** Three candidates, and this pass does
  **not** choose:
  1. the **waiter's bill modal** — the waiter speaks the amount the guest paid;
     the nearest to LE31's money domain, but it touches the shipped `index.html`,
     which is already owned by features 465/466/467/484;
  2. the **waiter's order line** — the waiter speaks "two coffees" (a **quantity**,
     not an amount — note that this is a *different* parse and must not be conflated);
  3. a **manager**-facing reconciliation surface.
- **Is the vocabulary language-scoped?** LE31 books in EUR and is deployed in one
  locale; the parser should probably support **one** language and **reject** an
  utterance in another rather than half-parsing it. Open.
- **Does a spoken amount need to be a *confirmation* rather than a *write*?** The
  source confirms before committing (read-back / clarification). LE31's charter §3.2
  requires *"explicit operational transitions only"*, which argues for a
  **read-back-then-confirm** rather than a parse-then-write. Open, and it is the
  reason this feature's verdict is `experiment` and not `build`.
- **How does this interact with feature 420** (`total_paid` means *tendered*, not
  *received*)? A spoken amount is most likely a *tendered* amount. If the parser
  feeds a `Bill.total_paid`, it must feed the **tendered** semantics, not the
  received ones. **Not resolved here.**

## Why this matters

**The zero-hit sweep is the finding.** Across 525 feature contracts and 487 HANDOFFs,
the corpus contains **zero** files that own a spoken-numeral vocabulary and **zero**
that own a spoken money amount. LE31 has a voice surface (feature 38) and a money
domain — and **no bridge between them**, and no rule about what happens when the
bridge fails to hear a number.

That failure mode is the interesting one. A team that adds a spoken amount without
the guard gets a ledger that silently records `0.00` for a transaction the operator
believes was captured. LE31 has already filed the *display* half of this bug class
(484) and the *stored-derived-value* half (457). This feature files the
**ingestion** half, and — because the parser's return type is
`ParsedAmount | None` — makes the safe behaviour the only one the type system
permits.

**The value is the guard, not the parser.** The numeral vocabulary is
reimplementable in a day. The rule *"an amount that was not heard is not a zero"* is
the thing that has to survive into the codebase, because the next person to touch
the write path will not be thinking about hallucination.

**Reference only, no code adopted.** The source is MIT-licensed and its mechanism is
portable, but it is **Kotlin / Jetpack Compose / Room / Firebase** — entirely
off-stack for LE31 (FastAPI + SQLModel + Postgres + aiogram). The *vocabulary-shape*
is adopted; the *code-shape* is not. Its ★0 and its README-only evidence mean the
mechanism is a design reference, not production validation.

## Evidence appendix — source README, verbatim

From `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.README.md`:

> *"**Colloquial Dialect Support**: Recognizes informal everyday phrasing:
> `করিম সাহেব বাকী নিলেন ৫০০ টাকা`, `রহিম জমা দিলেন ২০০`, `সুমন পাঁচশো পরিশোধ`,
> `নগদ বিক্রি ১,২০০ টাকা`."*
>
> *"**Spoken Word & Numeral Parsing**: Parses digits (`৪৫০`, `1250`) and verbal
> expressions (`এক হাজার`, `পাঁচশো`, `দেড় হাজার`, `আড়াই হাজার`)."*
>
> *"**Zero-Amount Hallucination Guard**: Never guesses or defaults to zero when no
> monetary value is spoken. The app alerts the merchant and prompts for clarification
> before committing to the ledger."*
>
> *"**Audio Readback Confirmation**: Optional Bengali voice synthesis confirms
> recorded transactions aloud to reassure busy shopkeepers."*
>
> *"All customer balances and ledger entries are stored as **integer 64-bit numbers
> (`Long`)** in **Paisa**, completely eliminating IEEE 754 floating-point drift."*

The README's own metrics are **self-reported by the repository author and are NOT
independently verified** — no test counts, no benchmark numbers and no user counts
are claimed from this source anywhere in this contract.
