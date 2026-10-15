# Evidence and design judgments

Sources checked 2026-10-15. These are vendor documentation and employer guidance,
not an independent comparison of all ATS parsers or validation of this skill.

- [Greenhouse supported uploads](https://support.greenhouse.io/hc/en-us/articles/360052218132-Supported-formats-for-resumes-cover-letters-and-other-candidate-uploads)
  includes PDF and DOCX. Upload acceptance and successful parsing are distinct.
- [Greenhouse parsing failures](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse)
  describes risks from columns, complex formatting, images, and essential text in
  headers, footers, or text boxes. It describes field extraction, not a universal
  hiring rejection rule.
- [Microsoft Careers transparency FAQ](https://careers.microsoft.com/v2/global/en/transparency.html)
  recommends simple PDF or DOCX and warns that complex formatting can impede
  extraction. Candidates can inspect and correct extracted profile information.
- [Roche resume parsing FAQ](https://careers.roche.com/global/en/resume-parsing-faq)
  recommends DOCX for parsing accuracy and recognizes PDF's formatting stability.
  It permits ordinary typographic emphasis and color that does not carry essential
  meaning. Treat the file preference as employer guidance, not a benchmark proving
  every DOCX outperforms every PDF.

Comfortable whitespace, restrained rules, approximate type sizes and margins, and
accepting a useful second page are design choices. They should be assessed against
the actual artifact and the user's preference for a less crowded resume. None is
a certified ATS threshold. A plain-text extraction check is useful evidence of
reading order, but does not reproduce every application's field extraction.
