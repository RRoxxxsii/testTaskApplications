from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.adapters.kafka.producer import CustomAIOKafkaProducer
from src.adapters.sqlalchemy.dao import SQLAlchemyApplicationDAO
from src.adapters.sqlalchemy.mapper import SQLAlchemyApplicationMapper


def get_dao():
    pass


def get_producer():
    pass


class ApplicationDAOProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def provide_dao(
        self,
    ) -> AsyncGenerator[SQLAlchemyApplicationDAO, None]:
        async with self.pool() as session:
            yield SQLAlchemyApplicationDAO(
                session, SQLAlchemyApplicationMapper()
            )


class AIOKafkaProvider:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    async def provide_kafka(self):
        kafka = CustomAIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers, topic=self.topic
        )
        await kafka.start()
        return kafka
