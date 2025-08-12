# Resume Repo

Version control for my resume

See [resume.md](resume.md) for full resume content.

## Generator Script

The python script `generator.py` will populate a LaTeX template in Jinja2 format with a JSON version of the resume and produce a PDF.

It supports adding an `overrides.json` file to customize sections of the resume instead of changing the base file with an optional command-line argument.

### Usage 
```commandline
python3 generator.py [-o override_flag]
```