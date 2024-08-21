from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Config(BaseSettings):
    OPENAI_API_KEY: str | None = ""
    MINIO_ENDPOINT: str | None = "localhost:9000"
    MINIO_ACCESS_KEY: str | None = ""
    MINIO_SECRET_KEY: str | None = ""
    MINIO_SECURE: bool = False
    MINIO_BUCKET_NAME: str | None = "englishfighter"
    DB_URL: str | None = (
        "postgresql+psycopg2://langchain:langchain@localhost:5444/langchain"
    )


config = Config()
