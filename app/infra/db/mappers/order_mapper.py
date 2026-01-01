from app.infra.db.mappers.base_mapper import BaseMapper
from app.infra.db.models.order_model import OrderTable

from app.domain.orders.entities.order_entity import OrderEntity

from typing import Optional

class OrderMapper(BaseMapper[OrderEntity, OrderTable]):
    @staticmethod
    def model_to_entity(model: OrderTable) -> OrderEntity:
        return OrderEntity.from_persistence(
            id=model.id,
            quantity=model.quantity,
            unit_price=model.unit_price,
            total_price=model.total_price,
            created_at=model.created_at,
            status=model.status,
            tracking_token=model.tracking_token,
            product_id=model.product_id
        )
    
    @staticmethod
    def entity_to_model(entity: OrderEntity, existing_model: Optional[OrderTable] = None):
        if existing_model is not None:
            existing_model.quantity = entity.quantity
            existing_model.unit_price = entity.unit_price
            existing_model.total_price = entity.total_price
            existing_model.created_at = entity.created_at
            existing_model.status = entity.status
            existing_model.tracking_token = entity.tracking_token
            return existing_model
        return OrderTable(
            tracking_token=entity.tracking_token,
            quantity=entity.quantity,
            status=entity.status,
            unit_price=entity.unit_price,
            total_price=entity.total_price,
            created_at=entity.created_at,
            product_id=entity.product_id
        )