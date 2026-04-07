from pydantic import BaseModel, HttpUrl

class SummarizeRequest(BaseModel):
    url: HttpUrl