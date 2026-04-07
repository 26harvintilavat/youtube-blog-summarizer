from fastapi import FastAPI 
from app.api.routes.health import router as health_router
from app.api.routes.summarize import router as summarize_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Summarize YouTube videos and blog articles using LangChain + Gemini"
)

app.include_router(health_router, prefix="/api")
app.include_router(summarize_router, prefix="/api")