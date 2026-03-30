from app.utils import is_youtube_url
from app.loaders.youtube_loader import load_youtube_transcript
from app.loaders.blog_loader import load_blog_text
from app.summarizer import ContentSummarizer
from app.config import settings

def main():
    if not settings.GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")
    
    url = input("Enter a YouTube or blog URL: ").strip()

    if not url:
        raise ValueError("URL cannot be empty.")
    
    if is_youtube_url(url):
        print("\nLoading YouTube transcript...\n")
        text = load_youtube_transcript(url)
    else:
        print("\nLoading blog content...\n")
        text = load_blog_text(url)

    summarizer = ContentSummarizer()
    result = summarizer.summarize(text)

    print("\n" + "=" * 80)
    print("SUMMARY RESULT")
    print("=" * 80)
    print(result)
    print("=" * 80)

if __name__ == "__main__":
    main()