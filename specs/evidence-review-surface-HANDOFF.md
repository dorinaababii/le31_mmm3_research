# evidence-review-surface — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/55-evidence-review-surface.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `55`
- Slug: `evidence-review-surface`
- Contract file: `features/55-evidence-review-surface.md`
- Bucket: v2 owner-pains (no new pip deps; composition of pre-existing
  features)
- Linear parent: HMM-62 (Brainstorm 2026-08-11 — daily)
- Linear sub-issue: see `le31 v1 — Core MVP` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in
the contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks. (Confidence: high; same-shape
evidence: `paulmurphynet/chronicle` pushed today in-window.)

Evidence precondition: **observed** (chronicle pushed 2026-08-11, 4
in-source corroborating pieces). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing
   rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract
   back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm
   job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them
from the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/models.py                            # NEW: EvidenceLink SQLModel
backend/app/services/evidence.py                 # NEW: nightly builder + query helpers
backend/app/bot/cook_bot_explain.py              # NEW: /explain + /verify handlers
backend/app/bot/cook_bot.py                      # EDIT: register 2 new handlers (2 lines)
backend/app/main.py                              # EDIT: register evidence_link_build APScheduler job
backend/app/config.py                            # NEW: OWNER_TELEGRAM_CHAT_IDS (reuse feature 39's)
backend/alembic/versions/<new>_evidence_link.py  # NEW migration
backend/scripts/backfill_evidence_links.py       # NEW: idempotent backfill
backend/scripts/verify_evidence_chain.py         # NEW: read-only CLI
backend/tests/test_evidence_link.py              # NEW: unit tests
backend/README.md                                # note the 2 bot commands + job registration
```

No new pip dependencies. APScheduler is already imported.

## Endpoints and contracts added

No new HTTP routes. All logic lives in the scheduler + bot webhook.

One new SQLModel table:

```python
# backend/app/models.py
class EvidenceLink(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    claim_kind: str = Field(index=True)   # enum-style: owner_recap_summary, void_with_reason, cook_channel_event, prep_checkoff_skip
    claim_ref_id: int = Field(index=True)
    evidence_table: str = Field(index=True)  # enum-style: stock_entry, void_rationale, cook_channel_event, prep_task
    evidence_ref_id: int = Field(index=True)
    added_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")), index=True)

    __table_args__ = (
        UniqueConstraint(
            "claim_kind", "claim_ref_id", "evidence_table", "evidence_ref_id",
            name="uq_evidence_link_claim_evidence",
        ),
    )
```

Append-only — rows never updated, never deleted.

One new Alembic migration:

```python
def upgrade():
    op.create_table(
        "evidence_link",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("claim_kind", sa.String(64), nullable=False),
        sa.Column("claim_ref_id", sa.Integer, nullable=False),
        sa.Column("evidence_table", sa.String(64), nullable=False),
        sa.Column("evidence_ref_id", sa.Integer, nullable=False),
        sa.Column("added_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_unique_constraint(
        "uq_evidence_link_claim_evidence",
        "evidence_link",
        ["claim_kind", "claim_ref_id", "evidence_table", "evidence_ref_id"],
    )
    op.create_index("ix_evidence_link_claim_kind_claim_ref", "evidence_link",
                    ["claim_kind", "claim_ref_id"])
    op.create_index("ix_evidence_link_evidence_table_evidence_ref", "evidence_link",
                    ["evidence_table", "evidence_ref_id"])

def downgrade():
    op.drop_table("evidence_link")
```

## Endpoints and bot commands added

Two new owner-only Telegram commands on the existing `cook_bot.py`:

- `/explain <recap_row_id>` — returns a structured per-claim
  evidence card. Markdown formatted. Falls back to "No recap row <R>"
  if not found; "No evidence links yet for this recap (builder hasn't
  run)" if the builder has not yet run on this row.
- `/verify last-week` — returns a 2-3 line gap-check summary. Falls
  back to "All clear — no missing evidence links." for a perfect 7-day
  run.

Both commands reject any non-owner chat_id with the same 1-line
"unauthorized" message used by feature 39's `/ack`.

## Verification protocol reference

Per `le31-conventions` "Verification" pattern. The coding agent MUST:

1. Unit-test `evidence_link_build()` with 3 fixtures (typical evening
   with all four claim kinds, an evening with only 86s, an evening
   with void-with-reason + cook-channel event).
2. Idempotency test: run the builder twice on the same evening; assert
   `EvidenceLink` row count unchanged.
3. Bot test: `/explain` returns the expected card for a fixture row;
   `/verify last-week` returns "All clear" after 7 evenings of fixtures.
4. CLI test: `scripts/verify_evidence_chain.py` prints the same data
   the bot would return.

After implementation, run the parent's verify-before-fixing protocol
(see `skills/verify-before-fixing/SKILL.md`) on the slice branch.

## Rollback path

- Migration is reversible (`op.drop_table("evidence_link")`).
- The two new bot commands are additive and isolated to a single
  module — feature-flag them in `cook_bot.py` so a partial deploy
  hides them behind `OWNER_EVIDENCE_REVIEW_ENABLED=1` (default ON).
- If the heuristic produces embarrassing moments (uncanny-valley
  bound), flip the env to OFF; the existing recap continues unchanged.
- Reversible in <5 min: feature-flag OFF + alembic downgrade on the
  next slot.

## What is explicitly NOT in this slice

- LLM-generated copy / moments. Slice is purely deterministic.
- Per-restaurant evidence chains.
- Cross-pipeline attachment to feature 57's `/why <recap_moment_index>`
  — that integration lives in feature 57's slice (so feature 55's
  evidence card layer is independent and feature 57 builds on top).
