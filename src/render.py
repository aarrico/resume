from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from model import Resume

_MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

# Backslash first: it is the escape character for every entry after it.
# `#` matters most in practice -- it is how Typst enters code mode, and the
# skills list contains "C#".
_SPECIAL = ("\\", "#", "$", "*", "_", "`", "[", "]", "<", ">", "@")


def typst_escape(value: object) -> str:
    text = str(value)
    for char in _SPECIAL:
        text = text.replace(char, f"\\{char}")
    return text


def month_year(value: str | None) -> str:
    if value is None:
        return "Present"
    year, month = value.split("-")
    return f"{_MONTHS[int(month) - 1]} {year}"


def _environment(templates: Path) -> Environment:
    env = Environment(
        loader=FileSystemLoader(templates),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["typst"] = typst_escape
    env.filters["month"] = month_year
    return env


def build_pdf(resume: Resume, templates: Path, out_dir: Path) -> Path:
    if shutil.which("typst") is None:
        raise SystemExit(
            "typst not found on PATH.\n"
            "  Arch/CachyOS: sudo pacman -S typst\n"
            "  macOS:        brew install typst"
        )

    out_dir.mkdir(parents=True, exist_ok=True)
    source = out_dir / f"{resume.slug}.typ"
    pdf = out_dir / f"{resume.slug}.pdf"

    template = _environment(templates).get_template("resume.typ.j2")
    source.write_text(template.render(resume.model_dump()))

    result = subprocess.run(
        ["typst", "compile", str(source), str(pdf)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"typst compile failed:\n{result.stderr}")

    return pdf
