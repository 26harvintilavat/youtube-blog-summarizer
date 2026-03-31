# YouTube / Blog Summarizer with LangChain + Gemini

## Features

- Summarize YouTube transcripts
- Summarize blog articles
- Chunk long text
- Map-reduce summarization
- Structured JSON output
- Save results to file
- Retry logic and cleaner project structure

## Setup

1. Create virtual environment
2. Install dependencies

````bash
pip install -r requirements.txt

## Add Gemini API key to .env
GOOGLE_API_KEY=your_key_here
GEMINI_MODEL=gemini-3.1-flash-lite-preview
# Run
python -m app.main

---

## Full flow

```text
User gives URL
   ↓
Detect source type
   ↓
Load raw text
   ↓
Split long text into chunks
   ↓
Summarize each chunk
   ↓
Combine chunk summaries into JSON
   ↓
Validate into Pydantic model
   ↓
Print result
   ↓
Save JSON file
````
