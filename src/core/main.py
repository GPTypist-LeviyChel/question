import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from src.core import middleware
from src.core.config import settings
from src.core.urls import api_router
from src.db.database import postgres_db_init
from src.logger import get_logger

logger = get_logger()

app = FastAPI(
    version='2.0',
    docs_url='/questions/docs',
    openapi_url='/questions/openapi.json',
    openapi_prefix='/api',
    middleware=middleware.utils
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event("startup")
async def connect_db() -> None:
    logger.debug("Connection to Postgres...")
    await postgres_db_init()


app.include_router(api_router, prefix=settings.API_URL)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=7040, log_level="debug")