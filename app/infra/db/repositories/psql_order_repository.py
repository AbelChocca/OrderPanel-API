from app.infra.db.repositories.psql_base_repository import BaseRepository
from app.infra.db.models.order_model import OrderTable

from app.domain.orders.entities.order_entity import OrderEntity

class PSQLOrderRepository(BaseRepository[OrderEntity, OrderTable]):
    pass