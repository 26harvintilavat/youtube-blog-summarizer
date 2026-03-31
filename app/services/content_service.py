from app.utils import is_youtube_url
from app.loaders.youtube_loader import load_youtube_transcript
from app.loaders.blog_loader import load_blog_text

def detect_source_type(url: str) -> str:
    return "youtube" if is_youtube_url(url) else "blog"

def load_content(url: str) -> tuple[str, str]:
    source_type = detect_source_type(url)

    if source_type == "youtube":
        return source_type, load_youtube_transcript(url)
    
    return source_type, load_blog_text(url)