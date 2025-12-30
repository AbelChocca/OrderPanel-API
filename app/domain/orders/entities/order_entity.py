from datetime import datetime
from typing import Optional, Union
from uuid import uuid4

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

    def generate_tracking_token(self, user_id: Optional[int] = None) -> str:
        return f"order-{uuid4()}-{user_id if user_id is not None else 0}"