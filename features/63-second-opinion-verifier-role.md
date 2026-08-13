# Feature 63 — Second-Opinion Verifier Role (PARKING-LOT)

> **Priority**: P2 · **Effort**: M (≤1 week) when implemented, but
> **not in v2-AI control-plane v1** · **Source**: brainstorm
> 2026-08-13 (cross-section pick C, **PARKING-LOT**) ·
> **Bucket**: **v2-AI control-plane, long-lead** — preserved as a
> future candidate until the multi-model policy question is
> resolved.
> **One-line**: add a *third role* between AI proposal and owner
> approval — an independent verifier model reads the proposal
> plus its evidence card and writes a
> `VerificationReport(approve|reject|insufficient_evidence, rationale)`
> before the owner sees the proposal — gated on a charter
> revision authorising multi-model orchestration.

## Status: PARKING-LOT (today)

This file is parked because two prerequisites are unresolved:

1. **Charter prerequisite (§3.2 / §4 single-model assumption)**:
   today's LE31 stack assumes one LLM provider at most. A
   second-model verifier would require an explicit charter
   revision. Per `skills/le31-conventions/SKILL.md` Conflict
   check, a hard conflict blocks a proposal until redesigned
   or explicitly overridden.

2. **Operational prerequisite**: the cost/benefit is not yet
   proven for a single-restaurant deployment. Feature 55
   (`evidence-review-surface`) already covers the *"show
   receipts"* need; a verifier model adds cost without
   addressing an observed LE31 pain.

`Frantz103/agent-os-opensource` (pushed **2026-08-13**, 1★,
Python, Apache-2.0) is the cross-section anchor and confirms the
shape exists in the wild. **The slice is preserved on file** so
that when (or if) LE31 adds a second model — most likely when
the daily menu-photo OCR pipeline swaps to a stronger
multimodal provider — this pick is unblockable by a charter
revision without redoing the brainstorm.

## Goal (when implemented)

Picks 58, 61, and 62 cluster into the v2-AI control plane.
Pick 63 is the *insurance plan* for that plane: when the AI's
proposal (DecisionRow kind=`ai_proposal`, feature 61) reaches
the owner, a *different* model — the verifier — has already
read the proposal plus its `evidence_link_ids` (feature 55)
and written one of three `VerificationReport` rows
(approve / reject / insufficient_evidence). Only after a
`pass` verification does the owner see the proposal card.

This is the *third row* of the same ledger:

```
DecisionRow #N    kind=ai_proposal        actor=ai
DecisionRow #N+1  kind=verification_pass  actor=verifier  (only when verifier_model_id agrees)
DecisionRow #N+2  kind=owner_decision     actor=owner     (only when verification passed)
```

When the verifier rejects or finds insufficient evidence, the
owner's daily-recap Telegram (`feature 39`) emits a
*"the AI wanted to <X>, but the verifier disagreed because <Y>"*
card, with no decision row written.

## Scope (when implemented)

**In scope (v2-AI control-plane long-lead):**

- New SQLModel table `verification_report(id, proposal_row_id,
  verifier_model_id, decision, rationale, prev_hash, row_hash,
  created_at)`. One new Alembic migration.
- New service `backend/app/services/verifier.py`: `verify(…)`
  that takes a `DecisionRow kind=ai_proposal` plus its
  `evidence_link_ids`, calls a *separate* LLM provider via
  `LLM_BASE_URL_VERIFIER`, and writes the resulting
  `VerificationReport` row.
- `backend/app/services/ai_control_plane.py`: extend the
  control plane to require a `pass` `VerificationReport` row
  before exposing the proposal to the owner. Default behaviour
  (no verifier) bypasses this gate, preserving feature 58's
  v1 path.
- New config `backend/app/config.py`: `VERIFIER_MODEL_ID`
  (None = bypass), `LLM_BASE_URL_VERIFIER` (None = bypass).
- New tests + a new bot command `/verify-policy` (owner-only)
  that prints the current verifier policy.
- One new Alembic migration; one new pip dependency
  (`httpx` is already in use; no actual new dep expected).

**Out of scope (parking-lot, possibly forever):**

- Multi-model orchestration in v1 of the v2-AI control plane.
- Owner-facing verifier training. The verifier's prompt is
  shipped in code, not learned from owner feedback.
- Cross-model agreement metrics. Out of scope; the verifier
  is binary (pass/fail).

## Description

`Frantz103/agent-os-opensource` (pushed 2026-08-13, 1★, Python,
Apache-2.0) — *"Local-first task, evidence, and
independent-review layer for AI coding runtimes"*. The phrase
**independent-review layer** is the key: a separate process
(possibly a separate model) reviews the agent's work before it
is surfaced to the human.

`chiga0/marshal-harness` (pushed 2026-08-13, Go, ★1) also
corroborates: *"independent verification, digest-bound review,
draft-only publication"*.

The cross-section pattern is real; the LE31 application is
deferred until a charter revision makes it actionable.

## Data model (when implemented)

```sql
CREATE TABLE verification_report (
    id                BIGSERIAL PRIMARY KEY,
    proposal_row_id   BIGINT NOT NULL REFERENCES decision_row(id),
    verifier_model_id TEXT NOT NULL,        -- e.g. "openai/gpt-4o-mini" or "gemini-flash-2"
    decision          TEXT NOT NULL,        -- pass|reject|insufficient_evidence
    rationale         TEXT,
    prev_hash         BYTEA NOT NULL,       -- chain: row_hash of the previous decision_row or verification_report
    row_hash          BYTEA NOT NULL,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX verification_report_proposal_idx ON verification_report (proposal_row_id);
```

APPEND-ONLY at the API layer. Hash chain mirror of feature 49 +
feature 61.

## Implementation steps (when unblocked)

1. Resolve the multi-model policy via a charter revision
   *first*. Without it, this slice cannot pass the Conflict
   check.
2. Add `backend/app/models/verification_report.py` with the
   SQLModel.
3. Add Alembic migration `XXXX_add_verification_report.py`.
4. Add `backend/app/services/verifier.py` (the
   LLM-calling wrapper).
5. Extend `backend/app/services/ai_control_plane.py` to
   require a `pass` report before exposing the proposal.
6. Add config: `VERIFIER_MODEL_ID`, `LLM_BASE_URL_VERIFIER`.
7. Add `backend/tests/test_verifier.py` (4 fixtures: bypass
   when None, pass path, reject path, insufficient-evidence
   path).
8. Add `/verify-policy` bot command and `backend/README.md`
   section.

## Telegram interaction if any (when unblocked)

- `/verify-policy` — owner-only. Reports the current verifier
  model id and whether the gate is bypass, enforce, or
  insufficient-evidence-only.
- The owner's `/ai-actions` reply (feature 58) gains a new
  inline field: "verifier: pass / reject / insufficient /
  bypassed".

## Dependencies

- **Feature 58** (`operator-ai-action-surface`) — the
  dispatcher.
- **Feature 61** (`holdfast-approval-ledger`) — the proposal
  row this slice reads.
- **Feature 55** (`evidence-review-surface`) — the
  `evidence_link_ids` this slice consumes.
- **Charter revision** — unblocks the multi-model assumption.
- **Future v2-AI feature** — a second LLM provider is the
  natural trigger for picking this up off the parking-lot.

## Open questions

- When, if ever, does LE31 cross the multi-model threshold?
  Recommendation: hold until the menu-photo OCR pipeline
  upgrades from RapidOCR + small LLM to a multimodal model,
  which is the natural second-model moment.
- Should the verifier policy be in `agents.yaml` (feature 62)
  or in `config.py`? Recommendation: agents.yaml — matches
  the existing ontology-as-data pattern, and surfaces the
  verifier policy to `git log`.
- Where do the verification costs go? Recommendation: an
  owner-facing daily-counter on the recap Telegram, gated
  on the charter revision.

## Why this matters (eventually)

The charter invariant *"AI may assist owner/staff, with
observable evidence and a non-AI fallback"* has two halves.
Picks 58 + 61 + 62 enforce *"observable evidence"*. Pick 63
would enforce *"AI may assist"* — the verifier is the
mechanism that limits the AI's reach to *assist* (not *decide*).
Without the verifier, the owner is the sole gate between the
AI and the dispatch; with the verifier, the owner is the
*second* gate.

This is exactly the layered safety pattern LE31's charter
aspirationally asks for. It is also exactly the pattern
that crosses from "AI as a tool" to "AI as an actor in a
multi-agent system", which is a real-line that the charter
today draws. The parking-lot preserves the option without
making the line-crossing a fait-accompli.

## Evidence (recorded)

- **Cross-section anchor 1**: `Frantz103/agent-os-opensource`
  (pushed 2026-08-13, 1★, Python, Apache-2.0) — *"Local-first
  task, evidence, and independent-review layer for AI coding
  runtimes"*. Read at
  `/tmp/le31-brainstorm-2026-08-13/gh_evidence_review.json`.
- **Corroborating anchor**: `chiga0/marshal-harness` (pushed
  2026-08-13, Go, ★1) — *"independent verification,
  digest-bound review"*.
- **Literature anchor**: OpenAlex `The Enterprise AI Governance
  Buyer's Guide` (DOI 10.5281/zenodo.18002693, 2026-07-16) —
  broader governance-buyer-guide context.
- **In-repo constraint**: charter §4 single-model assumption
  (governance boundary today); pick 58 + 61 + 62 already
  cover the v2-AI control-plane v1 shape.
