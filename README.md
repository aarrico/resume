# Resume

Resume content lives in [`resume.yaml`](resume.yaml). A small Python build validates the data, renders a single-column Typst layout, and produces a PDF. The same data can also update my portfolio's resume JSON and PDF, so I don't have to maintain three copies of the content.

## Build the PDF

You need Python 3.11+, [uv](https://docs.astral.sh/uv/), and [Typst CLI](https://github.com/typst/typst#installation) on your `PATH`.

```sh
./build
```

The executable uses this repo's uv environment and installs the locked Python dependencies as needed. Run `./build --help` for options. You can also invoke it by path from any directory:

```sh
~/repos/resume/build
```

The result is `out/Alexander_Arrico_Resume.pdf`. Generated files in `out/` are ignored by Git. The template prefers IBM Plex Sans, Liberation Sans, Arial, or Helvetica. Use `typst fonts` to check what's installed, and inspect the PDF for font substitutions.

## Edit the resume

Edit `resume.yaml`, then rebuild and review the PDF. The file contains the contact details, summary, skills, experience, projects, and education used by the template. Dates use `YYYY-MM`; `end: null` means a current role.

For a job-specific version, create `tailored/<slug>.yaml` with only the fields you want to override, then run:

```sh
./build --tailored acme
```

That writes the PDF under `out/acme/`. Tailored files are deep-merged with `resume.yaml`: nested mappings merge, while lists such as experience and skills replace the entire base list. Review tailored files before committing them.

## Update the portfolio

With the portfolio checkout next to this repo at `../portfolio`, run:

```sh
./build --sync
```

This writes `../portfolio/data/resume.json` and `../portfolio/public/resume.pdf`. The JSON omits the phone number; the PDF uses the contact details in `resume.yaml`. Tailored resumes cannot be synced.

## Repo map

| Path | Purpose |
| --- | --- |
| `build` | Executable entry point; works from any directory |
| `resume.yaml` | Base resume content |
| `tailored/<slug>.yaml` | Optional job-specific overrides |
| `src/model.py` | YAML loading and validation |
| `src/render.py` | Typst rendering and PDF compilation |
| `src/sync.py` | Portfolio output |
| `templates/resume.typ.j2` | PDF layout |
