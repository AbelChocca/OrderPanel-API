from typing import Dict, Any, List, Optional
from app.infra.messaging.kafka.clients.kafka_event_bus import get_kafka_event_bus

async def publish_event(topic: str, value: Dict[str, Any]) -> None:
    event_bus = get_kafka_event_bus()
    await event_bus.publish(
        event_name=topic,
        payload=value
    )

def get_next_topic(topics: List[str], current_topic: str) -> Optional[str]:
    current_topic_index: Optional[int] = None

    for index, topic in enumerate(topics):
        if topic == current_topic:
            current_topic_index = index

    if current_topic_index is None:
        return topics[0] # First value when current_topic is default event name
    
    return topics[current_topic_index + 1] if ((current_topic_index+1) < len(topics)) else None