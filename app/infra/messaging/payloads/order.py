from typing import TypedDict, Optional
from decimal import Decimal
from datetime import datetime

class OrderCreatedInfo(TypedDict):
    quantity: int
    total_price: Decimal
    created_at: datetime
    tracking_token: str
    status: str
    full_name: str
    email: str
    address_line: str
    city: str
    region: str
    country: str
    postal_code: Optional[int] = None
    delivery_notes: Optional[str] = None

class OrderCreatedPayload(TypedDict):
    event_name: str
    version: str
    info: OrderCreatedInfo