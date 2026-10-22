#!/usr/bin/env python3
"""도해: DBV-GB-1924-doris — 연표, 누가 어느 발화를 들었나, 기록의 사슬.

카드 3절·4절·6절의 사실만 그림으로 옮긴다. 기록이 아니다.
usage: python3 -I tools/diagrams/DBV-GB-1924-doris.py > assets/DBV-GB-1924-doris--timeline.svg
확인: qlmanage는 정사각으로 자르므로, 사본에서 height=1240·viewBox="0 -160 1240 1240"으로 세로 중앙에 놓고
      qlmanage -t -s 1240 → sips -c 920 1240(중앙 크롭)으로 미리보기를 만든다.
"""
W, H = 1240, 920
FONT = "'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic','Noto Sans CJK KR',sans-serif"
BG, INK, MUTE, LINE, ACC, ACC_BG, SOFT = "#faf8f8", "#2b2b2b", "#6b6b6b", "#284b63", "#b5541c", "#fbf1ea", "#eef2f5"

out = []
def el(s): out.append(s)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start"):
    el(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')
def lines(x, y, ls, size=12.5, fill=INK, lh=None):
    lh = lh or size + 5
    for i, s in enumerate(ls):
        text(x, y + i * lh, s, size, fill)
def rect(x, y, w, h, fill="#ffffff", stroke=LINE, sw=1.2, rx=6):
    el(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

el(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
el(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# 제목
text(20, 34, "1924년 런던 '도리스' 임종 환시 — 연표, 누가 어느 말을 들었나, 기록의 사슬", 20, INK, "bold")
text(20, 56, "카드 DBV-GB-1924-doris 3·4·6절의 사실만 옮김. 날짜는 Barrett 1926에 전재된 진술서와 GRO 색인(FreeBMD)에서. 출처 번호는 카드에 있다.", 12, MUTE)

# ── 1. 연표 ─────────────────────────────────────────────
y0 = 80
text(20, y0, "1. 연표", 14, LINE, "bold")
ty = y0 + 120  # 위쪽 본문(4줄)과 제목·절 제목이 겹치지 않도록 선을 내린다
el(f'<line x1="40" y1="{ty}" x2="{W - 40}" y2="{ty}" stroke="{LINE}" stroke-width="2"/>')
events = [
    (0.00, "1923년 4~6월", ["혼인(Shoreditch)", "GRO 색인 Q2 1923"], False),
    (0.16, "1923-12-25", ["언니 비다(34) 사망", "West Ham · 색인 Q4 1923", "도리스는 이미 중병"], False),
    (0.30, "12월 말~1월", ["가족의 숨김 조치:", "상복 안 입고 방문,", "편지는 남편이 먼저 검열"], False),
    (0.47, "1924-01-12", ["출산(조산) → 환시 → 사망", "Mothers' Hospital, Clapton", "색인: 사망 Q1 1924 Hackney(22세)", "출생 Q1 1924 Hackney, 모성 Clark"], True),
    (0.63, "1924-02", ["교구지(All Saints,", "Haggerston) 2월호에", "목사가 언급 — 미확인"], False),
    (0.78, "1924~1925", ["서명 진술서 3통:", "Lady Barrett 메모(직후, 날짜 없음)", "수간호사 Castle · 어머니 Clark", "Phillips 경유 수집"], False),
    (0.92, "1925 · 1926", ["1925-05-21 Barrett 사망", "1926 『Death-bed Visions』", "pp. 10–14 (Wellcome 스캔)"], False),
]
x_left, x_right = 60, W - 60
for i, (f, when, body, key) in enumerate(events):
    x = x_left + f * (x_right - x_left)
    el(f'<circle cx="{x}" cy="{ty}" r="{7 if key else 5}" fill="{ACC if key else LINE}"/>')
    up = i % 2 == 0
    if up:
        text(x, ty - 14, when, 12.5, ACC if key else LINE, "bold", "middle")
    else:
        text(x, ty + 24, when, 12.5, ACC if key else LINE, "bold", "middle")
    bx, by_ = max(20, x - 86), (ty + 34 if not up else ty - 112)
    # 본문은 아래/위 교대
    if up:
        lines(bx, by_ + 14, body, 11.5, INK, 15)
    else:
        lines(bx, by_ + 14 + 10, body, 11.5, INK, 15)
text(x_right, ty + 130, "2026-10-22 William이 GRO 색인(FreeBMD)으로 혼인·사망 2건·출생을 대조 — 책의 순서와 일치", 11.5, MUTE, "normal", "end")

# ── 2. 누가 어느 말을 들었나 ────────────────────────────
y1 = ty + 160
text(20, y1, "2. 1924-01-12 병동에서 — 누가 어느 말을 들었나 (진술서 3통의 교집합)", 14, LINE, "bold")
utts = [
    ("①", "\"It's getting so dark … darker and darker\""),
    ("②", "\"Lovely brightness — wonderful beings\""),
    ("③", "\"Why, it's Father! Oh, he's so glad I'm coming\""),
    ("④", "\"Do you think I ought to stay for baby's sake?\""),
    ("⑤", "\"Oh, why there's Vida\" (수간호사 쪽을 보며)"),
    ("⑥", "\"He has Vida with him\" (어머니에게, 어리둥절한 표정)"),
    ("⑦", "\"the man who married us\"를 불러 달라"),
]
wits = ["Lady Barrett", "Dr. Phillips", "수간호사 Castle", "어머니 Clark", "남편 W."]
# 진술서 근거: ● 본인 진술서에 있음 / ○ 같은 자리에 있었다고 기록됨(본인 진술 없음) / ◐ 불명 / · 없음
grid = {
    "①": "●●○··", "②": "●●○··", "③": "●●○◐·", "④": "●●○◐●",
    "⑤": "··●●●", "⑥": "··○●●", "⑦": "··●●●",
}
gx, gy = 20, y1 + 14
colw, roww, lab_w = 118, 26, 470
rect(gx, gy, lab_w + colw * 5, roww * 8 + 6, "#ffffff", LINE, 1)
for j, w in enumerate(wits):
    text(gx + lab_w + j * colw + colw / 2, gy + 18, w, 12, LINE, "bold", "middle")
for i, (n, u) in enumerate(utts):
    yy = gy + 24 + (i + 1) * roww - 8
    key = n in ("⑤", "⑥")
    if key:
        el(f'<rect x="{gx + 2}" y="{yy - 17}" width="{lab_w + colw * 5 - 4}" height="{roww}" fill="{ACC_BG}"/>')
    text(gx + 10, yy, f"{n} {u}", 12, ACC if key else INK, "bold" if key else "normal")
    for j, ch in enumerate(grid[n]):
        text(gx + lab_w + j * colw + colw / 2, yy, ch, 13, ACC if (key and ch == "●") else INK, "normal", "middle")
ly = gy + roww * 8 + 24
text(gx, ly, "● 본인 서명 진술서에 그 말이 있음   ○ 그 자리에 있었다고 기록됨(본인 진술에는 없음)   ◐ 있었는지 불명   · 없었음", 11.5, MUTE)
text(gx, ly + 18, "Lady Barrett은 ④ 뒤에 병동을 떠났고 수간호사가 자리를 이었다. ⑤·⑥이 검증 정보(V): 비다의 죽음은 환자에게 숨겨져 있었다.", 11.5, MUTE)

# ── 3. 비다의 죽음을 그 자리에서 알고 있던 사람 ────────
y2 = ly + 44
text(20, y2, "3. ⑤·⑥ 순간, 비다가 죽었다는 것을 알고 있던 사람", 14, LINE, "bold")
rect(20, y2 + 12, W - 40, 96, SOFT, LINE, 0.8)
cols = [
    ("어머니 Clark", "알았음 — 본인이 숨김을 주도"),
    ("남편 W.", "알았음 — 편지를 먼저 검열"),
    ("수간호사 Castle", "'자매의 죽음'은 알았음(숨기자고 조언), 이름 '비다'는 몰랐음"),
    ("Lady Barrett · Phillips", "몰랐음(Barrett) — 단 ⑤·⑥ 때는 자리에 없었음"),
]
cw = (W - 40) / 4
for i, (a, b) in enumerate(cols):
    x = 20 + i * cw + 12
    text(x, y2 + 40, a, 12.5, INK, "bold")
    lines(x, y2 + 60, [b[:30], b[30:]] if len(b) > 30 else [b], 11.5, MUTE, 15)
text(W - 30, y2 + 100, "→ 곁에 있던 사람이 알던 정보: 초심리(H2)와 사후 의식(H1)을 가르지 못하고, 누설(L)도 선기록으로 차단되지 않음", 11.5, MUTE, "normal", "end")

# ── 4. 기록의 사슬 ──────────────────────────────────────
y3 = y2 + 130
text(20, y3, "4. 기록의 사슬 — 이 카드가 읽은 것", 14, LINE, "bold")
chain = [
    ("메모 (1924-01, 날짜 없음)", ["Lady Barrett, \"written", "down soon afterwards\"", "원본 미열람"]),
    ("진술서 3통 (1924~25)", ["Castle 진술 · Clark 편지", "Phillips 서면 동의", "원본 미열람(SPR 소장 여부 미확인)"]),
    ("책 (1926)", ["Barrett 『Death-bed Visions』", "pp. 10–14 전재", "Wellcome b29813992 열람 ✔"]),
    ("GRO 색인 (1923~24)", ["혼인·사망 2건·출생", "FreeBMD로 대조 ✔", "이름·나이·지역·분기만"]),
    ("등급", ["R = B (6/10)", "V = V1 · 집계: V", "S층은 I0(독립성 ②)로 보류"]),
]
bw, gap = 222, 18
for i, (t, b) in enumerate(chain):
    x = 20 + i * (bw + gap)
    acc = i == 4
    rect(x, y3 + 12, bw, 98, ACC_BG if acc else "#ffffff", ACC if acc else LINE, 2 if acc else 1.2)
    text(x + 12, y3 + 34, t, 13, ACC if acc else LINE, "bold")
    lines(x + 12, y3 + 54, b, 11.5, INK, 16)
    if i < 4:
        el(f'<path d="M{x + bw + 3},{y3 + 61} h{gap - 8}" stroke="{MUTE}" stroke-width="1.5"/>')

text(20, H - 14, "도해 · William 작성(2026-10-22) · 기록이 아님 · 생성 코드 tools/diagrams/DBV-GB-1924-doris.py", 11, MUTE)
el("</svg>")
print("\n".join(out))
