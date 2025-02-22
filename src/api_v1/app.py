import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api_v1.routers import (
    recommendations_router,
    directions_router,
    points_router
)
from src.api_v1.container import Container


logging.basicConfig(level=logging.INFO)

container = Container()

app = FastAPI()

app.container = container

app.include_router(recommendations_router)
app.include_router(directions_router)
app.include_router(points_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
