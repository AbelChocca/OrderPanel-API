from sqlmodel.ext.asyncio.session import AsyncSession

from app.infra.db.repositories.psql_order_repository import PSQLOrderRepository
from app.infra.db.repositories.psql_order_shipping_repository import PSQLOrderShippingRepository
from app.infra.db.repositories.psql_product_repository import PSQLProductRepository

from app.infra.db.mappers.order_mapper import OrderMapper

from app.infra.db.models.order_model import OrderTable, OrderShippingTable

from app.domain.orders.entities.order_entity import OrderEntity
from app.domain.orders.entities.order_shipping_entity import OrderShippingEntity
from app.domain.products.entity import ProductEntity

class RepositoryFactory:
    def __init__(
            self,
            db_session: AsyncSession
            ):
        self.db_session: AsyncSession = db_session

    def get_order_repository(self) -> PSQLOrderRepository:
        return PSQLOrderRepository(
            db_session=self.db_session,
            model_table=OrderTable,
            mapper=OrderMapper
        )