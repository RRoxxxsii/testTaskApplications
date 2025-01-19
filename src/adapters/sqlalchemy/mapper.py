from collections.abc import Iterable

from sqlalchemy import Row

from src.adapters.common.mapper import AbstractApplicationMapper
from src.interactors.applications.dto import GetApplicationDTO


class SQLAlchemyApplicationMapper(AbstractApplicationMapper[Row]):
    def map_many_application_data(
        self, rows: Iterable[Row]
    ) -> list[GetApplicationDTO]:
        return [
            GetApplicationDTO(
                id=row.id,
                user_name=row.user_name,
                description=row.description,
                created_at=row.created_at,
            )
            for row in rows
        ]

    def map_one_application_data(self, row: Row) -> GetApplicationDTO:
        return GetApplicationDTO(
            id=row.id,
            user_name=row.user_name,
            description=row.description,
            created_at=row.created_at,
        )
