import logging

from src.tyuiu_recommendations.api.app import create_fastapi_app


logging.basicConfig(level=logging.INFO)

# app = create_fastapi_app()

import requests

r = requests.get("https://192.168.16.222:8800")
print(r)
