from __future__ import annotations

import json
import shutil
from pathlib import Path

from model import Resume


def portfolio_payload(resume: Resume) -> dict:
    """Portfolio-shaped JSON.

    Phone is dropped here rather than omitted from resume.yaml, so the public
    site never carries it by construction instead of by remembering.
    """
    data = resume.model_dump(exclude_none=True)
    data["basics"].pop("phone", None)
    return data


def sync(resume: Resume, pdf: Path, portfolio: Path) -> list[Path]:
    data_file = portfolio / "data" / "resume.json"
    pdf_file = portfolio / "public" / "resume.pdf"

    for directory in (data_file.parent, pdf_file.parent):
        if not directory.is_dir():
            raise SystemExit(f"portfolio checkout not found: {directory}")

    data_file.write_text(json.dumps(portfolio_payload(resume), indent=2) + "\n")
    shutil.copyfile(pdf, pdf_file)

    return [data_file, pdf_file]
