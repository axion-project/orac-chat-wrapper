# ORAC Chat Wrapper

A minimal FastAPI + HTML wrapper that allows beta users to chat with the ORAC LLM using their API key.

## 🚀 Setup

### 1. Start the Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --port 8001 --reload
```

### 2. Open the Frontend
Just open `frontend/index.html` in a browser.

## 🔧 Notes

- Set `ORAC_API_URL` in `main.py` to point to your actual ORAC endpoint.
- Add logging, authentication, or persistent history as needed.

Built for testing LLM access with custom API keys in a chat-style format.
