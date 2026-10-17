# HANDOFF — 337-sanjibani-cleancloud-mcp

**Status**: defer (parking-lot, watch-list, peer-awareness, no build today) — **v2-AI MCP-server-for-CleanCloud-POS-API-+-small-business-+-agent-tools-+-async-Python vocabulary only; the `cleancloud-mcp` codebase is fully compatible (MIT permissive) but NOT adopted because LE31 v1 + v2-AI has no MCP-server surface + the *MCP-server-for-a-POS-API + agent-tools + anthropic* posture requires explicit §3.4 charter-invariant review before any v2-AI build; a future v2-AI PR that wants an MCP-server-for-a-POS-API + agent-tools surface would adopt the 11-pentagram-primitive from scratch**

**Date**: 2026-10-17
**Active feature path**: `/opt/data/le31_mmm3_research_work/features/337-sanjibani-cleancloud-mcp-mit-mcp-server-cleancloud-pos-api-small-business-agent-tools-asyncio-python-31-tests-ruff-mypy-strict-v2-ai-vocabulary.md`
**LE31 feature gate verdict**: defer (LE31 v1 + v2-AI has no MCP-server surface today; the v1 charter pins minimal-software-only + no MCP-server; the v2-AI roadmap has no MCP-server-for-a-POS-API + agent-tools surface; the 11-pentagram-primitive vocabulary is the transferable item; sister-shape to features 263 (`multiples-hq/business-state-machine-mcp` — postgres-business-state-machine-ledger) + 327 (`musterhq/muster` — agent-harness-with-audit-ledger) + today's research PICK C (`donaldrichard19-LVD/pattern-mcp` — MCP-server-design-system-pattern-check-+-auditable-decision-ledger)).

## Trigger policy

This is a **defer artifact (parking-lot, MCP-server-for-a-POS-API-+-small-business-+-agent-tools-+-async-Python vocabulary only)** — a watch-list entry. It does not start a build. It surfaces the `sanjibani/cleancloud-mcp` GitHub repo (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **1★ / 0⑂**, **40 KB tiny = 2nd-smallest in-window brainstorm-vocabulary pick of the 79-pass series**, **Python ✓ ON-STACK + asyncio + MCP + Model-Context-Protocol + CleanCloud + agent-tools + anthropic + pos + small-business + dry-cleaning + laundry**, **pushed 2026-09-18T20:04:54Z = IN-WINDOW BY PUSH ONLY** (29-day-old repo with 79-day-old creation 2026-07-03T03:36:40Z)) as a dated, in-window **MCP-server-for-a-POS-API-+-small-business-+-agent-tools-+-async-Python vocabulary peer** for LE31's potential v2-AI *MCP-server-for-a-POS-API + agent-tools* surface.

If the trigger condition (LE31 first proposes a v2-AI surface that wants *MCP-server-for-a-POS-API* OR *small-business-MCP-server* OR *agent-tools-MCP-server* OR a future owner decision questions whether the v2-AI charter should be extended to support an MCP-server-for-a-POS-API + agent-tools surface) is met, the external coding agent should:

1. Load this artifact and the parent daily-brainstorm report (`/opt/data/le31-brainstorm-2026-10-17.md`).
2. Load the `cleancloud-mcp` repo: `https://github.com/sanjibani/cleancloud-mcp` — README + asyncio + MCP + Model-Context-Protocol + CleanCloud + agent-tools + anthropic + pos + small-business + dry-cleaning + laundry + 31 tests + ruff + mypy --strict clean; **the codebase is fully compatible (MIT permissive) but NOT adopted today because v1 + v2-AI has no MCP-server surface + the *MCP-server-for-a-POS-API + agent-tools + anthropic* posture requires explicit §3.4 charter-invariant review before any v2-AI build**.
3. Load the companion features 263 (`multiples-hq/business-state-machine-mcp` — postgres-business-state-machine-ledger) + 327 (`musterhq/muster` — agent-harness-with-audit-ledger) + today's research PICK C (`donaldrichard19-LVD/pattern-mcp` — MCP-server-design-system-pattern-check-+-auditable-decision-ledger) — the **v2-AI MCP-server-+-auditable-decision-ledger + agent-harness vocabulary cluster** is the LE31 v2-AI precedent for the `cleancloud-mcp` vocabulary.
4. **Adopt the vocabulary-shape (MCP-server-for-a-POS-API + agent-tools + anthropic + asyncio + small-business + pos + 31-tests + ruff-+-mypy--strict-clean), when the v2-AI surface opens**. The transferable items are: (a) *MCP-server-for-a-POS-API*; (b) *agent-tools + anthropic*; (c) *asyncio + Python ON-STACK posture*; (d) *small-business + pos*; (e) *31-tests + ruff-+-mypy--strict-clean*. Each is a *pattern* in LE31's v2-AI charter, not a *code dependency*.
5. Re-run the LE31 feature gate with the adoption in mind. **Critical charter checks before any adoption**:
   - §3.1 ✓ (Python + asyncio ✓)
   - §3.2 ✓ (MIT permissive; LE31 v2-AI §3.2 *permissive-license-only* invariant)
   - §3.4 partial (MCP-server + agent-tools + anthropic surface requires §3.4 *chokepoint-governed + human-gate + observable-evidence + non-AI-fallback* review — LE31 charter §3.4 forbids customer-facing AI; the MCP-server + agent-tools + anthropic is operator-tooling AI per §3.4 = the surface accepts the chokepoint-governed + human-gate + observable-evidence charter invariant)
   - §3.7 partial (POS-API-read-orders-customers-invoices-payments-business-accounts-pickup-availability primitive requires §3.7 *minimal-PII-only* review — POS-API customer + invoice + payment data is PII; the MCP-server-as-a-tool-for-AI-agents surface would expose PII to AI-agents = §3.7 review needed)
6. **Decide whether the proposed v2-AI surface benefits from the MCP-server-for-a-POS-API-+-small-business-+-agent-tools-+-async-Python primitive**. If the v2-AI surface wants *MCP-server-for-a-POS-API* OR *small-business-MCP-server* OR *agent-tools-MCP-server*, the `cleancloud-mcp` vocabulary is purpose-built for that use case. If the v2-AI surface only wants to extend the existing v1 minimal-software-only deployment, `cleancloud-mcp` adds no value.
7. **If the MCP-server-for-a-POS-API-+-small-business-+-agent-tools-+-async-Python vocabulary is proposed for adoption**: do NOT add `cleancloud-mcp` to `requirements.txt`; instead, design a fresh v2-AI MCP-server-for-a-POS-API from scratch that captures the *MCP-server + POS-API + small-business + agent-tools + asyncio + Python + 31-tests + ruff-+-mypy--strict-clean* primitives. Add to `requirements.txt` only the new dependencies (`mcp` for Model Context Protocol Python SDK — v2-AI dependency review needed, `httpx` for third-party-POS-API HTTP calls — already transitively pinned via fastapi; v2-AI dependency review needed for direct dep, `pydantic` already pinned). Skip the agent-tools + anthropic integration if LE31 v2-AI charter rejects the anthropic dependency (LE31 charter §3.4 is silent on the anthropic vendor but §3.4 *non-AI-fallback* requires an explicit review). Add a single test MCP-server-call against a mock third-party-POS-API. Add 31 tests + ruff-+-mypy--strict-clean discipline. Compare against the existing v1 minimal-software-only deployment. If the test MCP-server-call adds third-party-POS-API-bridge value, propose a v2-AI extension; if not, document the comparison and defer.
8. **If the MCP-server-for-a-POS-API-+-small-business-+-agent-tools-+-async-Python vocabulary is not adopted**: document the comparison and defer. No charter §3.1 + §3.2 + §3.4 + §3.7 change is needed.
9. **Pilot on one MCP tool first**. Do not ship the MCP-server-for-a-POS-API project-wide on the first pass.

If the trigger condition is **not** met, do nothing.

## Files to touch

**No files** for this defer artifact today. A future v2-AI PR that adopts the vocabulary would create:

- New Python module: `mcp_server.py` (the MCP-server entrypoint that exposes tools like `list_orders`, `get_customer`, `list_invoices` to AI-agents via MCP)
- New Python modules: `pos_api_client.py` (the third-party-POS-API HTTP client), `models.py` (Pydantic models for the POS-API responses), `tools.py` (the MCP tool definitions)
- New tests: `tests/test_mcp_server.py` (31 tests covering list_orders, get_customer, list_invoices, list_payments, get_business_account, get_pickup_availability + edge cases)
- New dev-deps: `mcp` (Model Context Protocol Python SDK — v2-AI dependency review needed), `httpx` (for third-party-POS-API HTTP calls — v2-AI dependency review needed for direct dep), `ruff` + `mypy` (already in dev-deps), `pytest` (already in dev-deps)

## Verification protocol reference

- **`le31-conventions` skill**: load before any v2-AI build; the §3.4 *chokepoint-governed + human-gate + observable-evidence + non-AI-fallback* charter-invariant review is mandatory for any v2-AI surface; the §3.7 *minimal-PII-only* charter-invariant review is mandatory for any surface that exposes PII to AI-agents
- **`le31-v1-feature-pattern` skill**: load for the v1 Python-module + Pydantic-model + pytest-test patterns; the v2-AI MCP-server surface would adopt the same v1 patterns
- **`le31-handoff-spec` skill**: load for the slice-contract template + the seven-check gate verdict; the slice contract for the v2-AI MCP-server surface would follow the same template
- **`le31-coding-agent-brief` skill**: load for the paste-in prompt; the v2-AI build prompt would follow the same template

## Rollback path

**Trivially reversible** (the defer artifact is a vocabulary-only artifact):

- The 11-pentagram-primitive is a documented vocabulary reference; no code is added; no Python modules are added; no Pydantic models are added; no tests are added; no dev-deps are added; no production-deps are added
- The artifact can be deleted by `rm /opt/data/le31_mmm3_research_work/features/337-sanjibani-cleancloud-mcp-mit-mcp-server-cleancloud-pos-api-small-business-agent-tools-asyncio-python-31-tests-ruff-mypy-strict-v2-ai-vocabulary.md` + `rm /opt/data/le31_mmm3_research_work/specs/337-sanjibani-cleancloud-mcp-HANDOFF.md`
- The artifact does not affect any production deployment; the v1 dependency-whitelist is unchanged; the v1 Python-module-set is unchanged; the v1 Pydantic-model-set is unchanged; the v1 test-set is unchanged; the v1 dev-deps are unchanged; the v1 production-deps are unchanged

## Mandatory LE31 skill list

The external coding agent **must** load these skills before any v2-AI build:

- `le31-conventions` — the §3.4 *chokepoint-governed + human-gate + observable-evidence + non-AI-fallback* charter-invariant review is mandatory for any v2-AI surface; the §3.7 *minimal-PII-only* charter-invariant review is mandatory for any surface that exposes PII to AI-agents
- `le31-feature-pipeline` — the v2-AI build follows the same feature-pipeline as v1; the v2-AI bucket projects (`le31 v2 owner-pains`, `le31 v2-AI`) DO NOT EXIST in the 3-project workspace — the v2-AI sub-issue is attached to `le31 Research` per the 2026-08-28 verified workspace structure
- `le31-v1-feature-pattern` — the v2-AI MCP-server surface would adopt the v1 Python-module + Pydantic-model + pytest-test patterns
- `le31-handoff-spec` — the v2-AI build follows the same slice-contract template as v1
- `le31-coding-agent-brief` — the v2-AI build follows the same paste-in prompt template as v1
- `le31-daily-research` — the v2-AI vocabulary references for the `cleancloud-mcp` surface are tracked in the daily-research picks list (features 263/327 + today's research PICK C = the v2-AI MCP-server-+-auditable-decision-ledger + agent-harness cluster)