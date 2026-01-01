from dataclasses import dataclass

from app.infra.db.repositories.psql_order_repository import PSQLOrderRepository

@dataclass
class GraphQLContext:
    order_repo: PSQLOrderRepository

async def get_context() -> GraphQLContext:
    pass