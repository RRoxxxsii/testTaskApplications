from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Generic, TypeVar

from src.interactors.applications.dto import GetApplicationDTO

RowType = TypeVar("RowType")


class AbstractApplicationMapper(ABC, Generic[RowType]):
    @abstractmethod
    def map_many_application_data(
        self, rows: Iterable[RowType]
    ) -> list[GetApplicationDTO]:
        raise NotImplementedError

    @abstractmethod
    def map_one_application_data(self, row: RowType) -> GetApplicationDTO:
        raise NotImplementedError
