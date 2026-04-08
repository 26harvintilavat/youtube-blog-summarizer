from functools import lru_cache
from app.services.summarization_service import SummarizationService

@lru_cache
def get_summarization_service() -> SummarizationService:
    return SummarizationService()