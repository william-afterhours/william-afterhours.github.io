#!/usr/bin/env python3
"""Diagram: DBV-US-1864-dryden — the deathbed, the mother's notes and memoir, and the memoir's road into print.
도해: 임종, 어머니의 메모와 회고록, 그리고 회고록이 인쇄물에 이르기까지의 경로.

Only facts from §3 and §4 of the card are drawn. This is not a record.
카드 3절·4절의 사실만 그림으로 옮긴다. 기록이 아니다.

usage:
  python3 -I tools/diagrams/DBV-US-1864-dryden.py en > assets/DBV-US-1864-dryden--chain.svg
  python3 -I tools/diagrams/DBV-US-1864-dryden.py ko > assets/DBV-US-1864-dryden--chain-ko.svg
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
    title="Daisy Dryden, San Jose 1864 — the deathbed, the mother's notes, the memoir of 1894 and its road into print",
    sub="Facts from §3 and §4 of card DBV-US-1864-dryden (the memoir, 3rd edition 1909; its reprint in JASPR, June 1918; the father's book of 1872). This is a diagram by William, not a record.",
    rows=[
        ("THE EVENT", SOFT, [
            ("early 1864", ["Her brother David Albion", "('Allie') dies of scarlet", "fever, aged six, about seven", "months before her death"]),
            ("summer 1864", ["Daisy, aged nine, has bilious", "fever, then typhoid (five", "weeks); seems to recover"]),
            ("last 3–4 days", ["Enteritis. She says Allie is", "with her, answers questions", "'when Allie comes'; describes", "other dead people to visitors"]),
            ("8 Oct 1864, 11.30 p.m.", ["'Allie has come for me' (11.15);", "at the hour she had named,", "'Come, Allie' — dies in her", "father's arms. Mother present"]),
        ]),
        ("THE RECORD", ACC_BG, [
            ("'a short time after'", ["The mother writes the dying", "words in her notebook.", "Notes not seen; known only", "from her own preface"]),
            ("1872", ["The father, Rev. D. A. Dryden,", "publishes They Rise: the dead", "have a spiritual body at once.", "Daisy is not mentioned"]),
            ("Oct 1894 · 30 years later", ["The mother, now a widow at", "Gilroy, writes the memoir", "'principally' from the notes;", "dates her preface"]),
            ("c. 1901", ["The mother dies before", "the memoir is printed", "(Higgins 1906; Hyslop 1918)"]),
        ]),
        ("INTO PRINT", SOFT2, [
            ("1905", ["First edition, Toronto:", "W. Briggs, 58 pp.; copyright", "entered in Canada by", "Rev. F. L. Higgins"]),
            ("1909", ["Third edition, Boston: Colonial", "Press, Higgins's introduction", "of 1906. A copy reaches", "William James's library"]),
            ("June 1918", ["Hyslop reprints the memoir", "in JASPR 12(6) pp. 375–391,", "with the living sister's", "permission"]),
            ("Oct 1918 →", ["Hyslop compares later cases", "with 'that of Daisy Dryden';", "Barrett 1926 reprints it", "in chapter III"]),
        ]),
    ],
    foot="Grades: S1 1 (a witness's memoir from notes made at the time; the notes not seen) · S2 1 (one named witness who was present: the mother) · S3 0 (30 years to the dated record) · S4 0 · S6 1 (no investigator; Hyslop reprinted 54 years later) · S7 2 → 3/10 → R C, no cap · V0 (claims about dead people the child is said not to have known; recorded only after) · independence I2",
)

T_KO = dict(
    font="'Apple SD Gothic Neo','Noto Sans KR','Malgun Gothic','Helvetica Neue',Arial,sans-serif",
    title="데이지 드라이든, 새너제이 1864 — 임종, 어머니의 메모, 1894년의 회고록, 그리고 활자에 이르는 길",
    sub="카드 DBV-US-1864-dryden 3절·4절의 사실(회고록 1909년 제3판, 1918년 6월 JASPR 재수록, 아버지의 1872년 책). 윌리엄이 그린 도해이며 기록이 아니다.",
    rows=[
        ("사건", SOFT, [
            ("1864년 초", ["남동생 데이비드 앨비언", "('앨리')이 성홍열로 여섯 살에", "사망. 데이지가 죽기", "약 일곱 달 전"]),
            ("1864년 여름", ["아홉 살 데이지, 담즙열에 이어", "장티푸스(5주).", "나아지는 듯함"]),
            ("마지막 3–4일", ["장염. 앨리가 곁에 있다고 말함.", "모르는 것은 '앨리가 오면'", "묻겠다고 함. 찾아온 이들에게", "다른 죽은 이들을 말함"]),
            ("1864년 10월 8일 밤 11시 반", ["\"앨리가 나를 데리러 왔어\"(11시 15분).", "자기가 말한 그 시각에", "\"와, 앨리\" — 아버지 품에서", "숨짐. 어머니가 곁에 있었음"]),
        ]),
        ("기록", ACC_BG, [
            ("'죽은 뒤 얼마 안 되어'", ["어머니가 마지막 말들을", "공책에 적음. 메모는", "보지 못함. 어머니의", "서문으로만 알려짐"]),
            ("1872년", ["아버지 D. A. 드라이든 목사가", "『그들은 일어난다』 출간:", "죽은 이는 곧 영의 몸을 입는다.", "데이지는 언급 없음"]),
            ("1894년 10월 · 30년 뒤", ["길로이에 사는 미망인이 된", "어머니가 메모를 '주로'", "바탕으로 회고록을 씀.", "서문에 날짜"]),
            ("1901년경", ["회고록이 인쇄되기 전에", "어머니 사망", "(히긴스 1906, 하이슬롭 1918)"]),
        ]),
        ("활자로", SOFT2, [
            ("1905년", ["초판, 토론토 W. 브리그스,", "58쪽. F. L. 히긴스 목사가", "캐나다에 저작권 등록"]),
            ("1909년", ["제3판, 보스턴 콜로니얼 프레스,", "히긴스의 1906년 서론.", "한 부가 윌리엄 제임스의", "서재에 들어감"]),
            ("1918년 6월", ["하이슬롭이 JASPR 12권 6호", "375–391쪽에 회고록을 재수록.", "살아 있는 언니의 허락"]),
            ("1918년 10월 →", ["하이슬롭이 뒤의 사례들을", "'데이지 드라이든의 경우'와", "비교. 바렛 1926이", "3장에 재수록"]),
        ]),
    ],
    foot="등급: S1 1(당시 메모를 바탕으로 한 목격자의 회고록, 메모는 못 봄) · S2 1(현장에 있던 이름 있는 목격자 한 명: 어머니) · S3 0(날짜 있는 기록까지 30년) · S4 0 · S6 1(조사자 없음, 54년 뒤 하이슬롭 재수록) · S7 2 → 3/10 → R C, 상한 없음 · V0(아이가 몰랐다는 죽은 이들에 관한 주장, 기록은 나중) · 독립성 I2",
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
