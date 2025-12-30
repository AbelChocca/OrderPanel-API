from sqlmodel import SQLModel, Field
from sqlalchemy import DateTime, Column
from datetime import datetime, timezone

from typing import Optional

class OrderTable(SQLModel, table=True):
    __tablename__= "orders"

    id: Optional[int] = Field(default=None, foreign_key=True)
    product_id: int = Field(foreign_key="products.id")

    tracking_token: str = Field(nullable=False)
    quantity: int = Field(nullable=False)
    status: str = Field(default="pending", nullable=False)
    unit_price: float = Field(nullable=False)
    total_price: float = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column=Column(DateTime(timezone=True)))

class OrderShippingTable(SQLModel, table=True):
    __tablename__="orders_shipping"

    id: Optional[int] =Field(default=None, foreign_key=True)
    order_id: int = Field(foreign_key="orders.id")
    
    full_name: str = Field(nullable=False, min_length=2, max_length=55)
    phone: str = Field(nullable=False, max_length=15)
    address_line: str = Field(max_length=255, nullable=False)
    city: str = Field(nullable=False, max_length=55)
    region: str = Field(nullable=False, max_length=55)
    country: str = Field(nullable=False, max_length=55)
    postal_code: Optional[str] = Field(default=None)
    delivery_notes: Optional[str] = Field(default=None, max_length=526)
