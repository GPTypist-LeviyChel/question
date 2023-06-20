from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, HttpUrl
from src.enums.topic import QuestionTopic


class QuestionBase(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    topic: QuestionTopic
    image_url: Optional[HttpUrl] = None


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    text: Optional[str] = Field(min_length=1, max_length=500)
    topic: Optional[QuestionTopic]
    image_url: Optional[HttpUrl]


class QuestionData(QuestionBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
