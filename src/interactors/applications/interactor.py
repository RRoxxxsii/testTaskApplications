from src.adapters.common.dao import AbstractApplicationDAO
from src.adapters.common.producer import AbstractProducer
from src.adapters.paginator import LimitOffsetPaginator
from src.interactors.applications.dto import (
    CreateApplicationDTO,
    GetApplicationDTO,
)
from src.interactors.common.interactor import CommonApplicationInteractor


class ApplicationInteractor(CommonApplicationInteractor):
    def __init__(
        self, dao: AbstractApplicationDAO, producer: AbstractProducer
    ):
        super().__init__(dao, producer)

    async def create_application(
        self, dto: CreateApplicationDTO
    ) -> GetApplicationDTO:
        application = await self._dao.create(dto)
        await self._producer.publish(key="message", value=dto.dict())
        return application

    async def get_all(
        self, page: int, size: int, filter_user_name: str | None
    ) -> list[GetApplicationDTO]:
        limit_offset = LimitOffsetPaginator(page=page, size=size).execute()
        return await self._dao.get_all(
            limit=limit_offset.limit,
            offset=limit_offset.offset,
            filter_user_name=filter_user_name,
        )
