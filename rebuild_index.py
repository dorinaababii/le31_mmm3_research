#!/usr/bin/env python3
"""Rebuild /tmp/le31-daily-2026-08-07/index.json as a proper JSON array
with EUR-Lex status overrides."""
import json, os, sys

RAW = '/tmp/le31-daily-2026-08-07'
INDEX = os.path.join(RAW, 'index.json')

# Read JSONL (each line is one JSON object)
entries = []
with open(INDEX) as f:
    for line in f:
        line = line.strip().rstrip(',')
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"skip bad line: {line[:80]}", file=sys.stderr)

# Status overrides from re-test of EUR-Lex with 60s timeout
overrides = {
    'eurlex_1.xml':  ('000', 'timeout 60s — WAF or upstream hang, no body received'),
    'eurlex_2.xml':  ('000', 'timeout 60s — WAF or upstream hang, no body received'),
    'eurlex_3.xml':  ('404', '404 page (55KB body) — endpoint not found at this rssId'),
    'eurlex_4.xml':  ('000', 'timeout 60s — WAF or upstream hang, no body received'),
    'eurlex_5.xml':  ('000', 'timeout 60s — WAF or upstream hang, no body received'),
    'eurlex_18.xml': ('000', 'timeout 60s — WAF or upstream hang, no body received'),
}

for e in entries:
    fn = e['filename']
    if fn in overrides:
        e['http_status'] = overrides[fn][0]
        e['note'] = overrides[fn][1]
    # refresh byte_size from disk
    path = os.path.join(RAW, fn)
    e['byte_size'] = os.path.getsize(path) if os.path.exists(path) else 0

# Write as JSON array
with open(INDEX, 'w') as f:
    json.dump(entries, f, indent=2)

print(f"Wrote {len(entries)} entries to {INDEX}")
for e in entries:
    print(f"  {e['filename']:40s} {e['http_status']:>5s} {e['byte_size']:>9d}")