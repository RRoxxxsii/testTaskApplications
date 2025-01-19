from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.adapters.common.mapper import AbstractApplicationMapper
from src.interactors.applications.dto import (
    CreateApplicationDTO,
    GetApplicationDTO,
)

SessionType = TypeVar("SessionType")
Model = TypeVar("Model")


class AbstractApplicationDAO(ABC, Generic[SessionType]):
    def __init__(
        self, session: SessionType, mapper: AbstractApplicationMapper
    ):
        self._session = session
        self._mapper = mapper

    @abstractmethod
    async def get_all(
        self, limit: int, offset: int, filter_user_name: str | None
    ) -> list[GetApplicationDTO]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, dto: CreateApplicationDTO) -> GetApplicationDTO:
        raise NotImplementedError
