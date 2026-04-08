import logging
import time
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings
from app.langchain.chains import build_map_chain, build_combine_chain
from app.core.exceptions import SummarizationError
from app.schemas.responses import SummaryResponse
from app.utils.helpers import extract_json_from_text

logger = logging.getLogger(__name__)

class ContentSummarizer:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = settings.CHUNK_SIZE,
            chunk_overlap = settings.CHUNK_OVERLAP
        )
        self.map_chain = build_map_chain()
        self.combine_chain = build_combine_chain()

    def split_text(self, text: str) -> list[str]:
        return self.text_splitter.split_text(text)
    
    def _invoke_with_retry(self, chain, payload: dict) -> str:
        last_error = None

        for attempt in range(1, settings.MAX_RETRIES + 1):
            try:
                logger.info("Invoking chain attempt=%s", attempt)
                return chain.invoke(payload)
            except Exception as exc:
                last_error = exc
                logger.warning("Chain invocation failed on attempt=%s: %s", attempt, exc)
                if attempt < settings.MAX_RETRIES:
                    time.sleep(1)
        
        raise SummarizationError(f"Chain invocation failed after retries: {last_error}")
    
    def summarize(self, text: str, 
                  source_url: str, 
                  source_type: str,
                  summary_style: str,
                  output_language: str) -> SummaryResponse:
        started = time.perf_counter()
        chunks = self.split_text(text)

        if not chunks:
            raise SummarizationError("No text chunks were created for summarization.")
        
        logger.info("Text split into %s chunks", len(chunks))

        partial_summaries = []
        for chunk in chunks:
            summary = self._invoke_with_retry(self.map_chain, {"context": chunk})
            partial_summaries.append(summary)

        combined_input = "\n\n".join(partial_summaries)
        final_output = self._invoke_with_retry(
            self.combine_chain, {            
                "context": combined_input,
                "summary_style": summary_style,
                "output_language": output_language                        
                })

        try:
            parsed = extract_json_from_text(final_output)
        except Exception as exc:
            raise SummarizationError(f"Failed to parse model output as JSON: {exc}") from exc
        
        elapsed_ms = int((time.perf_counter() - started) * 1000)
        
        try:
            return SummaryResponse(
                source_type=source_type,
                source_url=source_url,
                title=parsed.get("title", "Untitled"),
                summary_style=summary_style,
                output_language=output_language,
                short_summary=parsed.get("short_summary", ""),
                detailed_summary=parsed.get("detailed_summary", []),
                key_takeaways=parsed.get("key_takeaways", []),
                total_chunks=len(chunks),
                raw_text_length=len(text),
                processing_time_ms=elapsed_ms,
            )
        except Exception as exc:
            raise SummarizationError(f"Failed to build SummaryResult: {exc} ") from exc