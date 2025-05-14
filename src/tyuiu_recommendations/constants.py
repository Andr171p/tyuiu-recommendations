from typing import Literal

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ENV_PATH = BASE_DIR / ".env"

CSV_PATH = BASE_DIR / "datasets" / "csv" / "tyuiu_students_with_ids_2019-2024.csv"

PG_DRIVER: Literal["asyncpg"] = "asyncpg"

MIN_GPA = 3
MAX_GPA = 5

MIN_POINTS = 0
MAX_POINTS = 310

MIN_EXAM_POINTS = 0
MAX_EXAM_POINTS = 100

MIN_TOP_N = 1
MAX_TOP_N = 52

SUBJECTS_MAP = {
    "Русский язык": "russian",
    "Математика": "math",
    "Обществознание": "social_science",
    "Физика": "physics",
    "Химия": "chemistry",
    "История": "history",
    "Информатика": "informatics"
}

FEATURES = [
    "Пол",
    "Ср. балл док-та об образовании",
    "Сумма баллов",
    "Обществознание",
    "Математика",
    "Информатика",
    "Русский язык",
    "Физика",
    "Химия",
    "История"
]
