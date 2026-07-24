"""Tables router — list floor, seat a party, free a table.

Implements feature 01 (table management).
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from ..db import get_session
from ..models import Table, TableStatus, Visit, AppUser

router = APIRouter(prefix="/api/tables", tags=["tables"])


@router.get("")
def list_tables(session: Session = Depends(get_session)) -> list[dict]:
    """List all tables with current status. The waiter UI calls this on load."""
    tables = session.exec(select(Table)).all()
    return [
        {
            "id": t.id,
            "label": t.label,
            "section": t.section,
            "seats": t.seats,
            "x": t.x,
            "y": t.y,
            "status": _table_status(t.id, session),
        }
        for t in tables
    ]


@router.post("/{table_id}/seat")
def seat_party(
    table_id: int,
    party_size: int,
    adults: int,
    children: int = 0,
    server_id: int = 1,  # TODO: from auth token
    session: Session = Depends(get_session),
) -> dict:
    """Seat a party at a table → opens a new Visit."""
    table = session.get(Table, table_id)
    if not table:
        raise HTTPException(404, "Table not found")
    if party_size < 1 or adults < 1:
        raise HTTPException(400, "Need at least 1 adult")
    if adults + children < party_size:
        raise HTTPException(400, "adults + children must cover party_size")
    # TODO: reject if table is not FREE (need TableStatus column on Table)
    visit = Visit(
        table_id=table_id,
        server_id=server_id,
        party_size=party_size,
        adults=adults,
        children=children,
    )
    session.add(visit)
    session.commit()
    session.refresh(visit)
    return {"visit_id": visit.id, "table_id": table_id}


def _table_status(table_id: int, session: Session) -> str:
    """Derive a table's current status from the latest open Visit."""
    visit = session.exec(
        select(Visit).where(Visit.table_id == table_id, Visit.closed_at == None)
    ).first()
    if not visit:
        return TableStatus.free.value
    return TableStatus.seated.value  # could be 'ordered' / 'billed' with more checks