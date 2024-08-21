import os
from fastapi import APIRouter, File, UploadFile, HTTPException
from src.utils.minio import upload_file
from openai import OpenAI
from uuid import uuid4

ai_router = APIRouter(prefix="/gpt", tags=["GPT"])

client = OpenAI()


def delete_file(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        pass


@ai_router.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):
    with open("./tmp/audio.mp3", "wb") as audio:
        audio.write(file.file.read())

    with open("./tmp/audio.mp3", "rb") as audio:
        transcription = client.audio.transcriptions.create(
            file=audio, model="whisper-1"
        )

    upload_file("./tmp/audio.mp3", f"audio/{uuid4()}.mp3")
    delete_file("./tmp/audio.mp3")
    return transcription
