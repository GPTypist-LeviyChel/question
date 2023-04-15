from datetime import datetime
from pydantic import BaseModel, Field
from src.enums.topic import QuestionTopic


class QuestionBase(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    topic: QuestionTopic
    image_url: str = Field(min_length=1, max_length=500, null=True)


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass


class QuestionData(QuestionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
