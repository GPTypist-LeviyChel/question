from src.models.questions import Question
from src.schemas.questions import QuestionData


def prepare_question_data(question: Question) -> QuestionData:
    return QuestionData.from_orm(question)
