# Working in this repo

- Read `README.md` for the build commands and output locations. Keep this file focused on instructions for editing with an agent.
- Treat `resume.yaml` as the source for the base resume. Preserve the user's existing edits and don't invent or strengthen employers, dates, metrics, technologies, or outcomes. Ask when a factual change needs evidence.
- Keep the build small and direct. Use the existing YAML model and Typst template for resume changes; add dependencies or abstractions only when the requested work needs them.
- For job-specific changes, use `tailored/<slug>.yaml`. Nested mappings merge with the base data, but lists replace the base lists. Tailored files may contain private application details, so review them before committing.
- After changing resume data or rendering code, run `uv run src/build.py` and inspect the generated PDF. When changing the template, check available fonts with `typst fonts` and review the page layout.
- Run `uv run src/build.py --sync` only when the user asks to update the sibling portfolio checkout; it writes files outside this repo. Never sync a tailored resume.
