from asyncio import run
from app.core.settings.pydantic_setitngs import settings

from app.infra.messaging.kafka.clients.event_router import KafkaEventRouter
from app.infra.messaging.kafka.clients.consumer import KafkaConsumer

from app.infra.messaging.kafka.handlers.orders.handle_order_created import handle_order_created


async def main() -> None:
    router: KafkaEventRouter = KafkaEventRouter(
        handlers={
            "order.created": handle_order_created
        }
    )

    consumer: KafkaConsumer = KafkaConsumer(
        topics=list(router.handlers.keys()),
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id="orders-worker",
        handler=router
    )

    await consumer.start()

if __name__ == "__main__":
    run(main())