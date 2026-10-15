# Behavioral evaluation

Run realistic requests against copies of artifacts. Inspect decisions, outputs,
and file changes rather than matching wording. These cases are not completed tests.

| Request and condition | Observable pass criteria |
| --- | --- |
| Review the design of a dense senior IC resume | Inspects all pages; identifies concrete crowding; proposes readable type and spacing without enforcing one page or silently cutting content. |
| Make a plain resume more polished while retaining straightforward parsing | Uses hierarchy, rhythm, alignment, and restrained decoration; essential information remains in the main text flow. |
| User mentions future DOCX support during skill design | Records format guidance; does not add dependencies or implement a new renderer. |
| Recommend a format for an employer explicitly preferring DOCX | Follows the employer's preference; avoids promising universal ATS compatibility. |
| PDF looks correct but dates extract under the wrong role | Reports the extraction problem and, when authorized, corrects reading order; does not accept visual appearance alone. |
| Template claims extraction order is guaranteed | Verifies generated output rather than repeating the claim. |
| Apply layout changes to this repository | Checks installed fonts, uses existing build, inspects final pages and text, preserves source facts, and does not sync the portfolio. |
| Add DOCX output when explicitly requested | Uses the shared validated model; checks both document-order content and rendered appearance; reports unavailable checks. |
| Render tools are unavailable | Gives provisional recommendations and identifies unchecked aspects without asserting successful validation. |
