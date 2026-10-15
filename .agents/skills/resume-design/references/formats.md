# PDF and DOCX decisions

Use employer instructions and observed application behavior to choose an output.
If an employer prefers DOCX, recommend it. Otherwise assess available formats on
actual readability and extraction rather than treating the extension as a guarantee.
Retain PDF for stable visual presentation where accepted.

## When DOCX implementation is requested

Read the existing model and build entrypoint. Generate DOCX from the same validated,
merged resume data as PDF, including job-specific overrides. Keep one content source;
avoid reconstructing structure by converting the rendered PDF back into Word.
Select the smallest maintainable implementation that meets the requested output.

Use document-body paragraphs, recognizable headings, real list items, and styles
for typography and spacing. Keep contact information in the body. Prefer tab stops
or a separate date line over tables and floating text boxes; verify resulting
reading order. Keep essential text out of headers, footers, images, and shapes.

Inspect DOCX text in document order and compare with the canonical data. Verify
rendering in an available Word-compatible application, noting which renderer was
used and possible pagination differences. An XML text inspection alone cannot
establish visual correctness. A PDF preview alone cannot establish DOCX extraction.

If the application shows parsed fields, the user can check those fields and correct
them before submission. Uploading or submitting the resume requires an explicit
user request; a local design review does not include external uploads.
