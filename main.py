import logging

from src.api.app import create_app


logging.basicConfig(level=logging.INFO)

app = create_app()
