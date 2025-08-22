from dataclasses import dataclass
from typing import List


@dataclass
class ExperienceItem:
    """Represents a single job in your work history."""
    title: str
    company: str
    date: str
    duties: List[str]

    @staticmethod
    def from_dict(data: dict) -> "ExperienceItem":
        return ExperienceItem(
            title=data.get("title", ""),
            company=data.get("company", ""),
            date=data.get("date", ""),
            duties=data.get("duties", []),
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "company": self.company,
            "date": self.date,
            "duties": self.duties,
        }
