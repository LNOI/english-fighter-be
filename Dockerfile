FROM python:3.12-slim

WORKDIR /project
COPY requirements.txt /project/requirements.txt
# COPY ../certs/rootCA.pem /project/rootCA.pem

RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt
WORKDIR /project/src

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --reload --port 8000


