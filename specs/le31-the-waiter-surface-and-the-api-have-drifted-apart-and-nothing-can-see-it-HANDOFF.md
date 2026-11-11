# HANDOFF — Feature 467: the waiter surface and the API have drifted apart, and nothing can see it

> **Slice contract for the coding agent.** Feature: `features/467-le31-the-waiter-surface-and-the-api-have-drifted-apart-and-nothing-can-see-it-the-mock-up-calls-no-api-and-no-test-compares-the-two.md`.
> Bucket: **v1**. Gate verdict: **`build`**. Evidence class: **OBSERVED** (parsed from the shipped files on 2026-11-10).
> Filed by: Daily Brainstorm 2026-11-10 (100th daily-brainstorm pass), Pick C.

---

## 1. The active feature path

```
features/467-le31-the-waiter-surface-and-the-api-have-drifted-apart-and-nothing-can-see-it-the-mock-up-calls-no-api-and-no-test-compares-the-two.md
```

**Read it in full before writing code.** It carries the executed evidence, the exact boundary against features 388 / 08 / 01 / 24 / 460 / 465 / 466, and the recorded defaults for every open decision.

## 2. The seven-check gate verdict

| # | Check | Verdict | Evidence |
|---|---|---|---|
| 1 | Evidence is observed, not inferred | **PASS** | `grep -c "fetch(" index.html` → **0**. The fixture's six statuses, parsed from the shipped file: `free`, `seated`, **`ordered`**, **`billed`**, **`dirty`**. The API's `_table_status()`, verbatim: `return TableStatus.free.value` / `return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks`. **Three of the six fixture statuses are producible by nothing.** |
| 2 | The defect is in LE31's own code | **PASS** | `index.html` (30,530 bytes, 720 lines) is **the shipped waiter surface** — `backend/app/main.py` mounts it at `/`. `features/08-index-mockup.md`, verbatim: *"When the real backend exists, the same HTML can be served by FastAPI (static files at `/`)."* **It already is.** |
| 3 | No filed feature owns it | **PASS** | Sweep over **959** feature contracts + HANDOFFs: no UI-rendering check, no fixture-comparison check, no response-shape assertion. `PROJECT_CHARTER.md` §7 requires *"End-to-end before commit"* — **the repo contains nothing that could execute that clause.** |
| 4 | It is not a duplicate of an adjacent feature | **PASS** | **388** owns `Table.status` and the seat guard, and **explicitly puts `ordered`/`billed`/`dirty` out of scope** (*"The other three states exist as enum values and are not wired"*). **460** owns `Table.section`. **Feature 08** is the informal spec for the mock-up and says *"Real backend wiring"* is out of scope. **Nobody owns the relationship between the surface and the API.** |
| 5 | The demand is real | **PARTIAL — recorded honestly** | No operator has reported a wrong table colour — **because the surface is a fixture, and a fixture is allowed to be a fiction.** The demand is for the *check*, not for the bug. |
| 6 | It is cheap now and expensive later | **PASS** | One script and one small JSON file. **No schema change, no API change.** Expensive later: the same check becomes the only thing between a schema change and a floor incident, and by then it must handle real network calls, latency and error states. |
| 7 | The upstream-of-filed-work condition is checked | **PASS — it DOES fire, and it is the sharpest finding** | Feature **388** is about to add a `Table.status` column and start returning `ordered`/`billed`/`dirty`. **If the drift check reads a hand-written contract file, it will pass while the two have genuinely diverged again.** **The check must read the API's source.** |

**Overall: `build`.** The weakest link is check 5, weak for the same mechanical reason as the other two picks of this pass: **the surface that would produce the complaint does not exist yet.** That is also the reason it is cheap.

## 3. Files to touch

| File | Change | Notes |
|---|---|---|
| `api-contracts/tables.json` | **NEW — the machine-readable response shape** | The `status` enum lists **only** the states the API can actually return. **The load-bearing part.** |
| `scripts/check-surface-drift.py` | **NEW — the offline drift check** | **Plain script. No network, no database, no browser.** Exit 1 on any mismatch. |
| `index.html` | **Mark the fixture's impossible states + a one-line disclaimer** | Recorded default: **mark, do not delete.** See the feature's Open questions 2. |
| `features/08-index-mockup.md` | **One line** — record that the drift is a checked property | So the informal spec and the contract agree. |
| `features/388-…` | **One line** — name this feature | 388 changes what the API can return; **the check must be updated in the same PR.** |
| The repo's verification tooling (**check what exists**) | **One invocation** | **The repo has no canonical test command** — the implementer must say how this check is run, and the answer must be one a human will actually run. |

**Do NOT touch:** `backend/app/models.py` (388 owns the `status` column), `backend/app/routers/tables.py` (**check 2 only READS it** — never writes it), the bill modal's arithmetic (**feature 465**), the seat modal's bounds (**feature 466**), the floor grid (feature 24), `Table.section` values (feature 460).

## 4. The implementation, in order

1. **Write `api-contracts/tables.json`** — the response shape of `GET /api/tables`: `id`, `label`, `section`, `seats`, `x`, `y`, `status`. **The `status` enum contains only `free` and `seated`**, with a `note` naming the two missing states and the feature that owns them (388).
2. **Write `scripts/check-surface-drift.py`** — the five assertions. **It must exit 1 on today's repo**, because the fixture carries three states the contract does not list, and omits two fields (`x`, `y`) the contract does list.
3. **Mark the fixture's impossible states** (`T3`, `T4`, `T6`) with a `notYetImplemented: true` marker — or remove them, per the recorded decision. **Marking is the default.** **A marked state is *declared*; an unmarked one is *accidental*.**
4. **Add the one-line disclaimer to `index.html`** — that its data is a fixture, not API output, and that `scripts/check-surface-drift.py` is what keeps the two in agreement.
5. **Wire the check into the repo's verification tooling**, and **record that it must run before every commit that touches `index.html` or `backend/app/routers/tables.py`.**
6. **Write the regression test first** — it must fail on today's repo.

## 5. The four things that will go wrong if nobody tells you

1. **Reading a hand-written contract file instead of the API's source.** This is the whole feature's failure mode. A snapshot check passes while the two have genuinely diverged again — **and it fails the moment feature 388 lands correctly**, training people to disable the check. **The check must derive the API's producible statuses from `backend/app/routers/tables.py`'s source** (`TableStatus.<member>` returns) and compare *that* with the contract.
2. **Deleting the three impossible statuses and calling it a fix.** `ordered`, `billed` and `dirty` have **CSS rules** (`.table-card.status-ordered`, `.status-billed`, `.status-dirty`) and the fixture's `T3`/`T4`/`T6` are the **evidence that the five-state design was intended**. Feature 388 put the transitions out of scope — **not the design.** **Mark them, and let 388 decide.**
3. **Turning this into a browser test.** The charter §7's *"End-to-end before commit"* clause needs a rendered browser; **this slice is the cheap half — a shape check, not a rendering check.** **Saying so is part of the contract**, so nobody assumes §7 is now satisfied. **Adding a headless browser and a CI pipeline is a different slice.**
4. **Adding `x`/`y` to the fixture.** The API returns the floor-map coordinates; the fixture omits them. **That is feature 24's and 460's territory.** The correct action here is to declare the omission (*"not yet rendered by the surface"*), **not** to render coordinates the floor grid does not yet use.

## 6. Verification protocol

Five offline commands, plus the executed check:

```bash
cd /opt/data/le31_mmm3_research_work

# 1. The contract file exists and is parseable.
python3 -c "import json;d=json.load(open('api-contracts/tables.json'));print(d)"

# 2. The contract's status enum matches what the API's SOURCE can return —
#    not what the contract says.
python3 scripts/check-surface-drift.py --check-enum-only
#    -> asserts: {m for m in re.findall(r'TableStatus\.(\w+)', router_source)}
#                == set(contract['GET /api/tables']['item']['status']['enum'])

# 3. The fixture's statuses are all producible (or explicitly declared).
python3 scripts/check-surface-drift.py
#    -> asserts: every fixture status is in the contract enum,
#                OR carries the not-yet-implemented marker

# 4. The fixture's fields match the contract's fields.
#    -> asserts: no undeclared fixture field; every contract field is
#                present or declared as not-yet-rendered

# 5. The corpus agrees: the surface-vs-API relationship is now owned.
grep -rl "check-surface-drift\|api-contracts" features/ specs/ | wc -l   # must be >= 1

# 6. The mock-up says what it is.
grep -c "fixture" index.html      # must be >= 1 (the one-line disclaimer)

# 7. Nothing but the named files changed.
git diff --name-only | grep -vE "^(index.html|api-contracts/.*|scripts/.*)$" | wc -l
```

**The negative control** — add a fourth impossible status (`status: 'refunded'`) to the fixture and confirm the check's **exit code flips 0 → 1**. A check that has only ever passed proves nothing.

**Record in the HANDOFF:** how the check is invoked (**the repo has no canonical test command**); whether the enum is derived from the API's source or read from the contract file (**it must be derived**); and which of the three impossible states you marked or removed (**the default is to mark all three**).

## 7. Rollback path

**Fully reversible in one step.** `git revert <the commit>`.

**No data is at risk** — the mock-up writes nothing. **No schema change, no migration, no backfill. No API change** — `backend/app/routers/tables.py` is untouched; check 2 **reads** it, never writes it.

**The rollback is visible and harmless**: the fixture's three impossible states come back and the drift check is gone.

**⚠️ The one thing to note in the revert message:** after reverting, the repo is back to having **no drift check at all** — which is the state this feature was filed to end. **Say so explicitly in the commit message, so the revert is not mistaken for a neutral cleanup.**

## 8. The mandatory LE31 skill list

Read these before writing code — **all of them**, in this order:

1. `le31-conventions` — the schema conventions and the known conflicts.
2. `le31-data` — the data-model rules (strings, enums, money, timestamps).
3. `le31-v1-feature-pattern` — the v1 feature shape.
4. `le31-frontend` — the front-end conventions.
5. `le31-backend` — the FastAPI/SQLModel conventions.
6. `le31-handoff-spec` — the handoff format itself.
7. `le31-coding-agent-brief` — **produces the paste-in prompt from this contract. Do not paste chat excerpts.**

**And read these four feature contracts in full before you start:**

- `features/388-le31-table-state-machine-first-party-table-has-no-status-column-so-a-second-seat-opens-a-second-visit-v1-table-state-validation-and-seat-idempotency-vocabulary.md` — **the feature whose landing will move the enum.** Read its *Out of scope*: the other three states *"exist as enum values and are not wired"*. **Your check must notice when that stops being true.**
- `features/460-le31-a-tables-area-is-free-text-main-main-and-main-are-three-areas.md` — **owns `Table.section`.** Your check looks at the *shape*, not the *values* — **do not duplicate 460's canonicalisation rule.**
- `features/24-visual-table-layout-v2.md` — **the other `index.html` editor**, and the owner of the floor grid that `x`/`y` would feed.
- `features/08-index-mockup.md` — **the informal spec for this file.** Read it, and note the sentence that motivates the whole feature: *"When the real backend exists, the same HTML can be served by FastAPI."*

## 9. The one thing that matters

**LE31's owner makes every decision on a phone, standing up, holding a tray.** The floor view's colour *is* the state of the table. If a table that has been billed renders as free, **the next waiter seats a second party on it** — and the first party's bill is now attached to a table with a second visit on it, which is exactly the state feature **454** filed, arriving by a completely different road.

**But the real cost is not today's bug. It is that LE31 has no instrument.** The charter asks for end-to-end verification before commit, and **the repository contains nothing that could perform it.** Every pass for months has added rules to the corpus and checks to the contracts — **and no pass has added a check that would catch the surface and the API disagreeing about what a table is.**

**A repo with no drift check cannot know it has drifted.** That is the finding.
