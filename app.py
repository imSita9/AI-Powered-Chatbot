from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response
from database import init_db, save_chat

app = FastAPI()

init_db()

class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "AI Chatbot API Running"}


@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message

    bot_response = get_response(user_message)

    save_chat(user_message, bot_response)

    return {
        "user": user_message,
        "bot": bot_response
    }