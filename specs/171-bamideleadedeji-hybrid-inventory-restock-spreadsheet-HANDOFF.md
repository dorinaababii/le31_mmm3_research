# HANDOFF — Feature 171: `bamideleadedeji-hybrid-inventory-restock-spreadsheet`

**Slice contract for the coding agent. This is a `parking-lot` feature — no code change today. The HANDOFF is documentation only + a meta-brainstorm on the v1 product-wedge.**

## Active feature path

`features/171-bamideleadedeji-hybrid-inventory-restock-spreadsheet.md` — parking-lot (Pick B of Brainstorm 2026-09-13, parent research issue HMM-241).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | spreadsheet-as-ledger is compatible with explicit-state-transitions (every row is a transaction) |
| 2 | Charter §3.2 (permissive license) | ✓ | MIT |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | zero AI (Excel formulas only) |
| 4 | In-window by `pushed_at` | ✓ | pushed 2026-09-12T13:37:02Z (within 30-day window) |
| 5 | Ripgrep-verified unique vs features/ 1..169 | ✓ | no existing feature raises the *what-LE31-earns-its-way-OFF-spreadsheets* question |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 3/15/16/26/28/34/65/66 |
| 7 | Parking-lot verdict (no code change) | ✓ | 0★ + single-maintainer + spreadsheet (not Python) → no code adoption; the *meta-brainstorm* is the value |

**Gate verdict**: **parking-lot** — 7/7 gate checks pass, but the build verdict is `parking-lot` because the artifact is in spreadsheet format (despite `language:Python` in the GitHub-search qualifier) and the *meta-brainstorm* is the value, not the code.

## Bucket

**new** (meta-brainstorm) — the *naming of the wedge question* is the value. Bucket is `new` because no existing feature addresses the *what-LE31-earns-its-way-OFF-spreadsheets* question. Could also be classified as `v1 architecture reference`.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that proposes a v1 surface competing with the spreadsheet alternative), the implementation would be a *named architectural decision*: which of the four wedge answers (multi-user concurrency / structured audit log / Telegram-cook channel / owner-recap export / append-only-enforced) is the v1 product wedge?

## Verification protocol

1. Open the spreadsheet template (download the `.xlsx`)
2. Verify the description-vs-template match (does the template implement multi-department stock control + batch expiry + stockout alerts?)
3. If yes, file a cross-section evidence note in the feature contract
4. If no, downgrade to reject (the description is misleading)

**Do NOT do step 1 today.** The parking-lot verdict means the experiment is *deferred*, not executed.

## Rollback path

**N/A** — no code change today. The HANDOFF is documentation only.

If the future v1 trigger condition fires, the rollback path is: revert the v1 PR that adds the wedge surface. The spreadsheet-template pattern itself does not require a code change to LE31 v1.

## Mandatory LE31 skill list

- `le31-conventions` — naming, file structure, charter invariants
- `le31-v1-feature-pattern` — v1 feature template + parking-lot verdict semantics
- `le31-coding-agent-brief` — coding-agent invocation pattern
- `le31-handoff-spec` — HANDOFF.md template

## Cross-section evidence

- **features/ 3, 15, 16, 26, 28, 34, 65, 66** — sister-shape references
- **feature 153** (`sausageos-production-erp-append-only-stock-fefo-versioned-recipes`) — cross-section on the *batch expiry* primitive
- **feature 170** (`devshakib015-shopdesk-offline-pos-as-stock-ledger`) — sister-pick from same brainstorm session; both raise the offline-first wedge question
- **ad-hoc evidence**: `bamideleadedeji/Hybrid_Inventory_Restock_Master.xlsx` GitHub direct-GET verified by parent 2026-09-13

## Notes

- **Do not adopt the spreadsheet template**. The parking-lot verdict is based on (a) 0★ with single-maintainer cadence; (b) the artifact is in spreadsheet format (`.xlsx` extension in repo name); (c) brand-new repo (12-minute-old at push time). The *meta-brainstorm* is the value, not the code.
- **Do not propose code changes** to LE31 v1 today. The parking-lot artifact is documentation only.
- **The cross-section pattern** is the *naming of the wedge question* + the *naming of the four candidate wedge answers* (multi-user / audit log / Telegram / append-only-enforced). When the next v1 PR proposes a v1 surface that competes with the spreadsheet alternative, the parking-lot pattern is a ready-made named reference + the *naming of the test* the v1 design must answer.
- **Parent-verified**: GitHub API direct-GET `/repos/bamideleadedeji/Hybrid_Inventory_Restock_Master.xlsx` saved to `/tmp/verify_bamideleadedeji_Hybrid_Inventory_Restock_Master.xlsx.json` on 2026-09-13. All star/fork/license/pushed_at/created_at/description/topics/size values in the feature contract re-parsed byte-for-byte by parent.

---

**End of HANDOFF.**
