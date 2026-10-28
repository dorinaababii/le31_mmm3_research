# Feature 396 — `ServiceWhy`: a deterministic verifier that can answer "insufficient evidence" — giving §3.4's "observable evidence" a meaning

> **Pick C of Daily Research 2026-10-28 (90th pass).** Documents in-window GitHub repo `KoangWy/servicewhy` (**MIT ✓ §3.2 STRICTLY-COMPATIBLE**, **★2/⑂0 — no traction evidence in either direction**, **2,737 KB**, **Python ✓ + FastAPI ✓ ON-STACK**, created **2026-10-23T17:35:30Z AND pushed 2026-10-27T23:30:13Z = IN-WINDOW BY BOTH FIELDS**, 10 topics `['agents','ai-agents','explainability','fastapi','hackathon','meterless','nemotron','react','restaurant','zetaris']`, `default_branch=main`, `archived=false`, `fork=false`, 0 open issues). All field values read from a **direct `/repos/` GET** by the parent on 2026-10-28 (`/tmp/le31-daily-2026-10-28/gh/pv/KoangWy__servicewhy.json`), **not from search-result numbers**. Description (verbatim): *"ServiceWhy: an agent that explains why a restaurant night went wrong. Planner, Investigator, Verifier and Writer over Zetaris federated SQL, Meterless World Model and Nightshift. No receipt, no claim. Synthetic data."*
>
> **The README was read** (parent, 2026-10-28, `/tmp/le31-daily-2026-10-28/gh/readmes/KoangWy__servicewhy.md`). The decisive claim is quoted below: ***"The model never recomputes numbers."*** The verifier's rules V1–V5 are a **deterministic table of thresholds**, and the model contributes only a `block`/`pass` judgment — never a recomputation.
>
> Bucket: **v1**. Verdict: **`defer`** (vocabulary only). **0 build time.**

## Goal

Give LE31's §3.4 the phrase *"observable evidence"* a **concrete, implementable meaning** — without a second model, without a charter revision, and without any customer-facing AI.

The concrete outcome: **one document stating the three-line policy — recompute, compare, then *block* or answer *"insufficient evidence"* — and recording that a claim which cannot be recomputed must be answerable as "not enough evidence" rather than asserted.**

## Scope

**In scope (v1, defer):**

- **One document** recording the deterministic-verifier policy, with the verbatim V1–V5 rule table, the source URL, and the LE31-side vocabulary each rule names.
- **One explicit statement of the distinction** from LE31's three existing neighbouring features (63, 55, 68) — **none of which is a deterministic verifier** — so that this pick is not mistaken for a duplicate.
- **One explicit statement that this pick needs no charter revision**, because it is deliberately scoped to the **non-model** variant.

**Explicitly NOT in scope:**

- **Any second model, second provider, or multi-model orchestration.** Feature 63's parking-lot reason stands and is unaffected.
- **Any LLM integration of any kind.** No provider SDK, no prompt, no model call. **The deterministic variant needs none.**
- **Any customer-facing surface.** §3.1 forbids customer-facing AI outright, and this feature touches no guest-facing surface at all.
- **Any incident-management, root-cause, or "why did tonight go wrong" feature.** That is a **new owner-facing surface** (LE31 §3.1 names exactly two: waiter web UI, cook Telegram bot) and would need its own charter decision and its own gate run. **This feature does not create it.**
- **Any change to `backend/app/`.** Zero lines of application code change.
- **Any adoption of `ServiceWhy`'s architecture** — Zetaris federated SQL, the Meterless World Model, Nightshift as the model provider. **Explicitly rejected**; only the policy transfers.
- **Any change to the FastAPI / SQLModel / Postgres pins.**

## Description

### What `ServiceWhy` actually is

An **Open Agent Hackathon 2026 Track 02** entry (Team Irigo): *"an agent that explains why a restaurant night went wrong"*. A restaurant manager asks *"Why did Saturday dinner revenue drop 18%?"* and gets an evidence-backed answer assembled from POS tickets, table-service events, shift rosters and guest reviews, by four roles — **Planner → Investigator → Verifier → Writer**.

**There is no traction claim here and none is made.** ★2, 0 open issues, a hackathon entry, and the README states its own limits plainly: *"**All data is synthetic.** A seeded discrete-event simulator generates every guest, ticket, shift and review."* The banner says it: *"**No receipt, no claim.**"*

### The differentiator — and it is a *determinism* differentiator, not a model one

The README's own section header is *"The verifier (the differentiator)"*, and the reason it is a differentiator is **not** that a model verifies another model. It is the opposite:

> *"Applies the deterministic rules V1–V5 below, then one structured model judgment (`block`/`pass` plus a reason) that the claim matches what was measured: it blocks a claim whose metric or direction does not match, or that names a cause the data never recorded. **The model never recomputes numbers.**"*

The five rules are **thresholds in a table**, not prompts:

| # | Rule | Threshold | Action |
|---|---|---|---|
| V1 | Every value recomputed by an independent second query through the same federated surface: raw rows aggregated in code, with revenue rebuilt from `ticket_items` | mismatch > ±2% | 🔴 block |
| V2 | Minimum sample per segment | n < 15 blocks; 15 ≤ n < 30 downgrades confidence | 🔴 block · 🟡 downgrade |
| V3 | A causal claim needs a contrast (baseline group present) | none found | 🔴 block |
| V4 | Decoy split: how much of a revenue change fewer parties explain vs revenue per party | volume share ≥ 50% | 🟡 downgrade service findings and force the split into the answer |
| V5 | Retry budget | > 2 rejections | ⚪ **"insufficient evidence"** |

**Three properties of this table are the transferable ones, and each is directly useful to LE31:**

1. **The recomputation is independent and in code** (V1: *"raw rows aggregated in code"*, *"revenue rebuilt from `ticket_items`"*). It is not a second opinion; it is a **second derivation from the same data**. A number that cannot be rebuilt from raw rows is a number that cannot be trusted.
2. **Blocking is a first-class outcome** (🔴 block). A claim can be *refused*, not merely annotated.
3. **"Insufficient evidence" is a legitimate answer** (V5). After the retry budget is exhausted, the system does not lower its standards and guess — it **declines to answer**. This is the single most important line for LE31, because it is the operational form of §3.4's *"observable evidence"*: **a claim either has evidence you can point at, or it has none and must not be made.**

And the model's role is explicitly *bounded and secondary*: it contributes a **`block`/`pass` judgment plus a reason**, it **never recomputes numbers**, and any confounders that remain are *"stated as the finding's uncertainty and left to the manager's approval"*. The human still approves: *"The manager approves or rejects every recommended action (`POST /findings/{id}/approve|reject`), and each decision is logged with role and timestamp."*

### ⭐ LE31's §3.4 says "observable evidence" and never defines it

Parent-verified on 2026-10-28:

```
$ grep -rn -i "observable evidence\|non-AI fallback" PROJECT_CHARTER.md features/ coding-agent/skills/
```

The hits are **citations of the phrase**, not definitions of it — `features/145`, `features/297`, `features/62`, `features/68`, `features/231` all *name* §3.4's requirement and then apply it differently. **Nowhere in LE31 is there a rule of the form "a claim must be recomputable from named rows, and if it is not, the answer is 'insufficient evidence'."**

`ServiceWhy` is the **first external artifact in this series** to supply that rule in an implementable form that requires **no model at all** — V1 through V4 are pure code.

### ⭐ Why this is NOT a duplicate of the three existing neighbours

This is the most important part of this feature, and the reason it is filed at all.

| Existing feature | What it is | Why it is **not** this |
|---|---|---|
| **63** — second-opinion verifier | *"an **independent verifier model** reads the proposal plus its evidence card and writes a `VerificationReport(approve\|reject\|insufficient_evidence, rationale)` before the owner sees the proposal — gated on a charter revision authorising multi-model orchestration."* | It is a **second model**. LE31's stack assumes one LLM provider at most, so it is explicitly **PARKING-LOT** and blocked on a charter revision. **`ServiceWhy`'s V1–V4 need no second model** — they are thresholds in code. This pick is **deliberately scoped to the deterministic variant so it does not inherit feature 63's blocker.** |
| **55** — evidence review surface | *"an owner-facing evidence-review surface over the existing append-only ledger — 'show me the receipts'"*, composing features 30 + 47 + 49 + 50 into one Telegram surface answering *"what claim is *this* LE31 push backed by, and where is the evidence row?"* | It **shows a human the evidence row**. It **recomputes nothing** and **refuses nothing**. A receipt that is wrong is still displayed as a receipt. This feature is about the claim being **refusable**, not about the evidence being **visible**. |
| **68** — cook-assistant deterministic gate | An `AssistantProposal` table the v2-AI cook-assistant writes **before** any `StockEntry` is committed, which *"then runs the same deterministic gate the typed `/86 <item>` path enforces"*. | It gates **whether a proposed stock write may be committed**. It does **not** verify that a *claim about the business* is supported by the numbers it cites. |

**A deterministic, non-model verifier that recomputes a number and can refuse a claim — and whose answer to an unbackable claim is "insufficient evidence" — is none of the three.** They are adjacent, and they are compatible; none of them occupies this slot.

### The honesty is the part worth keeping

`ServiceWhy` is unusually careful about its own limits, and that is what makes it citable:

- *"**All data is synthetic.**"* — stated at the top, with a badge, and *"every UI screen says so."*
- *"**The published 8/10 is therefore an in-sample number** (same seed, same ten questions), not a held-out test."* — a published scorecard that states its own methodological weakness.
- *"The thresholds are initial values, tuned in one pass on real runs **before the feature freeze**"* — and then it names the freeze commit (`29cdff1`, 2026-10-27) and says *"from it on, the thresholds, those prompts and the simulator parameters do not change."*
- *"simulator ground truth was never an input to it"* — the tuning did not peek at the answer key.
- *"It never moves money"* is `settlewise`'s line, but the same discipline is visible here: *"The manager approves or rejects every recommended action."*

**The threshold-freezing discipline in particular is a candidate LE31 practice**: a verifier whose thresholds can be tuned after seeing the results is not a verifier. Recording it.

### The architecture is explicitly rejected

`ServiceWhy` runs on **Zetaris** (federated SQL across Postgres + Parquet on MinIO, with *"lightning database"* registrations), the **Meterless World Model** (an append-only, replayable store with content-hash ids, *"our own implementation of the Meterless reference architecture"*), and **Meterless Nightshift** as the model provider (an OpenAI-compatible endpoint). Its runs are bounded at *"at most 3 hypotheses, 2 retries each, 12 investigate+verify steps per run, 60 s per model call and 40 model calls per run."*

**None of that transfers to LE31**, and copying any of it would be a serious error: LE31 is **one restaurant, one Postgres, one service**, and its §3.5 fixes the stack. **The transferable part is a three-line policy, not a platform.** The federated-SQL layer would be a *new architecture*; the World Model would be a *new persistence concept*; Nightshift would be a *new provider* — all rejected.

## Data model

**No data model change. This feature changes zero lines of `backend/app/models.py`.**

The *shape* it is recording — **explicitly not proposed as an implementation today**:

```
A claim carries:
  - the evidence rows it rests on   (named, not summarised)
  - the derivation that produced its number
Verification is:
  1. recompute   -- rebuild the number from the named rows, in code
  2. compare     -- |recomputed - claimed| within tolerance?
  3. block       -- no => the claim is REFUSED (not annotated)
  4. insufficient -- out of retry budget => answer "insufficient evidence"
```

**The open question this feature deliberately does not answer:** which of LE31's existing tables provides the "named rows" for a given claim. LE31's `StockEntry` is append-only and carries `ref_order_item_id` (line 124), and `DecisionRationale` (feature 47) and the audit features (30, 49, 50) exist — but **no feature states which rows constitute the evidence for a given claim.** Recorded as an open question, not decided here.

## Implementation

**No implementation steps. This feature is a `defer` vocabulary artifact.**

For reference only, what a future implementer would need to decide (**not** this feature's scope):

- **Which claims get verified.** The policy is only worth having if there is at least one class of claim to verify. LE31 today has **no** AI-assisted claim surface (see Open questions), so the policy has nothing to govern yet — **which is precisely why this is `defer` and not `build`.**
- **The tolerance** (LE31's §3.6 money rule makes the tolerance a **money** question, not a percentage: `Decimal`, never float).
- **The retry budget** and whether exhaustion yields "insufficient evidence" or a refusal-with-reason.
- **Where the recomputation runs** — a service function, a read-model job, or a test. **In code, never in a model.**

## Telegram interaction

**None. No bot, no command, no surface change.**

Rationale, recorded so it is not re-litigated: `ServiceWhy`'s output is an **owner-facing incident report** — a *new surface* under §3.1, which names exactly two (waiter web UI, cook Telegram bot). The **verifier policy itself** is a rule about how claims are checked; it is not an interaction. **The one thing it contributes to the Telegram surface is a negative rule worth stating because the temptation is real:** a future contributor could point at this artifact and ask *"why not put an AI assistant on the cook bot?"* — the answer is that **LE31 may** (§3.4 permits AI assisting staff), and the bar such an assistant must clear is §3.4's *"observable evidence"* plus *"a non-AI fallback"*, **and this artifact is the concrete shape of that bar**: the assistant's claims must be recomputable from named rows, and a claim that is not must be answerable as *"insufficient evidence"* rather than asserted. **The artifact is a staff-facing tool, not a guest-facing one, so §3.1's prohibition is not triggered.**

## Dependencies

- **Charter §3.4** — *"AI may assist owner/staff, with observable evidence and a non-AI fallback."* **The phrase "observable evidence" is defined nowhere in LE31; this feature records a candidate definition.**
- **Feature 63** (second-opinion verifier, **PARKING-LOT**) — **read first.** It is the feature this pick is closest to, and the reason it is *not* a duplicate is the deterministic-vs-model distinction. Its charter blocker is **not** inherited by this pick.
- **Feature 55** (evidence review surface) — the *visibility* half. This feature is the *refusal* half.
- **Feature 68** (cook-assistant deterministic gate) — the *write-gating* half. Adjacent, compatible, different concern.
- **Feature 47** (`decision-rationale-mixin`) and **features 30/49/50** (append-only audit) — the existing evidence-bearing machinery a verifier would read from.
- **Charter §3.1** (two named surfaces; no customer-facing AI), **§3.5** (fixed stack), **§3.6** (exact EUR money, never float).
- **`skills/le31-conventions/SKILL.md`** — the seven-check gate and the *"research novelty is not user demand"* pitfall, which applies directly here.

## Open questions

1. **⭐ What would LE31 actually verify?** This feature's policy governs a claim; LE31 has **no** AI-assisted claim surface today, because the unmade question *"does LE31 get any AI surface at all?"* (raised on features 352, 354, 367 and now again here) is still unmade. **This pick deliberately does not answer it.** The verifier policy is **conditional on** that decision, and is filed so that the decision, when it is made, has a ready-made standard to meet.
2. **Which rows constitute the evidence for a given claim?** LE31's `StockEntry` is append-only and `DecisionRationale`/audit features exist, but no feature states the linkage.
3. **What tolerance, in money terms?** §3.6 makes this a `Decimal` question, not a percentage one.
4. **Does "insufficient evidence" mean *refuse* or *defer*?** `ServiceWhy` answers it with *"insufficient evidence"*; LE31's §3.1 phrase *"do not silently send, serve, close, or reconcile"* suggests **refusal**, but the exact user-facing wording is undecided.
5. **Is the threshold-freezing discipline a LE31 practice?** *"`from it on, the thresholds … do not change`"* — recorded, not adopted.
6. **Is the "decoy split" (V4) transferable?** It forces an answer to distinguish *"fewer parties"* from *"less spend per party"*. LE31's §3.6 money derivation may make an equivalent distinction necessary — **recorded, not picked.**

## Why this matters

**Because LE31's charter already requires the thing this artifact supplies, and does not know how to say it.**

§3.4 is the only clause in LE31's charter that **permits** AI at all. It is therefore the clause most likely to be invoked when someone proposes an AI-assisted feature — and it currently has **no operational meaning**. Any proposal that says *"this is staff-facing, so §3.4 is satisfied"* is, today, **unfalsifiable**: the clause offers no test the proposal can fail. `ServiceWhy` supplies a test that is:

1. **Deterministic** — the numbers are recomputed in code, never by a model.
2. **Refusable** — a claim can be blocked, not merely annotated.
3. **Honest at the limit** — when the evidence will not carry the claim, the answer is *"insufficient evidence"*, not a smaller number.

**None of that requires a second model.** That matters enormously here, because the *only* thing that has kept LE31's AI question parked for months is feature 63's realization that a second-model verifier needs a charter revision. **A deterministic verifier needs no charter revision and no second provider — so it is the one form of §3.4's requirement that LE31 could adopt without unlocking the rest of the AI question.** This is the smallest, cheapest, most reversible way to make §3.4 mean something.

**And the discipline it teaches is transferable to non-AI work.** *"The model never recomputes numbers"* is a statement about where authority lives. LE31's append-only ledger already holds authority in **rows**, not in any process's judgement; the verifier policy is the same idea applied to a **claim** rather than to a **quantity**. That is why this feature is filed even though LE31 has no AI surface — the vocabulary is useful before the surface exists.

## Evidence

- **Evidence class:** **reported**, confidence **medium** for the shape, **low** for LE31's need. ★2, a hackathon entry, **100% synthetic data**, *"No receipt, no claim."* No operator has asked LE31 for a verifier.
- **Raw artefacts:** `/tmp/le31-daily-2026-10-28/gh/pv/KoangWy__servicewhy.json`, `/tmp/le31-daily-2026-10-28/gh/readmes/KoangWy__servicewhy.md`.
- **Report:** `/opt/data/le31-daily-research-2026-10-28.md`.
- **Parent verification scripts:** `/opt/data/le31-verify-2026-10-28/rederive.py`, `rank.py`.
