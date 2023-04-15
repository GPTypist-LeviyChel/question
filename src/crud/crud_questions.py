from typing import List

from src.crud.base import CRUDBase
from src.models.questions import Question
from src.schemas.questions import QuestionCreate, QuestionUpdate


class CRUDQuestion(CRUDBase[Question, QuestionCreate, QuestionUpdate]):

    async def get_list(self) -> List[Question]:
        return await self.model.all()


crud_questions = CRUDQuestion(Question)
