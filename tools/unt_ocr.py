"""UNT Digital Library: rebuild page text from IIIF OCR annotations.
usage: unt_ocr.py <ark e.g. metadc461689> <npages> <out.txt> <dl_dir>
"""
import json, sys, urllib.request, os, re, time

ark, n, out, dl = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
os.makedirs(dl, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}
pages = []
for p in range(1, n + 1):
    f = os.path.join(dl, f"{ark}_p{p}.json")
    if not os.path.exists(f):
        url = f"https://digital.library.unt.edu/ark:/67531/{ark}/m1/{p}/annotations/ocr/"
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=60) as r:
            open(f, "wb").write(r.read())
        time.sleep(0.5)
    d = json.load(open(f))
    words = []
    for a in d.get("resources", []):
        m = re.search(r"xywh=(\d+),(\d+),(\d+),(\d+)", a.get("on", ""))
        if not m:
            continue
        x, y, w, h = map(int, m.groups())
        words.append((y, x, h, a["resource"]["chars"]))
    # group into lines by y proximity
    words.sort()
    lines, cur, cur_y = [], [], None
    for y, x, h, c in words:
        if cur_y is None or abs(y - cur_y) <= max(8, h // 2):
            cur.append((x, c))
            cur_y = y if cur_y is None else cur_y
        else:
            lines.append(" ".join(c for _, c in sorted(cur)))
            cur, cur_y = [(x, c)], y
    if cur:
        lines.append(" ".join(c for _, c in sorted(cur)))
    pages.append(f"\n===== PAGE {p} =====\n" + "\n".join(lines))
open(out, "w").write("".join(pages))
print(n, "pages ->", out, sum(len(x.split()) for x in pages), "words")
