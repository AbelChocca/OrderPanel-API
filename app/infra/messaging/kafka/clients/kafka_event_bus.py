from app.infra.messaging.event_bus import EventBus
from app.infra.messaging.kafka.clients.producer import KafkaProducer, kafka_producer
from functools import lru_cache

from typing import Dict, Any

class KafkaEventBus(EventBus):
    def __init__(self, producer: KafkaProducer):
        self._producer: KafkaProducer = producer

    async def publish(self, event_name: str, payload: Dict[str, Any]):
        return await self._producer.publish(topic=event_name, value=payload)
    
@lru_cache
def get_kafka_event_bus() -> KafkaEventBus:
    return KafkaEventBus(kafka_producer)