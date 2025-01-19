from fastapi import Depends

from src.adapters.common.dao import AbstractApplicationDAO
from src.adapters.common.producer import AbstractProducer
from src.controllers.di.providers import get_dao, get_producer
from src.interactors.applications.interactor import ApplicationInteractor


def get_application_service(
    dao: AbstractApplicationDAO = Depends(get_dao),
    producer: AbstractProducer = Depends(get_producer),
) -> ApplicationInteractor:
    return ApplicationInteractor(dao, producer)
