#!/usr/bin/env bash
# 연구 저장소의 마크다운을 Quartz 소스 트리에 올려놓는다.
# usage: site/assemble.sh <repo_dir> <quartz_src_dir>
# 로컬 확인: site/assemble.sh . ../quartz-src && (cd ../quartz-src && npm ci && npx quartz build)
set -euo pipefail
REPO=$(cd "$1" && pwd)
Q=$(cd "$2" && pwd)

cp "$REPO/site/quartz.config.ts" "$REPO/site/quartz.layout.ts" "$Q/"
cp "$REPO/site/custom.scss" "$Q/quartz/styles/custom.scss"
# 저자란 등 이 저장소만의 구성 요소
cp "$REPO"/site/components/*.tsx "$Q/quartz/components/"

rm -rf "$Q/content"
mkdir -p "$Q/content"
# ko/ 는 한국어 읽는 글(카드의 위층 번역)과 한국어 안내. 영어가 주 언어다.
for d in cases entities docs sources assets ko; do
  [ -d "$REPO/$d" ] && cp -R "$REPO/$d" "$Q/content/$d"
done
# 첫 페이지는 README. 제목은 아래 파이썬 단계가 첫 줄의 `# 제목`에서 올린다.
cp "$REPO/README.md" "$Q/content/index.md"

# 두 가지 손질.
# ① Quartz는 날짜를 `modified:`에서만 읽는다. 카드·엔티티의 `updated:`를 `modified:`로 복사해 넣는다.
# ② 본문 첫 줄이 `# 제목`이면 프론트매터 `title`로 올리고(없을 때만) 본문에서 뺀다.
#    Quartz가 제목을 따로 그리므로 두 번 보이는 것을 막고, 탐색기·그래프에 파일명 대신 제목이 뜬다.
python3 - "$Q/content" <<'PY'
import json, pathlib, re, sys
root = pathlib.Path(sys.argv[1])
n_mod = n_title = n_h1 = 0
for p in root.rglob("*.md"):
    t = p.read_text(encoding="utf-8")
    fm, body = "", t
    if t.startswith("---\n"):
        end = t.find("\n---\n", 4)
        if end >= 0:
            fm, body = t[4:end], t[end + 5:]
    orig_fm, orig_body = fm, body
    if fm and not re.search(r"^modified:", fm, re.M):
        m = re.search(r"^updated:\s*(\S+)", fm, re.M)
        if m:
            fm += f"\nmodified: {m.group(1)}"
            n_mod += 1
    lines = body.split("\n")
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        h1 = lines[i][2:].strip()
        if not re.search(r"^title:", fm, re.M):
            fm = (fm + "\n" if fm else "") + "title: " + json.dumps(h1, ensure_ascii=False)
            n_title += 1
        del lines[i]
        body = "\n".join(lines).lstrip("\n")
        n_h1 += 1
    if (fm, body) != (orig_fm, orig_body):
        p.write_text("---\n" + fm.strip("\n") + "\n---\n\n" + body, encoding="utf-8")
print(f"modified: {n_mod} files, title from H1: {n_title}, H1 removed: {n_h1}")
PY

echo "content: $(find "$Q/content" -name '*.md' | wc -l | tr -d ' ') md files"
