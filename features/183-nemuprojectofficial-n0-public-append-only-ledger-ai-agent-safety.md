# Feature 183 — `nemuprojectofficial-n0-public-append-only-ledger-ai-agent-safety` (defer)

> **NEW observation (2026-09-16).** Documents in-window GitHub repo `nemuprojectofficial-glitch/n0-public` (MIT, **0★/0⑂**, Python, **pushed 2026-09-16T05:37:14Z**, in-window by push only, **created 2026-09-06** — 10-day-old repo, 220+ KB). Topics (verbatim): `[accountability, agent-safety, ai-agents, append-only, audit-log, autonomous-agents, llm-agents, transparency]` — the strongest v2-AI control-plane topic-coverage of any in-window candidate in the 7-day window. Description (verbatim): *"An autonomous agent with 1,000 yen, a public append-only ledger, and no revenue yet. Includes a dependency-free verifier for the ledger format."* One net-new primitive: **"dependency-free verifier for the ledger format"** — the *trust-the-format-not-the-runtime* primitive. Bucket: **v2-AI control-plane (defer, parking-lot)** — watch-list defer. Zero build time today.

## Goal

Retain the **"dependency-free verifier for the ledger format"** primitive as a persistent cross-section reference for any future LE31 v2 surface that introduces a second stakeholder (accountant, tax authority, regulator) who needs to verify `audit_logs` without trusting the LE31 codebase. The artifact is the persistent cross-section reference + a candidate *trust-the-format-not-the-runtime* vocabulary for the next v2-AI control-plane moment. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the **"dependency-free verifier for the ledger format"** primitive: the verifier is a *separate* program from the writer; the verifier does *not* depend on the writer's runtime, libraries, or application dependencies. The verifier checks the *format* of the ledger (the schema, the chain integrity, the entry types) — not the *contents* (the writer's claims). This is the **trust-the-format-not-the-runtime** primitive.
- A written record of the **8-topic v2-AI control-plane vocabulary**: `[accountability, agent-safety, ai-agents, append-only, audit-log, autonomous-agents, llm-agents, transparency]` — the full v2-AI control-plane surface area. This is the strongest single-repo topic-coverage match for the v2-AI control-plane cluster in the 7-day window.
- A decision record: today's verdict is `defer` because no v2-AI surface exists today; the v2 trigger is the introduction of an LLM-assisted surface or a second stakeholder.
- A cross-section reference with the v2-AI control-plane cluster: features 137, 141, 145, 150, 152, 167, 169, 175.

**Out of scope (defer artifact):**
- Any change to LE31 v1's waiter web UI or cook Telegram bot.
- Any change to LE31 v1's `audit_logs` schema.
- Any LLM-assisted surface (LE31 v1 has no LLM integration; introducing one requires a charter §3.4 owner decision).
- Adoption of the n0-public codebase (the repo is 10 days old, MIT Python; the *primitive* is portable; the *codebase* is not adoptable without a full read-and-eval).
- Cross-pollination with charter §3.4 customer-facing-AI (the *autonomous-agent* framing is staff-tooling territory per §3.4; if a v2 surface ever exposes an LLM-assisted recommendation to a customer, this primitive becomes a hard requirement, not an option).

## Evidence / JTBD

When a future LE31 v2 surface introduces a second stakeholder (accountant, tax authority, regulator), the owner wants *a primitive that lets the stakeholder verify the LE31 `audit_logs` chain integrity without running the LE31 codebase*, but struggles because *LE31 v1's audit_logs are written by the FastAPI process and the verifier would have to depend on the FastAPI runtime*, so that *the v2 surface can offer external-auditor verification with a defensible answer*.

- **Evidence class**: observed (the n0-public description + 8 topics name the primitive directly).
- **Confidence**: medium-high for the primitive match (the description + topic-coverage are direct); low for transferability (LE31 v1 has no external-auditor surface).
- **Real observed LE31 JTBD**: zero-pain today; LE31 v1 has no accountant-facing surface; the v2 surface that would *use* the primitive doesn't exist.
- **The value is naming, not direct demand**: when the first v2 surface introduces a second stakeholder, the n0-public pattern is a ready-made *named* vocabulary slot.

## Description

GitHub `nemuprojectofficial-glitch/n0-public` (MIT, 0★/0⑂, Python, pushed 2026-09-16T05:37:14Z, created 2026-09-06, 220+ KB).

Description (verbatim): *"An autonomous agent with 1,000 yen, a public append-only ledger, and no revenue yet. Includes a dependency-free verifier for the ledger format."*

Topics (verbatim): `[accountability, agent-safety, ai-agents, append-only, audit-log, autonomous-agents, llm-agents, transparency]`

The architectural primitive has one core principle and three sub-properties:

1. **"dependency-free verifier"** — the verifier is a *separate* program from the writer; the verifier does *not* import the writer's runtime, libraries, or application code. The verifier checks the *format* of the ledger — not the *contents* of the writer's claims. This is the **trust-the-format-not-the-runtime** discipline.
2. **"for the ledger format"** — the verifier checks *schema* (every row matches the expected schema), *chain integrity* (no row is deleted or updated; row order is monotonic), and *entry types* (every `action` is a valid action enum, every `actor_user_id` is a valid user). The verifier does *not* check the *business logic* of the entries.
3. **"autonomous agent + public append-only ledger + dependency-free verifier"** — the three components form a closed-loop: the agent writes to the ledger, the ledger is publicly auditable, and the verifier proves the ledger's format without depending on the agent's runtime.

**The 1:1 mapping onto LE31 v2 architecture (if/when §3.4 surfaces):**

| n0-public primitive | LE31 v2 equivalent | Charter section | Status |
|---|---|---|---|
| Autonomous agent | (LE31 v1 has no autonomous agent; the cook Telegram bot is deterministic) | §3.4 (future v2) | **Not implemented** — requires §3.4 owner decision |
| Public append-only ledger | (LE31 v1 `audit_logs` is private to the single restaurant; *public* would require a v2 surface) | §3.1 + v2 hardening | **Partially implemented (v1, private)** |
| Dependency-free verifier | (LE31 v1 has no external-verifier; the FastAPI process *is* the writer) | v2 hardening | **Not implemented** — requires v2 trigger |
| 8-topic v2-AI control-plane vocabulary | (LE31 v1 has no LLM integration; v2 would adopt the full vocabulary) | §3.4 (future v2) | **Not implemented** |

## Data model

**No schema change today.** The defer artifact is documentation only.

If the future v2 trigger condition fires (first v2 surface that introduces a second stakeholder or an LLM-assisted surface), the v2 implementation would need:
- A `scripts/verify_audit_logs.py` standalone script (no FastAPI, no SQLModel, no aiogram — just `psycopg` + `argparse`).
- Optionally, the `chain_position` BIGSERIAL column on `audit_logs` (already proposed in feature 182) for chain-integrity verification.

**No existing schema change today.**

## Implementation steps

**None today.** The defer artifact is documentation only.

Future v2 implementation would include:
1. Write `scripts/verify_audit_logs.py` — a standalone Python script that reads `audit_logs` from PostgreSQL with read-only credentials and verifies (a) chain integrity (no row deleted or updated; monotonic `id`; no gaps) and (b) schema integrity (every row matches the expected schema; every `actor_user_id` is a valid user; every `action` is a valid action enum).
2. Add the script to the CI pipeline (run on every commit; fail CI if the verification fails).
3. Optionally expose the verifier as a CLI tool for v2 owner-facing audit verification.

**No existing code change today.**

## Telegram interaction if any

**None today.** The defer artifact is documentation only.

Future v2: the cook Telegram bot could call the verifier before any LLM-assisted recommendation is shown to the cook — but this would require an LLM-assisted surface (charter §3.4 owner decision required first).

## Dependencies

- **Charter §3.1 invariant compatibility**: ✓ (the verifier is read-only; the append-only invariant is preserved).
- **§3.2 license compatibility**: ✓ (MIT permissive).
- **§3.4 AI compatibility**: ✓ (the verifier itself is not AI; it's a format-checker; the *agent* that produces the ledger is autonomous-agents territory, but the verifier is not).
- **Stack compatibility**: ✓ (Python; `psycopg` + `argparse` are standard library / widely-available).

## Open questions

1. **Does LE31 v2 need a second-stakeholder surface at all?** The owner is the only stakeholder in v1; the question is whether v2 introduces an accountant, tax authority, or regulator. This is an owner decision per charter §3.4 + §3.5.
2. **Is the dependency-free verifier *strictly* dependency-free?** The verifier could still depend on `psycopg` (PostgreSQL client) and `argparse` (CLI). The discipline is *no LE31-application-runtime dependencies*, not *no Python packages at all*. Recommend documenting this distinction in the verifier's README when implemented.
3. **Should the verifier be a *separate* program, or a *subprocess* of the LE31 application?** The discipline says *separate* — the verifier must not be able to mutate `audit_logs` (it should have read-only DB access at most). Recommend a separate program with read-only DB credentials when implemented.

## Why this matters

The **"dependency-free verifier for the ledger format" + 8-topic v2-AI control-plane vocabulary** is the **external-auditor-facing vocabulary** that LE31 needs *before* it can answer the second-stakeholder question. Every other primitive in the v2-AI control-plane cluster (features 137/141/145/150/152/167/169/175) is *internal* (the LE31 codebase uses them to maintain its own invariants); the n0-public primitive is *external* (an accountant or regulator uses it to verify the LE31 invariants without running the LE31 codebase). This external-facing property is what makes feature 183 the **most likely primitive to be referenced when the first v2 surface introduces a second stakeholder**.

Companion artifacts: features 137 (NL-to-Executable-Obligations), 141 (KRINEIA), 145 (garde-fous-frozen-mandate), 150 (Mandato MCP), 152 (LATTICE), 167 (provtrail), 169 (openshare-ledger), 175 (geminka-agent-v2-ai-control-plane-watch-v3) — all ripgrep-verified distinct from this artifact. Parent research issue HMM-259 (Research 2026-09-16 — daily).
