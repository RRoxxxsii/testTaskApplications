import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    pg_dsn: str = os.getenv("PG_DSN")
    bootstrap_servers: str = os.getenv("BOOTSTRAP_SERVERS")
    application_topic: str = os.getenv("APPLICATION_TOPIC")


def get_config() -> Config:
    return Config()
