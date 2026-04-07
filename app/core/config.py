import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY: str | None = os.getenv("GOOGLE_API_KEY")
    GOOGLE_MODEL: str = os.getenv("GOOGLE_MODEL", "gemini-3.1-flash-lite-preview")

    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "2500"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "250"))
    MAX_RETRIES: int = int(os.getenv("MAX_RETRIES", "3"))
    
    APP_NAME: int = os.getenv("APP_NAME", "YouTube Blog Summarizer API")
    APP_VERSION: str = os.getenv("APP_VERSION", "2.0.0")

    TRANSCRIPT_LANGUAGES = ["en-IN", "en", "hi", "gu", "mr", "ta", "te", "kn", "ml", "bn", "pa"]

settings = Settings()