from sqlmodel import SQLModel, Field

from typing import Optional

class ProductTable(SQLModel, table=True):
    __tablename__= "products"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False, min_length=2, max_length=55)
    price: float = Field(nullable=False, le=4999, ge=1)
    image_url: str = Field(nullable=False)

    total_orders: int = Field(default=0)