#!/usr/bin/env python

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.toiec import router as toiec_router
from src.api.gpt import ai_router as gpt_router

# 4. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.1",
    description="A simple API server using LangChain's Runnable interfaces",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(toiec_router)
app.include_router(gpt_router)
