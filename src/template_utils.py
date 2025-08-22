import subprocess
from typing import List

from jinja2 import Environment, Template, FileSystemLoader, TemplateNotFound

from models.resume import Resume


def load_template(template_file: str) -> Template:
    # Change the delimiters to avoid conflicts with LaTeX syntax.
    env = Environment(
        loader=FileSystemLoader("tex_template/"),
        block_start_string="[%",
        block_end_string="%]",
        variable_start_string="<<",
        variable_end_string=">>",
        comment_start_string="[#",
        comment_end_string="#]",
    )
    try:
        template = env.get_template(template_file)
        print(f"Successfully loaded template: {template_file}")
        return template
    except TemplateNotFound:
        raise SystemExit(
            f"Error: Template file '{template_file}' not found. Please ensure it exists in the 'tex_template' directory."
        )
    except Exception as e:
        raise SystemExit(f"Error loading template: {e.with_traceback()}")


def render_and_compile(
    template: Template, resumes: List[Resume], output_dir: str
) -> None:
    try:
        print(f"\nFound {len(resumes)} resume(s) to process.")
        for resume in resumes:
            rendered_latex = template.render(resume.to_dict())
            with open(f"tex_template/{resume.get_output_filename()}.tex", "w") as f:
                f.write(rendered_latex)
            compile_to_pdf(output_dir, resume.get_output_filename())
    except Exception as e:
        print(e)
        raise SystemExit(f"Error during rendering or compilation: {e}")


def render_latex(template: Template, resume: Resume) -> str:
    return template.render(resume.to_dict())


def compile_to_pdf(output_dir: str, output_filename: str) -> None:
    print("\nAttempting to compile PDF...")
    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-jobname",
        output_filename,
        "-output-directory",
        output_dir,
        f"tex_template/{output_filename}.tex",
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("First compilation pass successful.")
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("Second compilation pass successful.")

        print(f"✅ Successfully created resume: {output_filename}")

    except FileNotFoundError:
        print("❌ Error: 'pdflatex' command not found.")
        print(
            "Please ensure you have a LaTeX distribution (MiKTeX, TeX Live, MacTeX) installed and in your system's PATH."
        )
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during PDF compilation. Return code: {e.returncode}")
        print("--- pdflatex output ---")
        print(e.stdout)
        print("--- pdflatex errors ---")
        print(e.stderr)
        print("Check the log file for more details.")
