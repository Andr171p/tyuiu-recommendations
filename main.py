import logging

from src.tyuiu_recommendations.api.app import create_fastapi_app


logging.basicConfig(level=logging.INFO)

app = create_fastapi_app()
