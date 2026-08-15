# solo-operator-shift-journal-pwa — HANDOFF

> **Slice for the coding agent.** Read this *and*
> `features/67-solo-operator-shift-journal-pwa.md` before touching any code.
> Do not paste chat excerpts back into the build.

## Frozen identifiers (do not rename)

- Feature ID: `67`
- Slug: `solo-operator-shift-journal-pwa`
- Contract file: `features/67-solo-operator-shift-journal-pwa.md`
- Bucket: v2 owner-pains (no-account owner surface; printable PDF)
- Linear parent: see Brainstorm 2026-08-15 — daily issue
- Linear sub-issue: see `le31 v2 owner-pains` project, label `Feature`

## LE31 feature-gate verdict (recorded)

Run per `skills/le31-conventions/SKILL.md` — all seven checks answered in the
contract file under "Why this matters" and the body of the report.
**Decision: build.** (with feature 29 `owner-no-account-live-floor-link` as a
prerequisite.) No failed checks.

Evidence precondition: **observed** (1 in-window GitHub repo pushed today —
`Sreenivas-Sadhu-Prabhakara/slotone` pushed 2026-08-15T03:05:39Z — shares the
no-account solo-operator day-book primitive). Confidence: **high**.

## Mandatory LE31 skill list (load these first)

External coding agent MUST load before starting:

1. `le31-conventions` (project invariants + the seven-check gate).
2. `le31-v1-feature-pattern` (canonical contract shape + slicing rules).
3. `le31-handoff-spec` (frozen-contract discipline; mirror contract back).
4. `le31-daily-brainstorm` (this pick came from the daily brainstorm job).
5. `le31-feature-pipeline` (so the agent understands how this slice will
   be sequenced after it ships).

If the destination repo does not yet ship these skills, request them from
the research-side Hermes instance before writing code.

## Files the slice touches

```
backend/app/models.py                                       # NEW: ShiftJournalNote SQLModel + append-only listener
backend/app/services/shift_journal.py                       # NEW: composer module (DecisionNote + StockEntry.rationale + OwnerRecap + Reservation + ShiftJournalNote)
backend/app/main.py                                         # NEW: FastAPI route registrations (3 routes)
backend/app/bot/cook_bot_ownerlink.py                       # PATCH: /ownerlink returns journal URL by default; live floor URL still reachable
backend/app/templates/owner_journal.html                    # NEW: chronological Jinja2 template
backend/app/templates/owner_journal_note.html               # NEW: single-note printable view
backend/app/templates/printable.journal.html                # NEW: print-friendly layout (single column, no nav)
backend/alembic/versions/<new>_shift_journal_note.py        # NEW migration
backend/README.md                                           # note the new routes + journal primitive
```

No new pip dependencies. Jinja2 is already imported for feature 29's
`owner.html`.

## Endpoints and contracts added

Three new FastAPI routes:

- `GET /owner/<token>/journal/<date>` — renders `owner_journal.html`
- `POST /owner/<token>/journal/<date>` — appends a `ShiftJournalNote` of
  `kind=note` from a single textarea; no CSRF token (signed URL is the
  auth)
- `GET /owner/<token>/journal/<date>/note/<note_id>` — renders a single
  printable note

All three routes validate the `OwnerLink` token (hash + 12h expiry); 410 Gone
on miss/expired.

One new SQLModel table:

```python
# backend/app/models.py
class ShiftJournalNote(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    ownerlink_id: int = Field(foreign_key="ownerlink.id", index=True)
    day_date: date = Field(index=True)
    kind: str = Field(max_length=20)  # 'decision' | 'void' | 'explain' | 'reservation' | 'note'
    body: str = Field(max_length=2000)
    created_at: datetime = Field(default_factory=lambda: datetime.now(ZoneInfo("Europe/Paris")))
    created_by_chat_id: int | None = Field(default=None)
```

Append-only (new `shiftjournalnote_append_only.py` listener — no `UPDATE` or
`DELETE` paths exist).

One new Alembic migration:

```python
def upgrade():
    op.create_table(
        "shiftjournalnote",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("ownerlink_id", sa.Integer, sa.ForeignKey("ownerlink.id"), nullable=False),
        sa.Column("day_date", sa.Date, nullable=False),
        sa.Column("kind", sa.String(20), nullable=False),
        sa.Column("body", sa.String(2000), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_by_chat_id", sa.BigInteger, nullable=True),
    )
    op.create_index("ix_shiftjournalnote_ownerlink_id", "shiftjournalnote", ["ownerlink_id"])
    op.create_index("ix_shiftjournalnote_day_date", "shiftjournalnote", ["day_date"])

def downgrade():
    op.drop_index("ix_shiftjournalnote_day_date", table_name="shiftjournalnote")
    op.drop_index("ix_shiftjournalnote_ownerlink_id", table_name="shiftjournalnote")
    op.drop_table("shiftjournalnote")
```

One patch to the existing `/ownerlink` cook-bot command (feature 29): the
URL returned now points to `/owner/<token>/journal/<today>` (the journal
view) by default. The original live-floor URL `/owner/<token>` is still
reachable.

One new composer module:

```python
# backend/app/services/shift_journal.py
from datetime import date
from sqlalchemy import select
from sqlmodel import Session
from app.models import DecisionNote, StockEntry, OwnerRecap, Reservation, ShiftJournalNote

def compose_journal(session: Session, day_date: date) -> list[dict]:
    """Composes the day's chronological journal from existing append-only
    tables plus the new ShiftJournalNote table.

    Returns a list of dicts: [{created_at, kind, body}, ...] sorted by
    created_at ascending. No duplication of existing rows — only
    ShiftJournalNote rows are stored; the rest are read on-the-fly.
    """
    entries = []
    # DecisionNote rows from feature 46
    for dn in session.exec(
        select(DecisionNote).where(DecisionNote.effective_from <= day_date)
    ).all():
        if dn.expires_at is None or dn.expires_at >= day_date:
            entries.append({"created_at": dn.created_at, "kind": "decision", "body": dn.body})
    # StockEntry rows with rationale (negative deltas only — voids)
    for se in session.exec(
        select(StockEntry).where(
            StockEntry.day_date == day_date,
            StockEntry.qty_delta < 0,
            StockEntry.rationale.isnot(None),
        )
    ).all():
        entries.append({"created_at": se.created_at, "kind": "void", "body": se.rationale})
    # OwnerRecap rows from feature 39
    for or_ in session.exec(
        select(OwnerRecap).where(OwnerRecap.sent_at >= day_date)
    ).all():
        entries.append({"created_at": or_.sent_at, "kind": "explain", "body": "(daily recap)"})
    # Reservation rows (out-of-scope stub; deferred to a follow-up)
    # ShiftJournalNote rows (owner-typed notes)
    for sjn in session.exec(
        select(ShiftJournalNote).where(ShiftJournalNote.day_date == day_date)
    ).all():
        entries.append({"created_at": sjn.created_at, "kind": sjn.kind, "body": sjn.body})
    return sorted(entries, key=lambda e: e["created_at"])
```

## Verification

1. `ShiftJournalNote` insert unit test — verify the append-only listener
   raises on `UPDATE` or `DELETE`.
2. `compose_journal()` unit test with mocked `DecisionNote` /
   `StockEntry.rationale` / `OwnerRecap` / `ShiftJournalNote` queries —
   verify the chronological ordering, the grouping by kind, and that no
   rows are duplicated.
3. End-to-end FastAPI test: create an `OwnerLink` → `GET
   /owner/<token>/journal/2026-08-15` → page renders with the seven
   sections → `POST /owner/<token>/journal/2026-08-15` with
   `body="test note"` → new `ShiftJournalNote` row written → page re-renders
   with the note appended.
4. `GET /owner/<token>/journal/<date>/note/<note_id>` — verify a single
   note renders as a printable page.
5. Expired-token test: `OwnerLink.expires_at` in the past → route returns
   410 Gone.
6. Print-friendly CSS test: `@media print` styles hide nav and other UI;
   the page is single-column when printed.
7. DST transition test: at the spring-forward boundary (last Sunday of
   March), `day_date` is computed in `Europe/Paris` correctly.
8. Existing tests still green.

## Rollback path

Set `OWNER_TELEGRAM_CHAT_IDS=` (empty) and remove the `/recap` command
registration in `.env` — the journal view is unreachable from the cook
bot but the existing `/ownerlink` live-floor URL still works. To fully
rollback: drop the `ShiftJournalNote` table (migration downgrade), remove
the new files, restore the original `/ownerlink` URL. No upstream feature
is broken by removing this.

## Dependencies

- No new pip dependencies.
- **Required upstream features**:
  - feature 29 (`owner-no-account-live-floor-link`) — supplies the
    `OwnerLink` token primitive. This contract **lists 29 as a
    prerequisite and will refuse to ship without it**.
  - feature 46 (`havemind-decision-notes`) — supplies the `DecisionNote`
    rows.
  - feature 37 (`void-rationale-ledger-field`) — supplies the `rationale`
    column on `StockEntry`.
  - feature 39 (`owner-daily-recap-telegram`) — supplies the `OwnerRecap`
    rows.
- **Required downstream features**:
  - feature 69 (`owner-no-account-shift-recap-link`) — uses the journal
    as the body of the printable end-of-shift recap.
