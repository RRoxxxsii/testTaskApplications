import datetime

from pydantic import BaseModel


class CreateApplicationResponseSchema(BaseModel):
    id: int
    user_name: str
    description: str
    created_at: datetime.datetime


class GetApplicationResponseSchema(BaseModel):
    id: int
    user_name: str
    description: str
    created_at: datetime.datetime
