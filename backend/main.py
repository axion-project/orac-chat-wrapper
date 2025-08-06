from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_methods=["*"],
    allow_headers=["*"]
)

ORAC_API_URL = "http://localhost:8000/generate"  # Update to your deployed ORAC endpoint

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    api_key = body.get("api_key", "")
    history = body.get("history", [])

    full_prompt = "\n".join(history + [f"User: {prompt}", "ORAC:"])

    response = requests.post(
        ORAC_API_URL,
        headers={"Authorization": f"Bearer {api_key}"} if api_key else {},
        json={"prompt": full_prompt}
    )

    if response.status_code == 200:
        return response.json()
    return {"error": response.text, "status": response.status_code}
