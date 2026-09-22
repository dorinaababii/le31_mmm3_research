# 215 — Salar-prog/netscan production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build HANDOFF

> **Status: defer (parking-lot)**. This HANDOFF documents the slice for the *next time* the v2 network-monitoring + safe-quarantine + FastAPI + HTMX + no-Node-build question becomes buildable. **Do not implement today.**

## 1. Active feature path

`features/215-Salar-prog-netscan-production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build.md` (defer artifact; **no code today**).

Bucket: **v2 no-build reactive-web + network-ops + operator-tooling (FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine primitive, parking-lot defer)**. Build verdict: **`defer`** (charter §3.1 + `le31-conventions` Feature gate).

## 2. Seven-check feature gate verdict (per `le31-conventions/SKILL.md`)

| # | Check | Verdict |
|---|---|---|
| 1 | **Raison d'être / JTBD** | "When a future LE31 v2 maintainer asks *'if v2 introduces a network-monitoring surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface, what is the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary that preserves the existing v1 no-network-monitoring + no-safe-quarantine posture?'*, the maintainer wants *evidence that another independent 2026 Python repo at 532 KB with 1★/0⑂ + MIT permissive license + 9 topics + both `pushed_at` AND `created_at` in-window is shipping the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* primitive as the v2 no-build reactive-web network-ops discipline*, but struggles because *v1 has no documented network-monitoring primitive in the charter*, so that *v2 can introduce the network-monitoring + safe-quarantine-model vocabulary with the explicit charter §3.1 explicit-state-transition discipline rather than reinventing the pattern*." **PASS** (zero-pain today; v1 has no network-monitoring trigger; the JTBD is primitive vocabulary extension + FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine documentation, not a build-need). |
| 2 | **Viability** | Owner can read 532 KB repo description + 9-topic vocabulary + FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling quintuple? Yes. No code change required. **PASS** (informational only). |
| 3 | **Practicability and confidence** | Public GitHub access; no new infrastructure; no new stack dependencies for v1 (the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary would be re-implemented against LE31's existing FastAPI + SQLModel + aiogram v3 + PostgreSQL stack, not imported from the MIT-permissive code; LE31 v1 has no network-monitoring surface today). Confidence: medium for the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary (1★/0⑂ + MIT permissive license + 9 topics + both fields in-window + description verbatim = §3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption; the *safe-quarantine-model* discipline IS the *charter §3.1 explicit-state-transition discipline applied to the network-state dimension*). Stack: FastAPI + PostgreSQL backend = on-pattern for v1 primitives; safe-quarantine-model = off-pattern for v1 (LE31 v1 has no network-monitoring surface); nmap-multi-probe-engine = off-pattern for v1 (LE31 v1 has no nmap surface); MIT permissive = §3.2 STRICTLY-COMPATIBLE. Practicability of adoption: vocabulary + architecture-reference adoption only; code would be re-implemented against LE31's existing stack. **PASS** (posture validation only; adoption is v2 question). |
| 4 | **Conflict** | None. The *safe-quarantine-model* discipline IS the *charter §3.1 explicit-state-transition discipline* applied to the network-state dimension (the *quarantine* discipline requires explicit operator action to transition). Charter §3.1 alignment (the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary is *explicit-state-transition* applied to the network-state dimension); §3.2 STRICTLY-COMPATIBLE (MIT permissive); §3.4 not triggered (no AI surface; the *network-monitoring + safe-quarantine* pattern is *operator-tooling*, not customer-facing AI). **PASS**. |
| 5 | **Outcome, appetite, scope** | v2 no-build reactive-web + network-ops + operator-tooling (FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling vocabulary); **zero build time today**. Maximum time worth spending: 1 hour (add cross-section to existing documentation). Keep time fixed; cut scope if the solution grows. **PASS**. |
| 6 | **Cost to operational value** | Document 532 KB repo + add cross-section to existing `HANDOFF.md` (1 hour). **Cost-to-value ratio: high** (532 KB is modest but the *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* primitive + the both-fields-in-window signal need to be referenced). **PASS**. |
| 7 | **Circuit breaker and reversibility** | Fully reversible: the artifact is informational (a cross-section reference document), no code change, no schema change, no operator surface change. Disable/delete path: delete `specs/215-Salar-prog-netscan-production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build-HANDOFF.md` and `features/215-Salar-prog-netscan-production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build.md`. No retained data; no safe-failure-mode concern. **PASS**. |

**Decision: defer** (all 7 checks pass; no code change today; the artifact is the persistent cross-section architectural vocabulary + FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling documentation for the next v2 no-build reactive-web network-ops review moment).

## 3. Files to touch

**NONE today.** The defer artifact is documentation only. Files to touch *if* the future v2 trigger condition fires (first v2 PR that adds a network-monitoring surface to the LE31 v2 operator surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface):

- `app/netmonitor/` — possibly add (the network-monitoring module; depends on the v2 change).
- `app/netmonitor/quarantine.py` — possibly add (the safe-quarantine-model primitive that moves network resources between healthy+active and quarantined+inactive states; depends on the v2 change).
- `app/netmonitor/nmap_probe.py` — possibly add (the nmap-multi-probe-engine wrapper; depends on the v2 change).
- `app/dashboards/network_dashboard.py` — possibly add (the FastAPI + HTMX + no-Node-build dashboard for the network-monitoring surface; depends on the v2 change).
- `tests/test_netmonitor_quarantine.py` + `tests/test_nmap_probe.py` + `tests/test_network_dashboard.py` — possibly add (the integration tests for the network-monitoring + safe-quarantine-model + nmap-multi-probe-engine + FastAPI + HTMX + no-Node-build dashboard surfaces; depends on the v2 change).

**No existing file changes today.** No migration, no SQLModel schema change, no FastAPI route change, no Telegram handler change, no network-monitoring surface added.

## 4. Verification protocol reference

Per `le31-verification-protocol/SKILL.md` (and the general `le31-conventions` §Definition of done):

**Today (defer artifact):**
- [ ] `features/215-Salar-prog-netscan-production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build.md` exists and is read back by the parent.
- [ ] `specs/215-Salar-prog-netscan-production-grade-ip-discovery-safe-quarantine-fastapi-htmx-no-node-build-HANDOFF.md` (this file) exists and is read back by the parent.
- [ ] The `Salar-prog/netscan` description is quoted verbatim (532 KB repo).
- [ ] The 1★/0⑂ + MIT permissive license (§3.2 STRICTLY-COMPATIBLE for vocabulary + architecture-reference adoption) + Python + both fields in-window + 9 topics + description *"Production-grade IP discovery and availability tracking — nmap multi-probe engine, safe quarantine model, FastAPI + HTMX dashboard, no Node build step"* is documented.
- [ ] The charter §3.1 alignment via *safe-quarantine-model = explicit-state-transition discipline applied to network-state* is documented.
- [ ] The charter §3.2 STRICTLY-COMPATIBLE (MIT permissive) is documented.
- [ ] The charter §3.4 not-triggered (no AI surface) is documented.
- [ ] No code change in `/opt/data/le31_mmm3_research_work/` beyond `features/` + `specs/`.

**Future v2 trigger (when the first v2 PR that adds a network-monitoring surface to the LE31 v2 operator surface, a safe-quarantine-model surface, or a FastAPI + HTMX + no-Node-build dashboard for any operator-tooling surface lands):**
- [ ] The PR is read back by the parent.
- [ ] The `Salar-prog/netscan` *FastAPI + HTMX + no-Node-build + safe-quarantine-model + nmap-multi-probe-engine + operator-tooling* vocabulary is evaluated against the PR's changes: does the change address the *network-monitoring + safe-quarantine-model* discipline? does the change preserve the *FastAPI + HTMX + no-Node-build dashboard* primitive? does the change preserve the *nmap-multi-probe-engine* primitive? does the change preserve the *charter §3.1 explicit-state-transition* pattern?
- [ ] The evaluation result is recorded in the PR's Linear issue.
- [ ] The evaluation result is recorded in this HANDOFF.md as a new "Verification log" section.

## 5. Rollback path

**Today (defer artifact):** No rollback needed; nothing was changed.

**Future v2 trigger (if the v2 network-monitoring surface is adopted):**
- Disable path: feature flag `LE31_NETMONITOR_ENABLED = False` (default; gates all `app/netmonitor/` routes); no data loss.
- Delete path: `rm -rf app/netmonitor/ app/dashboards/network_dashboard.py` + `rm -rf tests/test_netmonitor_quarantine.py tests/test_nmap_probe.py tests/test_network_dashboard.py`; remove `nmap + python-nmap + aio-pika` from `requirements.txt`; no retained data; no safe-failure-mode concern.
- Migration/rollback cost: low (no schema change; no `audit_logs` or `StockEntry` change).

## 6. Mandatory LE31 skill list (per `le31-feature-pipeline/SKILL.md` step 5)

The following skills MUST be loaded by the coding agent before any v2 trigger fires:

- `le31-conventions` — for the seven-check feature gate + charter §3.1 + §3.2 + §3.4 invariants.
- `le31-verification-protocol` — for the verification protocol + the "done means observed, not asserted" principle.
- `le31-feature-pattern` — for the existing v1 feature pattern (FastAPI + SQLModel + aiogram v3 + Postgres; first-class prepared-item stock via append-only `StockEntry` ledger).
- `le31-handoff-spec` — for the slice contract format (this file is an example).
- `le31-coding-agent-brief` — for the paste-in prompt that the coding agent will use to start work.

The following skills MAY be loaded depending on the trigger:

- `le31-research` — if the v2 trigger requires additional cross-section vocabulary.
- `le31-v1-feature-pattern` — if the v2 trigger requires extending the v1 feature pattern.
- `le31-frontend` / `le31-backend` — if the v2 trigger requires frontend or backend changes.