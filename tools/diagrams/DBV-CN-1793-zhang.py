#!/usr/bin/env python3
"""Diagram: DBV-CN-1793-zhang — the record's path, and the two transmission routes that stay open.
도해: 기록이 남은 길, 그리고 열려 있는 두 전파 경로.

Only facts from §3, §4 and §11 of the card are drawn. This is not a record.
카드 3·4·11절의 사실만 그림으로 옮긴다. 기록이 아니다.

usage:
  python3 -I tools/diagrams/DBV-CN-1793-zhang.py en > assets/DBV-CN-1793-zhang--routes.svg
  python3 -I tools/diagrams/DBV-CN-1793-zhang.py ko > assets/DBV-CN-1793-zhang--routes-ko.svg
check: headless Chrome screenshot of the file (window 1240x600)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
LANG = (sys.argv[1] if len(sys.argv) > 1 else "en").lower()
if LANG not in ("en", "ko"):
    sys.exit("lang must be en or ko")

W, H = 1240, 600
BG, INK, MUTE, LINE, ACC, ACC_BG, SOFT, SOFT2 = "#faf8f8", "#2b2b2b", "#6b6b6b", "#284b63", "#b5541c", "#fbf1ea", "#eef2f5", "#e4ebe4"

T_EN = dict(
    font="'Helvetica Neue',Helvetica,Arial,'Noto Sans',sans-serif",
    title="Lady Zhang, China, before 1793 — how the record reached paper, and the two routes of borrowing that stay open",
    sub="Facts from §3, §4 and §11 of card DBV-CN-1793-zhang (Ji Yun, Guwang tingzhi, preface dated 1793; Siku catalogue ch. 125; Taishō no. 412). This is a diagram by William, not a record.",
    rows=[
        ("RECORD", ACC_BG, [
            ("Before 1793 · undated", ["At the crisis of her illness", "Lady Zhang says she sees", "'those who went before', and", "that her guides are her", "husband's kin"]),
            ("At the bedside", ["She calls her daughters and", "daughters-in-law to the bed.", "The recorder's third aunt,", "née Zhang, hears it in person"]),
            ("Told to Ji Yun", ["The aunt tells her nephew", "Ji Yun (1724–1805), whose", "grandmother was the dying", "woman's elder sister. Date unknown"]),
            ("1793 · in print 1800", ["Ji Yun writes it into Guwang", "tingzhi, ch. 3 (preface: 25th day,", "7th month, guichou year of", "Qianlong). Collected works 1800"]),
        ]),
        ("ROUTE ②", SOFT, [
            ("1603", ["Matteo Ricci, Tianzhu shiyi:", "the soul does not perish;", "heaven and hell after death", "(Siku catalogue note)"]),
            ("1608", ["Ricci, Jiren shipian: two of", "its ten chapters are on", "keeping the hour of death", "in mind (Siku catalogue note)"]),
            ("1772–1782", ["The Siku catalogue reviews", "these Christian books. Ji Yun:", "'after fifty I led the editing", "of the palace books' (preface)"]),
            ("Not checked", ["Whether any Christian text in", "Chinese recorded deathbed", "visitors, and whether any", "reached this household → unknown"]),
        ]),
        ("ROUTE ③", SOFT2, [
            ("Attributed 7th century", ["Sutra of the Fundamental Vows", "of Ksitigarbha (Taishō 412),", "said to be translated by", "Śikṣānanda of Khotan"]),
            ("Its deathbed passage", ["Even good people, at death,", "see ghosts 'changed into", "parents and other kin' who", "come to lead them away"]),
            ("Origin disputed", ["No Sanskrit original found;", "some scholars think it was", "composed in China (lead only:", "Buswell 1990, not opened)"]),
            ("In the record itself", ["'I have heard that the dying", "see those who went before' —", "the idea was already a saying", "in her household → unknown"]),
        ]),
    ],
    foot="Grades: S1 1 (a collector who heard the witness in person) · S2 1 (one named witness, present) · S3 0 (decades; undated) · S4 0 · S6 1 (collector with a family interest, no checking) · S7 2 (Qing woodblock edition, scan opened) → 3/10 → R C · no verified information (V—) · independence I1 (routes ② and ③ unknown; ① ④ ⑤ ruled out)",
)

T_KO = dict(
    font="'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic','Helvetica Neue',Arial,sans-serif",
    title="장 부인, 중국, 1793년 이전 — 기록이 종이에 이르는 길, 그리고 열려 있는 두 차용 경로",
    sub="카드 DBV-CN-1793-zhang 3·4·11절의 사실(지윤 『고망청지』 1793년 서문, 『사고전서총목』 125권, 대정장 412번). 윌리엄이 그린 도해이며 기록이 아니다.",
    rows=[
        ("기록", ACC_BG, [
            ("1793년 이전 · 날짜 없음", ["병이 위중해지자 장 부인이", "'먼저 간 이들이 보인다'고", "말하고, 이끌러 온 이들이", "모두 시댁 사람이라고 함"]),
            ("임종 자리", ["딸과 며느리들을 침상 앞에", "불러 모음. 지윤의 셋째 숙모", "(장씨)가 직접 들음"]),
            ("지윤에게 전해짐", ["숙모가 조카 지윤(1724–1805)", "에게 이야기함. 지윤의 할머니가", "장 부인의 언니. 들은 날짜는", "알 수 없음"]),
            ("1793년 · 1800년 간행", ["지윤이 『고망청지』 3권에 적음", "(서문: 건륭 계축년 7월 25일).", "1800년 전집으로 간행"]),
        ]),
        ("경로 ②", SOFT, [
            ("1603년", ["마테오 리치 『천주실의』:", "영혼은 죽지 않고 사후에", "천당·지옥이 있다", "(사고전서총목 해제)"]),
            ("1608년", ["리치 『기인십편』: 열 편 중", "두 편이 '죽음의 때를 늘", "생각하라'(사고전서총목 해제)"]),
            ("1772–1782년", ["『사고전서총목』이 이 기독교", "서적들을 해제함. 지윤 서문:", "'쉰 이후 비서 편찬을", "맡았다'"]),
            ("확인 못 함", ["한문 기독교 문헌에 임종", "방문자 기록이 있었는지,", "이 집안에 닿았는지", "→ 알 수 없음"]),
        ]),
        ("경로 ③", SOFT2, [
            ("7세기로 전해짐", ["『지장보살본원경』(대정장 412),", "우전국 승려 실차난타가", "번역했다고 전함"]),
            ("그 경의 임종 대목", ["착한 사람도 죽을 때 귀신들이", "'부모와 친척으로 변해'", "와서 이끌어 간다"]),
            ("기원 논쟁", ["산스크리트 원본 없음.", "중국 찬술설 있음(단서만:", "버스웰 1990, 미열람)"]),
            ("기록 안에서", ["'죽어 가는 사람은 먼저 간", "이들을 본다더니' — 이미", "집안에 돌던 말", "→ 알 수 없음"]),
        ]),
    ],
    foot="등급: S1 1(증인에게 직접 들은 수집가) · S2 1(이름 있는 증인 한 명, 현장에 있었음) · S3 0(수십 년, 날짜 없음) · S4 0 · S6 1(집안 사람인 수집가, 검증 없음) · S7 2(청대 목판본 스캔 열람) → 3/10 → R C · 검증 정보 없음(V—) · 독립성 I1(경로 ②·③ 알 수 없음, ①④⑤ 배제)",
)

T = T_EN if LANG == "en" else T_KO


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(s, n):
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


o = []
o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{T["font"]}">')
o.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
o.append(f'<text x="40" y="38" font-size="19" font-weight="700" fill="{INK}">{esc(T["title"])}</text>')
y = 60
for ln in wrap(T["sub"], 150 if LANG == "en" else 95):
    o.append(f'<text x="40" y="{y}" font-size="11.5" fill="{MUTE}">{esc(ln)}</text>')
    y += 15

LEFT, LABEL_W, GAP = 40, 86, 14
BOX_W = (W - LEFT - 40 - LABEL_W - 3 * GAP) // 4
ROW_H, ROW_GAP, top = 118, 16, 102
for ri, (label, color, boxes) in enumerate(T["rows"]):
    ry = top + ri * (ROW_H + ROW_GAP)
    o.append(f'<rect x="{LEFT}" y="{ry}" width="{LABEL_W - 10}" height="{ROW_H}" rx="4" fill="{LINE}"/>')
    o.append(f'<text x="{LEFT + (LABEL_W - 10) / 2}" y="{ry + ROW_H / 2 + 5}" font-size="12.5" font-weight="700" fill="#ffffff" text-anchor="middle">{esc(label)}</text>')
    for bi, (date, lines) in enumerate(boxes):
        bx = LEFT + LABEL_W + bi * (BOX_W + GAP)
        o.append(f'<rect x="{bx}" y="{ry}" width="{BOX_W}" height="{ROW_H}" rx="6" fill="{color}" stroke="{LINE}" stroke-width="1"/>')
        o.append(f'<text x="{bx + 10}" y="{ry + 20}" font-size="12.5" font-weight="700" fill="{ACC}">{esc(date)}</text>')
        ty = ry + 38
        for ln in lines:
            o.append(f'<text x="{bx + 10}" y="{ty}" font-size="12" fill="{INK}">{esc(ln)}</text>')
            ty += 16
        if bi < 3:
            ax = bx + BOX_W
            o.append(f'<path d="M{ax + 2},{ry + ROW_H / 2} L{ax + GAP - 3},{ry + ROW_H / 2}" stroke="{LINE}" stroke-width="1.5"/>')
            o.append(f'<path d="M{ax + GAP - 7},{ry + ROW_H / 2 - 4} L{ax + GAP - 2},{ry + ROW_H / 2} L{ax + GAP - 7},{ry + ROW_H / 2 + 4}" fill="none" stroke="{LINE}" stroke-width="1.5"/>')

fy = top + 3 * (ROW_H + ROW_GAP) + 10
o.append(f'<rect x="{LEFT}" y="{fy}" width="{W - 80}" height="{H - fy - 20}" rx="6" fill="#ffffff" stroke="{ACC}" stroke-width="1"/>')
ty = fy + 20
for ln in wrap(T["foot"], 165 if LANG == "en" else 100):
    o.append(f'<text x="{LEFT + 12}" y="{ty}" font-size="12" fill="{INK}">{esc(ln)}</text>')
    ty += 16
o.append("</svg>")
print("\n".join(o))
