from typing import List

from tortoise.contrib.postgres.functions import Random

from src.crud.base import CRUDBase
from src.models.questions import Question
from src.schemas.questions import QuestionCreate, QuestionUpdate


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):

    async def get_list(self, limit: int) -> List[Question]:
        return await self.model.annotate(order=Random())\
            .all()\
            .order_by('order')\
            .limit(limit)


crud_questions = CRUDQuestion(Question)
