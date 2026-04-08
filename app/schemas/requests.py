from typing import Literal
from pydantic import BaseModel, HttpUrl, Field

SummaryStyle = Literal["brief", "detailed", "bullet", "executive"]

class SummarizeRequest(BaseModel):
    url: HttpUrl
    summary_style: SummaryStyle = Field(
        default="detailed",
        description="Style of final summary output."
    )

    output_language: str = Field(
        default="English",
        min_length=2,
        max_length=40,
        description="Language for final summary output."
    )