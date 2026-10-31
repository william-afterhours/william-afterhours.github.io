#!/usr/bin/env python3
"""Diagram: DBV-GB-1883-browning — the event, the letter and how the letter travelled into print.
도해: 사건, 편지, 그리고 그 편지가 인쇄물에 이르기까지의 경로.

Only facts from §3 and §4 of the card are drawn. This is not a record.
카드 3절·4절의 사실만 그림으로 옮긴다. 기록이 아니다.

usage:
  python3 -I tools/diagrams/DBV-GB-1883-browning.py en > assets/DBV-GB-1883-browning--chain.svg
  python3 -I tools/diagrams/DBV-GB-1883-browning.py ko > assets/DBV-GB-1883-browning--chain-ko.svg
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
    title="Louisa Browning, London 1883 — the deathbed, the letter written eight days later, and the letter's road into print",
    sub="Facts from §3 and §4 of card DBV-GB-1883-browning (the letter as printed in JASPR, July 1909, pp. 422–423; civil death index). This is a diagram by William, not a record.",
    rows=[
        ("THE EVENT", SOFT, [
            ("July 1867", ["Amelia Jane Ericsson,", "wife of John Ericsson,", "dies in Marylebone, aged 50"]),
            ("9 July 1868", ["Her niece Ellen Browning,", "of Auckland, marries", "General Sir Trevor Chute"]),
            ("Fri 26 Oct 1883", ["Amelia's sister Louisa", "Browning, 78, diabetic, falls", "in her bedroom; found by", "her servant; never rallies"]),
            ("Sun 28 Oct 1883, early", ["Unconscious, then: 'Oh Amelia!", "Amelia!' — reaches out her hand;", "dies at once. Heard by 'those", "watching by her' (unnamed)"]),
        ]),
        ("THE RECORD", ACC_BG, [
            ("5 Nov 1883 · 8 days later", ["Lady Chute writes from Egmont,", "Bracknell, to Capt. Ericsson in", "New York: a family letter, not", "written for publication"]),
            ("8 Mar 1889", ["Ericsson dies in New York.", "His papers go to his", "biographer, W. C. Church"]),
            ("1890 →", ["Church writes the Life of", "Ericsson (1890); finds the", "letter among the papers", "and happens to keep it"]),
            ("Civil index (checked 2026)", ["Deaths Oct–Dec 1883,", "Kensington: Browning, Louisa,", "age 78. Deaths Jul–Sep 1867,", "Marylebone: Ericsson, Amelia Jane, 50"]),
        ]),
        ("INTO PRINT", SOFT2, [
            ("17 Aug 1908", ["Church sends the original", "letter to the editor of", "The Open Court, Chicago"]),
            ("1908–09", ["The editor passes it to", "D. P. Abbott, who passes it", "to J. H. Hyslop (ASPR)"]),
            ("July 1909", ["Hyslop prints the letter in", "JASPR III(7) pp. 422–423,", "omitting 'personal' passages;", "describes the yellowed paper"]),
            ("1926", ["Barrett reprints it, abridged,", "in Death-bed Visions", "pp. 44–45 (chapter III)"]),
        ]),
    ],
    foot="Grades: S1 2 (contemporary letter) · S2 0 (the writer was not present; the watchers are unnamed) · S3 2 (8 days) · S4 1 · S6 1 (Hyslop checked provenance by letter) · S7 2 → 6/10, but cap ③ (S2 = 0) → R C · no verified information (V—) · independence I2 (record 1883, before the 1900 baseline; no non-Western record of the structure in English by 1883)",
)

T_KO = dict(
    font="'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic','Helvetica Neue',Arial,sans-serif",
    title="루이자 브라우닝, 런던 1883 — 임종, 여드레 뒤에 쓴 편지, 그리고 그 편지가 활자에 이르는 길",
    sub="카드 DBV-GB-1883-browning 3절·4절의 사실(1909년 7월 JASPR 422–423쪽에 실린 편지, 사망 색인). 윌리엄이 그린 도해이며 기록이 아니다.",
    rows=[
        ("사건", SOFT, [
            ("1867년 7월", ["존 에릭슨의 아내", "아멜리아 제인 에릭슨,", "메릴본에서 50세로 사망"]),
            ("1868년 7월 9일", ["조카 엘런 브라우닝(오클랜드)이", "트레버 슈트 장군과 결혼"]),
            ("1883년 10월 26일(금)", ["아멜리아의 언니 루이자", "브라우닝(78, 당뇨)이 침실에서", "넘어짐. 하녀가 발견.", "회복하지 못함"]),
            ("1883년 10월 28일(일) 새벽", ["의식이 없다가 \"오 아멜리아!", "아멜리아!\" — 손을 내밀고", "곧 사망. '곁을 지키던 이들'", "(이름 없음)이 들음"]),
        ]),
        ("기록", ACC_BG, [
            ("1883년 11월 5일 · 8일 뒤", ["슈트 부인이 브랙넬 자택에서", "뉴욕의 에릭슨 대령에게 편지.", "가족 소식 편지이지", "발표용 글이 아님"]),
            ("1889년 3월 8일", ["에릭슨 뉴욕에서 사망.", "문서는 전기 작가", "W. C. 처치에게"]),
            ("1890년 →", ["처치가 『에릭슨 전기』(1890)를", "쓰며 문서 더미에서", "이 편지를 발견해", "우연히 보관"]),
            ("사망 색인(2026년 확인)", ["1883년 10–12월 켄싱턴:", "Browning, Louisa, 78세.", "1867년 7–9월 메릴본:", "Ericsson, Amelia Jane, 50세"]),
        ]),
        ("활자로", SOFT2, [
            ("1908년 8월 17일", ["처치가 편지 원본을", "시카고 『오픈 코트』", "편집자에게 보냄"]),
            ("1908–09년", ["편집자 → D. P. 애벗 →", "J. H. 하이슬롭(ASPR)"]),
            ("1909년 7월", ["하이슬롭이 JASPR 3권 7호", "422–423쪽에 편지를 실음.", "'사적인' 대목은 뺌.", "누렇게 바랜 종이를 묘사"]),
            ("1926년", ["바렛이 『임종 환시』", "44–45쪽(3장)에", "요약해 재수록"]),
        ]),
    ],
    foot="등급: S1 2(당대 편지) · S2 0(쓴 이는 현장에 없었고 지켜본 이들은 이름이 없음) · S3 2(8일) · S4 1 · S6 1(하이슬롭이 서신으로 출처 확인) · S7 2 → 6/10이지만 상한 ③(S2=0) → R C · 검증 정보 없음(V—) · 독립성 I2(1883년 기록, 기준 연도 1900 이전; 1883년까지 영어로 열린 비서구 기록 없음)",
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
    if ri < 2:
        # arrow from the last box of this row down to the first box of the next row
        x1 = LEFT + LABEL_W + 3 * (BOX_W + GAP) + BOX_W / 2
        x0 = LEFT + LABEL_W + BOX_W / 2
        ym = ry + ROW_H + ROW_GAP / 2
        o.append(f'<path d="M{x1},{ry + ROW_H} L{x1},{ym} L{x0},{ym} L{x0},{ry + ROW_H + ROW_GAP - 3}" fill="none" stroke="{LINE}" stroke-width="1.2" stroke-dasharray="4,3"/>')
        o.append(f'<path d="M{x0 - 4},{ry + ROW_H + ROW_GAP - 8} L{x0},{ry + ROW_H + ROW_GAP - 2} L{x0 + 4},{ry + ROW_H + ROW_GAP - 8}" fill="none" stroke="{LINE}" stroke-width="1.2"/>')

fy = top + 3 * (ROW_H + ROW_GAP) + 10
o.append(f'<rect x="{LEFT}" y="{fy}" width="{W - 80}" height="{H - fy - 20}" rx="6" fill="#ffffff" stroke="{ACC}" stroke-width="1"/>')
ty = fy + 20
for ln in wrap(T["foot"], 165 if LANG == "en" else 100):
    o.append(f'<text x="{LEFT + 12}" y="{ty}" font-size="12" fill="{INK}">{esc(ln)}</text>')
    ty += 16
o.append("</svg>")
print("\n".join(o))
