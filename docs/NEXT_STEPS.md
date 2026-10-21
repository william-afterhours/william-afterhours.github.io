# NEXT_STEPS — 재개할 때 이것부터

## 현재 상태 (2026-10-21, 세션 1)

- **단계**: 연구 헌장·등급표·기록 구조·`git init` 전부 **승인됨**(2026-10-21 "그래"). 조사 시작 — 카드 1(NDE-NL-1979-dentures)부터.
- 이번 세션에 만든 것: `docs/CHARTER.md`(헌장 추천안), `docs/METHOD.md`(등급표 v0.1), `cases/_TEMPLATE.md`, `entities/_TEMPLATE.md`.
- 대표님 추가 지시(세션 중): 모든 가능성 열기, 집요·철저, 사건·인물의 시대를 넘는 연관 추적, 기록 장소 고민 → METHOD.md 가설 목록·연결 층 섹션과 CHARTER §4·§5로 반영.

## 승인되면 다음 세션에 할 일

1. `git init` (승인 시) → 첫 커밋.
2. 카드 1·2번부터: `NDE-NL-1979-dentures`(UNT JNDS 2008·2010 전문), `DBV-GB-1924-doris`(archive.org 1926 스캔, 식별자 `b29813992`). 둘 다 무료 전문이 있고 검증 정보 후보라 등급표 첫 시험에 맞다.
3. `entities/`에 첫 항목: 인물 Stevenson·Haraldsson·Barrett, 모티프 "잘못 데려감".
4. `tools/build_index.py` — 카드·엔티티 프론트매터를 읽어 `docs/TIMELINE.md`와 깨진 링크 목록 생성.

## 출처 접근 메모 (다시 조사하지 않기 위해)

- UNT 디지털 도서관(JNDS): WebFetch는 인증서 오류 → `curl`로 PDF 직접 받기. 사건별 ark 주소는 CHARTER §3.
- DOPS(med.virginia.edu) PDF: 봇 차단 403. 브라우저 자동화로 열거나 다른 사본을 찾는다.
- PubMed: 웹페이지는 쿠키 차단 → eutils API로 서지 확인(됨).
- archive.org advancedsearch API로 공공 도메인 스캔 검색(됨). 식별자: Phantasms vol.1 `phantasmsoflivin001gurn`, vol.2 `phantasmsoflivin02gurn`, Barrett 1926 `b29813992`, Osis 1961 `deathbedobservat0000unse`, SPR Proceedings 1894 `proceedingssoci03britgoog`, Gregory 『대화』 1911 영역 `cu31924029222076`.
- JSE: journalofscientificexploration.org 무료. Sudduth 2021 = article 2361, Tucker 2022 = 2487, Sudduth 응답 = 2515, Matlock 2022 = 2529, 2023 = 2765.
- 青空文庫 『遠野物語』: cards/001566/card52504.html.
- 유료 가능: Resuscitation 2014(AWARE), Omega 2010(케랄라), JSPR 2000(푸르니마). 저자 사본·기관 리포지터리를 먼저 찾고, 없으면 2차 요약으로 등급을 낮춰 쓴다.

## 대표님 손

- 헌장 승인(문장 하나). `git init` 승인. 그 외 없음.

## 토큰

- 세션 1: 약 35만 추정 — 등급표 설계 서브에이전트 12.3만(집계값) + 본 세션 약 20만(웹 검색 결과가 대부분, 추정). 다음 세션부터 `/cost` 기준으로 적는다.
- 등급표의 잠정값(1회차 조사에서 확정할 것): 매체 확산 기준 연도(NDE 1975 / CORT 1956 / CA·DBV 1900)는 근거 문헌 미확인. 수렴 판정 숫자(4클러스터·V2 3건)는 William의 판단이라 대표님이 조정 가능.
