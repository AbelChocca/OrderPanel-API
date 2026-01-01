from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Generic, TypeVar, Optional, Protocol

from app.infra.db.mappers.base_mapper import BaseMapper
from app.infra.db.exceptions import ModelNotFound, DatabaseException

class HasId(Protocol):
    id: Optional[int]

E = TypeVar("E", bound=HasId)
M = TypeVar("M", bound=SQLModel)

class BaseRepository(Generic[E, M]):
    def __init__(
            self,
            db_session: AsyncSession,
            model_table: Type[M],
            mapper: BaseMapper[E, M]
            ):
        self.db_session: AsyncSession = db_session
        self.model_table: Type[M] = model_table
        self.mapper: BaseMapper = mapper

    async def get_model_but_not_raises(self, model_id: int) -> Optional[M]:
        model: Optional[M] = await self.db_session.get(self.model_table, model_id)

        return model

    async def get_by_id(self, model_id: int) -> E:
        try:
            model: Optional[M] = await self.db_session.get(self.model_table, model_id)

            if not model:
                raise ModelNotFound(f"The model: {self.model_table.__name__} with id: {model_id} wasn't found.")
            
            return self.mapper.model_to_entity(model)
        except SQLAlchemyError as s:
            raise DatabaseException(f"Cannot get the model: {self.model_table.__name__} with id: {model_id}, internal server error: {str(s)}") from s

    async def save(self, entity: E) -> E:
        try:
            existing_model: Optional[M] = None
            if entity.id is not None:
                existing_model = await self.get_model_but_not_raises(entity.id)
            
            new_model: M = self.mapper.entity_to_model(
                entity=entity,
                existing_model=existing_model
            )

            self.db_session.add(new_model)
            await self.db_session.commit()
            await self.db_session.refresh(new_model)
            return self.mapper.model_to_entity(new_model)
        except SQLAlchemyError as s:
            await self.db_session.rollback()
            raise DatabaseException(f"Cannot save the model: {self.model_table}: {str(s)}") from s
    