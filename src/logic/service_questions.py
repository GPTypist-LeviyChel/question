from typing import List, Optional

from fastapi import HTTPException, status

from src.crud.crud_questions import crud_questions
from src.schemas.questions import QuestionCreate, QuestionData, QuestionUpdate
from src.enums.errors import QuestionErrors
from src.serializer import serialize_question


async def get_question_by_id(account_id: int) -> Optional[QuestionData]:
    """Get question by id."""
    question = await crud_questions.get(account_id)
    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=QuestionErrors.question_not_found.value
        )

    return serialize_question.prepare_question_data(question)


async def create_question(question_create: QuestionCreate) -> QuestionData:
    """Create question."""

    question = await crud_questions.create(question_create)
    return serialize_question.prepare_question_data(question)


async def update_question(question_id: int,
                          question_update: QuestionUpdate) -> QuestionData:
    """Update question."""
    question = await crud_questions.update(question_id, question_update)

    return serialize_question.prepare_question_data(question)


async def get_list_question() -> List[QuestionData]:
    """Get list question."""
    questions = await crud_questions.get_list()

    return [serialize_question.prepare_question_data(question)
            for question in questions]


async def delete_question(question_id: int) -> None:
    """Delete question."""
    await crud_questions.remove(question_id)
