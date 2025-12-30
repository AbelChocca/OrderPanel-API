
from typing import Optional, Union

class ProductEntity:
    def __init__(
            self,
            name: str,
            price: float,
            image_url: str,
            total_orders: int = 0,
            id: Optional[int] = None,
            ):
        self.name: str = name
        self.price: float = price
        self.image_url: str = image_url
        self.total_order: int = total_orders
        self.id: Union[int, None] = id