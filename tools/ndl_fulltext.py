"""Fetch the OCR full text of one NDL Digital Collections book through NDL Lab.

Usage: python3 -I tools/ndl_fulltext.py <pid> <out_dir>

Writes <out_dir>/<pid>.json (book metadata incl. table of contents) and
<out_dir>/<pid>.txt (one block per scan image: "=== p<page>" then the OCR text).
Page numbers are scan-image numbers (the NNNN of NNNN.jp2), not printed pages.
Endpoints (no key, 2026-11-06): /dl/api/book/<pid>, /dl/api/book/fulltext-json/<pid>.
"""
import json
import os
import sys
import urllib.request

pid, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
base = "https://lab.ndl.go.jp/dl/api/book/"
meta = json.load(urllib.request.urlopen(base + pid, timeout=60))
json.dump(meta, open(os.path.join(out, pid + ".json"), "w"), ensure_ascii=False, indent=1)
ft = json.load(urllib.request.urlopen(base + "fulltext-json/" + pid, timeout=120))
pages = sorted(ft["list"], key=lambda r: (r["page"], r.get("divide", 0)))
with open(os.path.join(out, pid + ".txt"), "w") as f:
    for r in pages:
        f.write("=== p%d\n%s\n" % (r["page"], r.get("contents", "")))
print(meta.get("title"), meta.get("publishyear"), len(pages), "blocks")
