MAP_PROMPT_TEMPLATE = """ 
You are a precise summarization assistant.

You are given one chunk from either:
- a YouTube transcript
- a blog article

Your task:
1. Identify the main idea of the chunk.
2. Capture important supporting points.
3. Ignore repetition, filler, sponsorship, and fluff.
4. Write a concise but information-dense summary.

Return plain text only.

Content CHUNK:
{context}
"""

COMBINE_PROMPT_TEMPLATE = """
You are a precise summarization assistant.

You are given partial summaries of a larger piece of content.

Generate a final answer in valid JSON with this exact structure:

{{
    "title": "string",
    "short_summary": "string",
    "detailed_summary": ["point 1", "point 2", "point 3"],
    "key_takeaways": ["takeaway 1", "takeaway 2", "takeaway 3"]
}}

Rules:
- title should be short and descriptive
- short_summary should be a concise paragraph
- detailed_summary should contain 6 to 10 bullet-style points as array items
- key_takeaways should contain 4 to 6 concise points as array items
- output must be valid JSON only
- do not wrap JSON in markdown
- do not add extra commentary

PARTIAL SUMMARIES:
{context}
"""