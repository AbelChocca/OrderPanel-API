from typing import Dict, Callable, Optional
from aiokafka.structs import ConsumerRecord

class KafkaEventRouter:
    def __init__(
            self,
            handlers: Dict[str, Callable]
            ):
        self.handlers: Dict[str, Callable] = handlers

    async def __call__(self, msg: ConsumerRecord) -> None:
        topic: str = msg.topic

        handler: Optional[Callable] = self.handlers.get(topic)
        if not handler:
            raise ValueError(f"There's not any handler about {topic}")

        await handler(msg)