import logging
import requests
from bs4 import BeautifulSoup
from app.core.exceptions import ContentLoadError
from app.core.config import settings

logger = logging.getLogger(__name__)

def load_blog_text(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        logger.info("Loading blog content from url=%s", url)

        response = requests.get(url, headers=headers, timeout=settings.REQUEST_TIMEOUT)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        if not text.strip():
            raise ValueError("No readable blog text found.")
        
        return text
    
    except Exception as exc:
        logger.exception("Failed to load blog content")
        raise ContentLoadError(f"Failed to load blog content: {exc}") from exc

# if __name__=="__main__":
#     url = "https://huggingface.co/blog"

#     try:
#         text = load_blog_text(url)
#         print("Blog text loaded successfully!")
#         print("\nFirst 1000 characters:\n")
#         print(text[:1000])

#     except Exception as e:
#         print("Error:", e)