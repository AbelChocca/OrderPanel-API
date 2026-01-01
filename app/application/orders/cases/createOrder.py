from app.infra.db.repositories.psql_order_repository import PSQLOrderRepository

from app.domain.orders.entities.order_entity import OrderEntity
from app.domain.orders.entities.order_shipping_entity import OrderShippingEntity

from app.application.orders.commands import CreateOrderCommad

class CreateOrderCase:
    def __init__(
            self,
            order_repo: PSQLOrderRepository,
            ):
        self.order_repo: PSQLOrderRepository = order_repo

    async def execute(self, command: CreateOrderCommad):
        order: OrderEntity = OrderEntity.create_new(
            quantity=command.quantity,
            unit_price=command.unit_price,
            user_id=command.user_id
        )

        order_shipping: OrderShippingEntity = OrderShippingEntity.create_new(
            full_name=command.full_name,
            phone=command.phone,
            address_line=command.address_line,
            city=command.city,
            region=command.region,
            country=command.country,
            postal_code=command.postal_code,
            delivery_notes=command.delivery_notes
        )

        order = await self.order_repo.save(order)
        
