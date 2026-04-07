# YouTube / Blog Summarizer API

A FastAPI backend using LangChain + Gemini to summarize YouTube transcripts and blog/article content.

## Features

- FastAPI REST API
- Health endpoint
- Summarization endpoint
- YouTube transcript summarization
- Blog/article summarization
- Map-reduce summarization with LangChain
- Structured JSON responses
- Environment-based configuration
- Error handling with custom exceptions
- Swagger API documentation

---

## Project Structure

```text
app/
├── api/
│   └── routes/
│       ├── health.py
│       └── summarize.py
├── core/
│   ├── config.py
│   └── exceptions.py
├── langchain/
│   ├── chains.py
│   ├── prompts.py
│   └── summarizer.py
├── loaders/
│   ├── blog_loader.py
│   └── youtube_loader.py
├── schemas/
│   ├── requests.py
│   └── responses.py
├── services/
│   ├── content_service.py
│   └── summarization_service.py
├── utils/
│   └── helpers.py
├── main.py
.env
.gitignore
README.md
requirements.txt
```

---

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate it

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add `.env`

```env
GOOGLE_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.1-flash-lite-preview
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

After running the server:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoints

### Health Check

```http
GET /health
```

#### Response

```json
{
  "status": "ok"
}
```

---

### Summarize Content

```http
POST /summarize
```

#### Request Body

```json
{
  "url": "https://www.youtube.com/watch?v=example"
}
```

#### Success Response

```json
{
  "summary": "This video explains the basics of FastAPI and LangChain..."
}
```

#### Error Response

```json
{
  "detail": "Could not extract transcript from the provided URL"
}
```

---

## Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
-H "Content-Type: application/json" \
-d '{
  "url": "https://www.youtube.com/watch?v=example"
}'
```

---

## Technologies Used

- FastAPI
- LangChain
- Gemini API
- Pydantic
- Uvicorn
- Python-dotenv
- YouTube Transcript API
- BeautifulSoup / Web scraping utilities

---

## Notes

- Make sure your Gemini API key is valid.
- Some YouTube videos may not have transcripts available.
- Some websites may block scraping.
- Use `.env` to securely manage secrets.

---

## Future Improvements

- Add authentication
- Add caching for repeated URLs
- Add database support
- Add frontend UI
- Add Docker support
- Add deployment guide
- Add multilingual summarization

---

## License

This project is for learning and educational purposes.
