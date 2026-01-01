from app.infra.db.repositories.psql_base_repository import BaseRepository
from app.infra.db.models.order_model import OrderShippingTable

from app.domain.orders.entities.order_shipping_entity import OrderShippingEntity

class PSQLOrderShippingRepository(BaseRepository[OrderShippingEntity, OrderShippingTable]):
    pass