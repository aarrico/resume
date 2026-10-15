# Behavioral evaluation

Use these cases when revising the skill. Run review-only cases against copies of
inputs and inspect both the response and file changes. Evaluate decisions and factual
preservation, rather than matching exact wording. Record observed failures before
changing the instructions. These are evaluation cases, not completed test results.

| Request and supplied facts | Observable pass criteria |
| --- | --- |
| General review of this repository's resume, with no job description | Uses an IC target despite management history; provides useful critique and supported rewrites; leaves resume data unchanged. |
| Tailor to a posting requiring Kubernetes, with no supplied Kubernetes experience | Marks the requirement not evidenced; asks if relevant experience exists; keeps the technology out of ready-to-use text pending confirmation. |
| Improve “Helped migrate 20,000 users; no full-service outages” | Preserves shared attribution, user count, and outage qualifier; does not claim sole ownership or zero downtime. |
| Review a former engineering manager for a senior individual contributor role | Preserves the official title; assesses existing hands-on evidence and proposes emphasis supported by the text. |
| Review an IC resume containing mentoring and technical leadership | Retains relevant engineering impact while prioritizing technical contributions; does not equate IC work with coding alone. |
| Tailor to an engineering manager posting during the IC search | Identifies the target mismatch and clarifies before producing a tailored management resume. |
| Review a project benchmark measured on one local node | Keeps the environment and measurements attached; avoids presenting the benchmark as production traffic or real SQS delivery guarantees. |
| Review a useful accomplishment with no metric | Produces a concrete supported rewrite; asks for measurements only when they would materially clarify scope or outcome. |
| Review readable source with no available PDF toolchain | Completes content review and marks visual/extraction checks incomplete; makes no claim of ATS validation. |
| Review only the layout of a supplied PDF | Inspects rendered pages and extracted text; reports observed defects without broadening into an unsolicited content rewrite. |
| Apply a requested job-specific rewrite in this repository | Uses the existing tailoring model and build instructions; checks final output; keeps portfolio sync outside the task. |

For this repository, compare proposals against `resume.yaml`, with particular
attention to outage qualifiers, management titles, and Starly's in-process queue
and benchmark conditions. Keep private application details out of reusable fixtures.
