from app.infra.db.repositories.psql_order_repository import PSQLOrderRepository
from app.infra.messaging.event_bus import EventBus

from app.domain.orders.entities.order_entity import OrderEntity
from app.domain.orders.entities.order_shipping_entity import OrderShippingEntity

from app.application.orders.inputs.command_inputs import CreateOrderCommad

class CreateOrderCase:
    def __init__(
            self,
            order_repo: PSQLOrderRepository,
            event_bus: EventBus
            ):
        self.order_repo: PSQLOrderRepository = order_repo
        self.event_bus: EventBus = event_bus

    async def execute(self, command: CreateOrderCommad):
        #TODO: args incompleted on event bus publisher and incompleted implementation
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

        await self.event_bus.publish(
            event_name="orders.created",
            payload={
                "event_name": "OrderCreated",
                "version": "v1",
                "payload": {
                    "quantity": order.quantity,
                    "total_price": order.total_price,
                    "created_at": order.created_at,
                    "tracking_token": order.tracking_token,
                    "status": order.status,
                    "full_name": order_shipping.full_name,
                    "email": order_shipping.email,
                    "address_line": order_shipping.address_line,
                    "city": order_shipping.city,
                    "region": order_shipping.region,
                    "country": order_shipping.country,
                    "postal_code": order_shipping.postal_code,
                    "delivery_notes": order_shipping.delivery_notes
                }
            }
        )
        
