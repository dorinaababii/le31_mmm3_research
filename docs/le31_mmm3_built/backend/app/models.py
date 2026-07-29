"""SQLModel database models.

These mirror the schema sketch in `docs/research/09-recommended-stack.md`.
Each class is a DB table AND a Pydantic model for request/response.

Conventions:
- IDs are auto-incrementing integers (SERIAL on Postgres, INTEGER on SQLite).
- Timestamps use UTC.
- Money uses Decimal (never float) — exact arithmetic.
- All tables have created_at; only mutable ones get updated_at.
"""

from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum

from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel, Relationship


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


# ───── Enums ─────

class TableStatus(str, Enum):
    free    = "free"
    seated  = "seated"
    ordered = "ordered"
    billed  = "billed"
    dirty   = "dirty"


class ItemStatus(str, Enum):
    new        = "new"
    preparing  = "preparing"
    ready      = "ready"
    served     = "served"
    cancelled  = "cancelled"


class PaymentMethod(str, Enum):
    cash = "cash"
    card = "card"


class UserRole(str, Enum):
    server  = "server"
    cook    = "cook"
    manager = "manager"


class StockReason(str, Enum):
    initial = "initial"
    sale    = "sale"
    waste   = "waste"
    restock = "restock"
    sold_out = "sold_out"


# ───── Tables ─────

class Table(SQLModel, table=True):
    __tablename__ = "table_"  # 'table' is a SQL reserved word

    id: int | None = Field(default=None, primary_key=True)
    label: str
    section: str = "main"
    seats: int = 4
    x: int = 0        # for floor map coords
    y: int = 0


class AppUser(SQLModel, table=True):
    __tablename__ = "app_user"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    pin_hash: str     # bcrypt-hashed
    role: UserRole


class MenuItem(SQLModel, table=True):
    __tablename__ = "menu_item"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    category: str
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    unit: str = "piece"
    is_prepared: bool = True    # if True, sales decrement a Batch
    photo_url: str | None = None


class Batch(SQLModel, table=True):
    """A concrete prepared quantity of a MenuItem for a specific day.

    E.g. '8 pieces of Tiramisu, prepared 09:00 today'.
    """
    __tablename__ = "batch"

    id: int | None = Field(default=None, primary_key=True)
    menu_item_id: int = Field(foreign_key="menu_item.id")
    qty_start: int
    qty_remaining: int
    prepared_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    expires_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    photo_url: str | None = None
    notes: str | None = None


class StockEntry(SQLModel, table=True):
    """Append-only ledger. Never UPDATE or DELETE rows.

    Current stock for a batch = SUM(qty_delta) WHERE batch_id = X.
    """
    __tablename__ = "stock_entry"

    id: int | None = Field(default=None, primary_key=True)
    batch_id: int = Field(foreign_key="batch.id", index=True)
    qty_delta: int              # positive = added, negative = consumed
    reason: StockReason
    ref_order_item_id: int | None = None
    by_user_id: int | None = None
    at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))


class Visit(SQLModel, table=True):
    __tablename__ = "visit"

    id: int | None = Field(default=None, primary_key=True)
    table_id: int = Field(foreign_key="table_.id")
    server_id: int = Field(foreign_key="app_user.id")
    opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    party_size: int
    adults: int
    children: int = 0


class OrderItem(SQLModel, table=True):
    __tablename__ = "order_item"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", index=True)
    menu_item_id: int = Field(foreign_key="menu_item.id")
    qty: int = 1
    unit_price: Decimal = Field(max_digits=10, decimal_places=2)
    course: str | None = None  # appetizer / main / dessert
    status: ItemStatus = ItemStatus.new
    notes: str | None = None
    fired_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    ready_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    served_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))


class Bill(SQLModel, table=True):
    __tablename__ = "bill"

    id: int | None = Field(default=None, primary_key=True)
    visit_id: int = Field(foreign_key="visit.id", unique=True)
    subtotal_items: Decimal = Field(max_digits=10, decimal_places=2)
    subtotal_tax: Decimal = Field(max_digits=10, decimal_places=2)
    total_due: Decimal = Field(max_digits=10, decimal_places=2)
    total_paid: Decimal = Field(max_digits=10, decimal_places=2)
    payment_method: PaymentMethod
    paid_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    closed_by: int = Field(foreign_key="app_user.id")


class DerivedTip(SQLModel, table=True):
    """Computed on bill close: tip = total_paid − (subtotal_items + subtotal_tax)."""
    __tablename__ = "derived_tip"

    bill_id: int = Field(foreign_key="bill.id", primary_key=True)
    amount: Decimal = Field(max_digits=10, decimal_places=2)
    formula_version: str = "v1"


class Shift(SQLModel, table=True):
    """For end-of-shift cash reconciliation."""
    __tablename__ = "shift"

    id: int | None = Field(default=None, primary_key=True)
    opened_at: datetime = Field(default_factory=utcnow, sa_column=Column(DateTime(timezone=True)))
    closed_at: datetime | None = Field(default=None, sa_column=Column(DateTime(timezone=True)))
    opening_float: Decimal = Field(max_digits=10, decimal_places=2)
    counted_cash: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    variance: Decimal | None = Field(default=None, max_digits=10, decimal_places=2)
    by_user_id: int = Field(foreign_key="app_user.id")