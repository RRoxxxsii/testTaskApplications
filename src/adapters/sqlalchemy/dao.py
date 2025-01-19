from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.common.dao import AbstractApplicationDAO
from src.adapters.common.mapper import AbstractApplicationMapper
from src.adapters.sqlalchemy.models import ApplicationORM
from src.interactors.applications.dto import (
    CreateApplicationDTO,
    GetApplicationDTO,
)


class SQLAlchemyApplicationDAO(AbstractApplicationDAO[AsyncSession]):
    def __init__(
        self, session: AsyncSession, mapper: AbstractApplicationMapper
    ) -> None:
        super().__init__(session, mapper)

    async def get_all(
        self, limit: int, offset: int, filter_user_name: str | None
    ) -> list[GetApplicationDTO]:
        stmt = (
            select(
                ApplicationORM.id,
                ApplicationORM.user_name,
                ApplicationORM.description,
                ApplicationORM.created_at,
            )
            .order_by(ApplicationORM.created_at.desc())
            .limit(limit=limit)
            .offset(offset=offset)
        )
        if filter_user_name:
            stmt = stmt.where(ApplicationORM.user_name == filter_user_name)

        data = (await self._session.execute(stmt)).all()
        return self._mapper.map_many_application_data(data)

    async def create(self, dto: CreateApplicationDTO) -> GetApplicationDTO:
        obj = ApplicationORM(
            user_name=dto.user_name, description=dto.description
        )
        self._session.add(obj)
        await self._session.commit()
        await self._session.refresh(obj)
        return self._mapper.map_one_application_data(obj)
