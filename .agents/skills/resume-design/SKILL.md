---
name: resume-design
description: Review or improve software engineering IC resume layout, typography, section structure, and PDF or DOCX parsing readiness. Use for visual design and formatting requests.
---

# Resume design

Make software engineering IC resumes comfortable to read and straightforward to
extract as text. Default to restrained typography, comfortable spacing, clear
hierarchy, and subtle rules. Treat that direction as the user's preference, not an
industry mandate. Give a design critique when asked for review; modify templates
when asked to redesign or apply changes.

## Establish the artifact and constraints

Read repository editing and build instructions, the canonical resume source, and
the layout template. Identify the target market, page size, existing outputs, and
any supplied employer upload instructions. Keep factual content intact during a
design pass; propose content cuts or rewrites separately when space requires them.

Distinguish a visual contact block at the top of page one from an actual document
header or text box: keep essential information in the main reading flow. Preserve
the existing data model and rendering stack unless the requested change needs more.

Done when the source, renderer, output format, and design scope are identified.

## Inspect before prescribing

For an existing PDF, inspect every rendered page and extract text using the PDF
skill or local tools such as `pdftoppm` and `pdftotext`. Compare the document with
the canonical source for missing text and incorrect role/date associations. Treat
template comments about reading order as intentions to verify in the artifact.

Separate findings into observed rendering defects, extraction problems, and design
judgments. Identify crowding, weak hierarchy, excessive wrapping, awkward breaks,
or scattered metadata with a page and concrete example. If output cannot be built
or inspected, mark recommendations provisional and identify the unavailable checks.

Done when the major layout issues are tied to observed evidence, or the review's
inspection limits are explicit.

## Design for reading and extraction

- **Reading flow:** Use a single main column with conventional section headings.
  Keep role, company, location, and dates visibly associated and correctly ordered
  in extracted text. Prefer simple text alignment over tables, sidebars, floating
  boxes, icons, or images carrying information.
- **Hierarchy:** Make the name, section headings, and roles easy to distinguish
  through a small, consistent set of sizes and weights. Use regular body text,
  selective bold, and limited italics. Thin rules or muted accents may support
  hierarchy; all meaning must survive grayscale and plain-text extraction.
- **Typography:** Use an installed, readable font and check substitutions. For a
  US Letter resume, begin around 11 pt body text and 0.6–0.75 inch margins, then
  judge the rendered result at normal viewing size. These are starting points,
  not ATS thresholds. Give supporting text comparable legibility; distinguish
  hierarchy through weight and spacing before shrinking dates or contact details.
- **Spacing:** Use a consistent rhythm between sections, roles, and bullets; keep
  wrapped lines visually grouped with their bullet. Allow whitespace that helps
  scanning. Avoid wide gaps caused by overprotecting large unbreakable blocks.
- **Pagination:** Keep headings with following content, and role headings with
  enough context to identify the work. Prefer intact bullets where practical.
  Inspect every page boundary, including long roles continued across pages.
  Choose length for relevant evidence and legibility: a useful second page is
  preferable to a cramped first page. Propose cuts before making type uncomfortably
  small; distinguish removing content from merely changing its presentation.
- **Section order:** For experienced IC candidates, keep relevant professional
  engineering experience prominent. Place skills, summary, and projects according
  to how much they help establish fit, rather than a rigid template. Preserve
  chronological and semantic associations when moving sections.
- **Contact and links:** Use actual text for email, phone, and recognizable URLs.
  Keep essential information in the document body and provide visible link text
  that remains useful when printed. Use standard bullets and separators, checking
  extraction for missing or substituted characters.

Prioritize usable reading order and legibility, then refine polish. Explain design
tradeoffs with the actual content; avoid invented ATS scores or pass guarantees.

Done when the proposed or implemented design addresses the observed problems and
has a coherent typography, spacing, hierarchy, and pagination plan.

## Choose formats deliberately

Follow employer upload instructions first. Simple text-based PDF and DOCX can both
be suitable; acceptance does not prove correct parsing. Preserve a working PDF
build. Treat DOCX as a useful additional output when requested or required by an
application, rather than automatically replacing the renderer.

For format recommendations, employer-specific requirements, or adding DOCX support,
read [formats.md](references/formats.md). The user's openness to future DOCX support
is context, not a request to implement it during skill creation or a design review.

## Implement and verify when requested

Edit maintained templates or rendering code, rather than generated files. Follow
the repository's font checks and build commands. Inspect every final page at a
readable scale for alignment, whitespace, wrapping, clipping, and page breaks.
Compare extracted text with source for contact details, headings, dates, roles,
skills, and bullets. Check ordinary extraction order as well as layout-preserving
extraction when diagnosing positioned text. Account for line wrapping and ligatures
before classifying textual differences as lost content.

When making both PDF and DOCX, inspect each independently; matching content does
not guarantee matching pagination. Recheck after the last layout change. If a check
is unavailable, report it as incomplete rather than inferring success.

Done when the build succeeds, rendered pages have been inspected, content has been
accounted for, and remaining limitations are explicit. Local checks establish
readability and extraction sanity, not behavior in every employer's ATS.

## Deliver

Explain the principal design issue and the decisions that address it. For a review,
provide prioritized recommendations; for an implementation, link final artifacts
and summarize visual and extraction checks. Identify remaining content decisions
without expanding the task into a rewrite.

For evidence behind parser guidance or disputed design rules, read
[evidence.md](references/evidence.md). When changing this skill, use
[evaluation.md](references/evaluation.md) to evaluate behavior.
