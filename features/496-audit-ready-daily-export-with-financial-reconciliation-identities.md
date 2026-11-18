# Feature 496 — `v1-audit-ready-daily-export-with-financial-reconciliation-identities`

> **Pick B of Daily Research 2026-11-18.** **Bucket: v1 (owner-reporting vocabulary reference).** **Verdict: `defer` — parking-lot reference.**
>
> **Source artifact:** `FreeOpenSourcePOS/FloCafe` — MIT, ★192 / ⑂91, TypeScript/Electron, created 2026-05-07, pushed 2026-11-18T00:46:39Z. Parent-verified direct repository GET: `/tmp/le31-daily-2026-11-18/gh/repo_07_FreeOpenSourcePOS_FloCafe.json`; README: `/tmp/le31-daily-2026-11-18/gh/readme_07_FreeOpenSourcePOS_FloCafe.md` (37,642 bytes); source URL: https://github.com/FreeOpenSourcePOS/FloCafe.
>
> **Why this pick:** FloCafe names a property LE31's corpus never names — an export that is not merely a dump but **carries financial reconciliation identities**, i.e. the exported numbers are checkable against each other rather than merely present. Parent-run dedup across all 1,016 feature and spec files: `reconciliation identit` → **1 hit** (feature 428, in an unrelated context — an aggregate rule that silently drops open visits), `audit.ready (csv|export)` → **0 hits**, `financial reconciliation` → **0 hits**. The mechanism is net-new.
>
> **The gap it addresses is already visible in LE31's own corpus.** Features 411 (money precision declared, not enforced), 420 (total paid means tendered, not received), 428 (avg dwell silently excludes open visits), and 457 (derived tip is not constrained to its own formula) are all defects where a stored number cannot be checked against the rule that produced it. A reconciliation identity is the general answer to that class.
>
> **Project constraint:** the workspace contains only `le31 v1 — Core MVP` (P-HMM-3), `le31 Workflow` (P-HMM-2), and `le31 Research` (P-HMM-1). The matching Linear sub-issue is attached to `le31 Research`; no v2 project was invented.

## Goal

Record the source artifact's **audit-ready export vocabulary** as the reference design for any future LE31 owner-facing total:

1. the export is **audit-ready** — it is produced to be checked, not merely to be read;
2. the export carries **explicit financial reconciliation identities** — named equations relating a total to its components;
3. the export format is **a flat file** (CSV/Excel) that an accountant can open without the application;
4. the identities are **stated in the artifact**, so a reader knows what was checked;
5. the check is **fail-visible**: an identity that does not hold is visible in the export, not silent.

No export, no reporting surface, and no schema change is built by this feature.

## Scope

**In scope (defer artifact):**

- Verbatim source evidence and the five-point mechanism summary above.
- The explicit link to the four existing LE31 defects this vocabulary would have surfaced (features 411, 420, 428, 457).
- The dedup result establishing the mechanism is net-new to the corpus.
- A named candidate list of reconciliation identities, explicitly recorded as **candidates for a future scoped feature**, not as this feature's decision.

## Out of scope

- No export endpoint, no scheduled job, no CSV or Excel writer.
- No owner-facing reporting surface — LE31 v1's charter names two operational surfaces (waiter web UI, cook Telegram bot), and a report for the owner is a third.
- No change to `Bill`, `Order`, `OrderItem`, `Payment`, or `StockEntry`.
- No new dependency, no charting, no dashboard.
- **No statement about which identities LE31 should adopt.** That is the owner's and a future scoped feature's decision.

## Description

FloCafe's README states the mechanism directly:

- *"**Daily sales & accounting export:** Audit-ready CSV/Excel reporting with financial reconciliation identities."*

The same README records the adjacent cashier-facing artifact:

- *"**Cash drawer management:** Cash pulse on checkout and end-of-shift cash drawer reconciliation."*

The transferable idea is the **difference between a report and a check**. A report states numbers; a reconciliation identity states a relationship between numbers and asserts that the relationship held. A CSV that carries the identity lets the reader recompute it without the application — which is what makes it audit-ready rather than merely exportable.

For LE31 the vocabulary is valuable because the corpus already contains four defects of exactly this shape, each of which a reconciliation identity would have caught at the moment it was introduced:

| Existing feature | The number that cannot be checked | The identity that would check it |
|---|---|---|
| 411 — money precision declared, not enforced | `Decimal(12, 345)` silently coerced on Postgres, silently stored on SQLite | declared precision == stored precision, per environment |
| 420 — total paid means tendered, not received | the P0 tip formula books change as tip | tendered − change == received |
| 428 — avg dwell silently excludes open visits | average drops a null closed-at row with no signal | Σ included durations == Σ all durations, with the exclusion stated |
| 457 — derived tip not constrained to its formula | the row "documented as computed" is a free-standing number | stored tip == formula(tendered, rate) |

Note the shape of the last one: LE31 *already* documents a derived value and a formula for it, and the corpus records that the value is unconstrained against the formula. An identity is the enforcement of that documentation.

## Data model

No schema change. The future reference shape, explicitly **not proposed today**, is:

```text
ReconciliationIdentity (future reference)
  id, version, scope          # e.g. daily | shift | bill
  lhs_expr, rhs_expr          # named, not evaluated in the app
  tolerance, currency, applies_to

ReconciliationRun (future reference)
  identity_id, run_at, passed, observed_lhs, observed_rhs, delta
```

The important design property in this shape is that `lhs_expr`/`rhs_expr` are **named strings, not executable code**. An identity is a published assertion; the export prints it and its observed values, and a reader (or a later tool) evaluates it. That keeps the identity from becoming a second, untested computation path inside the application — which would be a new way for the numbers to disagree.

## Implementation

None in this feature. When an owner-facing export is promoted into a scoped feature:

1. Choose the **candidate identities** from the four named defects above, and have the owner confirm which ones are worth publishing.
2. Decide the **scope**: per bill, per service day, or per shift. LE31's business date is `Europe/Paris` and the service day is not the calendar day, so the scope boundary is a real question, not a formatting one.
3. Decide the **tolerance**: LE31 uses exact EUR and never binary floats (charter §3.6), so most identities should be exact equality. If a tolerance is ever needed, it must be a named value in the export, not a hidden epsilon.
4. Decide the **currency and tax treatment** in the identity text — features 408 (tax rate has no home) and 410 (two conflicting money-rule sources) are unresolved, so an identity that crosses a tax boundary cannot be published until they are.
5. Make a **failed identity visible in the export itself** — a failed check that only appears in a log is not audit-ready.
6. Never let the export become the **source of truth**. It is a derived read model. The ledger stays authoritative.
7. Keep the export **out of the write path**. No identity may mutate `Bill`, `Payment`, or `StockEntry`.

## Telegram interaction

None. The cook Telegram bot has no use for a daily financial export, and nothing in this reference changes the cook's surface or its commands.

## Dependencies

- Existing feature 408 — tax rate has no home in config; the identity text cannot name a tax rate until this is resolved.
- Existing feature 410 — two money-rule sources (charter flat-rate total vs the coding-agent checklist's per-line VAT); an identity crossing that boundary would pick a side silently.
- Existing feature 411 — money precision declared, not enforced; the identity that checks it is one of the named candidates.
- Existing feature 420 — tendered vs received tip semantics.
- Existing feature 428 — avg dwell excluding open visits with no signal.
- Existing feature 457 — derived tip not constrained to its own formula.
- Existing feature 435 — a bill has no edge to order-item, so the stored subtotal is a number nobody can audit. This is the deepest structural blocker: **without bill-line membership, several identities are not computable at all.**
- Charter §3.1 — two operational surfaces; an owner report is a third and is therefore not v1 work without an explicit charter decision.
- Charter §3.6 — `Decimal`, never float; exact EUR; explicit tax/tip derivations.
- `le31 v2 owner-pains` and `le31 v2-AI` **do not exist** in the workspace; the sub-issue is attached to `le31 Research`.

## Open questions

1. Is an owner-facing export a real LE31 need? The charter names an owner but gives the owner no surface.
2. If yes, is the export a file download, a bot command, or both? A bot command would make the Telegram surface an owner surface, which the charter does not currently allow.
3. Which identities does the owner actually want to see checked — and would a failed identity ever be actionable by the owner, or merely informative?
4. What is the service-day boundary, and does the identity set change at daypart rollover (feature 09's daypart modelling)?
5. Do identities cross the tax boundary, and if so, are they blocked on features 408 and 410?
6. Should an identity that fails block the export, mark it, or both? The LE31 posture is fail-closed, but an export that cannot be produced is a worse outcome than an export that is produced and marked.
7. Is the identity set versioned, so that a reader can tell which rules produced last month's file?

## Why this matters

"Export the day's numbers" is a feature every restaurant system has and almost none of them make checkable. FloCafe's phrasing — *audit-ready CSV/Excel reporting with financial reconciliation identities* — names the difference in one line, and it is the general form of the answer to a defect class LE31's corpus already contains four instances of.

The correct disposition is nevertheless **defer**. The vocabulary is cheap and genuinely net-new, but LE31 v1 has no owner surface to export from, one of the deepest candidates (bill-line membership) is structurally unavailable while feature 435 is open, and two of the money-rule sources the identities would have to name are themselves unresolved. Filing it now preserves the concept and the candidate identity list without pretending the owner has asked for a report.
