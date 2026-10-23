# NEXT_STEPS — 재개할 때 이것부터

## 현재 상태 (2026-10-23, 세션 4)

- **읽기 개편 + 영어 주판(2026-10-23, 세션 4 후반, 대표님 지시)**: 대표님 지적 세 가지(사이트 제목에 William 이름이 있다 → 저자란으로, 사람이 쓴 글 같지 않아 읽기 어렵다, 사진·그림이 안 보인다)와 "출처도 중요한 단서니 꼭 기록", "물론 영문판이 main이겠지"를 반영했다.
  - ① 사이트 이름 **The Paranormal Ledger**, 저자란 컴포넌트 `site/components/Byline.tsx`(글쓴이·날짜·읽는 시간; 프론트매터 `lang: ko`면 "글 William · 2026년 10월 23일 · 읽는 데 n분"). `assemble.sh`가 Quartz `components/`로 복사한다.
  - ② 카드 **두 층**(METHOD 9절): 위층 "읽는 글"(리드 인용문 → What happened(사진·지도·도해를 해당 대목 사이에 캡션과 함께) → How far can this record be trusted → Other ways to explain it) / `---` / 아래층 "조사 장부" §1–13은 출처 번호·점수 그대로. 출처는 어느 층에서도 빠지지 않는다.
  - ③ **영어가 주판**: 카드 2건·README·템플릿을 영어로 다시 썼다(이전엔 한국어뿐이었다). 한국어는 `ko/cases/<id>-ko.md`에 읽는 글만 두고 "출처" 절이 영어 장부를 가리킨다. 장부는 한 벌(영어)만 — 두 벌이면 어긋난다. 파일명 `-ko` 접미사는 Quartz "shortest" 링크 해석의 충돌을 피하기 위해서다.
  - ④ 도해는 `tools/diagrams/<id>.py en|ko`로 두 언어 SVG(`--sequence.svg`/`--sequence-ko.svg`, `--timeline.svg`/`--timeline-ko.svg`). 1920년 지도의 설명 상자는 영어. 폴더 페이지 `index.md`(Cases·Documents·Entities·Sources·Materials, `ko/`는 한국어·사건 카드).
  - ⑤ 마크다운 굵게가 깨지는 패턴 `**…)**은`(닫는 `**` 앞이 문장부호, 뒤가 글자)을 `ko/index.md`·METHOD에서 고쳤다. 한국어 문서를 쓸 때 조심.
  - **아직 한국어인 것**: `docs/METHOD.md`·`CHARTER.md`·`entities/`·`sources/`·`assets/index.md` 본문. 영어 주판이므로 다음 세션에 옮긴다(README·폴더 페이지에 "translation in progress"라고 적어 둠).
  - 로컬 미리보기(재개용): Quartz 4.5.2 소스가 스크래치패드에 있으면 `bash site/assemble.sh . <quartz-src>` → `cd <quartz-src> && npx quartz build --serve --port 8080`(백그라운드; 종료되면 이 serve 명령만 다시). 헤드리스 Chrome 스크린샷은 1440×900 같은 보통 크기로 찍는다 — 탐색기가 현재 항목을 `scrollIntoView`해서 아주 긴 창에서는 화면이 밀려 보이는데 실제 브라우저 문제가 아니다.
  - **대표님 지시(2026-10-23)**: 보고에 비용·토큰 이야기를 쓰지 않는다. 아래 "토큰" 절은 기록용 한 줄만.
- **공개 준비(2026-10-23, 세션 4)**: 대표님이 "홈페이지 비슷한 거 만들어서 공개하는 거 아니었나"고 물음 → 공개 전환을 SYNTHESIS v1 시점에서 **지금으로 앞당기는 추천안**을 올리고 확인 대기 중. 작업 트리는 공개 가능하게 정리함: 운영 메모를 저장소 밖으로 이전, CHARTER의 다른 직원 언급 삭제, 카드 2의 1924년생 아기 이름을 이니셜로, README 카드 표에 카드 2 추가. 사이트 손질: 체크된 체크리스트의 취소선 제거(`site/custom.scss`), 첫 페이지 제목 중복 제거(`assemble.sh`). 로컬 미리보기(Quartz 4.5.2를 스크래치패드에 받아 `assemble.sh` → `npm ci` → `npx quartz build --serve --port 8080`, 헤드리스 Chrome 스크린샷)로 홈·카드 2 화면 확인해 대표님께 보냄.
  - **공개 직전에 할 것(대표님 확인 뒤)**: ① git 이력 정리 — 커밋 4곳(2bbc7bc·0c948d5·7eb7bf1·b0a0847 등)의 `docs/NEXT_STEPS.md`·`CHARTER.md`에 운영 문장이 남아 있음. 커밋 11개뿐이고 등급 변경 이력은 아직 없으므로 `git filter-branch --tree-filter`(Python 치환)로 그 문장만 지우고 force-push. 토큰·비밀번호는 이력에 없음(grep 확인). ② `gh repo edit --visibility public` ③ Pages 소스 "GitHub Actions"(API) ④ 워크플로 재실행 → https://william-afterhours.github.io/ 확인 ⑤ giscus는 대표님 브라우저(Trove 키와 묶음).
- **자료 층 신설(2026-10-22, 대표님 지시 "자료 사진 그림 삽화 등으로 잘 모아서 같이 정리", "신문 등은 이용하고 출처 확실히 남기고")**: `assets/`(파일 + `index.md` 목록·규칙), METHOD 9절 "시각 자료 규칙"(13절 "자료" 칸 추가), 카드·템플릿 13절, `tools/commons_fetch.py`(Commons 라이선스 확인·받기), `tools/diagrams/<id>.py`(도해 생성). 카드 1에 4건 적용(병원 1960 사진 CC BY-SA, 오이 범람원 참고 CC0, 크래시 카트 참고 CC0, 사건 순서 도해 SVG). 로컬 Quartz 빌드로 이미지·자료 페이지 확인됨.
  - 대표님의 "저작권 걸리면 다시 그리거나 다른 AI로 변경" 지시는 이렇게 처리: 저작권 있는 사진·쪽은 링크만, **사실(순서·배치·수치·지도)만 도해로 다시 그림**. 원본 표현을 베낀 그림은 2차 저작물이고 기록도 아니라서 쓰지 않는다(`assets/index.md`에 적음).
  - 신문: Delpher(KB) SRU API `https://jsru.kb.nl/sru/sru?x-collection=DDD_artikel&query=…`가 열린다(무료, 키 없음). 1979년 지역지 De Gelderlander는 미수록. 다음 카드부터 사건 직후 신문을 먼저 찾는다(Chronicling America·Trove·Papers Past·Delpher는 전부 무료·PD).
  - Wikimedia 축소본 URL은 API가 주는 폭(예 960·1280)만 받아들인다(임의 폭은 400). `commons_fetch.py`가 처리.
- **카드 2 완료(2026-10-22, 세션 3 후반)** `cases/DBV-GB-1924-doris.md` — **B/V1**, `independence: I0`, `countable: V`(V층만 집계).
  - 출처: Barrett 1926 『Death-bed Visions』 전문(Wellcome 텍스트 API) + pp.10–14 쪽 이미지 열람(S7=2). **GRO 색인(FreeBMD)으로 대조**: 혼인 1923 Q2 Shoreditch(Clark, Doris G. × Bargery, Stanley), 언니 Vida M. Clark 사망 1923 Q4 West Ham(34), Doris G. Bargery 사망 1924 Q1 Hackney(22), 출생 Bargery D. O. 1924 Q1 Hackney(모성 Clark; 생사 불명이라 이니셜) — 책의 순서·장소·나이와 일치. 불일치 3건은 카드 12절(수간호사 "3주"/어머니 "2주 4일", 아기 "him"/여아명, 남편 "W."/Stanley).
  - 등급 요지: 증인 4명이 각자 서명(S2=2), 2년 안에 출판(S3=1), 조사자 바렛이 첫 증인의 남편이자 SPR(S6=1), 1924-02 교구지 미확인(열리면 S3·S5 재검토). V2가 못 되는 이유 = 확인 이전의 날짜 있는 문서가 없고 정보(비다의 죽음)가 곁의 어머니·남편·수간호사가 알던 것(L·C 부분 배제). 이것이 DBV-V 구조의 일반 한계.
  - **I0 결정**: 기록자(레이디 바렛)가 이 모티프를 1917년에 출판한 바렛의 아내 → 독립성 경로 ② 확인. EU-W의 DBV S층은 SPR 바깥 기록(1882년 이전 또는 Osis 1961 같은 다른 조사 주체)으로 채운다.
  - 엔티티 4건 `P-Barrett-WF`·`P-Barrett-Florence`·`L-Mothers-Hospital-Clapton`·`M-dbv-visitor-unknown-dead`, 출처 요약 `sources/barrett-1926-death-bed-visions.md`(장별 OCR 오프셋 — 3·4장이 DBV·CA 후보 창고), 자료 4건(바렛 부부 초상 PD/CC BY, 병원 2018 CC BY-SA, 연표·발화·기록 사슬 도해).
  - 신문: 영국지는 BNA 유료라 안 씀. 무료 아카이브는 Papers Past·loc.gov·HathiTrust 봇 차단, Trove 키 필요 → **1924년 보도 유무 미확인**. 
- **단계**: 조사 진행 중. 카드 1 `cases/NDE-NL-1979-dentures.md` 완료(**C/V1**, `countable: V`). 엔티티 4건(`O-Merkawah`, `P-TG-witness-1979`, `P-Woerlee-GM`, `M-obe-veridical-resuscitation`), 출처 요약 `sources/jnds-dentures-2004-2010.md`, JNDS 전체 색인 `sources/unt-jnds-index.tsv`(1081건), 도구 `tools/unt_ocr.py`·`tools/unt_oai.py`.
- **METHOD v0.2**(이번 세션, 내 결정, 대표님께 보고·거부 가능): NDE "요소 2개 이상"은 S층 집계에만. V층 입장 = 생명 위기 + 체외 시점 + V요소. `countable: no/S/V/SV`. 거부되면 v0.1로 되돌리고 카드 1은 "유사 사례"로 둔다(10절에 기록).
- **기록 장소 확정(2026-10-21 "1번 좋아")**: GitHub 저장소(이 저장소 그대로) + Discussions(토론) + Quartz로 GitHub Pages(읽기용 사이트, 위키링크·백링크·그래프·검색) + giscus(페이지 댓글을 Discussions로 모음). 비용 0원. 처음 계획은 비공개로 올리고 SYNTHESIS v1(10건) 때 공개 전환 확인이었으나, **2026-10-23 대표님 질문으로 지금 공개하는 추천안을 올림(확인 대기)**. 되돌릴 수 없는 공개 발언이라 대표님 한마디 뒤에만 전환한다. 무료 계정의 Pages·giscus는 공개 저장소에서만 되므로 사이트는 공개 전환 때 켜진다.
  - 준비 완료: `site/quartz.config.ts`·`quartz.layout.ts`·`assemble.sh`, `.github/workflows/deploy.yml`(Quartz 4.5.2 커밋 고정, 비공개 동안 deploy 단계 생략), `README.md`(= 사이트 첫 페이지), `.gitignore`. **로컬 빌드 확인함**(Node 26, 10개 문서 → 41 파일, 위키링크·백링크 정상).
  - **저장소 개설 완료(2026-10-22)**: https://github.com/william-afterhours/william-afterhours.github.io (Discussions 켜짐, main 추적). 계정 `william-afterhours`. **운영 메모는 저장소 밖에 둔다(공개 저장소에 넣지 않는다). 재개할 때 그것도 읽는다.**
  - Actions `Deploy site`(build만) 런 39784436279·39787305222(자료 층 커밋 7eb7bf1) **success** 확인(2026-10-22). 비공개라 deploy 단계는 건너뜀.
  - 공개 전환 때 할 것(이력 정리는 위 세션 4 항목): Settings → Pages → Source "GitHub Actions"(API: `gh api -X POST repos/…/pages -f build_type=workflow`) → giscus 앱 설치(https://github.com/apps/giscus) → giscus.app에서 repoId·categoryId 받아 `site/quartz.layout.ts` 주석 해제 → push → 사이트 확인.

## 다음 세션에 할 일

**먼저**: 영어 주판 마무리 — `docs/METHOD.md`·`CHARTER.md`·`entities/*`·`sources/*`·`assets/index.md` 본문을 영어로(한국어는 `ko/`에 읽는 글만). 엔티티 제목이 영어가 되면 영어 카드의 백링크·그래프 표시도 영어가 된다.

1. 대표님 답을 반영: METHOD v0.2 유지/복귀(기록 장소는 확정·개설 완료).
2. 카드 3(추천): `NDE-US-1991-reynolds`(Sabom 1998; Woerlee 2011 반박 UNT metadc461684·461715 — 반대 자료가 무료로 열려 있어 counter 축을 제대로 쓸 수 있는 첫 카드). 대안 `NDE-INTL-2014-aware`(V층 대조군; Resuscitation 2014 저자 사본 탐색).
3. DBV 다음 카드는 **SPR 바깥·다른 클러스터**로: Osis & Haraldsson 1977 『At the Hour of Death』 인도 사례(SA, 조사 주체 ASPR/Osis) 무료 사본 탐색; Barrett 1926 3장(OCR 오프셋 38,885–112,510)에서 1882년 이전 기록이 있는 사례 목록 추출. Jennie & Edith 1889(미국)는 같은 조사 주체라 V 후보로만.
4. `tools/build_index.py` — 프론트매터 → `docs/TIMELINE.md` + 깨진 `[[링크]]` 목록. 지금 깨진 링크: `NDE-INTL-2014-aware`(카드 미작성, 의도적). 카드 2의 후보 id(`DBV-US-1889-jennie-edith`, `T-Cobbe-1882-peak-in-darien`)는 일부러 위키링크로 안 적었다.
5. 매체 기준 연도(NDE 1975) 근거 문헌: Moody 『Life After Life』 1975 초판·네덜란드어판 연도 확인(카드 1 독립성 ②·④가 '불명'인 이유). DBV 1900은 Cobbe 1882 원문을 열어 확인.
6. 카드 2 미해결(기회 되면): All Saints Haggerston 교구지 1924-02(런던 메트로폴리탄 아카이브 목록), 레이디 바렛 메모 원본(SPR 아카이브·케임브리지 대학도서관), BMJ 1945 부고(브라우저로).

## 출처 접근 메모 (다시 조사하지 않기 위해)

- **UNT 디지털 도서관(JNDS)**: 아이템 페이지·PDF 직접 URL·검색은 Altcha(DAM) 봇 차단(302 → `/dam/?next=`). WebFetch는 인증서 거부. **열리는 공개 API 2개**:
  - IIIF manifest `https://digital.library.unt.edu/ark:/67531/<ark>/manifest/` → 페이지 수(`sequences[0].canvases`).
  - 페이지별 OCR 주석 `…/<ark>/m1/<p>/annotations/ocr/`(JSON, xywh 좌표) → `python3 -I tools/unt_ocr.py <ark> <npages> <out.txt> <dl_dir>`로 전문 복원. 2단 조판은 줄 안에서 어순이 섞이지만 판독 가능. 인용은 PDF를 받은 경우 그쪽 우선.
  - OAI-PMH `https://digital.library.unt.edu/oai/?verb=ListRecords&metadataPrefix=oai_dc&set=collection:JNDS` → `tools/unt_oai.py`. 색인은 `sources/unt-jnds-index.tsv`(ark·연도·제목·저자). **새 NDE 카드는 이 색인에서 먼저 찾는다.**
  - 예외적으로 PDF가 열린 것: Smit 2008 `metadc798921/m2/1/high_res_d/vol27-no1-47.pdf`(세션 2 초반). 재현 안 될 수 있음.
- DOPS(med.virginia.edu) PDF: 봇 차단 403. 브라우저 자동화로 열거나 다른 사본을 찾는다.
- PubMed: 웹페이지는 쿠키 차단 → eutils API로 서지 확인(됨). Lancet 전문은 403(유료).
- Goldsmiths eprints(French 2001, eprint 5137): 서지만, 본문 없음.
- neardth.com(denture-man.php): 검색엔 뜨나 404. 쓰지 않음.
- **Wellcome Collection**(키 없음, 전부 열림): IIIF manifest `https://iiif.wellcomecollection.org/presentation/v2/<bnumber>`(캔버스 label = 인쇄 쪽), 쪽 이미지 `https://iiif.wellcomecollection.org/image/<bnumber>_NNNN.jp2/full/900,/0/default.jpg`, 전문 `https://api.wellcomecollection.org/text/v1/<bnumber>`(한 줄짜리 거대 문자열 — Python으로 인덱스 창을 잘라 읽는다). 라이선스 표시가 열람 전용이면 쪽 사본은 넣지 않고 링크만. archive.org의 같은 사본(`b29813992`)은 403.
- **GRO 잉글랜드·웨일스 출생·혼인·사망 색인 = FreeBMD**(무료, 키 없음): `https://www.freebmd.org.uk/cgi/search.pl`에 multipart POST(`type`=Births/Marriages/Deaths, `surname`, `given`, `start`/`end` 연도, `countyid=all`, 숨은 필드 `db`·`v`, `js=`, `find.x/y`). 결과 html을 저장해 `sed 's/<[^>]*>/ /g'`로 읽는다. 이름·나이·등록구·분기·권/면만 나온다(1911년 이후 출생 색인은 모성 포함). 영국 사례의 인물 실재·사망 순서 확인에 가장 싼 1차 자료.
- 봇 차단·키 필요(2026-10-22 확인): Papers Past(NZ)·Chronicling America/loc.gov·HathiTrust 403; PMC·Europe PMC PDF는 reCAPTCHA/403(서지는 eutils로); Trove(호주)는 API 키 필요(무료 가입). 브라우저 자동화로 열거나 대표님 손.
- Wikidata API로 인물 생몰년 확인(됨): W. F. Barrett Q369067, Florence Barrett Q5460561.
- archive.org advancedsearch API로 공공 도메인 스캔 검색(됨). 식별자: Phantasms vol.1 `phantasmsoflivin001gurn`, vol.2 `phantasmsoflivin02gurn`, Barrett 1926 `b29813992`, Osis 1961 `deathbedobservat0000unse`, SPR Proceedings 1894 `proceedingssoci03britgoog`, Gregory 『대화』 1911 영역 `cu31924029222076`.
- JSE: journalofscientificexploration.org 무료. Sudduth 2021 = article 2361, Tucker 2022 = 2487, Sudduth 응답 = 2515, Matlock 2022 = 2529, 2023 = 2765.
- 青空文庫 『遠野物語』: cards/001566/card52504.html.
- 유료 가능: Resuscitation 2014(AWARE), Omega 2010(케랄라), JSPR 2000(푸르니마). 저자 사본·기관 리포지터리를 먼저 찾고, 없으면 2차 요약으로 등급을 낮춰 쓴다.

## 대표님 손

- **답 1개 남음**: METHOD v0.2(NDE V층 입장 조건) 유지 여부. 답이 없으면 유지한 채 진행하고, 거부하면 v0.1로 되돌린다.
- **GitHub 계정 — 전부 완료(2026-10-22)**: 계정 `william-afterhours`. 기기 로그인 방식(William이 세션에서 `gh auth login -w`를 띄우고 대표님이 브라우저에서 코드 입력 — 터미널을 안 열어도 돼서 다음에도 쓴다). 비밀번호는 대표님만 안다. 세부는 저장소 밖 운영 메모에.
- **지금 남은 대표님 손: 공개 전환 확인 1개(2026-10-23 올림).** "공개해도 된다" 한마디면 William이 이력 정리 → 공개 → Pages까지 처리한다.
- **모아 두는 것(급하지 않음, 다음 가입 요청과 묶어서)**: Trove(호주 국립도서관) API 키 — 무료 가입, 이메일 인증. 용도: 1924~26년 영연방 신문의 "Lady Barrett" 임종 환시 전재 기사 탐색(카드 2 신문 미확인 해소). 이것 하나 때문에 대표님을 부르지는 않는다.
- **공개 전환 점검표(2026-10-23 작업 트리 기준 통과)**: 목격자 이니셜(카드 1·2 확인), 키·비밀번호 없음(이력까지 grep), `.claude/settings.json`은 모델·effort만이라 공개해도 됨, `tools/commons_fetch.py`의 UA 이메일은 공개 연락처라 유지. 남은 것은 git 이력의 운영 문장 정리뿐.

## 토큰

- 세션 1: 약 35만 추정 — 등급표 설계 서브에이전트 12.3만(집계값) + 본 세션 약 20만(추정).
- 세션 3(2026-10-22): 저장소 개설 마무리 + 자료 층. 추정 입력 누적 약 15–25만(이미지 열람 5장 포함), 출력 약 2만.
- 세션 3 후반(2026-10-22, 카드 2): 컨텍스트가 한 번 가득 차 요약됐다. 추정 입력 누적 약 30–40만(Barrett OCR 창 읽기, 쪽 이미지 5장, FreeBMD 결과 4건, Commons 이미지 3장, 도해 렌더 2회), 출력 약 4만(카드·엔티티 4·출처 요약·도해 코드). 절감: 전문 OCR은 스크래치패드에만 두고 장별 오프셋만 `sources/`에 기록해 다음 DBV 카드는 필요한 창만 읽는다.
- 세션 4(2026-10-23, 공개 준비): 추정 입력 누적 약 10–15만(사이트 스크린샷 4장 열람 포함), 출력 약 1만. 큰 읽기 없음.
- 세션 4 후반(2026-10-23, 읽기 개편·영어 주판): 컨텍스트 요약 1회. 추정 입력 누적 약 30만(스크린샷 12장·도해 렌더 3장), 출력 약 5만(카드 2건 영어 재작성, 한국어 읽는 글 2건, 템플릿·README·도해 코드 2벌). 기록용 한 줄 — 보고에는 쓰지 않는다(대표님 지시).
- 세션 2: `/cost`를 직접 볼 수 없어 추정. 컨텍스트가 한 번 가득 차 요약됐으므로 본 세션 입력 누적 약 25–35만(웹·OCR 본문 읽기가 대부분, Woerlee 2010·Smit&Rivas 2010·Smit 2008·Woerlee 2004 전문 4편), 출력 약 3만. 대표님이 `/cost`를 치면 정확한 수치가 나온다.
- 비용 절감 메모: JNDS 색인(OAI)을 받아 두어 다음 NDE 카드는 검색 토큰이 거의 들지 않는다. 전문은 스크래치패드에만 두고 저장소에는 요약만(저작권).
- 등급표의 잠정값(1회차 조사에서 확정할 것): 매체 확산 기준 연도(NDE 1975 / CORT 1956 / CA·DBV 1900)는 근거 문헌 미확인. 수렴 판정 숫자(4클러스터·V2 3건)는 William의 판단이라 대표님이 조정 가능.
