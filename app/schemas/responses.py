from typing import List, Literal, Optional
from pydantic import BaseModel, Field

class SummaryResponse(BaseModel):
    source_type: Literal["youtube", "blog"]
    source_url: str
    title: str = "Untitled"
    summary_style: str
    output_language: str
    short_summary: str
    detailed_summary: List[str] = Field(default_factory=list)
    key_takeaways: List[str] = Field(default_factory=list)
    total_chunks: int
    raw_text_length: int
    processing_time_ms: int

class HealthResponse(BaseModel):
    status: str
    app_name: str
    version: str

class ErrorResponse(BaseModel):
    detail: str
    error_type: Optional[str] = None