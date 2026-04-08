import logging
from youtube_transcript_api import YouTubeTranscriptApi

from app.utils.helpers import extract_youtube_video_id
from app.core.config import settings
from app.core.exceptions import ContentLoadError

logger = logging.getLogger(__name__)

def load_youtube_transcript(url: str) -> str:
    try:
        video_id = extract_youtube_video_id(url)
        logger.info("Loading YouTube transcript for video_id=%s", video_id)

        transcript_items = YouTubeTranscriptApi().fetch(
            video_id,
            languages=settings.TRANSCRIPT_LANGUAGES
            )
        transcript_text = " ".join(item.text for item in             transcript_items)

        if not transcript_text.strip():
            raise ContentLoadError("Transcript is empty or unavailable.")
        
        return transcript_text
    
    except Exception as exc:
        logger.exception("Failed to load YouTube transcript.")
        raise ContentLoadError(f"Failed to load YouTube transcript: {exc}") from exc
    
# if __name__=="__main__":
#     url = "https://www.youtube.com/shorts/t93OS8SgHb0"

#     try:
#         transcript = load_youtube_transcript(url)
#         print("Transcript loaded successfully!")
#         print("\nFirst 500 characters:\n")
#         print(transcript[:500])
#     except Exception as e:
#         print("Error:", e)