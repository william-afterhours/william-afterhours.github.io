#!/usr/bin/env python3
"""Wikimedia Commons 파일을 메타데이터와 함께 받는다. 표준 라이브러리만 쓴다.

usage:
  python3 -I tools/commons_fetch.py --out <dir> [--width 1280] "File:제목.jpg=로컬이름" ...

각 파일마다 라이선스·저자·날짜·설명을 API(prop=imageinfo)에서 받아 `assets/index.md`에
붙여 넣을 수 있는 마크다운 표 행을 출력하고, 지정 폭의 축소본을 <dir>/<로컬이름>.<ext>로 받는다.
라이선스가 PD·CC0·CC BY·CC BY-SA가 아니면 받지 않고 경고만 낸다(공개 저장소에 올리므로).
받은 파일은 반드시 눈으로 열어 캡션이 사진 내용과 맞는지 확인한 뒤 assets/로 옮긴다.
"""
import argparse, html, json, pathlib, re, sys, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "WilliamAfterhours/0.1 (research; williamafterhours@proton.me)"
OK_LICENSE = re.compile(r"^(Public domain|CC0|CC BY(-SA)? [0-9.]+)", re.I)


def strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


def api(params):
    q = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("items", nargs="+", help='"File:제목=로컬이름" (로컬이름은 확장자 없이)')
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    pairs = []
    for it in a.items:
        title, _, local = it.rpartition("=")
        if not title:
            sys.exit(f"형식 오류: {it}")
        pairs.append((title, local))
    d = api({
        "action": "query", "prop": "imageinfo", "format": "json",
        "iiprop": "url|extmetadata|size|mime", "iiurlwidth": a.width,
        "titles": "|".join(t for t, _ in pairs),
    })
    pages = {p["title"]: p for p in d["query"]["pages"].values()}
    norm = {}
    for n in d["query"].get("normalized", []):
        norm[n["from"]] = n["to"]
    print("| 파일 | 무엇 | 출처 | 저자·연도 | 라이선스 |")
    print("|---|---|---|---|---|")
    for title, local in pairs:
        p = pages.get(norm.get(title, title))
        if not p or "imageinfo" not in p:
            print(f"!! 없음: {title}", file=sys.stderr)
            continue
        ii = p["imageinfo"][0]
        em = ii.get("extmetadata", {})
        g = lambda k: strip(em.get(k, {}).get("value", ""))
        lic = g("LicenseShortName")
        if not OK_LICENSE.match(lic):
            print(f"!! 라이선스 부적합({lic}): {title}", file=sys.stderr)
            continue
        url = ii.get("thumburl") or ii["url"]
        url = url.replace("https://thumb.wikimedia.org", "https://upload.wikimedia.org").split("?")[0]
        ext = {"image/jpeg": "jpg", "image/png": "png", "image/svg+xml": "svg"}.get(ii.get("mime"), "jpg")
        if local.lower().endswith((".jpg", ".jpeg", ".png", ".svg")):
            local = local.rsplit(".", 1)[0]
        dest = out / f"{local}.{ext}"
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
            f.write(r.read())
        page = "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(p["title"].replace(" ", "_"))
        date = re.sub(r"date QS:.*$", "", g("DateTimeOriginal"))[:20]
        print(f"| `{dest.name}` | {g('ImageDescription')[:120]} | [Commons]({page}) | {g('Artist')[:60]} · {date} | {lic} |")
        print(f"   -> {dest} ({dest.stat().st_size // 1024} KB, 원본 {ii.get('width')}x{ii.get('height')})", file=sys.stderr)


if __name__ == "__main__":
    main()
