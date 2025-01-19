from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.ext.asyncio import create_async_engine as create_async_engine_

from src.config import Config


def create_async_engine(config: Config) -> AsyncEngine:
    return create_async_engine_(config.pg_dsn)


def create_async_pool(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False, autoflush=False)
