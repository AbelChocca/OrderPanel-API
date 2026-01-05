from strawberry import type, field
from typing import Any

from app.api.graphql.mutations.orders.input import CreateOrderInput

from app.application.orders.commands.createOrder import CreateOrderCase

# TODO: there was incomplete mutation
@type
class OrderMutation:
    @field
    async def create_order(self, info, input: CreateOrderInput) -> Any:
        case: CreateOrderCase = CreateOrderCase(
            order_repo=info
        )
