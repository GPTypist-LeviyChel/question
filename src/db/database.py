from tortoise import Tortoise
from src.core.config import settings
from src.logger import get_logger

MODELS_LIST = ["src.models.questions"]


async def postgres_db_init() -> None:
    logger = get_logger()
    logger.debug(settings.POSTGRES_URI)
    await Tortoise.init(
        db_url=settings.POSTGRES_URI,
        modules={'models': MODELS_LIST}
    )

    await Tortoise.generate_schemas()
