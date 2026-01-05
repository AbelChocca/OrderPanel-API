from aiokafka.consumer import AIOKafkaConsumer
from typing import Iterable

from app.infra.messaging.kafka.clients.event_router import KafkaEventRouter

class KafkaConsumer:
    def __init__(
            self,
            topics: Iterable[str],
            bootstrap_servers: str,
            handler: KafkaEventRouter,
            group_id: str
            ):
        self.consumer: AIOKafkaConsumer = AIOKafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            enable_auto_commit=False
        )
        self.handler: KafkaEventRouter = handler

    async def start(self) -> None:
        await self.consumer.start()
        try:
            async for msg in self.consumer:
                await self.handler(msg)
                await self.consumer.commit()
        finally:
            await self.consumer.stop()