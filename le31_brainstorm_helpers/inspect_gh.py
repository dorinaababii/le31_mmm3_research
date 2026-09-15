#!/usr/bin/env python3
"""Surface the top hits across all GitHub search JSONs in window."""
import json
from pathlib import Path
from datetime import datetime

GH = Path("/tmp/le31-brainstorm-2026-08-29/gh")
WIN_FROM = datetime.fromisoformat("2026-07-30T00:00:00+00:00")
WIN_TO = datetime.fromisoformat("2026-08-29T06:51:00+00:00")

for f in sorted(GH.glob("*.json")):
    if f.name.startswith("_FAIL") or "_FAIL_" in f.name:
        continue
    try:
        d = json.loads(f.read_text())
    except Exception:
        continue
    if "items" in d:
        items = d.get("items", [])
        tc = d.get("total_count", 0)
        kind = "search"
    elif "stargazers_count" in d:
        items = [d]
        tc = 1
        kind = "direct"
    else:
        continue
    print(f"=== {f.name}  ({kind}, total_count={tc}, items={len(items)}) ===")
    for it in items[:5]:
        stars = it.get("stargazers_count", 0)
        forks = it.get("forks_count", 0)
        lang = it.get("language")
        lic = (it.get("license") or {}).get("spdx_id") if it.get("license") else None
        ca = it.get("created_at", "?")
        pa = it.get("pushed_at", "?")
        try:
            ca_dt = datetime.fromisoformat(ca.replace("Z", "+00:00"))
            pa_dt = datetime.fromisoformat(pa.replace("Z", "+00:00"))
            in_window_create = WIN_FROM <= ca_dt <= WIN_TO
            in_window_push = WIN_FROM <= pa_dt <= WIN_TO
        except Exception:
            in_window_create = in_window_push = False
        win = ("CREATE" if in_window_create else "no_create") + "/" + ("PUSH" if in_window_push else "no_push")
        desc = (it.get("description") or "")[:100]
        print(f"   {it.get('full_name'):40}  ★{stars}  fork={forks}  lang={lang}  lic={lic}  win={win}  -- {desc}")
