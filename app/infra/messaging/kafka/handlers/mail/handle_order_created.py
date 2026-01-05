from aiokafka import ConsumerRecord
from json import loads
from typing import Dict, Optional
from asyncio import sleep

from app.infra.messaging.payloads.order import OrderCreatedPayload, OrderCreatedInfo
from app.infra.mail.client import get_mail_service
from app.infra.messaging.kafka.helpers import publish_event, get_next_topic

from app.application.mail.templates.order_confirmation.helper import render_order_confirmation_html



RETRY_DELAYS: Dict[str, int] = {
    "mail.order_created.retry.10s": 10,
    "mail.order_created.retry.20s": 20,
    "mail.order_created.retry.30s": 30,
}

async def handle_order_created(msg: ConsumerRecord) -> None:
    payload: OrderCreatedPayload = loads(msg.value)
    info: OrderCreatedInfo = payload['info']
    delay: Optional[int] = RETRY_DELAYS.get(msg.topic, None)

    if delay is not None:
        await sleep(delay)
    
    email_client = get_mail_service()

    html_content: str = render_order_confirmation_html(info)

    try:
        email_client.send_email(
            to_email=info['email'],
            subject="Order Confirmation",
            html_content=html_content
        )
    except Exception as e:
        next_topic: Optional[str] = get_next_topic(
            topics=list(RETRY_DELAYS.keys()), 
            current_topic=msg.topic
            )
        if next_topic:
            await publish_event(
                topic=next_topic,
                value=payload
            )

        # Do not DQL for now