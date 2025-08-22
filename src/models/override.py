import json
from dataclasses import dataclass
from typing import Dict, Any, List


@dataclass
class Override:
    company: str
    job_title: str
    job_url: str
    overrides: Dict[str, Any]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Override":
        return Override(
            company=data.get("company", ""),
            job_title=data.get("job_title"),
            job_url=data.get("job_url"),
            overrides=data.get("overrides", {}),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "company": self.company,
            "job_title": self.job_title,
            "job_url": self.job_url,
            "overrides": self.overrides,
        }

    @classmethod
    def from_json_file(cls, file_path: str) -> List["Override"]:
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
            print(f"Successfully loaded override data from: {file_path}")
            return [cls.from_dict(item) for item in data]
        except FileNotFoundError:
            raise SystemExit(f"Error: The file '{file_path}' was not found.")
        except json.JSONDecodeError:
            raise SystemExit(f"Error: Could not decode JSON from '{file_path}'.")
        except Exception as e:
            raise SystemExit(f"An unexpected error occurred: {e}")
