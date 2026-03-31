import json
import os

from app.config import settings
from app.exceptions import AppError
from app.services.content_service import load_content
from app.summarizer import ContentSummarizer
from app.utils import ensure_directory, sanitize_filename

def main():
    if not settings.GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")
    
    url = input("Enter a YouTube or blog URL: ").strip()

    if not url:
        raise ValueError("URL cannot be empty.")
    
    try:
        print("\nLoading content...\n")
        source_type, text = load_content(url)

        summarizer = ContentSummarizer()
        result = summarizer.summarize(
            text=text,
            source_url=url,
            source_type=source_type
        )

        ensure_directory(settings.OUTPUT_DIR)
        filename = sanitize_filename(result.title) + ".json"
        output_path = os.path.join(settings.OUTPUT_DIR, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)

        print("=" * 80)
        print("SUMMARY RESULT")
        print("=" * 80)
        print(f"Title: {result.title}")
        print(f"Source Type: {result.source_type}")
        print(f"Chunks Used: {result.total_chunks}")
        print("\nSHORT SUMMARY:")
        print(result.short_summary)

        print("\nDETAILED SUMMARY:")
        for idx, point in enumerate(result.detailed_summary, start=1):
            print(f"{idx}. {point}")

        print("\nKEY TAKEAWAYS:")
        for idx, point in enumerate(result.key_takeaways, start=1):
            print(f"{idx}. {point}")

        print(f"\nSaved JSON output to: {output_path}")
        print("=" * 80)

    except AppError as exc:
        print(f"Application error: {exc}")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()