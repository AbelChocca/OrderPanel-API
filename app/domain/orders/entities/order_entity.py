from datetime import datetime
from typing import Optional, Union

class OrderEntity:
    def __init__(
            self,
            tracking_token: str,
            quantity: int,
            unit_price: float,
            total_price: float,
            created_at: datetime,
            status: str = "pending", 
            id: Optional[int] = None,
            product_id: Optional[int] = None
            ):
        self.tracking_token: str = tracking_token
        self.quantity: int = quantity
        self.unit_price: float = unit_price
        self.total_price: float = total_price
        self.created: datetime = created_at
        self.status: str = status
        self.id: Union[int, None] = id
        self.product_id: Union[int, None] = product_id