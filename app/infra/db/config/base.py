from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio.engine import AsyncEngine, create_async_engine

from app.core.settings.pydantic_setitngs import settings

engine: AsyncEngine = create_async_engine(url=settings.DA, echo=False)

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)