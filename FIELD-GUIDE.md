# University dataset field guide

One row describes one program/track at one comparison endpoint. Match `programme_id` across `earlier` and `later`; `institution_id` groups programs at an institution. Reference periods are nominal 2021–22 and 2026–27. Source editions, entrant cohorts and actual delivery dates can differ.

The named-title measure concerns explicit AI/ML subjects in degree rules. A strict-title negative or zero does not establish no AI teaching or student competence. Selectability concerns major or formal-route requirements. Blank numbers are unknown, not zero. JSON arrays preserve multiple values; source URL/title/locator/edition arrays align by position. A null locator or edition is unverified.

Credit values retain local units. Cambridge exam evidence does not establish compulsory-course credits. Lisbon plan credits have unverified ECTS equivalence. Berlin's later rule applies to October 2026 entrants and schedules first teaching for 2027–28; actual delivery is not established. Read row notes before comparing values.

## Fields

### universities.csv

One program at one observed endpoint; tracks remain distinct.

| Field | Meaning |
| --- | --- |
| `programme_id` | Stable identity for a degree/track across earlier and later observations. |
| `institution_id` | Shared institutional identity across its programs. |
| `institution_name` | Readable, source-supported institutional name. |
| `country` | Recorded program country. |
| `degree_name` | Source-supported degree/track wording. |
| `study_panel` | US or European research panel; not a representative population label. |
| `observation_id` | Stable identifier for one program observation |
| `comparison_endpoint` | Earlier or later comparison observation |
| `reference_period` | Study reference period; distinct from source date |
| `source_document_editions` | Relevant source editions with dating qualifications |
| `applicable_entrant_cohort` | Rule applicability to entrants where established |
| `time_basis` | Defined basis for interpreting timing |
| `unavoidable_named_ai_ml` | All permissible paths require named AI/ML course or qualifying assessment |
| `unavoidable_named_ai_ml_course` | All permissible paths require named AI/ML course specifically |
| `requirement_basis` | single_required, ai_only_choice, required_exam_section, none or unresolved |
| `named_ai_ml_course_selectable` | Named course eligible within selectable major or formal route requirements |
| `named_ai_ml_avoidable_path` | Documented path avoids named AI/ML study and assessment |
| `explicit_ai_ml_named_optional_route` | Formal optional route named AI or ML |
| `ai_ml_optional_route_names` | Names of formal AI/ML-named optional routes |
| `other_route_requires_ai_ml` | Optional non-AI/ML-named route requires named AI/ML beyond any universal core |
| `other_ai_ml_required_route_names` | Names of those qualifying routes; not all optional routes |
| `minimum_named_ai_ml_course_credits` | Minimum unavoidable named-course credits across permitted paths under strict title measure |
| `credit_unit` | Original local credit system; no invented equivalence |
| `credit_evidence_status` | Credit value evidence status, preserving unresolved and exam-only cases |
| `compulsory_study_details` | Named courses, choices or assessments underlying the finding |
| `notes` | Material source, credit, timing and interpretation qualifications |
| `source_status` | Recorded completeness, applicability or provisional status |
| `source_url` | Readable university evidence references |
| `source_title` | Source document/page identity and edition |
| `source_locator` | Supporting page or section where recorded |

## Categorical values

Requirement and route indicators use `yes`, `no`, `unresolved` or, where recorded, `not_assessed`. `unresolved` means the evidence does not settle the finding; `not_assessed` means no finding was made. Neither is a negative.

| Requirement basis | Meaning |
| --- | --- |
| `single_required` | A named AI/ML course is compulsory. |
| `ai_only_choice` | A compulsory choice permits only named AI/ML options. |
| `required_exam_section` | A qualifying named assessment section is required; compulsory course credits need not follow. |
| `none` | No unavoidable named requirement under this measure. |
| `unresolved` | Available evidence does not settle the requirement. |

| Credit evidence status | Interpretation |
| --- | --- |
| `zero_by_strict_named_title_rule` | Zero unavoidable named-course credits under the defined measure. |
| `unresolved_compulsory_rule` | Compulsory rules are unresolved; minimum not established. |
| `verified` | Recorded local credits supported by source evidence. |
| `verified_component_sum` | Minimum calculated from supported required components. |
| `verified_future_rule`, `verified_future_plan`, `verified_late_rule` | Supported published rule/plan with future or later dating; read timing. |
| `qualified_late_edition`, `qualified_credit_year`, `qualified_retrospective`, `qualified_informative_guide`, `qualified_provisional` | Credit finding carries the stated edition/year/evidence qualification; read notes. |
| `exam_only_course_credit_not_established` | Required exam evidence does not establish compulsory course credits. |

`source_status` describes recorded coverage or applicability: `complete`/`full`, `partial`/`incomplete`, `provisional` or `missing`. It does not certify program delivery or source correctness. Row notes preserve material credit, timing and interpretation limits.
