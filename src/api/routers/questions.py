from fastapi import APIRouter, status

from src.api.const import USER_BASE_RESPONSES
from src.enums.base import BaseMessage
from src.enums.errors import QuestionErrors
from src.logic import service_questions
from src.schemas.questions import QuestionCreate, QuestionData, QuestionUpdate
from src.schemas.base import MessageErrorSchema

from src.logger import get_logger

logger = get_logger()

app = APIRouter()


@app.get(
    "/getQuestionById/{question_id}",
    summary='Get question by id',
    status_code=status.HTTP_200_OK,
    response_model=QuestionData,
    responses={
        **USER_BASE_RESPONSES,
        status.HTTP_200_OK: {"description": BaseMessage.obj_data.value},
        status.HTTP_404_NOT_FOUND: {
            "model": MessageErrorSchema,
            "description": QuestionErrors.question_not_found.docs_response
        },
    }
)
async def get_question_by_id(question_id: int):
    return await service_questions.get_question_by_id(question_id)


@app.get('/getQuestions/{count}',
            summary='Get questions',
            status_code=status.HTTP_200_OK,
            response_model=list[QuestionData],
            responses={
                **USER_BASE_RESPONSES,
                status.HTTP_200_OK: {"description": BaseMessage.obj_data.value},
            }
            )
async def get_questions(count: int):
    return await service_questions.get_list_question(count)

@app.post("/createQuestion",
          summary='Create question',
          status_code=status.HTTP_201_CREATED,
          response_model=QuestionData,
          responses={
              status.HTTP_201_CREATED: {
                  "description": BaseMessage.obj_is_created.value}
          },
          )
async def create_question(question_create: QuestionCreate) -> QuestionData:
    return await service_questions.create_question(question_create)


@app.post("/updateQuestion",
         summary='Update question',
         status_code=status.HTTP_200_OK,
         response_model=QuestionData,
         responses={
             status.HTTP_200_OK: {
                 "description": BaseMessage.obj_is_created.value},
             status.HTTP_404_NOT_FOUND: {
                 "model": MessageErrorSchema,
                 "description": QuestionErrors.question_not_found.docs_response
             }
         },
         )
async def update_question(question_id: int, question_update: QuestionUpdate) \
        -> QuestionData:
    return await service_questions.update_question(question_id, question_update)


@app.delete("/deleteQuestion",
            summary='Delete question',
            status_code=status.HTTP_200_OK,
            responses={
                status.HTTP_200_OK: {
                    "description": BaseMessage.obj_is_created.value},
                status.HTTP_404_NOT_FOUND: {
                    "model": MessageErrorSchema,
                    "description": QuestionErrors.question_not_found.docs_response
                }
            },
            )
async def delete_question(question_id: int):
    await service_questions.delete_question(question_id)
