from src.models.questions import Question
from src.schemas.questions import QuestionData


def prepare_question_data(account: Question) -> QuestionData:
    return QuestionData.from_orm(account)
