import pandas as pd

from src.core.entities import Applicant


class ApplicantMapper:
    @staticmethod
    def to_df(applicant: Applicant) -> pd.DataFrame:
        applicant_dict = {
            "Пол": applicant.gender,
            "Ср. балл док-та об образовании": applicant.gpa,
            "Сумма баллов": applicant.points,
            "Обществознание": applicant.exams_dict.get("social_science", 0),
            "Математика": applicant.exams_dict.get("math", 0),
            "Информатика": applicant.exams_dict.get("informatics", 0),
            "Русский язык": applicant.exams_dict.get("russian", 0),
            "Физика": applicant.exams_dict.get("physics", 0),
            "Химия": applicant.exams_dict.get("chemistry", 0),
            "История": applicant.exams_dict.get("history", 0)
        }
        return pd.DataFrame(applicant_dict, index=[0])
