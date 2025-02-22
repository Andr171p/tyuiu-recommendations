import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api_v1.routers import (
    recommendations_router,
    directions_router
)
from src.api_v1.container import Container
from src.api_v1.lifespan import lifespan


logging.basicConfig(level=logging.INFO)

print("Start add vector to chroma")
from scripts import add_vectors_chroma
print("Vectors added to chroma successfully")
print("Start add directions to sqlite")
from scripts import create_db
from scripts import add_directions_sqlite
print("Direction added to sqlite successfully")

container = Container()

app = FastAPI()

app.container = container

app.include_router(recommendations_router)
app.include_router(directions_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
