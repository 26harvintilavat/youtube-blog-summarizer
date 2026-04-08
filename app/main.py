import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI 

from app.api.routes.health import router as health_router
from app.api.routes.summarize import router as summarize_router
from app.core.config import settings
from app.core.exceptions import ConfigurationError
from app.core.logging_config import setup_logging

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger = logging.getLogger(__name__)

    if not settings.GOOGLE_API_KEY:
        raise ConfigurationError("GOOGLE_API_KEY is missing in environment variables.")

    logger.info("Starting application %s v%s", settings.APP_NAME, settings.APP_VERSION)
    yield
    logger.info("Shutting down application")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Summarize YouTube videos and blog articles using LangChain + Gemini",
    lifespan=lifespan,
)

app.include_router(health_router, prefix="/api")
app.include_router(summarize_router, prefix="/api")