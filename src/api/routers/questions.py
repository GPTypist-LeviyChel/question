from fastapi import FastAPI

app = FastAPI()


@app.get("/getQuestionById/{id}")
async def get_question_by_id(id):
    pass


@app.post("/createQuestion")
async def create_question():
    pass

@app.put("/updateQuestion")
async def update_question():
    pass

@app.delete("/deleteQuestion")
async def delete_question():
    pass
