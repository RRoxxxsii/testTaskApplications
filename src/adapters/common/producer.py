from abc import ABC, abstractmethod


class AbstractProducer(ABC):
    @abstractmethod
    async def publish(self, key: str, value: dict) -> None:
        raise NotImplementedError
