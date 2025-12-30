from abc import ABC, abstractmethod
from sqlmodel import SQLModel
from typing import TypeVar, Generic, Optional

E = TypeVar("E")
M = TypeVar("M", bound=SQLModel)

class BaseMapper(Generic[E, M], ABC):
    @staticmethod
    @abstractmethod
    def model_to_entity(model: M) -> E:
        ...

    @staticmethod
    @abstractmethod
    def entity_to_model(entity: E, existing_model: Optional[M] = None) -> M:
        ...
