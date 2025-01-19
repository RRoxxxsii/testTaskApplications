from pydantic import BaseModel


class CreateApplicationSchema(BaseModel):
    user_name: str
    description: str
