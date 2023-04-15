from fastapi import APIRouter

from src.api.routers.questions import app as question_router

api_router = APIRouter()


api_router.include_router(question_router, tags=["questions"])
