# salestrics-mcp-native-crm-watch — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/86-salestrics-mcp-native-crm-watch.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `86`
- Slug: `salestrics-mcp-native-crm-watch`
- Contract file: `features/86-salestrics-mcp-native-crm-watch.md`
- Bucket: **v2-AI control-plane** — parking-lot (research-only, no code)
- Linear parent: `HMM-107` (Brainstorm 2026-08-19 — daily, created in this cron)
- Linear sub-issue: **HMM-110** (created in this cron; project `le31 v1 — Core MVP`, label `Feature`)

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md`. Evidence precondition:
**observed** (in-window HN Show HN of `Salestrics`, 1pt 2026-08-08, "An open MCP
server and CRM for AI-native revenue teams", `https://www.salestrics.com/`).
Confidence: **low** for the peer signal (1 HN point = weak validation; no public
repo to read; no star count; team size unknown), **high** for the architectural
relevance (MCP-native is a real and growing integration fabric in the small-team
SaaS lane).

**Decision: parking-lot.** The cross-section is real but the peer signal is weak
and the scope is significant (MCP-server surface requires explicit charter approval).
Failed checks:
- **Practicability**: MCP surface is not in v1/v2 scope today; charter §3.1 explicitly defines two primary operational surfaces (waiter web UI + cook Telegram bot) and does not include an MCP-server surface. Charter approval is a hard prerequisite.
- **Cost-to-value**: 1 HN point = weak peer signal; no public repo to verify; team size unknown.
- **Scope**: the MCP-server surface would require 3 new tables (McpTool, McpCall, McpAuth), an MCP server (FastAPI route), an auth layer, a rate limiter, 10 acceptance tests, and a security review — all required before any work begins.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules; even though this is v2-AI control-plane, the slicing discipline inherits).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job on 2026-08-19).
5. `le31-feature-pipeline` (so the agent understands how this slice will be sequenced after re-elevation).
6. `le31-research` (for the cross-section evidence base).

If the destination repo does not yet ship these skills, request them from the research-side Hermes instance before writing code.

## Files the slice will touch (when re-elevated to build — NOT planned today)

```
features/86-salestrics-mcp-native-crm-watch.md                    # NEW (this artifact)
specs/salestrics-mcp-native-crm-watch-HANDOFF.md                  # NEW (this file)
INDEX.md                                                              # EDIT: append one row to "Active feature pipeline" table
backend/app/models/mcp.py                                            # NEW: McpTool, McpCall, McpAuth SQLModels
backend/alembic/versions/XXXX_add_mcp_server.py                    # NEW: one migration (3 tables)
backend/app/services/mcp_server.py                                   # NEW: MCP server (FastAPI route for protocol)
backend/app/services/mcp_auth.py                                     # NEW: token issuance + scope enforcement + revocation
backend/app/services/mcp_rate_limit.py                               # NEW: per-tool per-agent rate limiter
backend/app/bot/cook_bot.py                                          # EDIT: no change (MCP-server is external-facing, not cook-bot-facing)
backend/tests/test_mcp_server.py                                     # NEW: 10 acceptance tests
backend/README.md                                                    # note the new MCP server surface + tool list
```

Three new tables (McpTool, McpCall, McpAuth). `McpCall` is append-only (per charter §3.1 stock + state invariants). `McpAuth` is revocable (per charter §3.2 privacy). One new pip dependency: Anthropic's MCP SDK for Python (or community alternative — to be evaluated when re-elevated).

## Verification protocol

After the artifact ships (post-re-elevation):

1. **Read back** `features/86-salestrics-mcp-native-crm-watch.md` and confirm it matches the daily-brainstorm report's "86-salestrics-mcp-native-crm-watch" pick description.
2. **Read back** the new row in `INDEX.md` "Active feature pipeline" table and confirm the date (2026-08-19), pick slug, feature path, and Linear sub-issue ID.
3. **Run the 10 acceptance tests** in `backend/tests/test_mcp_server.py`:
   - empty McpTool table → server returns empty tools list
   - one McpTool registered → server returns it in tools list
   - valid tool call from authenticated agent → McpCall row appended with status=success
   - tool call from unauthenticated agent → HTTP 401, no McpCall row
   - tool call with revoked token → HTTP 401, no McpCall row
   - rate limit exceeded → HTTP 429, McpCall row with status=rate_limited
   - tool call with invalid input → HTTP 400, McpCall row with status=invalid_input
   - tool call with valid input that triggers a v2-AI control-plane feature → verify the underlying feature runs (e.g., `le31.stock.add` triggers feature 03 / 26 / 38 logic)
   - audit log query → McpCall rows are append-only (cannot update or delete)
   - revocation flow → McpAuth row updated with `revoked_at`; subsequent calls with the token return HTTP 401
4. **Run the LE31 test suite** (`pytest` or equivalent) and confirm it still passes.
5. **Hand-test with an MCP client**: configure Claude Desktop or Cursor to point at the LE31 MCP server; trigger `le31.stock.add` from the agent; verify the StockEntry row appears in the LE31 database.
6. **Security review**: separate scope; ensure the auth layer + rate limiter + audit log cover the threat model from the TENET paper (arXiv `2608.17538v1`, 2026-08-18, "TENET: Telegram Mini App (in)security") and the TeleGapper paper (arXiv `2608.13390`, 2026-08-13, privacy-policy compliance).
7. **On a future daily-brainstorm pass**: re-query HN `solo-founder-saas` + GitHub `topic:mcp` + OpenAlex `model context protocol` for new in-window MCP-native small-team SaaS peers. If ≥3 in-window peers with public repos surface, escalate evidence and re-evaluate.

## Rollback path

The artifact is a parking-lot (no code shipped today). When re-elevated and shipped, rollback is: drop the three MCP tables via Alembic downgrade; remove the MCP server route; remove the auth layer + rate limiter; revert any LE31 tool wrappings. The slice is reversible at zero data-loss cost (no production `McpCall` rows will exist on the day of the rollback if the feature never saw real traffic).
