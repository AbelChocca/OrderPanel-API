from strawberry import input
from typing import Optional

@input
class CreateOrderInput:
    quantity: int
    unit_price: float
    product_id: int
    
    #Order shipping info
    full_name: str
    phone: str
    address_line: str
    city: str
    region: str
    country: str
    postal_code: Optional[int] = None
    delivery_notes: Optional[str] = None

    user_id: Optional[int] = None