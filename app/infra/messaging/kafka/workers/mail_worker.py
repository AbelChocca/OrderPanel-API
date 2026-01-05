from asyncio import run

from app.infra.messaging.kafka.clients.consumer import KafkaConsumer
from app.infra.messaging.kafka.clients.event_router import KafkaEventRouter
from app.core.settings.pydantic_setitngs import settings

from app.infra.messaging.kafka.handlers.mail.handle_order_created import handle_order_created

async def main():
    router: KafkaEventRouter = KafkaEventRouter(
        handlers={
            "mail.order_created": handle_order_created,
            "mail.order_created.retry.10s": handle_order_created,
            "mail.order_created.retry.20s": handle_order_created,
            "mail.order_created.retry.30s": handle_order_created,
        }
    )
    consumer: KafkaConsumer = KafkaConsumer(
        topics=list(router.handlers.keys()),
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        handler=router,
        group_id="mail-workers"
    )

    await consumer.start()


if __name__ == "__main__":
    run(main())