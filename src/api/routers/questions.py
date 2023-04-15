from fastapi import FastAPI
from src.logic import service_questions
from src.schemas.questions import QuestionCreate, QuestionUpdate

app = FastAPI()


@app.get("/getQuestionById/{id}")
async def get_question_by_id(id: int):
    return service_questions.get_question_by_id(id)


@app.post("/createQuestion")
async def create_question(question_create: QuestionCreate):
    return service_questions.create_question(question_create)


@app.put("/updateQuestion")
async def update_question(question_id: int, question_update: QuestionUpdate):
    return service_questions.update_question(question_id, question_update)


@app.delete("/deleteQuestion")
async def delete_question(question_id: int):
    await service_questions.delete_question(question_id)
