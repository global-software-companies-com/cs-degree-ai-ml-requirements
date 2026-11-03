# Reproducing the figures in GSC's article on CS degrees and AI (#2)

Run `python3 reproduce.py` in this folder (Python 3, standard library only). It recomputes the figures below from `universities.csv` and prints `OK` or `MISMATCH` for each.

## Rules

- **Programs and tracks.** One program or track per `programme_id`, with two rows: `comparison_endpoint` `earlier` (2021–22) and `later` (2026–27). `study_panel` is `US` or `Europe`.
- **"Requires a named AI/ML course"** is `unavoidable_named_ai_ml = yes`.
- **"Has a path avoiding one"** is `named_ai_ml_avoidable_path = yes`. **"Optional"** also needs `named_ai_ml_course_selectable = yes`.
- **Before-and-after comparisons** use `unavoidable_named_ai_ml_course` on programs resolved (`yes` or `no`) at both endpoints, as the field guide asks.

## Published values checked

| Figure | Value |
| --- | ---: |
| US: degree tracks | 25 |
| US: institutions | 21 |
| US: requires a named AI/ML course (earlier) = no | 22 |
| US: requires a named AI/ML course (earlier) = unresolved | 1 |
| US: requires a named AI/ML course (earlier) = yes | 2 |
| US: requires a named AI/ML course (later) = no | 19 |
| US: requires a named AI/ML course (later) = yes | 6 |
| US: tracks resolved at both endpoints (course-only) | 24 |
| US: of those, requiring a named AI/ML course (earlier) | 2 |
| US: of those, requiring a named AI/ML course (later) | 6 |
| US: path avoiding a named AI/ML course (earlier) | 22 |
| US: selectable and avoidable, "optional" (earlier) | 19 |
| US: institutions with a required track (earlier) | 2 |
| US: path avoiding a named AI/ML course (later) | 19 |
| US: selectable and avoidable, "optional" (later) | 18 |
| US: institutions with a required track (later) | 5 |
| Europe: degree tracks | 21 |
| Europe: requires a named AI/ML course (earlier) = no | 12 |
| Europe: requires a named AI/ML course (earlier) = unresolved | 3 |
| Europe: requires a named AI/ML course (earlier) = yes | 6 |
| Europe: requires a named AI/ML course (later) = no | 10 |
| Europe: requires a named AI/ML course (later) = unresolved | 3 |
| Europe: requires a named AI/ML course (later) = yes | 8 |
| Europe: tracks resolved at both endpoints (course-only) | 16 |
| Europe: of those, requiring a named AI/ML course (earlier) | 4 |
| Europe: of those, requiring a named AI/ML course (later) | 7 |
