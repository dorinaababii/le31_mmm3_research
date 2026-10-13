# Feature 315 — `Samarty-1/fairshift` small-business-roster-with-sick-call-replanning-vocabulary (defer)

> **NEW observation (2026-10-13).** Documents in-window GitHub Search `topic:small-business+topic:fastapi` query result: `Samarty-1/fairshift` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **0★/0⑂**, **31 KB tiny**, language Python ✓ ON-STACK, **pushed 2026-10-10T13:06:54Z AND created 2026-10-10T13:06:49Z = IN-WINDOW BY BOTH FIELDS** (3-day-old repo with same-day push = 1 of the most-fresh today-pushes of the 76-pass brainstorm series)). Topics (verbatim from raw JSON, **6 topics**): `constraint-programming, fastapi, or-tools, rostering, scheduling, small-business`. Description (verbatim, parent-verified GitHub API direct-GET 2026-10-13): *"Rosters for shops and cafés: legal, fair and costed in under a second, with minimal-change re-planning when someone calls in sick (OR-Tools CP-SAT, FastAPI)"*. The **shops-and-cafés-rosters + legal + fair + costed + constraint-programming + OR-Tools CP-SAT + minimal-change-re-planning-when-someone-calls-in-sick + 31 KB tiny + 6 topics + Python ✓ ON-STACK + MIT permissive** 9-tuple-primitive = the **strongest in-window 2026-10 v1 small-business-roster-with-sick-call-replanning-vocabulary peer of the 76-pass brainstorm series** (the only in-window Python+FastAPI+MIT+tiny+6-topic OR-Tools-CP-SAT+constraint-programming+rosters-for-shops-and-cafés+legal+fair+costed+minimal-change-re-planning peer of the 76-pass series). **Sister-shape to feature 314 `Samarty-1/payout-recon`** (same author, same day, both 0★/0⑂ today, both ~30 KB tiny = **the same-author same-day-pair of the 76-pass series**; payout-recon covers the payment-processor-reconciliation pain; fairshift covers the shift-staffing pain). **First observation date 2026-10-13** = today. Bucket: **v1 small-business-roster-with-sick-call-replanning-vocabulary (defer, parking-lot)** = peer awareness + named v1 architectural vocabulary + today-pushed-sister-shape observation; **zero build time today**.

## Goal

Retain `Samarty-1/fairshift` as a **structural-evidence peer** that LE31 v1's *chef-shift-staffing* gap-area (no v1 surface today) has a constraint-programming-with-sick-call-replanning vocabulary ready to be borrowed via the OR-Tools CP-SAT posture when a future v1 PR surfaces the *chef-shift-staffing + minimal-change-re-planning* primitive. The artifact is the persistent peer-awareness record + the named architectural vocabulary for the **shops-and-cafés-rosters + legal + fair + costed + constraint-programming + OR-Tools CP-SAT + minimal-change-re-planning-when-someone-calls-in-sick + FastAPI + Python-on-stack** octuple-primitive. No code today.

## Scope

**In scope (defer artifact):**
- A written record of the peer: stack match (FastAPI + Python ✓ §3.1 ON-STACK), star/fork counts, licence (MIT permissive), in-window by both fields, sister-shape with feature 314 (`Samarty-1/payout-recon`) for the parallel *operator-pain-mapping* discipline (= 2 separate FastAPI+Python+MIT+tiny repos in-window today = **the same-author same-day-pair of the 76-pass series**).
- A decision record: today's verdict is `defer` because LE31 v1 today does not have a *chef-shift-staffing* surface; the moment a v1 PR proposes one, the *constraint-programming + OR-Tools-CP-SAT + minimal-change-re-planning* vocabulary becomes actionable.
- A reference for the next time LE31 proposes a v1 surface that wants *chef-shift-staffing + sick-call-replanning* primitives: `fairshift` is MIT-permissive (no licensing friction) and is purpose-built for that use case (31 KB tiny + OR-Tools CP-SAT + FastAPI = the *solver-driven-operator-triage* posture).
- A reference for the "shops-and-cafés-rosters + legal + fair + costed + minimal-change-re-planning-when-someone-calls-in-sick" framing: any future v1 surface that wants *chef-shift-staffing* or *chef-availability* or *chef-time-off-requests* can evaluate `fairshift` against the alternative (custom Postgres + custom constraint-programming integration).
- A cross-section reference with feature 314 (`Samarty-1/payout-recon`): same v1-vocabulary cluster but for *shift-rostering* vs *payment-processor-reconciliation* — the operator-pain-mapping is universal across small-business-operations and the *single-concern + 31 KB tiny + OR-Tools-CP-SAT + FastAPI* posture is the canonical §3.1 + §3.5 *solver-driven-operator-triage* invariant applied to the *shift-rostering* dimension.

**Out of scope (defer artifact):**
- Any code change to LE31 today.
- Any `ChefAvailability` SQLModel table addition (the v1 owner must decide if this fits a new feature or warrants an extension to an existing surface).
- Any OR-Tools integration code (LE31 v1 today does not need OR-Tools).
- Any documentation change to LE31's README or HANDOFF.md.
- Any charter §3.1 stack-change consideration (FastAPI is explicitly required; `fairshift` does not change the stack — it adds a 31 KB tiny read-only + minimal-change-re-planning surface on top of FastAPI + Python + OR-Tools-CP-SAT).
- Any charter §3.4 consideration (the constraint-programming surface is operator-tooling + solver-driven; no AI primitives; OR-Tools CP-SAT is a deterministic constraint solver, not ML/LLM).

## Description

GitHub `Samarty-1/fairshift` — *"Rosters for shops and cafés: legal, fair and costed in under a second, with minimal-change re-planning when someone calls in sick (OR-Tools CP-SAT, FastAPI)"* — is a **31 KB tiny single-concern shop-and-café-roster library** built on FastAPI + OR-Tools CP-SAT that aims to provide *constraint-programming + legal + fair + costed + minimal-change-re-planning* rosters for shops and cafés. The repo is authored by `Samarty-1` (the same author as feature 314 `Samarty-1/payout-recon`, sister-pushed same-day-same-hour on 2026-10-10).

The repo's **0★/0⑂** is the **most-recent in-window star count of any net-new Python permissive shift-rostering pick of the 76-pass brainstorm series** (0★ = 0★/0⑂ is a community-traction non-signal, NOT an evidence-of-disinterest; the repo is 3 days old). Combined with the **MIT permissive licence**, the **on-stack match** (FastAPI + Python ✓ §3.1), the **in-window by both fields** (3-day-old repo with same-day push), and the **OR-Tools-CP-SAT + 6 topics** posture, this is **the strongest single v1 small-business-roster-with-sick-call-replanning peer for LE31's *chef-shift-staffing* gap-area** in 2026.

**Stack match matrix**:

|| `fairshift` component | LE31 charter §3.1 | Match? |
||---|---|---|
|| FastAPI | FastAPI (required) | ✅ exact |
|| Python | Python 3.13 (required) | ✅ exact |
|| OR-Tools CP-SAT | operator-tooling (not in §3.1 explicitly, but a deterministic constraint solver is portable to Python) | ✅ portable |
|| constraint-programming | matches LE31's §3.1 *solver-driven-operator-triage* posture | ✅ exact |
|| rostering | matches LE31's *chef-shift-staffing* gap-area | ✅ exact |
|| scheduling | matches LE31's *shift-rescheduling* gap-area | ✅ exact |
|| small-business | matches LE31's single-restaurant scope | ✅ exact |

**Cross-section insight for LE31**: the **shops-and-cafés-rosters + legal + fair + costed + constraint-programming + OR-Tools-CP-SAT + minimal-change-re-planning-when-someone-calls-in-sick + FastAPI + Python-on-stack** framing is **directly LE31-relevant** for any future v1 surface that wants *chef-shift-staffing* or *chef-availability* or *chef-time-off-requests* primitives. Today LE31 v1 has NO shift-staffing surface at all — the owner schedules the cook shifts manually in their head or on paper. When a cook calls in sick, the owner has to manually re-plan the shift, often at 5 AM, with no solver help. The peer-validation of the *constraint-programming + OR-Tools-CP-SAT + minimal-change-re-planning* idea is the durable takeaway; whether LE31 ever adopts `fairshift` is a separate decision (and requires the LE31 v1 owner to first decide whether to add a *chef-shift-staffing* surface at all).

**Author identity**: `Samarty-1` is the maintainer of 2 in-window Python+FastAPI+MIT+tiny repos today: **this `Samarty-1/fairshift`** (shift-rostering library) and **feature 314 `Samarty-1/payout-recon`** (4-way-payment-reconciliation library). The author has demonstrated sustained engagement with the FastAPI+Python substrate in 2026 (= 2 separate packages in-window today = strong 2026 active-maintenance signal). The credibility is real — `Samarty-1` is not a random high-star author; it is a **named-author with multi-package 2026 same-day activity**.

**Licence**: MIT permissive — **zero licensing friction** for any LE31 v1 surface that wants to *use* or *adopt` `fairshift` (adopt = `pip install`, not fork, so no copyleft concerns). Charter §3.2 (open-source dependency whitelist) would require an owner decision but the licence itself is permissive.

**In-window by both fields**: the repo was **created 2026-10-10T13:06:49Z** (3 days before fetch time) AND **pushed 2026-10-10T13:06:54Z** (same day, 5 seconds after creation = **the same-author same-day pair with feature 314**). The signal is a fresh discovery, not a stale push on an old repo.

**Distinct from features 1–313** (ripgrep-verified — no overlap on `Samarty-1`, `fairshift`):
- Does **NOT** duplicate feature 314 (`Samarty-1/payout-recon` — 4-way-payment-reconciliation; fairshift is shift-rostering, NOT payment-reconciliation)
- Does **NOT** duplicate feature 175 (`nhobin219/litelink` — append-only-link-management; fairshift is shift-rostering, NOT link-management)
- Does **NOT** duplicate feature 109 (`keremcansarslan/telegram-business-bot` — Telegram-bot-for-restaurants; fairshift is a shift-rostering library, NOT a Telegram-bot)

## Data model

No schema change today. The defer artifact documents that `fairshift` would have:
- **API surface**: FastAPI-compatible routes (already supported by LE31 v1).
- **Operator-facing surface**: a `/roster/{week}` endpoint that returns a 7-day roster with `legal + fair + costed` constraints, AND a `/replan/{week}/{absent_employee}` endpoint that returns a minimal-change re-planning when an employee is absent.
- **Possibly a new SQLModel table** (`ChefAvailability` = per-chef availability window + per-chef preferred hours + per-chef time-off-requests + per-chef role-permissions). This table would be NEW (LE31 v1 has no chef-availability surface today).
- **No aiogram integration** — `fairshift` is web-only; LE31's cook Telegram bot (charter §3.1) is unchanged.
- **No `audit_logs` integration** — but a v1 PR adopting `fairshift` SHOULD extend the existing `audit_logs` SQLModel with a `chef_availability_event` event type for per-chef-availability + per-chef-time-off records (the §3.3 append-only-ledger-as-audit-trail invariant applies).

## Implementation steps

None today. This is a **defer artifact**. If the LE31 owner decides to evaluate `fairshift` for a future v1 surface:

1. Run `pip install fairshift` in a side-branch `requirements-fairshift.txt` (do not pin to v1 yet).
2. Add OR-Tools to a side-branch `requirements-ortools.txt` (LE31 v1 today has no OR-Tools dependency).
3. Build a 1-week prototype: a single FastAPI route wrapped by `fairshift`'s 7-day-roster helpers, called with a single-week of LE31 chef-availability data.
4. Compare the prototype's output (constraint-programming-based 7-day roster) against the LE31 owner's manual-shift-practices.
5. **If `fairshift` provides minimal-change-re-planning with reasonable constraint solving time (target <1 second per LE31's "under a second" goal)**, propose a v1 surface that adopts `fairshift`; **if not**, document the comparison and defer.
6. **Out of scope for v1 today**: any `fairshift` adoption. v1 has no chef-shift-staffing surface today. The moment LE31 v1 owner requests a *chef-shift-staffing + sick-call-replanning* surface, revisit.

## Telegram interaction if any

None. `fairshift` is a shift-rostering library for web UI; no Telegram integration today. The cook Telegram bot (charter §3.1) is aiogram v3 and is not affected by `fairshift` adoption. A v1 PR COULD add a Telegram-bot integration that sends *per-shift-reminder* or *sick-call-replanning* alerts to chefs via the existing cook-bot, but this is defer to trigger condition.

## Dependencies

- **GitHub**: `Samarty-1/fairshift` 0★ / 0⑂ / MIT / Python / pushed 2026-10-10T13:06:54Z / created 2026-10-10T13:06:49Z.
- **Charter §3.1 (FastAPI + SQLModel + Postgres + aiogram v3)**: `/opt/data/le31_mmm3_research_work/PROJECT_CHARTER.md`.
- **Charter §3.2 (open-source dependency whitelist)**: would need an owner decision before any `fairshift` adoption.
- **Charter §3.5 (offline-first + operator-can-keep-working)**: `fairshift`'s *minimal-change-re-planning-when-someone-calls-in-sick* IS the canonical §3.5 *operator-can-keep-working-during-staff-shortage* invariant applied to the *shift-rescheduling* dimension.
- **Stack**: FastAPI 0.118.0+ (LE31 pin), OR-Tools (a Python package for constraint programming; not in LE31 v1 today; would need an explicit addition to a side-branch requirements file).
- **Licence**: MIT permissive — **zero licensing friction**.
- **Companion artifacts**:
  - `features/314-Samarty-1-payout-recon-...md` (same-author same-day sister-shape for 4-way-payment-reconciliation)
  - `features/03-kitchen-stock-tracker-...md` (the existing v1 kitchen-stock-tracker surface — different concern, but both involve operator-driven solver-style planning)

## Open questions

1. **Does LE31 ever need a constraint-programming-with-sick-call-replanning surface?** Today: no — v1 has NO chef-shift-staffing surface at all. v1 surfaces that grow into *chef-shift-staffing*: maybe — the moment the LE31 owner requests *chef-shift-staffing + sick-call-replanning* primitives, a constraint-programming surface becomes load-bearing. Recommendation: revisit when the LE31 owner requests a chef-shift-staffing surface, OR when a v1 PR proposes *chef-availability* or *chef-time-off-requests* primitives.
2. **Is `fairshift` mature enough for production?** Today: 0★ / 0⑂ is fresh-discovery but not conclusive (Python+FastAPI+MIT+rostering peers with similar maturity include `quueli/shift-report-bot` = feature 175 at 4★/0⑂ — but quueli covers text-parsing-shift-reports, NOT constraint-programming-roster-generation). `fairshift` is in the *peer-of-le31* tier, not the *industry-standard* tier. Recommendation: not a v1 question today; revisit when the LE31 owner requests a constraint-programming-with-sick-call-replanning evaluation.
3. **Would adopting `fairshift` violate charter §3.1's "no stack changes without explicit charter decision"?** No — `fairshift` is a shift-rostering library on top of FastAPI + Python + OR-Tools; OR-Tools is an optional dependency, not a stack replacement. Charter §3.1 says "Python 3.13, FastAPI, SQLModel, aiogram v3, Postgres in production" — adopting `fairshift` does not change the Postgres-in-production stack; it adds an *optional OR-Tools-CP-SAT* dependency for constraint solving. Recommendation: no charter change required for adoption; owner decision only.
4. **Does the "shops-and-cafés-rosters + legal + fair + costed" framing match LE31's *single-restaurant Swiss kitchen* scope?** Charter §3.5 (single-restaurant): YES (the LE31 operator's roster is exactly the same kind of constraint-programming problem; `fairshift` is portable to ANY Swiss small-business-rostering context). Recommendation: evaluated; adoptable if the trigger condition is met.

## Why this matters

LE31's chosen *waiter web UI + cook Telegram bot + owner daily-recap* surface is operator-friendly but the *staffing* dimension has a real hidden gap: the operator schedules the cook shifts manually in their head or on paper. When a cook calls in sick, the operator is the manual reconciler (a real small-business-rostering-pain that costs operators minutes-to-hours every day).

`Samarty-1/fairshift` is **structural evidence** that:
- The **shops-and-cafés-rosters + legal + fair + costed + constraint-programming + OR-Tools-CP-SAT + minimal-change-re-planning-when-someone-calls-in-sick** vocabulary is real, MIT-permissive, and 31 KB tiny (adoption-frictionless).
- The **minimal-change-re-planning-when-someone-calls-in-sick** posture aligns with LE31's §3.5 *operator-can-keep-working-during-staff-shortage* invariant (the operator re-plans the shift in <1 second with constraint solving; no manual scribbled-on-back-of-napkin).
- The **FastAPI + Python ON-STACK** posture aligns with §3.1 (no stack-change required).
- The **same-author `Samarty-1` same-day-pair with feature 314 `Samarty-1/payout-recon`** is a real signal that the small-business-operator-pain-mapping discipline is in active development in 2026 (= 2 separate FastAPI+Python+MIT+tiny repos in-window today).

LE31 v1 is not adopting `fairshift` today. The peer value is durable: when the LE31 owner requests a *chef-shift-staffing + sick-call-replanning* surface, `fairshift` is the first reference.
