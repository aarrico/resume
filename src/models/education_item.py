from dataclasses import dataclass


@dataclass
class EducationItem:
    degree: str
    university: str
    date: str
    location: str

    @staticmethod
    def from_dict(data: dict) -> "EducationItem":
        return EducationItem(
            degree=data.get("degree", ""),
            university=data.get("university", ""),
            date=data.get("date", ""),
            location=data.get("location", ""),
        )

    def to_dict(self) -> dict:
        return {
            "degree": self.degree,
            "university": self.university,
            "date": self.date,
            "location": self.location,
        }
