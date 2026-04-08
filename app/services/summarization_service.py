from app.langchain.summarizer import ContentSummarizer
from app.schemas.responses import SummaryResponse
from app.services.content_service import load_content

class SummarizationService:
    def __init__(self):
        self.summarizer = ContentSummarizer()

    def summarize_from_url(
        self, 
        url: str,
        summary_style: str,
        output_language: str) -> SummaryResponse:

        source_type, text = load_content(url)

        return self.summarizer.summarize(
            text=text,
            source_url=url,
            source_type=source_type,
            summary_style=summary_style,
            output_language=output_language
        )