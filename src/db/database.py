from tortoise import Tortoise
from src.core.config import settings

MODELS_LIST = ["src.models.questions"]


async def postgres_db_init() -> None:
    await Tortoise.init(
        db_url=settings.POSTGRES_URI,
        modules={'models': MODELS_LIST}
    )

    await Tortoise.generate_schemas()
