import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Iterable

from .education_item import EducationItem
from .experience_item import ExperienceItem
from .override import Override
from .project_item import ProjectItem
from .technical_proficiencies import TechnicalProficiencies


@dataclass
class Resume:
    first_name: str
    last_name: str
    title: str
    location: str
    phone: str
    email: str
    github: str
    linkedin: str
    summary: str
    technical_proficiencies: TechnicalProficiencies
    accomplishments: List[str]
    experience: List[ExperienceItem]
    education: List[EducationItem]
    personal_projects: List[ProjectItem]
    hobbies: List[str]
    custom_sections: Optional[Dict[str, Any]] = field(default_factory=dict)

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Resume":
        """
        Factory method to create a Resume instance from a dictionary.
        This method intelligently separates known fields from custom ones.
        """
        data = dict(data)  # shallow copy
        tp = TechnicalProficiencies.from_dict(data.get("technical_proficiencies", {}))
        exp = [ExperienceItem.from_dict(x) for x in data.get("experience", [])]
        edu = [EducationItem.from_dict(x) for x in data.get("education", [])]
        proj = [ProjectItem.from_dict(x) for x in data.get("personal_projects", [])]

        known = {
            "first_name",
            "last_name",
            "title",
            "location",
            "phone",
            "email",
            "github",
            "linkedin",
            "summary",
            "accomplishments",
            "hobbies",
            "technical_proficiencies",
            "experience",
            "education",
            "personal_projects",
        }
        custom = {k: v for k, v in data.items() if k not in known}

        return Resume(
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            title=data.get("title", ""),
            location=data.get("location", ""),
            phone=data.get("phone", ""),
            email=data.get("email", ""),
            github=data.get("github", ""),
            linkedin=data.get("linkedin", ""),
            summary=data.get("summary", ""),
            technical_proficiencies=tp,
            accomplishments=data.get("accomplishments", []),
            experience=exp,
            education=edu,
            personal_projects=proj,
            hobbies=data.get("hobbies", []),
            custom_sections=custom,
        )

    def to_dict(self) -> Dict[str, Any]:
        base = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "title": self.title,
            "location": self.location,
            "phone": self.phone,
            "email": self.email,
            "github": self.github,
            "linkedin": self.linkedin,
            "summary": self.summary,
            "technical_proficiencies": self.technical_proficiencies.to_dict(),
            "accomplishments": self.accomplishments,
            "experience": [e.to_dict() for e in self.experience],
            "education": [e.to_dict() for e in self.education],
            "personal_projects": [p.to_dict() for p in self.personal_projects],
            "hobbies": self.hobbies,
        }
        return {**base, **(self.custom_sections or {})}

    @classmethod
    def from_json_file(cls, file_path: str) -> "Resume":
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            print(f"Successfully loaded resume data from: {file_path}")
            return cls.from_dict(data)
        except FileNotFoundError:
            raise SystemExit(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            raise SystemExit(f"Error: Could not decode JSON from '{file_path}'.")
        except Exception as e:
            raise SystemExit(f"An unexpected error occurred: {e}")

    def to_json(self, **kwargs) -> str:
        return json.dumps(self.to_dict(), **kwargs)

    def apply(self, override_data: Override) -> "Resume":
        merged_data = self._deep_merge(self.to_dict(), override_data.to_dict())
        merged_data["application_for"] = {
            "company": override_data.company,
            "job_title": override_data.job_title,
            "job_url": override_data.job_url,
        }
        return Resume.from_dict(merged_data)

    def build_customized_resumes(self, overrides: Iterable[Override]) -> List["Resume"]:
        return [self.apply(ov) for ov in overrides]

    def get_output_filename(self) -> str:
        filename = f"{self.first_name}_{self.last_name}_Resume".replace(" ", "_")
        if self.custom_sections:
            filename += f"_{self.custom_sections['application_for']['company']}"
        return f"{filename}"

    @staticmethod
    def _deep_merge(base: Dict[str, Any], overrides: Dict[str, Any]) -> Dict[str, Any]:
        result = base.copy()
        for key, value in overrides.items():
            if isinstance(value, dict) and isinstance(result.get(key), dict):
                result[key] = Resume._deep_merge(result[key], value)
            else:
                result[key] = value
        return result
