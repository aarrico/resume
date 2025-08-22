import argparse
import os.path

from template_utils import (
    load_template,
    render_and_compile,
)
from models.override import Override
from models.resume import Resume

JSON_FILE = os.path.abspath("resume_data/resume_base.json")
OVERRIDE_FILE = os.path.abspath("resume_data/overrides.json")
TEMPLATE_FILE = "template.jinja2"
OUTPUT_DIR = os.path.abspath("output/")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a LaTeX resume from JSON data."
    )
    parser.add_argument(
        "-o",
        "--override",
        action="store_true",
        help="Specify to use a JSON file containing overrides for the base resume.",
    )
    args = parser.parse_args()

    template = load_template(TEMPLATE_FILE)
    base_resume = Resume.from_json_file(JSON_FILE)
    resumes = [base_resume]

    if args.override:
        overrides = Override.from_json_file(OVERRIDE_FILE)
        resumes.extend(base_resume.build_customized_resumes(overrides))

    render_and_compile(template, resumes, OUTPUT_DIR)


if __name__ == "__main__":
    main()
