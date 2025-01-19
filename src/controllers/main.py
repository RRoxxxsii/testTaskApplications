from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.adapters.sqlalchemy.main import create_async_engine, create_async_pool
from src.config import get_config
from src.controllers.applications.router import router as application_router
from src.controllers.di.providers import (
    AIOKafkaProvider,
    ApplicationDAOProvider,
    get_dao,
    get_producer,
)


def build_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:8080"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_routers(app: FastAPI) -> None:
    app.include_router(application_router)


def setup_dependencies(app: FastAPI) -> None:
    config = get_config()
    engine = create_async_engine(config)
    pool = create_async_pool(engine)
    dao_session_provider = ApplicationDAOProvider(pool)
    aio_kafka_provider = AIOKafkaProvider(
        bootstrap_servers=config.bootstrap_servers,
        topic=config.application_topic,
    )

    app.dependency_overrides[
        get_dao
    ] = dao_session_provider.provide_dao  # noqa
    app.dependency_overrides[
        get_producer
    ] = aio_kafka_provider.provide_kafka  # noqa


def build_app() -> FastAPI:
    app = FastAPI()

    include_routers(app)
    setup_dependencies(app)
    build_middlewares(app)

    return app
