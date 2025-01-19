import datetime

from fastapi import APIRouter, Depends
from starlette import status

from src.controllers.applications.schemas.request import (
    CreateApplicationSchema,
)
from src.controllers.applications.schemas.response import (
    CreateApplicationResponseSchema,
    GetApplicationResponseSchema,
)
from src.controllers.di.services import get_application_service
from src.interactors.applications.dto import CreateApplicationDTO
from src.interactors.applications.interactor import ApplicationInteractor

router = APIRouter(prefix="/v1/applications", tags=["Заявки"])


@router.post(
    "/",
    summary="Создание заявки",
    responses={
        status.HTTP_201_CREATED: {
            "description": "Заявка успешно создана",
            "content": {
                "application/json": {
                    "example": [
                        CreateApplicationResponseSchema(
                            id=1,
                            user_name="user_1234",
                            description="Hello world!",
                            created_at=datetime.datetime.now(),
                        ).model_dump()
                    ]
                }
            },
        },
    },
    status_code=status.HTTP_201_CREATED,
)
async def create_application(
    schema: CreateApplicationSchema,
    service: ApplicationInteractor = Depends(get_application_service),
) -> CreateApplicationResponseSchema:
    application = await service.create_application(
        CreateApplicationDTO(
            user_name=schema.user_name, description=schema.description
        )
    )

    return CreateApplicationResponseSchema(
        id=application.id,
        user_name=application.user_name,
        description=application.description,
        created_at=application.created_at,
    )


@router.get(
    "/",
    summary="Получение списка заявок",
    responses={
        status.HTTP_200_OK: {
            "description": "Заявка успешно создана",
            "content": {
                "application/json": {
                    "example": [
                        [
                            CreateApplicationResponseSchema(
                                id=1,
                                user_name="user_1234",
                                description="Hello world!",
                                created_at=datetime.datetime.now(),
                            ).model_dump(),
                        ]
                    ]
                }
            },
        },
    },
    status_code=status.HTTP_200_OK,
)
async def get_applications(
    page: int,
    size: int,
    filter_user_name: str | None = None,
    service: ApplicationInteractor = Depends(get_application_service),
) -> list[GetApplicationResponseSchema]:
    applications = await service.get_all(page, size, filter_user_name)
    return [
        GetApplicationResponseSchema(
            id=application.id,
            user_name=application.user_name,
            description=application.description,
            created_at=application.created_at,
        )
        for application in applications
    ]
