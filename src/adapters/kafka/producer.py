import json

from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError

from src.adapters.common.producer import AbstractProducer


class CustomAIOKafkaProducer(AbstractProducer):
    def __init__(self, bootstrap_servers: str, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = None

    async def start(self) -> None:
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers
        )
        await self.producer.start()

    async def publish(self, key: str, value: dict) -> None:
        if not self.producer:
            raise RuntimeError(
                "Продюсер не был запущен. "
                "Для запуска вызовите метод `start`"
            )
        try:
            value_as_bytes = json.dumps(value).encode("utf-8")
            key_as_bytes = key.encode("utf-8") if key else None

            result = await self.producer.send_and_wait(
                self.topic, key=key_as_bytes, value=value_as_bytes
            )
            print(
                f"Сообщение отправлено в {self.topic} "
                f"| Смещение: {result.offset}"
            )
        except KafkaError as e:
            print(f"Ошибка при попытке отправить запрос: {e}")
