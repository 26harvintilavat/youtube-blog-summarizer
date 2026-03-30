from urllib.parse import urlparse, parse_qs

def is_youtube_url(url: str) -> bool:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    return "youtube.com" in domain or "youtu.be" in domain

def extract_youtube_video_id(url: str) -> str:
    parsed = urlparse(url)

    if "youtu.be" in parsed.netloc:
        return parsed.path.lstrip("/")
    
    if "youtube.com" in parsed.netloc:
        query_params = parse_qs(parsed.query)
        if "v" in query_params:
            return query_params["v"][0]
        
        # Support shorts URLs like/shorts/<id>
        path_parts = [part for part in parsed.path.split("/") if part]
        if len(path_parts) >= 2 and path_parts[0] == 'shorts':
            return path_parts[1]
        
    raise ValueError("Could not extract YouTube video ID from URL.")

# if __name__=='__main__':
#     test_urls = [
#         "https://www.youtube.com/watch?v=7I3G21RyARs",
#         "https://www.youtube.com/shorts/UZI1OKZN7R0",
#         "https://google.com"
#     ]

#     for url in test_urls:
#         print(f"\nURL: {url}")
#         print("Is YouTube URL:", is_youtube_url(url))

#         try:
#             video_id = extract_youtube_video_id(url)
#             print("Video ID:", video_id)
#         except ValueError as e:
#             print("Error:", e)