from app.infra.db.config.base import engine
from sqlmodel.ext.asyncio.session import AsyncSession

from typing import AsyncGenerator

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session