
from typing import Optional, Union

class OrderShippingEntity:
    def __init__(
            self,
            full_name: str,
            phone: str,
            address_line: str,
            city: str,
            region: str,
            country: str,
            postal_code: Optional[int] = None,
            delivery_notes: Optional[str] = None,
            id: Optional[int] = None,
            order_id: Optional[int] = None
            ):
        self.full_name: str = full_name
        self.phone: str = phone
        self.address_line: str = address_line
        self.city: str = city
        self.region: str = region
        self.country: str = country
        self.postal_code: int = postal_code
        self.delivery_notes: str = delivery_notes
        self.id: Union[int, None] = id
        self.order_id: Union[int, None] = order_id
        