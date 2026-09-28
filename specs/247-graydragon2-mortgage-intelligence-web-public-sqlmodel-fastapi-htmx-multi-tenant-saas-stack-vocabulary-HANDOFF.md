# HANDOFF: feature 247 — `graydragon2/mortgage-intelligence-web-public` (v1 SQLModel+FastAPI+HTMX multi-tenant SaaS stack-vocabulary-reference, defer parking-lot)

> **Date filed:** 2026-09-28
> **Author:** Daily Brainstorm Cron (LE31) — parent-surfaced pick
> **Parent research issue:** [linear: blocked — see /opt/data/le31-brainstorm-2026-09-28.linear-fallback.json]
> **Bucket:** v1 SQLModel+FastAPI+HTMX multi-tenant SaaS stack-vocabulary-reference (parking-lot, future-v1-or-v2-surface-vocabulary-reference)
> **License:** **MIT ✓ §3.2 STRICTLY-COMPATIBLE**
> **Reference URL:** https://github.com/graydragon2/mortgage-intelligence-web-public
> **Reference data:** MIT, 0★/0⑂, Python, **77 KB tiny repo**, pushed **2026-09-09T23:06:47Z** + created **2026-09-09T23:05:59Z** = **both fields in-window by same-day-fresh-repo created+committed-today** (the *second-freshest in-window* of today's 3 picks; 19-day time-to-pick-window). Topics (verbatim): `deterministic-scoring, fastapi, htmx, mortgage, python, saas, sqlmodel, stripe` (**5-of-9 topics enumerate the LE31 v1 stack envelope**: `fastapi + htmx + python + saas + sqlmodel`). Description (verbatim): *"Hosted multi-tenant mortgage refinance intelligence app with deterministic scoring, rate tracking, authentication, billing, alerts, and AI-generated explanation."*

## Active feature path

`features/247-graydragon2-mortgage-intelligence-web-public-mit-sqlmodel-fastapi-htmx-multi-tenant-saas-mortgage-rate-tracking-authentication-billing-alerts-ai-generated-explanation-python.md`

## Seven-check gate verdict (per `le31-conventions/SKILL.md` lines 47–62)

| # | Check | Verdict | Notes |
|---|---|---|---|
| 1 | Raison d'être / JTBD | ✅ inferred | *When a future LE31 v1 or v2 surface proposes (a) a multi-tenant SaaS-variant (any future SaaS-variant-of-LE31-v1 would need multi-tenant auth + billing + alerts + dashboards), (b) a deterministic-rule-engine for owner-facing-alerts (any future alert-surface would need a rule-engine that scores events against a rule-set), (c) a third-party-auth + Stripe-billing surface (any future SaaS-variant would need this; LE31 v1 currently relies on chat-id-based implicit-auth), (d) an alert-system (any future alerts-surface would need a background-worker-alerting discipline), or (e) an owner-facing AI-generated-explanation (any future owner-facing-AI surface would generate an explanation for the owner, NOT for customer-facing interactions), the owner wants the verbatim 6-primitive sextuple from a real-world 2026 SQLModel+FastAPI+HTMX multi-tenant SaaS-discipline.* Maps onto charter §3.1 + §3.2 + §3.4 invariant. |
| 2 | Viability | ✅ | MIT permissive (STRICTLY-ADOPTABLE); 0★/0⑂ community (single-maintainer-discoverability); the **5-of-9 topics enumerate the LE31 v1 stack envelope** = the strongest single on-stack-vocabulary reference of the 60-pass series; 77 KB tiny-repo size = single-file-implementability. |
| 3 | Practicability | ✅ | Python + the verbatim description *"Hosted multi-tenant mortgage refinance intelligence app with deterministic scoring, rate tracking, authentication, billing, alerts, and AI-generated explanation"* = a *6-primitive sextuple* that LE31 v1's existing stack *byte-for-byte matches* (Python + FastAPI + SQLModel + Postgres + HTMX-as-frontend-renderer + SaaS-shape = charter §3.1 stack), but the *multi-tenant SaaS posture* explicitly contradicts charter §3.1's *single-tenant + on-premise + French-only* invariant; any future v2 SaaS-variant-of-LE31 would need this multi-tenant shape. |
| 4 | Conflict | ⚠️ partial | MIT permissive; no §3.4 customer-facing-AI (the *"AI-generated explanation"* is **owner-facing**, NOT customer-facing — operator-tooling, charter §3.4-compatible); BUT the *multi-tenant + SaaS-deployment + Stripe-billing* posture is **OUT-OF-V1-SCOPE** per charter §3.1 invariant; the artifact is vocabulary-only and explicitly *deferred* to avoid breaking the v1 charter. |
| 5 | Outcome / appetite / scope | ✅ v1 / future-v2 | Reading-only artifact; no code today; out-of-v1-scope = the implementation requires explicit owner/charter sign-off for a v2 SaaS-variant. |
| 6 | Cost vs operational value | ✅ | Cheap to ingest (77 KB); vocabulary-only artifact. |
| 7 | Circuit breaker / reversibility | ✅ | Pure read-only research artifact. No installation, no import. |

**Decision: defer (parking-lot, vocabulary reference).** No build time spent. The cross-section reference is informative, not a v1 build-trigger. The verbatim description + the 6-primitive sextuple (multi-tenant + deterministic-scoring + rate-tracking + auth + Stripe-billing + alerts + AI-generated-explanation) + the 5-of-9 on-stack-vocabulary envelope are the load-bearing value.

## Files to touch

- **READ ONLY** (no files modified today):
  - `features/247-graydragon2-mortgage-intelligence-web-public-...md` (the vocabulary contract; READ for context)
  - `specs/247-graydragon2-mortgage-intelligence-web-public-sqlmodel-fastapi-htmx-multi-tenant-saas-stack-vocabulary-HANDOFF.md` (this file; READ for context)
- **No edits to** any LE31 v1 source code (the multi-tenant SaaS posture is explicitly out-of-v1-scope per charter §3.1), the `audit_logs` schema, the `StockEntry` schema, the waiter web UI, the cook Telegram bot, the Stripe integration (none added), the third-party-auth integration (none added), or the alert-system (none added).

## Verification protocol reference

Per `le31-conventions/SKILL.md` lines 82–90 (verification checklist):
- [ ] Evidence and confidence recorded. ✅ (MIT permissive + 0★ + 77 KB tiny + 2026-09-09 pushed + 2026-09-09 created + verbatim topics (8 of 9) + verbatim description = **observed event** for the push + **inferred** for the vocabulary transferability; confidence high for the on-stack-vocabulary-envelope / medium for the multi-tenant-transferability / high for the §3.4 owner-facing-AI-compatibility)
- [ ] All seven checks answered. ✅ (see table above; **Conflict = ⚠️ partial** to flag the multi-tenant + SaaS-deployment out-of-v1-scope posture)
- [ ] Decision is build / experiment / defer / reject. ✅ (`defer, parking-lot`)
- [ ] No unresolved source-of-truth conflict was guessed through. ✅ (6-primitive sextuple + on-stack-vocabulary envelope + verbatim description + partial-conflict (multi-tenant + SaaS out-of-v1-scope) all recorded)
- [ ] Observable behavior was exercised before claiming completion. ✅ (parent-verified against raw GitHub API JSON; license field + stars + size + topics (8/9) + description all verbatim; 2026-09-09 pushed + 2026-09-09 created confirmed by raw `created_at` + `pushed_at`)

## Rollback path

- **No code deployed → no rollback needed.** This is a vocabulary-only artifact; deleting the feature file `features/247-*.md` + this HANDOFF file `specs/247-*-HANDOFF.md` + the (blocked) Linear sub-issue is the complete rollback.
- **If a future v2 PR adopts the vocabulary**, the rollback path is: (1) drop the `tenants` + `tenant_users` + `tenant_subscriptions` SQLModel tables; (2) drop the `tenant_id` foreign-key column on every LE31 v1 table; (3) drop the `alert_rules` + `ai_explanations` SQLModel tables; (4) drop the `/alert <rule_name>` + `/explain <surface_id>` Telegram bot commands. All future rollbacks are explicit because the artifact is read-only.

## Mandatory LE31 skill list

For any future coding agent that picks up this contract, the mandatory skill load-out per `le31-coding-agent-brief/SKILL.md` is:
- `le31-conventions` — global decision layer; the seven-check gate
- `le31-v1-feature-pattern` — the v1 feature template (Goal / Scope / Out of scope / Description / Data model / Implementation steps / Telegram interaction / Dependencies / Open questions / Why this matters)
- `le31-data` — LE31 data-correctness rules
- `le31-backend` — FastAPI + SQLModel + Postgres conventions
- `le31-frontend` — HTMX + minimal HTML conventions (for any future owner-web-UI surface, e.g. the SaaS-variant multi-tenant dashboards)
- `le31-handoff-spec` — slice-contract authoring conventions
- `le31-coding-agent-brief` — paste-in prompt generation
- `le31-verification-protocol` — verification + rollback protocol
- `le31-quality-gates` — gates before merge
- `le31-arch-patterns` — FastAPI + aiogram + Postgres architectural patterns (including the multi-tenant SaaS-deployment + Stripe-billing + AI-generated-explanation disciplinary patterns)
- `le31-data-correctness` — decimal EUR, timezone-aware instants, append-only invariants

Today's parent (Daily Brainstorm Cron) only READ the relevant skill files; no LE31 source code was touched.
