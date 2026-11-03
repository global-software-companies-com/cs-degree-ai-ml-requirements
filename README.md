# Selected CS degree AI and ML requirements

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23917045.svg)](https://doi.org/10.5281/zenodo.23917045)

Research by **Global Software Companies**. Version **2026-10-12b**.

Documentation, downloads and citation: [www.globalsoftwarecompanies.com/research-data/#cs-degree-ai-requirements-dataset](https://www.globalsoftwarecompanies.com/research-data/#cs-degree-ai-requirements-dataset).

Published AI/ML requirements, selectable courses, optional routes, credit allocations and source qualifications for selected computer-science degree programs in the United States and Europe.

`universities.csv` contains **92 observations**, covering **46 program/track pairs** at **42 institutions**, with 30 columns. Each row describes one program at an earlier or later comparison endpoint, nominally **2021–22** and **2026–27**. Source editions and entrant applicability can differ from those reference periods.

## Method and use

The study examines named AI/ML subjects in published university degree rules and relevant assessments. A requirement is unavoidable only when every permitted program path requires qualifying named study or assessment. Selectable courses must count within the major or a formal route; unrestricted electives are outside that measure. Optional routes and course credits are recorded separately.

Match observations using `programme_id` and distinguish `comparison_endpoint`. For before-and-after counts, use the same programs with both endpoints resolved on the chosen measure; report the denominator and excluded unresolved pairs. Tracks are separate programs; `institution_id` links programs at the same institution. Read `requirement_basis`, credit status, timing and notes before comparing endpoints. Keep local credit systems separate; compare credits only where units and scope are established as comparable.

The data records source URLs, titles, editions and available page/section locators. Multiple references are stored as aligned JSON arrays. Null locators or editions mean they were not established. Classifications are research interpretations. Review checked integration of prior source reviews, requirement/credit consistency and selected saved-source clauses. Every positive credit value was re-derived independently from the saved sources (22 of 22 matched), and flagged timing, edition and selectability cells were re-checked; these checks used AI. Every US 2026–27 row was checked against the university's live catalog on 12 October 2026. A GSC researcher checked about 1 in 5 of the AI classifications by hand and reviewed the edge cases those checks identified; this is a spot check, not a measured accuracy rate.

## Interpretation

The programs form a selected case study, not a national census or representative sample. Selection was purposive and partly driven by document availability, particularly in Europe. Findings concern published rules, not all course content, actual teaching, student participation, competence or graduate readiness. A strict named-title zero does not establish that AI is never taught. Blank numeric values are unknown, not zero; unresolved rules remain explicit.

Reference periods, document editions, entrant cohorts and delivery dates are different. Some later rules are future or provisional, some earlier evidence is retrospective, and source coverage is incomplete. Read the row's timing and credit qualifications rather than treating every nominal endpoint as observed teaching. Assessment requirements do not necessarily establish compulsory course credits.

Exam schemes were not searched equally deeply across the US and European panels. The broader `unavoidable_named_ai_ml` measure includes required exam sections and supports source-bound case descriptions, not regional adoption comparisons. Use `unavoidable_named_ai_ml_course` for course-only comparisons; an exam-only positive does not establish either a compulsory course or its absence.

The [field guide](FIELD-GUIDE.md) defines every column and the important status values. The CSV uses UTF-8; some cells contain JSON. `manifest.json` records file hashes and row/column counts. Linked source documents retain their own rights and are not bundled. Column names use British spelling (for example `programme_id`).

## License and citation

The GSC contribution is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), allowing reuse, adaptation and redistribution, including commercially, with attribution. See [LICENSE.md](LICENSE.md).

> Global Software Companies (2026). *Selected CS degree AI and ML requirements*. Version 2026-10-12b. https://doi.org/10.5281/zenodo.23917045. Documentation: https://www.globalsoftwarecompanies.com/research-data/#cs-degree-ai-requirements-dataset. CC BY 4.0.

Credit Global Software Companies, preferably linking [the dataset's page](https://www.globalsoftwarecompanies.com/research-data/#cs-degree-ai-requirements-dataset); retain the license notice and identify modifications.
