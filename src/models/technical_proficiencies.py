from dataclasses import dataclass
from typing import List


@dataclass
class TechnicalProficiencies:
    backend: List[str]
    frontend_mobile: List[str]
    cloud_dev_ops: List[str]
    apis_testing: List[str]
    methodologies: List[str]

    @staticmethod
    def from_dict(data: dict) -> "TechnicalProficiencies":
        return TechnicalProficiencies(
            backend=data.get("backend", []),
            frontend_mobile=data.get("frontend_mobile", []),
            cloud_dev_ops=data.get("cloud_devops", []),
            apis_testing=data.get("apis_testing", []),
            methodologies=data.get("methodologies", []),
        )

    def to_dict(self) -> dict:
        return {
            "backend": self.backend,
            "frontend_mobile": self.frontend_mobile,
            "cloud_devops": self.cloud_dev_ops,
            "apis_testing": self.apis_testing,
            "methodologies": self.methodologies,
        }
