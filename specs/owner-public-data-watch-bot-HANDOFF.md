# owner-public-data-watch-bot — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/82-owner-public-data-watch-bot.md` before touching any
> code. Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `82`
- Slug: `owner-public-data-watch-bot`
- Contract file: `features/82-owner-public-data-watch-bot.md`
- Bucket: **v2 owner-pains** — defer (watch-list; EUR-Lex RSS blocked on VPS)
- Linear parent: `HMM-99` (Brainstorm 2026-08-18 — daily, created in this cron)
- Linear sub-issue: **TBD** (create as a draft public-data-watch artifact)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (in-window GitHub `topic:small-business` cluster — `djfksjd/sole-search` 45★ Python, 206KB, in-window push 2026-07-30T08:10:40Z, Korean small-business-owner public-support-program research agent skill).

**Confidence:** **high** for the JTBD pull (45★ is the strongest small-business-owner JTBD signal of the 19-pass daily-brainstorm series; the profile-aware public-data push pattern is universal), **medium** for the EU-specific stack match (the anchor peer is Korean government programs; LE31's EU analogues are EUR-Lex / ECB / CNIL).

**Decision: defer.** The hard blocker for immediate build is **EUR-Lex RSS is currently blocked on this VPS** (14+ consecutive days of WAF-block HTTP 202/0-byte, with a recent shift to HTTP 404 / 55KB HTML "Page Not Found - EUR-Lex"). The slice is wired to switch to EUR-Lex REST API (CEF API) when implemented; verify reachability with a `curl -sS "https://eur-lex.europa.eu/..."` smoke test before committing to the slice.

**Failed checks:**
- **Practicability**: EUR-Lex RSS unreachable. EUR-Lex REST API smoke-test required before build.
- **Cost-to-value**: no observed owner pain in window. Scope creep risk to "regulatory compliance dashboard" (v3 territory).

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-18).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after EUR-Lex REST API is verified reachable).
6. `le31-research` (for the cross-section evidence base; the daily-research pass has been reporting the EUR-Lex RSS block for 14+ consecutive days).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice will touch (when re-elevated to build)

```
features/82-owner-public-data-watch-bot.md                # NEW (this artifact)
specs/owner-public-data-watch-bot-HANDOFF.md             # NEW (this file)
INDEX.md                                                  # EDIT: append one row to "Active feature pipeline" table
agent/services/public_data/eurlex.py                      # NEW (EUR-Lex REST API client)
agent/services/public_data/ecb.py                         # NEW (ECB FX client; reuse daily-research cache)
agent/services/public_data/cnil.py                        # NEW (CNIL client; reuse daily-research cache)
agent/services/rule_engine.py                             # NEW (deterministic profile filter)
agent/models/owner_watch_keywords.py                      # NEW (SQLModel)
alembic/versions/xxx_add_owner_watch_keywords.py          # NEW (Alembic migration)
cook_bot/handlers/whats_new_today.py                      # NEW (aiogram v3 /whats-new-today handler)
cook_bot/handlers/watch_add_rm.py                         # NEW (aiogram v3 /watch-add /watch-rm handlers)
agent/tests/test_whats_new_today.py                       # NEW (6 acceptance tests)
```

One new SQLModel table (`owner_watch_keywords`) + one Alembic migration. **Zero schema impact on the core ledger (`StockEntry`, `Visit`, `Order`, `OrderItem`, `Bill`, `Payment`).** Zero new pip dependencies (the EUR-Lex REST API returns JSON via stdlib `httpx` which is already a dependency).

## Verification protocol

After the artifact ships (post-EUR-Lex-REST-API-reachability):

1. **Smoke-test EUR-Lex REST API** from this VPS: `curl -sS "https://eur-lex.europa.eu/...?...&type=notice" -o /tmp/eurlex-test.json` and confirm HTTP 200 + non-empty JSON. If blocked, the slice is blocked.
2. **Read back** `features/82-owner-public-data-watch-bot.md` and confirm it matches the daily-brainstorm report's "82-owner-public-data-watch-bot" pick description.
3. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-18), pick slug, feature path, and Linear sub-issue ID.
4. **Run the 6 acceptance tests** in `agent/tests/test_whats_new_today.py`:
   - empty data sources → "no new items today"
   - EUR-Lex has 2 notices matching "VAT" → both surface in summary
   - EUR-Lex has 10 notices → only top 5 by recency surface
   - owner keyword "service-charge" with 0 matches → "0 matches" in summary
   - owner profile excludes `alcohol_license` → alcohol-related notices are filtered out
   - cache hit within 1h → second call within 1h does NOT re-hit EUR-Lex
5. **Run the LE31 test suite** (`pytest` or equivalent) and confirm it still passes.
6. **Hand-test on the cook bot**: trigger `/whats-new-today` in a test chat; verify the summary renders within the 4096-char Telegram limit.
7. **On a future daily-brainstorm pass**: re-query the GitHub `topic:small-business` cluster for new in-window EU-specific profile-aware public-data peers. If a new ≥10★ peer surfaces, escalate evidence and re-evaluate.

## Linear sub-issue

Create a Linear sub-issue in project `le31 v1 — Core MVP` (project ID `fdb233e0-044c-4425-8574-1b72c3787563`) with label `Feature`.

- Title: `Feature 82 — owner-public-data-watch-bot`.
- Body: short summary + the file path to `features/82-owner-public-data-watch-bot.md` (≤1500 chars).
- Parent: `HMM-99` (Brainstorm 2026-08-18 — daily).
- Status: `Backlog` (defer until EUR-Lex REST API is verified reachable).

## Rollback path

Delete `features/82-owner-public-data-watch-bot.md` and this HANDOFF.md. Remove the corresponding row from `INDEX.md`. Remove `agent/services/public_data/`, `agent/services/rule_engine.py`, `agent/models/owner_watch_keywords.py`, the Alembic migration, the cook bot handlers, and the test file. Revert the Alembic migration (`alembic downgrade -1`). No data loss to revert (the new table is empty at the defer state).

## Why this matters (for the coding agent)

The owner of a single small restaurant is regulatorily exposed: VAT rules change, EUR/USD swings hit USD-imported ingredients, CNIL privacy updates affect guest data handling, BOFiP tax notices affect payroll. Without a profile-aware public-data push, the owner learns about regulatory changes only when something breaks (an inspector visit, a tax audit, a privacy complaint). With `/whats-new-today`, the owner gets a daily plain-language summary of the regulatory deltas that affect their specific profile, on the surface they already use (Telegram), in the language they already understand (no jargon). The cross-section pattern (profile + public-data + rule filter + push) is observed in the in-window Korean sole-search agent at 45★ — the strongest small-business-owner JTBD signal of the 19-pass series.

**Status: defer.** Re-evaluate when (a) EUR-Lex REST API smoke-test passes from this VPS, OR (b) an in-window ≥10★ EU-specific profile-aware public-data peer surfaces, OR (c) the LE31 owner explicitly asks for it.
