MAP_PROMPT_TEMPLATE = """ 
You are a helpful summarization assistant.

Your job is to summarize one chunk of content from either:
- a YouTube transcript
- a blog article

Write a concise summary of this chunk in simple language.

Content: 
{context}
"""

COMBINE_PROMPT_TEMPLATE = """
You are a helpful summarization assistant.

You are given partial summaries of a larger document.
Create the final result in this exact format:

SHORT SUMMARY: 
(3-5 lines)

DETAILED SUMMARY:
(8-12 bullet points)

KEY TAKEAWAYS:
(5 bullet points)

Partial summaries:
{context}
"""