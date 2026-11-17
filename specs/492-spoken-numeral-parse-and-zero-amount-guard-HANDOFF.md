# HANDOFF — Feature 492: A spoken amount is parsed from numerals AND words, and a zero is never a guess

## Active feature path

`features/492-spoken-numeral-parse-and-zero-amount-guard.md`

**Disposition:** `experiment` — **vocabulary + rule reference, with a small, self-contained
implementation (a pure parser) that a coding agent MAY build.** The *wiring* of the
parser into any surface is **NOT authorized by this handoff** — see "Trigger to
promote". Feature 38's file is **not** to be modified.

**What a coding agent may build from this handoff:** a pure, offline,
dependency-free function that recovers a monetary amount from a spoken utterance, and
that returns `None` — never `0` — when no amount was heard, together with its test
suite.

**What a coding agent may NOT build from this handoff:** a Telegram command, a
speech-to-text integration, a browser voice API, a waiter-surface change, a schema
change, a bill/order write path, or any dependency on a cloud service.

## Seven-check gate verdict

| Check | Verdict |
|---|---|
| 1. Raison d'être / JTBD | **INFERRED.** LE31 has a voice surface (feature 38) and a money domain; the corpus sweep proves no contract bridges them. The need for a *spoken amount* specifically is inferred from the gap, not observed from an LE31 user. |
| 2. Viability | **PASS in principle.** A numeral parser is deterministic and offline; the zero-amount guard is a type-level rule (`ParsedAmount \| None`). |
| 3. Practicability / confidence | **MEDIUM.** The parser is straightforward. The *consuming surface* is not chosen, which is why the verdict is `experiment` and not `build`. The source is ★0, off-stack, README-only evidence. |
| 4. Conflict | **No hard conflict.** The parser adds no table, no column and no dependency. It must not modify feature 38's flow; feature 38 owns the cook's input modality, this feature owns the amount vocabulary. |
| 5. Outcome, appetite, scope | **EXPERIMENT.** The safe half (parser + refusal rule) is small and worth building. The unsafe half (which surface consumes it) needs the owner's decision. |
| 6. Cost to operational value | **LOW to build** (one module + tests, no deps); **UNKNOWN to operational value** until a consuming surface is chosen. |
| 7. Circuit breaker / reversibility | **PASS.** A pure function in a new module. Deleting the module deletes the feature; nothing else is touched. |

## Files to touch

**Authorized in this disposition:**

- `backend/app/services/spoken_amount.py` — **NEW**. The `ParsedAmount` dataclass and
  the `parse_spoken_amount(text: str) -> ParsedAmount | None` function, plus the
  word→value vocabulary and the minor-unit conversion.
- `backend/app/config.py` — **NEW field only**: `SPOKEN_AMOUNT_ENABLED: bool = False`
  (default off). Do **not** restructure the config module.
- `backend/tests/test_spoken_amount.py` — **NEW** (or the repo's existing test
  location — check `backend/tests/` before creating a new tree).

**Explicitly NOT to be touched:**

- `features/38-cook-voice-note-to-stockentry.md` — feature 38's contract. Upstream
  reference only; **do not edit**.
- `backend/app/models.py` — **no schema change in this slice.**
- `backend/app/bot/cook_bot.py` — **no Telegram handler in this slice.**
- `index.html` — **no shipped-surface change in this slice.**
- `backend/app/routers/*` — **no new route in this slice.**

**Read-only dependencies to read before coding:** `backend/app/models.py` (for the
`Decimal(10,2)` money convention), `features/38-cook-voice-note-to-stockentry.md`
(for the transcript boundary), and `features/457-*.md` (for the "free-standing
number" constraint this parser must not create).

## Verification protocol reference

**Documentary verification (required, cheap):**

1. Read `features/492-spoken-numeral-parse-and-zero-amount-guard.md` in full.
2. Read the source evidence at
   `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.README.md` and the
   repository metadata at
   `/tmp/le31-brainstorm-2026-11-17/gh/beingmushfiq__Baki-Bondhu.repo.json`.
   Re-derive the in-window claim from the metadata: `created_at` **and** `pushed_at`
   must both fall in 2026-10-18..2026-11-17.
3. Confirm the parent's report at `/opt/data/le31-brainstorm-2026-11-17.md` records
   the pick as `experiment` and labels the source as a **vocabulary reference with no
   code adopted**.

**Executed verification (required for the parser itself):**

4. The parser test suite passes, and — critically — the suite contains at least
   **four** cases asserting `None` (not `0`) for utterances with **no** monetary
   value: a pure-noise utterance, a bare count (*"two coffees"*), an utterance whose
   only number is a non-monetary number, and an empty string.
5. **A spoken zero is distinguishable from absence.** Assert
   `parse_spoken_amount("zero euros")` returns `ParsedAmount(minor_units=0, ...)` —
   the distinction is carried by the **type**, not the value. A test that only
   checks `minor_units` cannot make this distinction and is a **vacuous pass**.
6. **The minor-unit conversion is not a float.** Assert that the conversion to EUR
   uses `Decimal(minor_units) / 100` and never `minor_units / 100` in Python.
7. **Negative control.** The zero-amount guard's assertion must be proven
   load-bearing: temporarily change the parser to return
   `ParsedAmount(0, "EUR", "")` on the no-amount path, confirm the suite **fails**,
   restore, confirm it **passes**, and assert no residue (no `.bak`, no stray file).
   A guard that cannot fail proves nothing.
8. **No `float` in money paths.** `grep -rn "float(" backend/app/services/spoken_amount.py`
   must return **0**, and the file must import `Decimal` if it formats an amount.

**Charter checks:**

9. Charter §3.3 — the typed path remains the default and always-available fallback;
   the spoken path is opt-in via `SPOKEN_AMOUNT_ENABLED` (default `False`).
10. Charter §3.2 — no third-party code is copied. The source is MIT but **off-stack**
    (Kotlin / Compose / Room / Firebase). The *vocabulary-shape* is adopted; the
    *code-shape* is not. The Bengali/Paisa vocabulary is **not** adopted.

## Rollback path

- Delete `backend/app/services/spoken_amount.py`.
- Delete the parser test file.
- Revert the single `SPOKEN_AMOUNT_ENABLED` line in `backend/app/config.py`.
- Delete `features/492-spoken-numeral-parse-and-zero-amount-guard.md`.
- Delete `specs/492-spoken-numeral-parse-and-zero-amount-guard-HANDOFF.md`.
- Remove the feature-492 row from `/opt/data/INDEX.md` and from the in-repo
  `INDEX.md`.
- **No data rollback:** no table, no column, no migration was created.

## Mandatory LE31 skill list

Before any implementation, load and follow:

- `le31-conventions` — money invariants and charter boundaries (§3.2, §3.3, §7);
- `le31-research-workflow` — source-evidence discipline, signed deltas;
- `le31-v1-feature-pattern` — contract conventions;
- `le31-handoff-spec` — frozen-contract and HANDOFF discipline;
- `le31-coding-agent-brief` — paste-in prompt generation from this slice contract;
- `pre-merge-review` — independent review before merge.

## Trigger to promote

Promote the **wiring** (i.e. attaching this parser to a surface) only when **one** of
these becomes true:

1. The owner names the consuming surface — most likely the **waiter's bill modal**
   (speaking the amount the guest paid), or the **manager**'s reconciliation view.
2. Feature 38's `transcribe_ogg` is available and a transcript can reach the parser.
3. The **tendered-vs-received** semantics of feature 420 are resolved, because a
   spoken amount is most likely a **tendered** amount and feeding it into a
   `Bill.total_paid` must honour that semantics.

**Promotion gate:** the wiring must carry a **read-back-then-confirm** step
(charter §3.2 — *"explicit operational transitions only"*), not a
parse-then-write. A parse-then-write wiring of a money amount **must not** be
promoted without that confirmation step, because the parser's `None` is the only
thing standing between a misheard utterance and a silently-recorded `0.00`.

**Do not promote** a waiter-surface change under this feature: the shipped
`index.html` is owned by features 465 / 466 / 467 / 484, and this feature's parser
must land first and be wired separately.
