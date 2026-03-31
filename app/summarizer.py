import json
import time
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import settings
from app.chains import build_map_chain, build_combine_chain
from app.exceptions import SummarizationError
from app.models import SummaryResult
from app.utils import extract_json_from_text

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
                return chain.invoke(payload)
            except Exception as exc:
                last_error = exc
                if attempt < settings.MAX_RETRIES:
                    time.sleep(1)
        
        raise SummarizationError(f"Chain invocation failed after retries: {last_error}")
    
    def summarize(self, text: str, 
                  source_url: str, 
                  source_type: str) -> SummaryResult:
        chunks = self.split_text(text)

        if not chunks:
            raise ValueError("No text chunks were created for summarization.")
        
        partial_summaries = []
        for chunk in chunks:
            summary = self._invoke_with_retry(self.map_chain, {"context": chunk})
            partial_summaries.append(summary)

        combined_input = "\n\n".join(partial_summaries)
        final_output = self._invoke_with_retry(self.combine_chain, {"context": combined_input})

        try:
            parsed = extract_json_from_text(final_output)
        except Exception as exc:
            raise SummarizationError(f"Failed to parse model output as JSON: {exc}") from exc
        
        try:
            return SummaryResult(
                source_type=source_type,
                source_url=source_url,
                title=parsed.get("title", "Untitled"),
                short_summary=parsed.get("short_summary", ""),
                detailed_summary=parsed.get("detailed_summary", []),
                key_takeaways=parsed.get("key_takeaways", []),
                total_chunks=len(chunks),
                raw_text_length=len(text)
            )
        except Exception as exc:
            raise SummarizationError(f"Failed to build SummaryResult: {exc} ") from exc