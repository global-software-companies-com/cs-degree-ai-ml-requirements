#!/usr/bin/env python3
"""Recompute the figures in GSC's article #2 (do US computer science degrees require AI?) from universities.csv.

Run in this folder: python3 reproduce.py   (Python 3, standard library only)
"""
import collections
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPECTED = {
    "US: degree tracks": 25,
    "US: institutions": 21,
    "US: requires a named AI/ML course (earlier) = no": 22,
    "US: requires a named AI/ML course (earlier) = unresolved": 1,
    "US: requires a named AI/ML course (earlier) = yes": 2,
    "US: requires a named AI/ML course (later) = no": 19,
    "US: requires a named AI/ML course (later) = yes": 6,
    "US: tracks resolved at both endpoints (course-only)": 24,
    "US: of those, requiring a named AI/ML course (earlier)": 2,
    "US: of those, requiring a named AI/ML course (later)": 6,
    "US: path avoiding a named AI/ML course (earlier)": 22,
    "US: selectable and avoidable, \"optional\" (earlier)": 19,
    "US: institutions with a required track (earlier)": 2,
    "US: path avoiding a named AI/ML course (later)": 19,
    "US: selectable and avoidable, \"optional\" (later)": 18,
    "US: institutions with a required track (later)": 5,
    "Europe: degree tracks": 21,
    "Europe: requires a named AI/ML course (earlier) = no": 12,
    "Europe: requires a named AI/ML course (earlier) = unresolved": 3,
    "Europe: requires a named AI/ML course (earlier) = yes": 6,
    "Europe: requires a named AI/ML course (later) = no": 10,
    "Europe: requires a named AI/ML course (later) = unresolved": 3,
    "Europe: requires a named AI/ML course (later) = yes": 8,
    "Europe: tracks resolved at both endpoints (course-only)": 16,
    "Europe: of those, requiring a named AI/ML course (earlier)": 4,
    "Europe: of those, requiring a named AI/ML course (later)": 7
}
ENDS = ('earlier', 'later')


def main():
    rows = list(csv.DictReader(open(HERE / 'universities.csv', encoding='utf-8', newline='')))
    progs = collections.defaultdict(dict)
    for r in rows:
        progs[r['programme_id']][r['comparison_endpoint']] = r
    got = {}
    for panel in ('US', 'Europe'):
        ps = {p: e for p, e in progs.items() if e['later']['study_panel'] == panel}
        got[f'{panel}: degree tracks'] = len(ps)
        got[f'{panel}: institutions'] = len({e['later']['institution_id'] for e in ps.values()})
        for end in ENDS:
            for v, k in collections.Counter(e[end]['unavoidable_named_ai_ml'] for e in ps.values()).items():
                got[f'{panel}: requires a named AI/ML course ({end}) = {v}'] = k
        field = 'unavoidable_named_ai_ml_course'
        pairs = {p: e for p, e in ps.items() if all(e[end][field] in ('yes', 'no') for end in ENDS)}
        got[f'{panel}: tracks resolved at both endpoints (course-only)'] = len(pairs)
        for end in ENDS:
            got[f'{panel}: of those, requiring a named AI/ML course ({end})'] = sum(e[end][field] == 'yes' for e in pairs.values())
        if panel == 'US':
            for end in ENDS:
                got[f'US: path avoiding a named AI/ML course ({end})'] = sum(e[end]['named_ai_ml_avoidable_path'] == 'yes' for e in ps.values())
                got[f'US: selectable and avoidable, "optional" ({end})'] = sum(
                    e[end]['named_ai_ml_avoidable_path'] == 'yes' and e[end]['named_ai_ml_course_selectable'] == 'yes'
                    for e in ps.values())
                got[f'US: institutions with a required track ({end})'] = len(
                    {e[end]['institution_name'] for e in ps.values() if e[end]['unavoidable_named_ai_ml'] == 'yes'})
    ok = bad = 0
    for key, want in EXPECTED.items():
        have = got.get(key, 0)
        same = have == want
        ok += same
        bad += not same
        print(f"{'OK      ' if same else 'MISMATCH'} {key:<72} {have}  (published {want})")
    print(f'\n{ok} figures reproduced, {bad} mismatches.')
    raise SystemExit(1 if bad else 0)


if __name__ == '__main__':
    main()
