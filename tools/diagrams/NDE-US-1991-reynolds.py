#!/usr/bin/env python3
"""Diagram: NDE-US-1991-reynolds — the operation hour by hour, and when the verified perceptions occurred.
도해: 수술의 시간표와 검증된 지각이 일어난 시각.

Only facts from §3 and §6 of the card are drawn. This is not a record.
카드 3절·6절의 사실만 그림으로 옮긴다. 기록이 아니다.

usage:
  python3 -I tools/diagrams/NDE-US-1991-reynolds.py en > assets/NDE-US-1991-reynolds--timeline.svg
  python3 -I tools/diagrams/NDE-US-1991-reynolds.py ko > assets/NDE-US-1991-reynolds--timeline-ko.svg
check: qlmanage -t -s 1240 -o <dir> <svg>, or a headless Chrome screenshot of the file (window 1240x730)
"""
import math
import sys

sys.stdout.reconfigure(encoding="utf-8")
LANG = (sys.argv[1] if len(sys.argv) > 1 else "en").lower()
if LANG not in ("en", "ko"):
    sys.exit("lang must be en or ko")

W, H = 1240, 760
BG, INK, MUTE, LINE, ACC, ACC_BG, SOFT = "#faf8f8", "#2b2b2b", "#6b6b6b", "#284b63", "#b5541c", "#fbf1ea", "#eef2f5"
BAND2 = "#d7e3ec"

T_EN = dict(
    font="'Helvetica Neue',Helvetica,Arial,'Noto Sans',sans-serif",
    title="The Pam Reynolds case, Phoenix 1991 — the operation hour by hour, and when the verified perceptions occurred",
    sub="Times from the operative record as restated by Sabom (2007) and Augustine (2007, Fig. 1); perceptions from Sabom 1998 as quoted in JNDS 2007–2011. Facts from §3 and §6 of card NDE-US-1991-reynolds only.",
    band_anaes="General anaesthesia 7:15 → ~14:00 (thiopental, midazolam, sufentanil, vecuronium; isoflurane / nitrous oxide)",
    band_bypass="Cardiopulmonary bypass: cooling from 10:50 · rewarming 11:30 → ~12:35",
    band_silent="Brain electrically silent: cortex (SSEP) from 11:10, brainstem (BAEP) from 11:24",
    band_silent2="end of silence not timed in the quoted record (anaesthetic resumed 12:05)",
    band_stand="11:25–11:30 standstill: blood drained, aneurysm clipped (body ~15.5 °C)",
    hour=lambda h: f"{h}:00",
    ev_fs=11.5, ev_lh=15,
    events=[
        (7, 15, ["7:15 anaesthesia", "induced"], 0, False, "start"),
        (8, 42, ["~8:40–8:50  ★1 ★2 ★3", "drill sound · saw · a woman's", "voice about small arteries", "(anaesthetised, warm, eyes taped)"], 1, True, "start"),
        (10, 50, ["10:50 bypass on,", "cooling begins"], 0, False, "start"),
        (11, 27, ["11:25–11:30 standstill", "and clip; bypass back on,", "rewarming (65 min)"], 1, False, "start"),
        (12, 5, ["12:05 isoflurane", "resumed"], 0, False, "start"),
        (12, 50, ["12:50 nitrous", "oxide resumed"], 0, False, "start"),
        (13, 20, ["~12:35–14:00 closing  ★4", "'Hotel California' playing", "as she 'returned'"], 1, True, "start"),
        (14, 0, ["~14:00 operation", "ends; 14:10 to", "recovery"], 0, False, "end"),
    ],
    mid_title="What Reynolds said that was confirmed (§6) — and when",
    items=[
        ("★1 The drill: \"a natural D\"", ["A pneumatic bone drill was in use;", "the pitch itself cannot be checked"], "~8:45 · anaesthetised, normal temperature"),
        ("★2 The saw and its case", ["blades in a \"socket wrench case\": accurate", "\"a groove at the top\": does not fit the saw"], "~8:45 · same"),
        ("★3 \"Arteries too small… other side\"", ["Record: bilateral femoral cut-downs", "by the cardiac surgeon (a woman)"], "~8:40 (1 h 25 min after induction) · same"),
        ("★4 \"Hotel California\"", ["Played in the operating room", "during closing"], "after rewarming; anaesthetic resumed 12:05"),
    ],
    mid_note="All four were known to people in the room → psi (H2) and survival (H1) cannot be separated. None falls inside the silent period (11:10/11:24 → ~11:30 and after).",
    bot_title="Other ways to explain it (§7) — hence the grades C / V1",
    col_fs=12, col_lh=16,
    cols=[
        ("Hearing under anaesthesia (L·N)", ["Awareness under general anaesthesia", "occurs in ~1–2 per 1,000 (Augustine;", "Woerlee). Against it: moulded ear", "speakers, 100 dB clicks 11/s, white", "noise; the surgeon: \"inconceivable\".", "Woerlee: possible by bone conduction;", "his own verdict: data insufficient.", "→ partly ruled out"]),
        ("Told afterwards · memory (L·D)", ["First record Nov 1994, 3+ years later.", "Staff explain operations to patients;", "no source read asks what she was told.", "The saw was described with a groove", "it does not have.", "→ L partly ruled out, D not ruled out"]),
        ("Timing (the central point)", ["Operative record: silent brain from", "11:10/11:24, standstill 11:25–11:30.", "Every checked perception lies outside", "that window. The tunnel, light and", "relatives carry no time at all.", "Sabom himself: \"tantalizing clues but", "no definite answers\"."]),
        ("Grades", ["Source: investigator's interview +", "record extracts; book unopened (S7=1)", "· one experiencer · 3 years · one", "sympathetic investigator → R = C", "Verified items, but no record before", "checking and no leak-proof document", "→ V = V1 · counted in both layers (S at I0)"]),
    ],
    foot="Diagram · drawn by William (2026-10-25) · not a record · generating code tools/diagrams/NDE-US-1991-reynolds.py en",
)

T_KO = dict(
    font="'Noto Sans KR','Apple SD Gothic Neo','Malgun Gothic','Noto Sans CJK KR',sans-serif",
    title="1991년 피닉스 팸 레이놀즈 사례 — 수술의 시간표와 검증된 지각이 일어난 시각",
    sub="시각은 수술 기록을 Sabom(2007)과 Augustine(2007, 그림 1)이 옮긴 것, 지각은 JNDS 2007–2011에 인용된 Sabom 1998. 카드 NDE-US-1991-reynolds 3절·6절의 사실만.",
    band_anaes="전신마취 7:15 → ~14:00 (티오펜탈·미다졸람·수펜타닐·베쿠로늄; 이소플루란/아산화질소)",
    band_bypass="인공심폐: 냉각 10:50부터 · 재가온 11:30 → ~12:35",
    band_silent="뇌 전기 활동 소실: 대뇌(SSEP) 11:10부터, 뇌간(BAEP) 11:24부터",
    band_silent2="회복 시각은 인용된 기록에 없음(마취제 재개 12:05)",
    band_stand="11:25–11:30 순환 정지: 혈액 배출, 동맥류 결찰 (체온 ~15.5 °C)",
    hour=lambda h: f"{h}시",
    ev_fs=11.5, ev_lh=15,
    events=[
        (7, 15, ["7:15 마취 유도"], 0, False, "start"),
        (8, 42, ["~8:40–8:50  ★1 ★2 ★3", "드릴 소리 · 톱 · 동맥이", "작다는 여성의 목소리", "(마취 중, 정상 체온, 눈 테이프)"], 1, True, "start"),
        (10, 50, ["10:50 인공심폐 시작,", "냉각"], 0, False, "start"),
        (11, 27, ["11:25–11:30 순환 정지·", "결찰, 인공심폐 재개,", "재가온(65분)"], 1, False, "start"),
        (12, 5, ["12:05 이소플루란", "재개"], 0, False, "start"),
        (12, 50, ["12:50 아산화질소", "재개"], 0, False, "start"),
        (13, 20, ["~12:35–14:00 봉합  ★4", "'호텔 캘리포니아'가", "흐르는 중 '돌아옴'"], 1, True, "start"),
        (14, 0, ["~14:00 수술 끝,", "14:10 회복실"], 0, False, "end"),
    ],
    mid_title="레이놀즈가 말한 것 중 확인된 것 (6절) — 그리고 그 시각",
    items=[
        ("★1 드릴 소리: \"자연 D음\"", ["공압 골 드릴이 쓰이고 있었다;", "음높이 자체는 확인할 수 없다"], "~8:45 · 마취 중, 정상 체온"),
        ("★2 톱과 그 케이스", ["\"소켓 렌치 케이스\"에 든 날: 맞음", "\"위쪽의 홈\": 그 톱에는 없음"], "~8:45 · 같음"),
        ("★3 \"동맥이 너무 작다… 반대쪽\"", ["기록: 심장외과의(여성)가", "양쪽 대퇴 혈관을 절개"], "~8:40(유도 1시간 25분 뒤) · 같음"),
        ("★4 \"호텔 캘리포니아\"", ["봉합 중 수술실에서", "틀어 둔 노래"], "재가온 뒤; 마취제 재개 12:05"),
    ],
    mid_note="넷 다 수술실의 사람들이 알던 정보 → 초심리(H2)와 사후 의식(H1)을 가르지 못함. 뇌 활동 소실 구간(11:10/11:24 → ~11:30 이후) 안에 든 것은 없음.",
    bot_title="이렇게도 설명된다 (7절) — 그래서 등급이 C / V1",
    col_fs=12, col_lh=17,
    cols=[
        ("마취 중 청각 (L·N)", ["전신마취 중 각성은 1,000명에 1–2명", "(Augustine; Woerlee). 반대 근거:", "양쪽 귀의 몰드 스피커, 100 dB 클릭", "초당 11회, 백색 소음; 집도의는", "\"상상할 수 없다\". Woerlee: 골전도로", "가능; 그 자신의 결론은 \"자료 불충분\".", "→ 부분 배제"]),
        ("나중에 들음 · 기억 (L·D)", ["첫 기록은 3년 뒤인 1994년 11월.", "의료진은 환자에게 수술을 설명한다;", "무엇을 들었는지 물은 출처가 없다.", "톱에 없는 홈을 묘사했다.", "→ L 부분 배제, D 배제 못 함"]),
        ("시각 (핵심)", ["수술 기록: 뇌 활동 소실 11:10/11:24,", "순환 정지 11:25–11:30.", "확인된 지각은 전부 그 구간 밖에 있다.", "터널·빛·친척은 시각 표시가 없다.", "Sabom 자신: \"감질나는 단서, 그러나", "확정적 답은 없다\"."]),
        ("등급", ["출처: 조사자 면담 + 기록 발췌,", "책은 미열람(S7=1) · 체험자 1인 ·", "3년 뒤 · 공감적 조사자 1인 → R = C", "검증 항목은 있으나 확인 전 기록이", "없고 누설 차단 문서도 없음 → V = V1", "집계: S·V 두 층(S층은 I0)"]),
    ],
    foot="도해 · William 작성(2026-10-25) · 기록이 아님 · 생성 코드 tools/diagrams/NDE-US-1991-reynolds.py ko",
)

T = T_EN if LANG == "en" else T_KO

out = []
def el(s): out.append(s)
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def text(x, y, s, size=13, fill=INK, weight="normal", anchor="start"):
    el(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>')
def lines(x, y, ls, size=13, fill=INK, lh=None, anchor="start"):
    lh = lh or size + 5
    for i, s in enumerate(ls):
        text(x, y + i * lh, s, size, fill, "normal", anchor)
def box(x, y, w, h, title, body, accent=False, fs=12.5, lh=18):
    el(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="6" fill="{ACC_BG if accent else "#ffffff"}" stroke="{ACC if accent else LINE}" stroke-width="{2 if accent else 1.2}"/>')
    text(x + 12, y + 24, title, 14, ACC if accent else LINE, "bold")
    lines(x + 12, y + 46, body, fs, INK, lh)
def star(cx, cy, r=8):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append(f"{cx + rr * math.cos(ang):.1f},{cy + rr * math.sin(ang):.1f}")
    el(f'<polygon points="{" ".join(pts)}" fill="{ACC}" stroke="#ffffff" stroke-width="1"/>')

# time → x  (7:00 → 14:30)
X0, X1 = 70, W - 40
def tx(h, m=0):
    return X0 + ((h * 60 + m) - 420) * (X1 - X0) / 450

el(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{T["font"]}">')
el(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# Title
text(20, 34, T["title"], 20, INK, "bold")
text(20, 56, T["sub"], 11.5, MUTE)

# Bands.  side: "in" = label inside at the left edge; "left" = label to the left of the band; "right" = to the right.
BH = 20
def band(y, x1, x2, fill, stroke, label, side="in", dashed_to=None, dashed_label=None):
    el(f'<rect x="{x1:.1f}" y="{y}" width="{x2 - x1:.1f}" height="{BH}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
    if dashed_to is not None:
        el(f'<rect x="{x2:.1f}" y="{y}" width="{dashed_to - x2:.1f}" height="{BH}" rx="3" fill="none" stroke="{stroke}" stroke-width="1" stroke-dasharray="4,3"/>')
        if dashed_label:
            text(dashed_to + 8, y + 14, dashed_label, 11, MUTE)
    if side == "in":
        text(x1 + 8, y + 14, label, 11.5, INK)
    elif side == "left":
        text(x1 - 8, y + 14, label, 11.5, INK, "normal", "end")
    else:
        text((dashed_to if dashed_to is not None else x2) + 8, y + 14, label, 11.5, INK)

band(84, tx(7, 15), tx(14, 0), SOFT, LINE, T["band_anaes"], side="in")
band(110, tx(10, 50), tx(12, 35), BAND2, LINE, T["band_bypass"], side="left")
band(136, tx(11, 10), tx(11, 30), ACC_BG, ACC, T["band_silent"], side="left", dashed_to=tx(12, 5), dashed_label=T["band_silent2"])
el(f'<rect x="{tx(11, 25):.1f}" y="162" width="{max(tx(11, 30) - tx(11, 25), 6):.1f}" height="{BH}" rx="2" fill="{ACC}"/>')
text(tx(11, 30) + 8, 176, T["band_stand"], 11.5, ACC, "bold")

# Axis
AY = 215
el(f'<line x1="{X0}" y1="{AY}" x2="{X1}" y2="{AY}" stroke="{INK}" stroke-width="1.5"/>')
for h in range(7, 15):
    x = tx(h)
    el(f'<line x1="{x:.1f}" y1="{AY - 5}" x2="{x:.1f}" y2="{AY + 5}" stroke="{INK}" stroke-width="1"/>')
    text(x, AY - 10, T["hour"](h), 11, MUTE, "normal", "middle")
    el(f'<line x1="{x:.1f}" y1="80" x2="{x:.1f}" y2="{AY - 22}" stroke="{LINE}" stroke-width="0.4" stroke-dasharray="2,4"/>')

# Events
for h, m, ls, level, is_star, anchor in T["events"]:
    x = tx(h, m)
    ty = AY + (12 if level == 0 else 68)
    el(f'<line x1="{x:.1f}" y1="{AY}" x2="{x:.1f}" y2="{ty}" stroke="{ACC if is_star else MUTE}" stroke-width="{1.5 if is_star else 1}"/>')
    if is_star:
        star(x, AY)
    else:
        el(f'<circle cx="{x:.1f}" cy="{AY}" r="3.5" fill="{INK}"/>')
    lx = x - 4 if anchor == "start" else x + 4
    lines(lx, ty + 15, ls, T["ev_fs"], ACC if is_star else INK, T["ev_lh"], anchor)

# Middle: confirmed items (§6)
y2 = 378
text(20, y2, T["mid_title"], 14, LINE, "bold")
BOX2 = 100
el(f'<rect x="20" y="{y2 + 12}" width="{W - 40}" height="{BOX2}" rx="6" fill="{SOFT}" stroke="{LINE}" stroke-width="0.8"/>')
cw = (W - 40) / 4
for i, (a, b, c) in enumerate(T["items"]):
    x = 20 + i * cw + 12
    text(x, y2 + 36, a, 11.5, ACC, "bold")
    lines(x, y2 + 55, b, 11, INK, 14)
    text(x, y2 + 93, c, 10.5, MUTE)
text(W - 30, y2 + 12 + BOX2 + 17, T["mid_note"], 11, MUTE, "normal", "end")

# Bottom: other explanations (§7)
y3 = y2 + 12 + BOX2 + 42
text(20, y3, T["bot_title"], 14, LINE, "bold")
cw3 = (W - 40 - 3 * 16) / 4
for i, (t, b) in enumerate(T["cols"]):
    x = 20 + i * (cw3 + 16)
    box(x, y3 + 12, cw3, 184, t, b, accent=(i == 3), fs=T["col_fs"], lh=T["col_lh"])

# Tag
text(20, H - 12, T["foot"], 11, MUTE)
el("</svg>")
print("\n".join(out))
