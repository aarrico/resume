---
name: resume-review
description: Review resumes for software engineering individual contributor roles; assess technical evidence and readability, propose grounded rewrites, or tailor to a supplied IC job description.
---

# Resume review

Help a reader recognize the candidate's fit for a software engineering individual
contributor (IC) role through relevant engineering work and personal contribution.
Default to critique and proposed rewrites. Change resume files only when the user
asks for edits or tailoring. Follow repository instructions for sources and builds.

## Establish the target

Read the supplied resume and local editing instructions. Identify the intended role,
level, and market from the request and resume. Default to IC roles; a management
title in the candidate's history does not change the search target. If the supplied
posting is a people-management role, clarify the target before tailoring.
State material assumptions; ask only
for missing context that changes the recommendations. A general review can proceed
without a job description. Treat a stated target level as a goal to assess against,
rather than a qualification already established by the resume.

For a supplied job description, separate required qualifications from preferences
and map each material requirement to resume evidence: demonstrated, partial, or
not evidenced. Cite the relevant role or bullet. Absence from the resume means
unknown experience, not a proven lack of ability. Distinguish a wording omission
from a substantive gap; recommend adding a keyword only when the experience supports it.

Done when the target and review scope are explicit and, for tailoring, the material
requirements have evidence mappings.

## Diagnose before rewriting

Review the entire resume, including older roles and projects, before selecting fixes.
Assess these dimensions with concrete examples:

- **Positioning:** Can the opening and most prominent experience explain the fit?
  Surface documented coding, design, and operational contributions, including work
  performed under management titles. Preserve official titles. Retain mentoring and
  technical leadership when they demonstrate engineering impact; prioritize direct
  technical evidence over hiring, headcount growth, and process administration.
- **Engineering evidence:** Do the strongest bullets explain the system or problem,
  the candidate's action, and the resulting change? Look for relevant technical
  decisions, constraints, ownership, and operational responsibility. Distinguish
  personal contribution from team outcomes. Assess senior IC fit through evidence
  of engineering judgment, technical scope, and delivery ownership rather than years
  of service or management seniority alone.
- **Credibility:** Flag ambiguous attribution, inconsistent dates, unexplained
  metrics, and claims broader than the described implementation. Preserve benchmark
  conditions and distinguish prototypes from production systems.
- **Selection:** Allocate space by relevance and distinct evidence. Identify
  redundancy and lower-value detail before proposing cuts. Projects earn space
  through evidence they add beyond professional experience.
- **Readability:** Assess terminology, bullet density, section order, and how easily
  a reader can locate roles, dates, skills, and accomplishments. Choose length based
  on relevant evidence and legibility; treat one or two pages as a tradeoff rather
  than a universal rule.

Rank findings by their likely effect on understanding fit, with credibility and
missing core evidence ahead of cosmetic preferences. Label subjective advice as
judgment. Use qualitative assessments tied to evidence, not invented ATS scores,
shortlist predictions, or hiring probabilities.

Done when all dimensions have been considered and each reported problem has a
specific location, reason it matters, and actionable correction. Preserve strengths
that the proposed changes could accidentally remove.

## Propose grounded changes

For high-priority findings, show the original excerpt, proposed wording, and why
the revision helps. Prefer action, technical mechanism, and outcome where supported;
a concrete deliverable or constraint can be useful without a numerical result.
Retain the candidate's voice and enough technical detail to distinguish the work.

Every factual statement in a rewrite must trace to supplied material or an explicit
user confirmation. Preserve employers, official titles, dates, technologies, scope,
metric qualifiers, and strength of causal claims. Never fill an evidence gap with
an invented number or turn team participation into sole ownership. Existing claims
are supplied evidence, not independently verified facts.

When a stronger bullet needs new information, give a safe rewrite using known facts
and ask a focused question separately. Keep unconfirmed placeholders out of proposed
ready-to-use resume text. Continue reviewing material unaffected by the question.

Done when every proposed rewrite is supported and each unresolved factual dependency
is identified as a question rather than silently incorporated.

## Check the delivered document

When a PDF is available or buildable locally, inspect rendered pages and extracted
text. Use the available PDF skill for visual inspection, or render with `pdftoppm`
and extract with `pdftotext`. Keep the repository's existing build and output paths.
Check clipping, page breaks, readable type, contact details, heading order, and
association of dates with the right roles in extracted text. Extraction is a local
sanity check, not proof of compatibility with an employer's parser.

When only source text is available, complete the content review and state that PDF
layout and extraction remain unchecked. Keep documents local unless the user requests
an external service. A layout-only request should remain a layout review.

After authorized edits, rebuild and inspect the final artifact according to the
repository instructions. Report any unavailable check accurately.

## Deliver the review

Lead with the main positioning finding, then a short prioritized set of fixes and
grounded rewrites. Include the requirement mapping when a job description was
supplied, remaining factual questions, and what document checks were completed.
Scale detail to the request; avoid a full rewrite when the user asked for a review.

For the research basis or disputed advice, read [evidence.md](references/evidence.md).
For checking changes to this skill, use [evaluation.md](references/evaluation.md).
