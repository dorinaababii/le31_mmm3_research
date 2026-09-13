# HANDOFF — Feature 170: `devShakib015-shopdesk-offline-pos-as-stock-ledger`

**Slice contract for the coding agent. This is a `defer` (parking-lot) feature — no code change today. The HANDOFF is documentation only.**

## Active feature path

`features/170-devshakib015-shopdesk-offline-pos-as-stock-ledger.md` — defer/parking-lot (Pick A of Brainstorm 2026-09-13, parent research issue HMM-241).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Charter §3.1 (explicit state transitions) | ✓ | shopdesk uses "stock as a ledger" (append-only discipline); LE31 v1 already implements this in `StockEntry` |
| 2 | Charter §3.2 (permissive license) | ✓ | MIT |
| 3 | Charter §3.4 (no customer-facing AI) | ✓ | zero AI; deterministic barcode-driven UI |
| 4 | In-window by `pushed_at` | ✓ | pushed 2026-09-02T14:19:28Z (within 30-day window 2026-08-14..2026-09-13) |
| 5 | Ripgrep-verified unique vs features/ 1..169 | ✓ | no existing feature covers the *offline-first wedge + day-close-report* surface |
| 6 | Cross-section with ≥1 existing feature | ✓ | features 3/5/26/27/34/39/40/54/69/131/165 |
| 7 | Defer verdict (parking-lot, no code change) | ✓ | 0★ + single-maintainer + 5-year-old repo + Windows-desktop stack mismatch → no code adoption; the *demand signal* is the value |

**Gate verdict**: **defer (parking-lot)** — 7/7 gate checks pass, but the build verdict is `defer` because the code is not adoptable (single-maintainer + 5-year-old + Windows-desktop stack).

## Bucket

**v1** (operator-surface inspiration) — the *shape* is the value, not the code.

## Files to touch

**None today.** The defer artifact is documentation only.

If the future v1 trigger condition fires (first v1 PR that adds an offline-first wedge surface), the implementation would not require a code change — the LE31 v1 surface already implements the *stock-as-ledger + SQLite + offline* wedge. The HANDOFF is to evaluate whether the offline-first wedge is the right product-wedge for the next v1 PR.

## Verification protocol

1. `git clone https://github.com/devShakib015/BusinessMonitoringApp` (NOT to be done today — defer)
2. Read the README + the entry-point script + the SQLite schema
3. Verify the description-vs-code match (does the code implement "stock as a ledger"?)
4. If yes, file a cross-section evidence note in the feature contract
5. If no, downgrade to reject (the description is misleading)

**Do NOT do step 1 today.** The defer verdict means the experiment is *deferred*, not executed.

## Rollback path

**N/A** — no code change today. The HANDOFF is documentation only.

If the future v1 trigger condition fires, the rollback path is: revert the v1 PR that adds the offline-first wedge. The ShopDesk pattern itself does not require a code change to LE31 v1.

## Mandatory LE31 skill list

- `le31-conventions` — naming, file structure, charter invariants
- `le31-v1-feature-pattern` — v1 feature template + parking-lot verdict semantics
- `le31-coding-agent-brief` — coding-agent invocation pattern
- `le31-handoff-spec` — HANDOFF.md template

## Cross-section evidence

- **features/ 3, 5, 26, 27, 34, 39, 40, 54, 69, 131, 165** — sister-shape references
- **feature 40** (`satisfecho-python-pos-watch`) — sister-shape Python POS; AGPL-3.0 blocked; ShopDesk is the MIT alternative shape
- **feature 170** (this feature) — MIT permissive + offline-first + day-close-report surface
- **ad-hoc evidence**: `devShakib015/BusinessMonitoringApp` GitHub direct-GET verified by parent 2026-09-13

## Notes

- **Do not adopt the ShopDesk codebase**. The defer verdict is based on (a) 0★ with single-maintainer cadence; (b) Windows-desktop stack mismatch; (c) 5-year-old repo with single re-activation push. The *demand signal* is the value, not the code.
- **Do not propose code changes** to LE31 v1 today. The defer artifact is documentation only.
- **The cross-section pattern** is the *naming of the offline-first wedge* + the *demand signal* for that wedge. When the next v1 PR touches the offline-first surface, the ShopDesk pattern is a ready-made named reference.
- **Parent-verified**: GitHub API direct-GET `/repos/devShakib015/BusinessMonitoringApp` saved to `/tmp/verify_devShakib015_BusinessMonitoringApp.json` on 2026-09-13. All star/fork/license/pushed_at/created_at/description/topics/size values in the feature contract re-parsed byte-for-byte by parent.

---

**End of HANDOFF.**
