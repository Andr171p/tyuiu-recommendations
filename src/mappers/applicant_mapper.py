from src.dto import ApplicantVector
from src.core.entities import Applicant


class ApplicantMapper:
    @staticmethod
    def to_applicant_vector(applicant: Applicant) -> ApplicantVector:
        return ApplicantVector(
            gender=applicant.gender,
            foreign_citizenship=applicant.foreign_citizenship,
            military_service=applicant.military_service,
            gpa=applicant.gpa,
            points=applicant.points,
            bonus_points=applicant.bonus_points,
            russian=applicant.exams_dict.get("russian"),
            social_science=applicant.exams_dict.get("social_science"),
            math=applicant.exams_dict.get("math"),
            physics=applicant.exams_dict.get("physics"),
            chemistry=applicant.exams_dict.get("chemistry"),
            history=applicant.exams_dict.get("history"),
            informatics=applicant.exams_dict.get("informatics")
        )
