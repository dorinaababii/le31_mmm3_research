# HANDOFF — Feature 396: a deterministic verifier that can answer "insufficient evidence" — giving §3.4's "observable evidence" a meaning

**This is a `defer` slice. There is no code to write today, and there is no Linear issue to hang it under (Linear MCP write endpoint blocked — 41st consecutive day).**

**The one-line reason it is `defer` and not `build`:** the policy governs a **claim**, and **LE31 has no AI-assisted claim surface today** — the unmade question *"does LE31 get any AI surface at all?"* is still unmade. This pick is filed so that **when that question is answered, §3.4's bar is already written down**, and — critically — **in the one form that needs no charter revision and no second model**.

**⭐ The distinction that makes this pick worth filing at all:** `ServiceWhy`'s verifier is **deterministic where it matters** — *"The model never recomputes numbers"* — and its rules V1–V5 are **thresholds in a table**, not prompts. Feature 63 (the second-opinion verifier) is **explicitly PARKING-LOT**, because a second *model* requires a charter revision under LE31's single-provider assumption. **A deterministic verifier needs neither.** This pick is deliberately scoped to the deterministic variant precisely so it does not inherit feature 63's blocker.

**Discovery chain:** Daily Research 2026-10-28 → the parent read the README of the in-window repo `KoangWy/servicewhy` (MIT, ★2, 2,737 KB, Python/FastAPI, created 2026-10-23, **pushed 2026-10-27T23:30:13Z**) whose verifier section gives five numbered threshold rules (V1 *"Every value recomputed by an independent second query … mismatch > ±2% → 🔴 block"*; V2 *"n < 15 blocks"*; V3 *"A causal claim needs a contrast"*; V5 *"> 2 rejections → ⚪ 'insufficient evidence'"*) and states ***"The model never recomputes numbers"*** → the parent then went and grepped **LE31's own tree** and found `grep -rn -i "observable evidence\|non-AI fallback" PROJECT_CHARTER.md features/ coding-agent/skills/` returns **citations of the phrase, never a definition of it** → so §3.4, the only clause in LE31's charter that permits AI at all, currently has **no operational meaning**, and any proposal claiming *"it's staff-facing, so §3.4 is satisfied"* is **unfalsifiable**.

**Full evidence record: `features/396-koangwy-servicewhy-mit-python-fastapi-react-restaurant-night-incident-explainer-planner-investigator-verifier-writer-evidence-cited-numbers-human-approval-v1-deterministic-verifier-and-insufficient-evidence-vocabulary.md`**

## Active feature path

`features/396-koangwy-servicewhy-mit-python-fastapi-react-restaurant-night-incident-explainer-planner-investigator-verifier-writer-evidence-cited-numbers-human-approval-v1-deterministic-verifier-and-insufficient-evidence-vocabulary.md` — **`defer`** (Pick C of Daily Research 2026-10-28).

## Seven-check gate verdict

| # | Check | Pass? | Note |
|---|-------|-------|------|
| 1 | Raison d'être / JTBD | ✓ **PASS** | *When LE31's §3.4 permits an AI assistant to staff, the owner wants a claim it can check, but struggles because "observable evidence" is defined nowhere in LE31, so that an AI suggestion can be refused rather than merely doubted.* Links to features **63**, **55**, **68**. **Pass as prior art for a standard, NOT as demand** — and the standard is the deliverable. |
| 2 | Viability | ✓ | A deterministic verifier that recomputes a number needs **no model, no API key, and no per-call cost** — the owner can run it offline. **No new role, no new surface, no admin.** **Pass.** |
| 3 | Practicability and confidence | ⚠ **CONDITIONAL** | MIT ✓, Python ✓, FastAPI ✓. **The named rabbit hole is the architecture**: the artifact runs on Zetaris federated SQL + the Meterless World Model + Nightshift as model provider — **all explicitly rejected**. The transferable part is a **three-line policy**, not a platform. Confidence: **medium** for the shape, **low** for LE31's need. |
| 4 | Conflict | ✓ | **None, provided the shape stays deterministic.** A *model-based* verifier would hit feature 63's parking-lot reason (LE31's single-provider assumption, a charter revision). **This pick is scoped to the deterministic variant so it does not need that revision.** §3.1's *"no customer-facing AI"* is not triggered: the artifact is staff-facing and touches no guest surface. |
| 5 | Outcome + appetite + scope | ✓ | v1 vocabulary, one paragraph. **Explicitly NOT in scope:** any second model or provider, any LLM integration of any kind, any customer-facing surface, any incident-management or root-cause feature (a **new owner-facing surface** under §3.1, needing its own charter decision and its own gate), any change to `backend/app/`, **the artifact's Zetaris / Meterless / Nightshift architecture (explicitly rejected)**, any pin bump. |
| 6 | Cost to operational value | ✓ | Near-zero cost; the value is that it gives §3.4 a **concrete meaning at zero model cost**. **The asymmetry that decides the ordering: cheap now (one paragraph); expensive after — if LE31's first AI-assisted claim ships without a written standard, the standard becomes whatever the first implementation happened to do, and §3.4 stays unfalsifiable.** ICE/RICE as vocabulary only. |
| 7 | Circuit breaker + reversibility | ✓ | A vocabulary note. **Fully reversible by deleting one file.** **Stop evidence:** the pre-flight below. **Review point:** when the AI-surface question is answered, re-read the contract. **Pre-mortem:** someone reads *"Verifier"* and thinks a second model is being proposed — **it is not; V1–V4 are code, and the model contributes only a `block`/`pass` judgement.** |

**Gate verdict: `defer`** — check 3 is conditional on the AI-surface question, and check 1 passes as prior art rather than as demand.

## Bucket

**v1** — Pick C of Daily Research 2026-10-28. Per `le31-feature-pipeline/SKILL.md` step 4 the matching project is **`le31 v1 — Core MVP` (P-HMM-3)**. Per `le31-feature-pipeline/SKILL.md` line 33, the parent confirmed with `list_projects` on **2026-10-28** that the workspace contains exactly three projects (`le31 v1 — Core MVP` P-HMM-3, `le31 Workflow` P-HMM-2, `le31 Research` P-HMM-1) and that **`le31 v2 owner-pains` / `le31 v2-AI` do not exist**. Because the **parent research issue for this pass also failed to create** (Linear MCP write endpoint blocked — **41st consecutive day**), there is no parent issue to hang the sub-issue under; the sub-issue is routed to **`le31 Research` (P-HMM-1)** in the fallback payload as the parent research issue's home, and **no project attachment actually occurred**. The `Feature` label id (`972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`) **was re-verified this pass** via `list_issue_labels`.

## Files to touch

**Today: none. This slice touches zero files outside `features/` and `specs/`.**

When the AI-surface question is answered, the files a future implementer would touch (recorded so the shape is not lost — **not** this slice's scope):

- `backend/app/services/` (or a verification module) — the **recompute-and-compare** function. **Pure code. No model call.** If you find yourself importing an LLM SDK here, **STOP — that is feature 63's shape, and it is parked.**
- `backend/app/models.py` — **no new model**, unless a future proposal decides that claims need to be **stored**. If it does, that is a **separate** proposal with its own gate — **not** this slice.
- `backend/app/routers/` — the **refusal** must be visible on the surface that made the claim. **Do not add a new router**; a new owner-facing surface is a **separate charter decision**.
- `backend/app/bot/cook_bot.py` — **no new command, no new output.**
- `backend/requirements.txt` — **no dependency change.** In particular **no LLM provider SDK** — that is the entire point of the deterministic variant.
- `PROJECT_CHARTER.md` — **if** §3.4's *"observable evidence"* is formally defined, **that is the natural home** — and it is **this slice's most likely eventual deliverable**, because the phrase is currently cited in five places and defined in none.

**Do NOT touch (out of scope, explicitly):**

- **Any LLM / model / provider integration of any kind.** No Anthropic, OpenAI, Mistral, local model, or agent framework. **The deterministic variant needs none.**
- Any **second-model** verifier — **feature 63**, explicitly PARKING-LOT.
- Any **customer-facing** surface — §3.1 forbids customer-facing AI outright.
- Any **incident-management / root-cause / "why did tonight go wrong"** feature — a new owner-facing surface under §3.1.
- `backend/app/models.py` — any new claim/evidence table, without its own gated proposal.
- The FastAPI / SQLAlchemy / SQLModel / Postgres pins.
- Features 30 / 47 / 49 / 50 / 55 (append-only audit and the evidence-review surface) — **read** them; do not re-implement them.

### ⭐ Architecture rejection (recorded so this is not mistaken for an architecture recommendation)

`ServiceWhy` runs on **Zetaris** (federated SQL across Postgres + Parquet on MinIO), the **Meterless World Model** (an append-only, replayable store with content-hash ids), and **Meterless Nightshift** as the model provider, with runs bounded at *"at most 3 hypotheses, 2 retries each, 12 investigate+verify steps per run, 60 s per model call and 40 model calls per run."*

**None of that transfers to LE31**, and copying any of it would be a serious error: LE31 is **one restaurant, one Postgres, one service**, and §3.5 fixes the stack. **The transferable part is a three-line policy — recompute, compare, block or answer "insufficient evidence" — not a platform.**

## The load-bearing checks (for the future implementer — none of these run today)

1. **The recomputation is independent and in code** — assert the verifier's number is rebuilt from **named raw rows**, not read back from the claim. **A verifier that reads the claim's own number is not a verifier.**
2. **A claim can be REFUSED, not merely annotated** — assert that a claim failing the threshold produces a **block**, and that the blocked claim does **not** appear in the output as an assertion.
3. **"Insufficient evidence" is a legitimate, reachable outcome** — assert that exhausting the retry budget produces that answer rather than a smaller-confidence assertion. **This is the property that makes §3.4 falsifiable.**
4. **No model call occurs in the recomputation path** — assert the verification path makes **zero** LLM requests. **This is what keeps the feature off feature 63's charter blocker.**
5. **The tolerance is a money tolerance, not a percentage** — §3.6 requires `Decimal`, never float; the comparison must not introduce a float rounding step.
6. **The human still approves** — assert that any recommended action requires an explicit approve/reject and that the decision is logged with role and timestamp (the artifact's `POST /findings/{id}/approve|reject` pattern).
7. **Thresholds are frozen before results are seen** — the artifact's discipline: *"from it on, the thresholds, those prompts and the simulator parameters do not change."*

## Verification protocol reference

- **`coding-agent/skills/le31-verification-protocol/SKILL.md`** — the general protocol for exercising behaviour, not asserting it.
- **`coding-agent/skills/le31-quality-gates/SKILL.md`** — the quality gates this slice must pass **when it is built**.
- **`coding-agent/skills/le31-data-correctness/SKILL.md`** — mandatory if the verification path touches money (§3.6).
- **`coding-agent/skills/le31-cook-bot-ux/SKILL.md`** — mandatory if a refusal surfaces on the cook bot (it does not today).
- **`skills/le31-conventions/SKILL.md`** — the seven-check gate and the *"research novelty is not user demand"* pitfall.

**The definition of done for this slice, as it stands: the document exists, the standard is stated, and nothing else was done.** That is the correct outcome for a `defer` pick.

## Rollback path

**Nothing to roll back.** This slice adds:

- One Markdown file under `features/` (the contract).
- One Markdown file under `specs/` (this handoff).
- One row in `/opt/data/INDEX.md`.

**All three are reversible by deletion, and none of them is referenced by running code.** No database change, no schema change, no dependency, no configuration. **No data is destroyed by removing them.**

**If the slice is later built**, the rollback is: drop the verification module and return the call sites to their prior form. **The one irreversible thing is any claim already published without a standard behind it** — which is why the standard should be written **before** the first AI-assisted claim, not after.

## Trigger condition

This slice activates when **any** of the following becomes true:

1. **The owner decides whether LE31 gets any AI surface at all.** **This is the primary trigger** — the unmade question surfaced on features 352, 354, 367 and now again here. **This pick is filed so the decision, when made, has a ready-made §3.4 standard to meet.**
2. **A PR proposes an AI-assisted claim** of any kind — an assistant, a summary, a recommendation, an explanation. **If you are reading this because you are about to write one, STOP and read the feature contract first.**
3. **A PR adds a second-model verifier** — **feature 63**, and its charter blocker still applies. **This pick is the deterministic alternative; it does not remove feature 63's blocker, it sidesteps it.**
4. **§3.4's "observable evidence" is formally defined** anywhere in LE31 — check for drift against this contract.
5. **A PR adds an owner-facing third surface** — a §3.1 surface-count question that needs its own charter decision and its own gate.

## Mandatory LE31 skill list

The external agent **must** load these before acting:

1. **`skills/le31-conventions/SKILL.md`** — the seven-check gate, the hard invariants (§3.4 and §3.1 especially), and the *"research novelty is not user demand"* pitfall. **Read first.**
2. **`skills/le31-v1-feature-pattern/SKILL.md`** — the v1 contract shape and slicing rules.
3. **`skills/le31-handoff-spec/SKILL.md`** — the handoff package discipline.
4. **`coding-agent/skills/le31-verification-protocol/SKILL.md`** — how to *exercise* the behaviour rather than assert it.
5. **`coding-agent/skills/le31-quality-gates/SKILL.md`** — the gates this slice must pass when built.
6. **`coding-agent/skills/le31-data-correctness/SKILL.md`** — mandatory if money enters the verification path.
7. **`coding-agent/skills/le31-conventions-coder/SKILL.md`** — coding conventions.
8. **`skills/le31-research/SKILL.md`** — to understand what was and was not established by the research pass.

## Read-first ordering (a stranger must be able to act from this package alone)

1. `features/396-...-v1-deterministic-verifier-and-insufficient-evidence-vocabulary.md` — **the contract**, including the explicit non-duplication argument against features 63, 55 and 68.
2. `features/63-second-opinion-verifier-role.md` — **the closest neighbour, and the one this pick must NOT be confused with.** Read to see the deterministic-vs-model distinction and the charter blocker that applies to the model variant only.
3. `features/55-evidence-review-surface.md` — the *visibility* half (shows a human the evidence row).
4. `features/68-cook-assistant-deterministic-gate.md` — the *write-gating* half.
5. `/opt/data/le31-daily-research-2026-10-28.md` — the full report.

## Linear reference

- **Parent research issue:** **not created** — Linear MCP write endpoint blocked (**41st consecutive day**, HTTP 400 `invalid_request` *"You've exceeded the free issue limit for this workspace"*; two write probes, requestIds `a51808a5284dd349` and `a51808cf1e574e32`, **both failed before any write**).
- **Sub-issue:** **not created** — same blocker. **Intended:** project `le31 Research` (P-HMM-1), state `Backlog`, label `Feature` (`972f1a1c-5e66-488c-923f-f6a4ea3ef2bb`, re-verified this pass).
- **Fallback payload:** `/opt/data/le31-daily-research-2026-10-28.linear-fallback.json`.
- **Read endpoints were verified reachable** on 2026-10-28: `list_projects` (3 projects), `list_issue_statuses` (`Done` = `449bbe45-5f5b-40f6-9d6c-ec69ba432ffc`), `list_issue_labels` (`Feature`), `list_issues` (confirms no 2026-10-28 issue exists).
