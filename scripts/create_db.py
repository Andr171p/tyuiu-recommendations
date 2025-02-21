import sqlite3
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent

DATABASE_PATH: Path = BASE_DIR / "db.sqlite3"


connection = sqlite3.connect(DATABASE_PATH)

connection.close()
