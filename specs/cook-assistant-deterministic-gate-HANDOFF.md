# cook-assistant-deterministic-gate — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/68-cook-assistant-deterministic-gate.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `68`
- Slug: `cook-assistant-deterministic-gate`
- Contract file: `features/68-cook-assistant-deterministic-gate.md`
- Bucket: v2-AI (the AI-safety gate primitive for every future v2-AI feature)
- Linear parent: see Brainstorm 2026-08-15 — daily issue
- Linear sub-issue: see `le31 v2-AI` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build.** No failed checks. Independent of any new feature;
requires the existing `StockEntry` table + feature 37's gate logic.

Evidence precondition: **observed** (1 in-window GitHub repo —
`4242labs/memento` pushed 2026-08-14T20:34:45Z — explicitly names "the model
proposes, deterministic gates decide, append-only, human-readable, one
isolated store per consumer"). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate; charter
   §3.3 non-AI fallback rule is the foundation of this slice).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from
the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/models.py                                          # NEW: AssistantProposal SQLModel + append-only listener; ALTER StockEntry.proposal_id
backend/app/services/assistant_gate.py                         # NEW: propose() + resolve() functions
backend/app/bot/cook_bot_reply.py                              # NEW: reply path for rejected proposals (cook gets a Telegram message with the gate reason)
backend/app/config.py                                          # NEW: AI_PROPOSALS_ENABLED config field (default True)
backend/alembic/versions/<new>_assistant_proposal.py           # NEW migration (AssistantProposal table + StockEntry.proposal_id column)
backend/README.md                                              # note the new gate primitive + AI_PROPOSALS_ENABLED env var
```

No new pip dependencies. The gate uses existing models, existing
validators, existing aiogram primitives.

## Endpoints and contracts added

No new HTTP routes. The gate is an internal service module.

One new SQLModel table:

```python
# backend/app/models.py
class AssistantProposal(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    source: str = Field(max_length=80, index=True)
    menu_item_id: int = Field(foreign_key="menuitem.id", index=True)
    qty_delta: int
    rationale_proposed: str = Field(max_length=500)
    status: str = Field(max_length=20)  # 'pending' | 'promoted' | 'rejected' — set ONCE at gate resolution
    gate_reason: str = Field(max_length=500)
    promoted_stockentry_id: int | None = Field(default=None, foreign_key="stockentry.id", index=True)
```

Append-only (new `assistantproposal_append_only.py` listener —
`status` / `gate_reason` / `promoted_stockentry_id` are set ONCE at gate
resolution; no `UPDATE` or `DELETE` paths exist).

One new column on `StockEntry`:

```python
# backend/app/models.py
class StockEntry(SQLModel, table=True):
    ...  # existing fields unchanged
    proposal_id: int | None = Field(default=None, foreign_key="assistantproposal.id", index=True)
```

`StockEntry.proposal_id` is NULL for typed writes; non-NULL for AI-proposed
writes. Set once at insert time; never updated.

One new Alembic migration:

```python
def upgrade():
    op.create_table(
        "assistantproposal",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("source", sa.String(80), nullable=False),
        sa.Column("menu_item_id", sa.Integer, sa.ForeignKey("menuitem.id"), nullable=False),
        sa.Column("qty_delta", sa.Integer, nullable=False),
        sa.Column("rationale_proposed", sa.String(500), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("gate_reason", sa.String(500), nullable=False),
        sa.Column("promoted_stockentry_id", sa.Integer, sa.ForeignKey("stockentry.id"), nullable=True),
    )
    op.create_index("ix_assistantproposal_source", "assistantproposal", ["source"])
    op.create_index("ix_assistantproposal_menu_item_id", "assistantproposal", ["menu_item_id"])
    op.create_index("ix_assistantproposal_promoted_stockentry_id", "assistantproposal", ["promoted_stockentry_id"])
    op.add_column("stockentry", sa.Column("proposal_id", sa.Integer, sa.ForeignKey("assistantproposal.id"), nullable=True))
    op.create_index("ix_stockentry_proposal_id", "stockentry", ["proposal_id"])

def downgrade():
    op.drop_index("ix_stockentry_proposal_id", table_name="stockentry")
    op.drop_column("stockentry", "proposal_id")
    op.drop_index("ix_assistantproposal_promoted_stockentry_id", table_name="assistantproposal")
    op.drop_index("ix_assistantproposal_menu_item_id", table_name="assistantproposal")
    op.drop_index("ix_assistantproposal_source", "assistantproposal")
    op.drop_table("assistantproposal")
```

One new config field:

```python
# backend/app/config.py
AI_PROPOSALS_ENABLED: bool = True
```

`.env` key:
```
AI_PROPOSALS_ENABLED=true
```

One new service module:

```python
# backend/app/services/assistant_gate.py
from sqlmodel import Session
from app.models import AssistantProposal, StockEntry
from app.config import AI_PROPOSALS_ENABLED

class ProposalsDisabledError(Exception):
    pass

def propose(
    session: Session,
    *,
    source: str,
    menu_item_id: int,
    qty_delta: int,
    rationale_proposed: str,
) -> AssistantProposal:
    """Write a pending AssistantProposal row. The gate has NOT yet run.
    Caller is responsible for calling resolve() next.
    """
    if not AI_PROPOSALS_ENABLED:
        raise ProposalsDisabledError("AI proposals are disabled (AI_PROPOSALS_ENABLED=false)")
    proposal = AssistantProposal(
        source=source,
        menu_item_id=menu_item_id,
        qty_delta=qty_delta,
        rationale_proposed=rationale_proposed,
        status="pending",
        gate_reason="",
        promoted_stockentry_id=None,
    )
    session.add(proposal)
    session.commit()
    session.refresh(proposal)
    return proposal

def resolve(session: Session, proposal: AssistantProposal) -> AssistantProposal:
    """Run the deterministic gate (same rules as the typed /86 <item>
    path). Set status + gate_reason + (if promoted) promoted_stockentry_id
    ONCE. No UPDATE or DELETE on the proposal row afterwards.
    """
    # Lift the existing gate logic from feature 37's validate_void_rationale()
    # and the typed /86 <item> handler. Identical rules.
    gate_passed, reason = _run_gate(
        menu_item_id=proposal.menu_item_id,
        qty_delta=proposal.qty_delta,
    )
    if gate_passed:
        se = StockEntry(
            menu_item_id=proposal.menu_item_id,
            qty_delta=proposal.qty_delta,
            rationale=proposal.rationale_proposed,
            source=f"assistant:{proposal.source}",
            proposal_id=proposal.id,
        )
        session.add(se)
        session.commit()
        session.refresh(se)
        proposal.status = "promoted"
        proposal.gate_reason = "all checks passed"
        proposal.promoted_stockentry_id = se.id
    else:
        proposal.status = "rejected"
        proposal.gate_reason = reason
    session.add(proposal)
    session.commit()
    session.refresh(proposal)
    # If rejected, send a Telegram reply to the cook with the gate reason.
    if proposal.status == "rejected":
        from app.bot.cook_bot_reply import send_gate_rejection_reply
        send_gate_rejection_reply(proposal=proposal, reason=reason)
    return proposal

def _run_gate(*, menu_item_id: int, qty_delta: int) -> tuple[bool, str]:
    """The deterministic gate. SAME rules as the typed /86 <item> path.
    Returns (passed, reason)."""
    # TODO: lift the actual gate logic from feature 37 + the typed /86 handler.
    # For the first slice, this is a stub that always passes (the gate logic
    # is documented in feature 37 and will be lifted into this function as
    # part of the slice build).
    return True, "all checks passed (stub)"
```

## Verification

1. `AssistantProposal` insert unit test — verify the append-only listener
   raises on `UPDATE` or `DELETE`.
2. `propose()` unit test — verify a pending `AssistantProposal` row is
   written with `status='pending'`, `gate_reason=''`,
   `promoted_stockentry_id=None`.
3. `resolve()` unit test — verify:
   - When the gate passes: `status='promoted'`, `gate_reason='all checks
     passed'`, `promoted_stockentry_id=<new StockEntry.id>`, and a new
     `StockEntry` row exists with `proposal_id=<AssistantProposal.id>`.
   - When the gate fails: `status='rejected'`, `gate_reason=<reason>`,
     `promoted_stockentry_id=None`, and **no `StockEntry` row is written**.
4. **Gate-identity regression test** — for every rule the typed `/86
   <item>` path enforces, the assistant gate enforces the same rule.
   This is the most important test in the slice: the gate must be
   **identical**, not just "similar".
5. `AI_PROPOSALS_ENABLED=false` test — `propose()` raises
   `ProposalsDisabledError`; no row is written.
6. Bot reply test — when the gate fails, the cook gets a Telegram message
   with the gate reason.
7. Existing tests still green (the typed `/86 <item>` path is unchanged;
   `StockEntry.proposal_id` defaults to NULL; no existing test should
   break).

## Rollback path

Set `AI_PROPOSALS_ENABLED=false` in `.env` and restart — `propose()` raises
`ProposalsDisabledError`; the AI surface degrades to "AI unavailable"
without affecting the typed variant. To fully rollback: drop the
`AssistantProposal` table (migration downgrade), drop the
`StockEntry.proposal_id` column (migration downgrade), remove the new
files. No upstream feature is broken by removing this.

## Dependencies

- No new pip dependencies.
- **Required upstream features**:
  - feature 37 (`void-rationale-ledger-field`) — supplies the existing
    gate logic that the new gate reuses (via `_run_gate()`). Without 37,
    there is no business-rule gate to lift.
- **Required downstream features**: every future v2-AI feature that wants
  to write a `StockEntry` should call `assistant_gate.propose()` +
  `assistant_gate.resolve()` instead of writing directly. The contract
  documents this requirement.
