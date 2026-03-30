import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY: str | None = os.getenv("GOOGLE_API_KEY")
    GOOGLE_MODEL: str = os.getenv("GOOGLE_MODEL", "gemini-3.1-flash-lite-preview")

    CHUNK_SIZE: int = 2000
    CHUNK_OVERLAP: int = 200

    TRANSCRIPT_LANGUAGES = ["en-IN", "en", "hi", "gu", "mr", "ta", "te", "kn", "ml", "bn", "pa"]

settings = Settings()