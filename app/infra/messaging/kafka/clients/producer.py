from aiokafka import AIOKafkaProducer
from app.infra.messaging.kafka.config import KafkaConfig
from app.infra.messaging.kafka.serializer import json_serializer

from app.core.settings.pydantic_setitngs import settings

from typing import Dict, Optional

class KafkaProducer:
    def __init__(self, config: KafkaConfig):
        self._producer: AIOKafkaProducer = AIOKafkaProducer(
            bootstrap_servers=config.bootstrap_servers,
            client_id=config.client_id,
            value_serializer=json_serializer
        )

    async def start(self):
        await self._producer.start()

    async def stop(self):
        await self._producer.stop()

    async def publish(
            self,
            topic: str,
            value: Dict,
            key: Optional[str] = None
    ) -> None:
        await self._producer.send_and_wait(
            topic=topic,
            value=value,
            key=key.encode() if key else None
        )
    
kafka_producer: KafkaProducer = KafkaProducer(
    KafkaConfig(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        client_id=settings.KAFKA_CLIENT_ID
    )
)