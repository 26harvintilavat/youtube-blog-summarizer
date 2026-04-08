import logging
from fastapi import status, APIRouter, HTTPException, Depends
from starlette.concurrency import run_in_threadpool

from app.api.deps import get_summarization_service
from app.core.exceptions import AppError
from app.schemas.requests import SummarizeRequest
from app.schemas.responses import SummaryResponse, ErrorResponse
from app.services.summarization_service import SummarizationService

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Summarization"])

@router.post(
    "/summarize", 
    response_model=SummaryResponse,
    responses={
        400: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)
async def summarize(
    payload: SummarizeRequest,
    service: SummarizationService = Depends(get_summarization_service),
):
    try:
        logger.info(
            "Received summarize request url=%s style=%s language=%s",
            payload.url,
            payload.summary_style,
            payload.output_language,
        )
        result = await run_in_threadpool(
                service.summarize_from_url,
                str(payload.url),
                payload.summary_style,
                payload.output_language,
            )
        return result

    except AppError as exc:
        logger.warning("Application error: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        logger.exception("Unexpected server error")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected server error: {exc}",
        ) from exc