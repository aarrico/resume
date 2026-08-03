from __future__ import annotations

import argparse
from pathlib import Path

import model
import render
import sync

ROOT = Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT.parent / "portfolio"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a PDF resume from resume.yaml.")
    parser.add_argument(
        "--tailored",
        metavar="SLUG",
        help="deep-merge tailored/<SLUG>.yaml over the base resume",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="also write ../portfolio/data/resume.json and public/resume.pdf",
    )
    args = parser.parse_args()

    tailored = None
    out_dir = ROOT / "out"
    if args.tailored:
        tailored = ROOT / "tailored" / f"{args.tailored}.yaml"
        if not tailored.is_file():
            raise SystemExit(f"no such tailored resume: {tailored}")
        out_dir = out_dir / args.tailored

    resume = model.load(ROOT / "resume.yaml", tailored)
    pdf = render.build_pdf(resume, ROOT / "templates", out_dir)
    print(f"built {pdf.relative_to(ROOT)}")

    if args.sync:
        if args.tailored:
            raise SystemExit("refusing to sync a tailored resume to the public portfolio")
        for path in sync.sync(resume, pdf, PORTFOLIO):
            print(f"synced {path}")


if __name__ == "__main__":
    main()
