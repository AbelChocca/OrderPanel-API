from abc import ABC, abstractmethod

from app.domain.products.entity import ProductEntity

class ProductRepository(ABC):
    @abstractmethod
    async def save(self, product: ProductEntity) -> ProductEntity:
        pass

    @abstractmethod
    async def get_by_id(self, product_id: int) -> ProductEntity:
        pass

    @abstractmethod
    async def delete(self, product_id: int) -> ProductEntity:
        pass