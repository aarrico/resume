from __future__ import annotations

from pathlib import Path
from typing import Annotated, Any

import yaml
from pydantic import BaseModel, Field

YearMonth = Annotated[str, Field(pattern=r"^\d{4}-(0[1-9]|1[0-2])$")]


class Links(BaseModel):
    website: str
    linkedin: str
    github: str


class Basics(BaseModel):
    name: str
    title: str
    headline: str | None = None
    location: str
    email: str
    phone: str
    links: Links


class SkillGroup(BaseModel):
    category: str
    items: list[str] = Field(min_length=1)


class Experience(BaseModel):
    company: str
    role: str
    location: str
    start: YearMonth
    end: YearMonth | None = None
    lede: str | None = None
    bullets: list[str] = Field(min_length=1)


class Project(BaseModel):
    name: str
    tagline: str
    stack: list[str] = Field(min_length=1)
    link: str | None = None
    bullets: list[str] = Field(min_length=1)


class Education(BaseModel):
    school: str
    degree: str
    start: YearMonth
    end: YearMonth


class Resume(BaseModel):
    basics: Basics
    summary: str
    skills: list[SkillGroup] = Field(min_length=1)
    experience: list[Experience] = Field(min_length=1)
    projects: list[Project] = []
    education: list[Education] = Field(min_length=1)

    @property
    def slug(self) -> str:
        return f"{self.basics.name.replace(' ', '_')}_Resume"


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load(base: Path, tailored: Path | None = None) -> Resume:
    data = yaml.safe_load(base.read_text())
    if tailored is not None:
        data = _deep_merge(data, yaml.safe_load(tailored.read_text()))
    return Resume.model_validate(data)
