from typing import Dict, Protocol, Any

class EventBus(Protocol):
    async def publish(self, event_name: str, payload: Dict[str, Any]) -> None:
        ...