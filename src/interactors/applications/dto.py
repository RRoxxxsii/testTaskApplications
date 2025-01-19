import datetime
from dataclasses import dataclass

from src.interactors.common.dto import BaseDTO


@dataclass(frozen=True)
class CreateApplicationDTO(BaseDTO):
    user_name: str
    description: str


@dataclass(frozen=True)
class GetApplicationDTO(BaseDTO):
    id: int
    user_name: str
    description: str
    created_at: datetime.datetime
