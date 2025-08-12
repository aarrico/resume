import argparse
import json
import subprocess
from jinja2 import Environment, FileSystemLoader, Template

JSON_FILE = "resume_base.json"
TEMPLATE_FILE = "template.jinja2"
OUTPUT_FILE = "tex/resume.tex"
CUSTOM_FILE = "overrides.json"


def deep_merge(base: dict, custom: dict) -> dict:
    """
    Recursively merges the 'custom' dictionary into the 'base' dictionary.
    - If a key in 'custom' exists in 'base' and both values are dicts, it merges them.
    - Otherwise, the value from 'custom' overwrites the value in 'base'.
    """
    for key, value in custom.items():
        if isinstance(base.get(key), dict) and isinstance(value, dict):
            base[key] = deep_merge(base[key], value)
        else:
            base[key] = value
    return base


def main():
    parser = argparse.ArgumentParser(description="Generate a LaTeX resume from JSON data.")
    parser.add_argument(
        "-o", "--override",
        action="store_true",
        help="Specify to use a JSON file containing overrides for the base resume."
    )
    args = parser.parse_args()

    # Change the delimiters to avoid conflicts with LaTeX syntax.
    env = Environment(
        loader=FileSystemLoader('.'),  # looks for templates in the current directory
        block_start_string='[%',  # For statements like loops, if
        block_end_string='%]',
        variable_start_string='<<',  # For variables
        variable_end_string='>>',
        comment_start_string='[#',  # For comments
        comment_end_string='#]'
    )

    template = load_template(env)
    resume_data = load_resume(args)
    render_latex(template, resume_data)
    compile_to_pdf(OUTPUT_FILE)


def load_template(env: Environment) -> Template:
    try:
        template = env.get_template(TEMPLATE_FILE)
        print(f"Successfully loaded template: {TEMPLATE_FILE}")
        return template
    except Exception as e:
        print(f"Error loading template: {e}")


def load_resume(args):
    try:
        with open(JSON_FILE, 'r') as f:
            resume_data = json.load(f)
        print(f"Successfully loaded data from: {JSON_FILE}")
        if args.override:
            print(f"Using override file")

            with open(CUSTOM_FILE, 'r') as f:
                custom_data = json.load(f)

            print("Merging base and custom data...")
            resume_data = deep_merge(resume_data, custom_data)
    except Exception as e:
        print(f"Error loading JSON data: {e}")

    return resume_data


def render_latex(template, resume_data):
    rendered_latex = template.render(resume_data)
    print("Template has been rendered with your data.")
    try:
        with open(OUTPUT_FILE, 'w') as f:
            f.write(rendered_latex)
        print(f"Rendered LaTeX saved to: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving output file: {e}")


def compile_to_pdf(tex_file):
    print("\nAttempting to compile PDF...")
    command = ["pdflatex", "-interaction=nonstopmode", tex_file]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("First compilation pass successful.")
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("Second compilation pass successful.")

        pdf_file = tex_file.replace('.tex', '.pdf')
        print(f"✅ Successfully created resume: {pdf_file}")

    except FileNotFoundError:
        print("❌ Error: 'pdflatex' command not found.")
        print(
            "Please ensure you have a LaTeX distribution (MiKTeX, TeX Live, MacTeX) installed and in your system's PATH.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during PDF compilation. Return code: {e.returncode}")
        print("--- pdflatex output ---")
        print(e.stdout)
        print("--- pdflatex errors ---")
        print(e.stderr)
        print("Check the log file for more details.")


if __name__ == "__main__":
    main()
