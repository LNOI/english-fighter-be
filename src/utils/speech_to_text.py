from fastapi import FastAPI, File, UploadFile
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
app = FastAPI()


@app.post("/audio/")
async def create_upload_file(file: UploadFile = File(...)):
    transcription = client.audio.transcriptions.create(
        file=file.file, model="whisper-1"
    )
    return transcription
