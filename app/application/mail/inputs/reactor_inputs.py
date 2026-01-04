from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from typing import Optional

@dataclass
class SendMailOfOrderCommand:
    #order
    quantity: int
    total_price: Decimal
    created_at: datetime
    tracking_token: str
    status: str
    
    #shipping
    full_name: str
    email: str
    address_line: str
    city: str
    region: str
    country: str
    postal_code: Optional[int] = None,
    delivery_notes: Optional[str] = None
