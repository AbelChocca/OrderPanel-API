from datetime import datetime, timezone
from typing import Optional, Union
from uuid import uuid4
from decimal import Decimal

class OrderEntity:
    def __init__(
            self,
            *,
            quantity: int,
            unit_price: Decimal,
            total_price: Decimal,
            created_at: datetime,
            tracking_token: str,
            status: str = "pending", 
            id: Optional[int] = None,
            product_id: Optional[int] = None
            ):
        self.quantity: int = quantity
        self.unit_price: Decimal = unit_price
        self.total_price: Decimal = total_price
        self.created_at: datetime = created_at
        self.status: str = status
        self.tracking_token: str = tracking_token
        self.id: Union[int, None] = id
        self.product_id: Union[int, None] = product_id
    
    @classmethod
    def create_new(cls, quantity: int, unit_price: int, user_id: Optional[int] = None):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if unit_price <= 0:
            raise ValueError("Unit price must be greater than zero")
        
        tracking_token: str = f"order-{uuid4()}-{user_id or 0}"

        total: Decimal = quantity * unit_price

        return cls(
            quantity=quantity,
            unit_price=unit_price,
            total_price=total,
            created_at=datetime.now(timezone.utc),
            status="pending",
            tracking_token=tracking_token
        )
    
    @classmethod
    def from_persistence(
        cls,
        *,
        id: int,
        quantity: int,
        unit_price: Decimal,
        total_price: Decimal,
        created_at: datetime,
        status: str,
        tracking_token: str,
        product_id: Optional[int] = None,
    ):
        return cls(
            id=id,
            quantity=quantity,
            unit_price=unit_price,
            total_price=total_price,
            created_at=created_at,
            status=status,
            tracking_token=tracking_token,
            product_id=product_id,
        )