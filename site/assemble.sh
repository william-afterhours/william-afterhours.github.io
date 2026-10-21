#!/usr/bin/env bash
# 연구 저장소의 마크다운을 Quartz 소스 트리에 올려놓는다.
# usage: site/assemble.sh <repo_dir> <quartz_src_dir>
# 로컬 확인: site/assemble.sh . ../quartz-src && (cd ../quartz-src && npm ci && npx quartz build)
set -euo pipefail
REPO=$(cd "$1" && pwd)
Q=$(cd "$2" && pwd)

cp "$REPO/site/quartz.config.ts" "$REPO/site/quartz.layout.ts" "$Q/"

rm -rf "$Q/content"
mkdir -p "$Q/content"
for d in cases entities docs sources; do
  [ -d "$REPO/$d" ] && cp -R "$REPO/$d" "$Q/content/$d"
done
{ printf -- '---\ntitle: "William · 초자연 현상 기록"\n---\n'; cat "$REPO/README.md"; } > "$Q/content/index.md"

# Quartz는 날짜를 `modified:`에서만 읽는다. 카드·엔티티의 `updated:`를 `modified:`로 복사해 넣는다.
python3 - "$Q/content" <<'PY'
import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
n = 0
for p in root.rglob("*.md"):
    t = p.read_text(encoding="utf-8")
    if not t.startswith("---\n"):
        continue
    end = t.find("\n---\n", 4)
    if end < 0:
        continue
    fm = t[4:end]
    if re.search(r"^modified:", fm, re.M):
        continue
    m = re.search(r"^updated:\s*(\S+)", fm, re.M)
    if not m:
        continue
    p.write_text(t[:end] + f"\nmodified: {m.group(1)}" + t[end:], encoding="utf-8")
    n += 1
print(f"modified: injected into {n} files")
PY

echo "content: $(find "$Q/content" -name '*.md' | wc -l | tr -d ' ') md files"
