from fastapi import status, APIRouter, HTTPException

from app.core.config import settings
from app.core.exceptions import AppError
from app.schemas.requests import SummarizeRequest
from app.schemas.responses import SummaryResponse, ErrorResponse
from app.services.summarization_service import SummarizationService

router = APIRouter(tags=["Summarization"])
service = SummarizationService()

@router.post(
    "/summarize", 
    response_model=SummaryResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

def summarize(payload: SummarizeRequest):
    if not settings.GOOGLE_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="GOOGLE_API_KEY is missing in environment variables."
        )
    
    try:
        return service.summarize_from_url(str(payload.url))
    except AppError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected server error: {exc}"
        ) from exc