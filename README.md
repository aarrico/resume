# Resume Repo

Canonical source for my resume. `resume.yaml` is the only file edited by hand — the PDF and the
portfolio site's copy are both generated from it.

Design notes and the rationale behind the content decisions live in
[docs/superpowers/specs/2026-07-31-resume-pipeline-design.md](docs/superpowers/specs/2026-07-31-resume-pipeline-design.md).

## Setup

```sh
uv sync
```

Typst does the typesetting, and the template targets an Arial-compatible font:

```sh
sudo pacman -S typst ttf-liberation   # Arch / CachyOS
brew install typst                    # macOS — Arial and Helvetica ship with the OS
```

## Usage

```sh
uv run src/build.py                  # -> out/Alexander_Arrico_Resume.pdf
uv run src/build.py --sync           # also updates ../portfolio
uv run src/build.py --tailored acme  # -> out/acme/
```

`--sync` writes `../portfolio/data/resume.json` (phone stripped) and `../portfolio/public/resume.pdf`.

Tailored resumes live in `tailored/<slug>.yaml` and deep-merge over `resume.yaml`. `--sync`
refuses to run with `--tailored`, so a resume written for one application can't reach the
public site.

## Layout

```
resume.yaml              canonical data
tailored/<slug>.yaml     per-application overrides, never synced
templates/resume.typ.j2  ATS-oriented Typst layout
src/
  build.py               entrypoint
  model.py               pydantic schema + YAML loading + deep merge
  render.py              Typst escaping, date formatting, compile
  sync.py                portfolio artifacts
out/                     generated, gitignored
```
