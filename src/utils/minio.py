from minio import Minio
from minio.error import S3Error
from src.config import config


def upload_file(source_file: str, destination_file: str):
    try:
        print(config)
        client = Minio(
            endpoint=config.MINIO_ENDPOINT,
            access_key=config.MINIO_ACCESS_KEY,
            secret_key=config.MINIO_SECRET_KEY,
            secure=config.MINIO_SECURE,
        )

        found = client.bucket_exists(config.MINIO_BUCKET_NAME)
        if not found:
            client.make_bucket(config.MINIO_BUCKET_NAME)
            print("Created bucket", config.MINIO_BUCKET_NAME)

        client.fput_object(
            bucket_name=config.MINIO_BUCKET_NAME,
            object_name=destination_file,
            file_path=source_file,
        )

        return True
    except S3Error as exc:
        print("error occurred:", exc)
        return False


def get_url(file_name: str):
    return f"http://{config.MINIO_ENDPOINT}/{config.MINIO_BUCKET_NAME}/{file_name}"
