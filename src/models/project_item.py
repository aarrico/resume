from dataclasses import dataclass


@dataclass
class ProjectItem:
    """Represents a single personal project."""
    type: str
    title: str
    technologies: str
    description: str

    @staticmethod
    def from_dict(data: dict) -> "ProjectItem":
        return ProjectItem(
            type=data.get("type", ""),
            title=data.get("title", ""),
            technologies=data.get("technologies", ""),
            description=data.get("description", ""),
        )

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "title": self.title,
            "technologies": self.technologies,
            "description": self.description,
        }
