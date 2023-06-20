from typing import TypeVar
from uuid import UUID

from pydantic import BaseModel

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class UpdatedBase(BaseModel):
    id: UUID
    updated_fields: dict


class Message(BaseModel):
    msg: str


class DetailError(BaseModel):
    msg: str
    type: str


class MessageErrorSchema(BaseModel):
    detail: DetailError
