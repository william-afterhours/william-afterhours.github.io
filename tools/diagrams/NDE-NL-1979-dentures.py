#!/usr/bin/env python3
"""도해: NDE-NL-1979-dentures 사건 순서와 검증 정보가 놓인 자리.

카드 3절·6절·7절의 사실만 그림으로 옮긴다. 기록이 아니다.
usage: python3 -I tools/diagrams/NDE-NL-1979-dentures.py > assets/NDE-NL-1979-dentures--sequence.svg
확인: qlmanage -t -s 1240 -o <dir> assets/NDE-NL-1979-dentures--sequence.svg
"""
W, H = 1240, 740
FONT = "'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic','Noto Sans CJK KR',sans-serif"
BG, INK, MUTE, LINE, ACC, ACC_BG, SOFT = "#faf8f8", "#2b2b2b", "#6b6b6b", "#284b63", "#b5541c", "#fbf1ea", "#eef2f5"

out = []
def el(s): out.append(s)
def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start"):
    el(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{s}</text>')
def lines(x, y, ls, size=13, fill=INK, lh=None):
    lh = lh or size + 5
    for i, s in enumerate(ls):
        text(x, y + i * lh, s, size, fill)
def box(x, y, w, h, title, body, accent=False):
    el(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{ACC_BG if accent else "#ffffff"}" stroke="{ACC if accent else LINE}" stroke-width="{2 if accent else 1.2}"/>')
    text(x + 12, y + 24, title, 14, ACC if accent else LINE, "bold")
    lines(x + 12, y + 46, body, 12.5, INK, 18)
def arrow(x1, y, x2):
    el(f'<line x1="{x1}" y1="{y}" x2="{x2 - 6}" y2="{y}" stroke="{MUTE}" stroke-width="1.5" marker-end="url(#ah)"/>')

el(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">')
el(f'<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{MUTE}"/></marker></defs>')
el(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# 제목
text(20, 34, "1979년 네덜란드 틀니 사례 — 사건 순서와 검증 정보가 놓인 자리", 20, INK, "bold")
text(20, 56, "카드 NDE-NL-1979-dentures 3절·6절·7절의 사실만 옮김. 세부는 판본에 따라 다르며 카드에 출처 번호가 있다.", 12, MUTE)

# 위: 사건 순서 6칸
bw, gap, by, bh = 185, 18, 80, 172
xs = [20 + i * (bw + gap) for i in range(6)]
steps = [
    ("1 발견", ["1979년 말 추운 밤.", "오이(Ooij) 초원에", "누워 있던 40대 남성 B.", "무맥박·무호흡·", "심실세동. 얼마나", "누워 있었는지 불명."]),
    ("2 이송", ["구급대 소생 시작,", "30분 안에 네이메헌", "카니시우스 병원", "CCU 소생실로.", "푸른 반점·얼음처럼", "찬 몸·동공 무반응."]),
    ("3 틀니", ["삽관하려다 틀니 발견.", "간호사 T.G.가 빼서", "크래시 카트의 이미", "빼놓은 나무 미닫이", "판 위에 올림.", "(순환 상태는 판본 차이)"]),
    ("4 소생", ["1시간 이상. 수동·기계", "심장마사지, 제세동", "5회. 15분쯤 뒤 팀은", "중단을 눈짓으로 논의.", "눈은 감겨 있었음.", "→ ICU 수일."]),
    ("5 재회", ["1주 이상 뒤 재활 병동.", "B.가 T.G.를 보자마자", "“당신이 내 틀니를", "꺼내 그 카트 판 위에", "놓았다”. 소생실 배치·", "팀원 외모도 묘사."]),
    ("6 기록", ["1991 간호지 Cordiaal", "(전언, 짧게)", "1994 Merkawah 면담", "12쪽 (최초 상세 기록)", "2001 Lancet 요약", "2008 재면담: 1994와 일치"]),
]
for i, (t, b) in enumerate(steps):
    box(xs[i], by, bw, bh, t, b, accent=(i == 2))
    if i < 5:
        arrow(xs[i] + bw, by + bh / 2, xs[i + 1])
# 핵심 표시
el(f'<path d="M{xs[2] + bw / 2},{by + bh} v22" stroke="{ACC}" stroke-width="1.5"/>')
el(f'<rect x="{xs[2] - 30}" y="{by + bh + 22}" width="{bw + 60}" height="46" rx="6" fill="{ACC}"/>')
text(xs[2] + bw / 2, by + bh + 41, "검증 정보가 만들어진 순간", 13, "#ffffff", "bold", "middle")
text(xs[2] + bw / 2, by + bh + 59, "B.는 의식 없음 · 눈 감김 · 동공 무반응으로 기록됨", 11.5, "#ffffff", "normal", "middle")

# 가운데: 검증 정보 4가지 (6절)
y2 = by + bh + 92
text(20, y2, "B.가 말한 것 중 확인된 정보 (6절)", 14, LINE, "bold")
el(f'<rect x="20" y="{y2 + 12}" width="{W - 40}" height="78" rx="6" fill="{SOFT}" stroke="{LINE}" stroke-width="0.8"/>')
items = [
    ("틀니를 꺼낸 사람이 T.G.", "T.G.는 1주 이상 B.를 못 봄"),
    ("틀니를 올린 자리: 빼놓은 나무 판, 위에 병 잔뜩", "카트는 그 방 전용·병원 유일"),
    ("소생실 배치(세면대·거울·카트·캐비닛)", "B.는 이 병원 첫 입원"),
    ("팀원 외모·중단 논의·T.G.의 마사지", "일부는 청각으로도 설명 가능"),
]
cw = (W - 40) / 4
for i, (a, b) in enumerate(items):
    x = 20 + i * cw + 12
    text(x, y2 + 40, a, 12, INK, "bold")
    text(x, y2 + 60, b, 11.5, MUTE)
text(W - 30, y2 + 82, "전부 당시 소생팀이 알던 정보 → 초심리(H2)와 사후 의식(H1)을 가르지 못함", 11, MUTE, "normal", "end")

# 아래: 이렇게도 설명된다 (7절)
y3 = y2 + 118
text(20, y3, "이렇게도 설명된다 (7절) — 그래서 등급이 C / V1", 14, LINE, "bold")
cols = [
    ("청각 재구성 (N)", ["마사지 중 관류로 의식이 조금 있어", "소리를 듣고 장면을 재구성했다", "(Woerlee 2004·2010).", "↔ 판의 위치·팀원 외모는 소리로", "안 되고, 카트는 그 방 유일", "(Smit·Rivas 2010). → 부분 배제"]),
    ("정보 누설 (L)", ["ICU에서 1주 넘게 지내는 동안", "직원이 틀니 이야기를 했을 수 있다.", "어느 조사자도 이 경로를 묻지", "않았다. → 배제 못 함"]),
    ("기억 변화·단일 증인 (D·X)", ["최초 상세 기록은 사건 12년 뒤.", "증인은 T.G. 한 사람. 판본마다", "세부가 다르다(상악/상·하 틀니,", "순환 유무). 1994↔2008은 일치.", "→ 배제 못 함"]),
    ("등급", ["출처 2차(면담 기록) · 단일 증인 ·", "회고 12년 · 조사 주체 1곳", "→ R = C", "검증 정보 있음, 확인 전 기록 없음", "→ V = V1", "집계: V층만(countable: V)"]),
]
cw3 = (W - 40 - 3 * 16) / 4
for i, (t, b) in enumerate(cols):
    x = 20 + i * (cw3 + 16)
    box(x, y3 + 12, cw3, 150, t, b, accent=(i == 3))

# 꼬리표
text(20, H - 16, "도해 · William 작성(2026-10-22) · 기록이 아님 · 생성 코드 tools/diagrams/NDE-NL-1979-dentures.py", 11, MUTE)
el("</svg>")
print("\n".join(out))
