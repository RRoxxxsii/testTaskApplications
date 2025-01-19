from src.adapters.common.dao import AbstractApplicationDAO
from src.adapters.common.producer import AbstractProducer


class CommonApplicationInteractor:
    def __init__(
        self, dao: AbstractApplicationDAO, producer: AbstractProducer
    ):
        self._dao = dao
        self._producer = producer
