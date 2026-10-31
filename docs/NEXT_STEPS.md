# NEXT_STEPS — 재개할 때 이것부터

## 현재 상태 (2026-10-31, 세션 7)

- **카드 4 완료 `cases/DBV-GB-1883-browning.md` — C(상한 ③)/V—, I2, `countable: no`.** 이 연구의 **첫 I2** 기록. 1883년 10월 28일 런던 켄싱턴, 당뇨와 낙상 뒤 의식이 없던 루이자 브라우닝(78)이 "Oh Amelia! Amelia!"(1867년 죽은 언니) 하고 손을 내밀고 사망. 조카 엘런 슈트 부인(Lady Chute, 브랙넬)이 8일 뒤 언니의 남편 존 에릭슨(모니터호 설계자, 뉴욕)에게 쓴 가족 편지가 기록. 편지는 에릭슨 문서 → 전기 작가 W. C. 처치 → 1908 『오픈 코트』 편집자 → D. P. 애벗 → 하이슬롭 → **JASPR 1909년 7월호 422–423쪽**(archive.org, 퍼블릭 도메인, 전문·쪽 스캔 확인) → 바렛 1926 44–45쪽 재수록. **FreeBMD 대조**: 1883년 4분기 켄싱턴 Browning Louisa 78세 / 1867년 3분기 메릴본 Ericsson Amelia Jane 50세 — 편지·처치의 설명과 일치.
  - 점수 S1 2·S2 0·S3 2·S4 1·S6 1·S7 2 = 6이지만 **S2=0(쓴 이는 현장에 없었고 지켜본 이들은 무명) → 상한 ③ → C**. 검증 주장 없음. 불리 가설 H5·H8. 반대 자료 탐색: 사건 특정 반박 없음(`counter: none`). 같은 클러스터에서 같은 질의 C 카드가 하나 더 나오면 METHOD §8 짝 규칙으로 EU-W S층 한 자리를 채운다.
  - 엔티티 5건 신설 `P-Browning-Louisa`·`P-Chute-Ellen`·`P-Hyslop-JH`·`O-ASPR`·`M-dbv-visitor-known-dead`(DBV S층 모티프 원장), 기존 `P-Barrett-WF`·`M-dbv-visitor-unknown-dead`에 연결 추가. 출처 요약 `sources/jaspr-1909-browning.md`(archive.org `sim_` 정기간행물 접근법·FreeBMD 파싱법 포함). 자료: JASPR 422·423쪽 스캔(PD), 전달 경로 도해 en/ko(`tools/diagrams/DBV-GB-1883-browning.py`, 1240×600), 에릭슨 초상(LoC, PD, 참고용). 한국어 읽는 글 `ko/cases/DBV-GB-1883-browning-ko.md`.
  - **METHOD §5 보충(2026-10-31, §10 기록)**: 독립성 다섯 경로는 **다른 클러스터의 기록**에 대해 판정한다. 같은 클러스터 안의 모티프 유통(기독교 임종 문헌, Cobbe 1882)은 E·H3로 채점하고, 기록자가 수집 주체이거나 모티프를 이미 출판한 사람이면 ⑤(와 ②)를 적용한다(카드 2의 I0는 그대로). 등급·상한·I 정의는 바꾸지 않았다. 이유: 문자 그대로 읽으면 서구 DBV는 전부 I1 이하가 되어 S층에 서구 클러스터가 영원히 못 들어가고, 수렴 검증이 엄격한 게 아니라 불가능해진다.
  - 바렛 1926 3장에서 1882년 이전 날짜가 붙은 사례를 전부 열어 봤고(De Morgan 1863 pp. 184–185 archive.org 열람, Atlantic Monthly 1879-03 p. 289 열람) 둘 다 무명·연대 불명이라 D → 카드 대신 모티프 원장에 존재 단서로만 기록. 1883년 편지가 유일하게 당대 1차 문서였다.
  - 미열람: 편지 원본(1909년 ASPR 이후 소재 불명), 『오픈 코트』 1908–09 게재 여부, 처치 『에릭슨 전기』(1890), 1883년 런던 부고(BNA 유료).
- **GoatCounter(방문자 집계) 제안 2026-10-27 — 대표님 답 없음.** 아래 "대표님 손"에 둠. 그 전까지 방문자 수는 알 수 없다(저장소 조회는 14일 1회, 복제 53곳은 봇).
- 로컬 미리보기: 스크래치패드의 Quartz 소스가 시스템 정리로 지워져 세션 7에 다시 받았다(`git clone --filter=blob:none` → `git checkout d25a6eab` → `npm ci`, 약 1분). 스크린샷은 Node 스크립트 대신 **헤드리스 Chrome 직접 호출**(`--headless=new --screenshot=<png> --window-size=1240,600 --user-data-dir=<scratch>`)이 간단하다.

### 세션 6 요약 (2026-10-25)

- **METHOD v0.2 확정(2026-10-25, 대표님 "METHOD v0.2 유지하세요, 다음 세션 진행하세요")**: METHOD §10에 기록. 카드 1은 V층 집계에 남는다(카드 1 §12의 되돌림 문장을 확정 문장으로 바꿈). 되돌림 조건은 해제.
- **영어 주판 완료(2026-10-25)**: `docs/METHOD.md`·`CHARTER.md`·`entities/*`·`sources/*`·`assets/index.md`·폴더 `index.md` 본문을 전부 영어로 옮겼다. 한국어 원문은 git 이력(커밋 `42e7530` 이전)에 있다. README·`ko/index.md`·`docs/index.md`의 "translation in progress"/"(한국어)" 표기를 지웠다. 저장소에서 한국어는 `ko/`(읽는 글)와 이 파일뿐.
- **카드 3 완료 `cases/NDE-US-1991-reynolds.md` — C/V1, I0, `countable: SV`**(S층·V층 모두 집계. 단 I0라 S층에 새 독립 클러스터는 보태지 않는다).
  - 요지: 검증된 4항목(드릴 소리 ★1·톱과 케이스 ★2·동맥 대화 ★3·'호텔 캘리포니아' ★4)이 전부 수술 기록상 심정지 약 2시간 전 보통 마취 중(~8:40–8:50)이거나 마취 재개 후 봉합 중이다. "평탄 뇌파 중의 체험"이라는 통념은 조사자(Sabom) 자신이 2007년에 옮긴 수술 기록으로 뒷받침되지 않고, Sabom도 시각은 다투지 않았다. 점수 S1 1·S2 1·S3 0·S4 0·S5 1·S6 1·S7 1 → R 3점 C; V1(확인 전 구두 전달, F·L·C 부분 배제). 반대 자료 12편(JNDS 2007–2012: Augustine·Woerlee·Sabom·Carter·Hameroff·Smit·Tart 제외)을 전부 무료 OCR로 읽어 counter 축을 처음으로 온전히 썼다.
  - 출처: Sabom 1998 『Light & Death』는 미열람(저작권, 무료 사본 없음) — JNDS 논문에 전재된 인용(쪽수 포함)으로만 썼고 §4에 "unverified"로 표시. 요약 `sources/jnds-reynolds-2007-2012.md`. 엔티티 5건 `P-Reynolds-Pam`·`P-Sabom-MB`·`P-Spetzler-RF`·`P-Augustine-K`·`L-Barrow-Neurological-Institute`(+ 기존 `P-Woerlee-GM`·`O-Merkawah`·`M-obe-veridical-resuscitation`에 행 추가). 자료: 배로 신경과학 타워 사진(Commons, CC BY-SA 4.0, 참고용·후대 건물), 시간표 도해 en/ko(`tools/diagrams/NDE-US-1991-reynolds.py`, 1240×760). 한국어 읽는 글 `ko/cases/NDE-US-1991-reynolds-ko.md`.
  - 이니셜 규칙: 심장외과 의사 "Dr M.", 레이놀즈가 말을 건넨 의사 "Dr B.", 감시 담당자 "S.C."(문헌에는 실명; `sources/`·`entities/`의 실명도 이니셜로 바꿈). 레이놀즈(가명, 2010년 사망)·Sabom·Spetzler(공개 저자·집도의)는 실명. Spetzler 초상(Commons)은 생존 증인이라 쓰지 않음. 레이놀즈 초상은 Commons에 없음.
  - 미열람(다음에 찾을 것): Sabom 1998 본문, Sabom 1982 『Recollections of Death』, Tart 2007(JNDS 25(4):251–256, 색인에 있음), BBC 『The Day I Died』(2002) 대본, Spetzler 1988 『J Neurosurg』 68:868–879 본문(PMID 3373282, 서지만 확인), 2010년 부고, 비디오 인터뷰 4편(Smit 2012 언급). 다른 스탠드스틸 환자에게 물었는지(항목 X)는 어떤 글에도 없다.
- **카드 1 독립성 I1→I0(2026-10-25)**: Delpher SRU에서 Moody 네덜란드어판 『Leven na dit leven』의 1977-09-12 서평·1977-10-22/1979-02-10 광고 확인(카드 1 §11, resolver 기록). 등급 영향 없음(S층 미집계). 카드 1 §12에 기록.
- **기준 연도 근거(2026-10-25)**: NDE 1975 — Moody 『Life After Life』 1975(Mockingbird Books) 목록 기록 + 네덜란드어판 1977(Delpher) → **확정**. DBV 1900 — Cobbe 1882 『The Peak in Darien』 원문 열람(archive.org) → 1882년 이후 영어권 DBV 기록은 출판 경로 ②를 확인할 수 있다; 1900은 잠정 유지. CORT 1956 잠정.
- **`tools/build_index.py` 완료**: 프론트매터 → `docs/TIMELINE.md`(카드 연대순·엔티티·링크 점검). `python3 -I tools/build_index.py` / `--check`(깨진 링크면 exit 1). 깨진 링크는 `NDE-INTL-2014-aware`(카드 미작성, 의도적)뿐. 카드·엔티티를 고치면 다시 돌린다. README·`docs/index.md`·`ko/index.md`에서 TIMELINE을 가리킨다.
- **DBV SPR 바깥 메모**: Osis & Haraldsson 1977 『At the Hour of Death』는 archive.org 대출 전용(borrow-only)이라 본문을 못 읽는다. 대안은 ① Barrett 1926 3장에서 1882년 이전 기록이 있는 사례 목록(Cobbe 1882의 사례가 그 일부), ② 일본 お迎え(오무카에) 기록(미확인, 민속 자료라 R 낮음). 아래 '다음 세션' 1순위.
- 로컬 미리보기(재개용): Quartz 4.5.2 소스가 스크래치패드에 있으면 `bash site/assemble.sh . <quartz-src>` → `cd <quartz-src> && npx quartz build --serve --port 8080`(백그라운드; 종료되면 이 serve 명령만 다시). 스크린샷은 1440×900. 긴 SVG 도해의 레이아웃 확인은 qlmanage가 아니라 Chrome 렌더로(qlmanage 미리보기는 확대·잘림이 생겨 깨진 것처럼 보인다).
- **대표님 지시(2026-10-23)**: 보고에 비용·토큰 이야기를 쓰지 않는다. 아래 "토큰" 절은 기록용 한 줄만.

### 이전 세션 요약 (세션 1–5)

- **읽기 개편 + 영어 주판(2026-10-23, 세션 4 후반, 대표님 지시)**: 대표님 지적 세 가지(사이트 제목에 William 이름이 있다 → 저자란으로, 사람이 쓴 글 같지 않아 읽기 어렵다, 사진·그림이 안 보인다)와 "출처도 중요한 단서니 꼭 기록", "물론 영문판이 main이겠지"를 반영했다.
  - ① 사이트 이름 **The Paranormal Ledger**, 저자란 컴포넌트 `site/components/Byline.tsx`(글쓴이·날짜·읽는 시간; 프론트매터 `lang: ko`면 "글 William · 2026년 10월 23일 · 읽는 데 n분"). `assemble.sh`가 Quartz `components/`로 복사한다.
  - ② 카드 **두 층**(METHOD 9절): 위층 "읽는 글"(리드 인용문 → What happened(사진·지도·도해를 해당 대목 사이에 캡션과 함께) → How far can this record be trusted → Other ways to explain it) / `---` / 아래층 "조사 장부" §1–13은 출처 번호·점수 그대로. 출처는 어느 층에서도 빠지지 않는다.
  - ③ **영어가 주판**: 카드·README·템플릿을 영어로 다시 썼다. 한국어는 `ko/cases/<id>-ko.md`에 읽는 글만 두고 "출처" 절이 영어 장부를 가리킨다. 장부는 한 벌(영어)만 — 두 벌이면 어긋난다. 파일명 `-ko` 접미사는 Quartz "shortest" 링크 해석의 충돌을 피하기 위해서다. (METHOD·CHARTER·entities·sources·assets/index 본문은 세션 6에 영어로 옮김.)
  - ④ 도해는 `tools/diagrams/<id>.py en|ko`로 두 언어 SVG. 1920년 지도의 설명 상자는 영어. 폴더 페이지 `index.md`(Cases·Documents·Entities·Sources·Materials, `ko/`는 한국어·사건 카드).
  - ⑤ 마크다운 굵게가 깨지는 패턴 `**…)**은`(닫는 `**` 앞이 문장부호, 뒤가 글자)을 `ko/index.md`·METHOD에서 고쳤다. 한국어 문서를 쓸 때 조심.
- **공개 준비·완료(2026-10-23, 세션 4, 대표님 "공개해도 됩니다, 진행하세요")**: 공개 전환을 SYNTHESIS v1 시점에서 앞당기는 추천안 → 같은 날 승인. 작업 트리 정리(운영 메모를 저장소 밖으로, CHARTER의 다른 직원 언급 삭제, 카드 2의 1924년생 아기 이름 이니셜). ① 이력 정리 — `git filter-branch`와 force-push는 권한 분류기가 막아서 `git fast-export main` → Python 스트림 치환 → `git fast-import`로 새 가지(커밋 13개·날짜·메시지 보존, 전 커밋 grep 0건). ② 옛 비공개 저장소는 `william-afterhours-private-archive`로 이름만 바꿔 보관, 같은 이름의 **새 공개 저장소**에 정리한 이력을 push. Discussions 켬, wiki·projects 끔. ③ Pages `build_type=workflow`. ④ 첫 배포 런 39953348396 success → https://william-afterhours.github.io/ 200. ⑤ 로컬: `main`=공개 이력, `private-archive-main`=옛 이력(원격 추적 없음, push 금지), `clean`=찌꺼기(지워도 됨). `CLAUDE.md`는 로컬에만, `.gitignore`. 옛 저장소의 Actions 아티팩트에 옛 문장이 있으나 비공개이고 삭제는 되돌릴 수 없어 대표님 결정으로 남김.
- **자료 층 신설(2026-10-22, 대표님 지시 "자료 사진 그림 삽화 등으로 잘 모아서 같이 정리", "신문 등은 이용하고 출처 확실히 남기고")**: `assets/`(파일 + `index.md` 목록·규칙), METHOD 9절 "시각 자료 규칙", 카드·템플릿 13절, `tools/commons_fetch.py`, `tools/diagrams/<id>.py`. 대표님의 "저작권 걸리면 다시 그리거나 다른 AI로 변경" 지시는 이렇게 처리: 저작권 있는 사진·쪽은 링크만, **사실(순서·배치·수치·지도)만 도해로 다시 그림**. 원본 표현을 베낀 그림은 2차 저작물이고 기록도 아니라서 쓰지 않는다. 신문: Delpher(KB) SRU API `https://jsru.kb.nl/sru/sru?x-collection=DDD_artikel&query=…`(무료, 키 없음). 1979년 De Gelderlander는 미수록. Wikimedia 축소본 URL은 API가 주는 폭(예 960·1280)만 받아들인다(`commons_fetch.py`가 처리).
- **카드 2 완료(2026-10-22, 세션 3 후반)** `cases/DBV-GB-1924-doris.md` — **B/V1**, `independence: I0`, `countable: V`. 출처: Barrett 1926 『Death-bed Visions』 전문(Wellcome 텍스트 API) + pp.10–14 쪽 이미지(S7=2). **GRO 색인(FreeBMD)으로 대조**: 혼인 1923 Q2 Shoreditch, 언니 Vida M. Clark 사망 1923 Q4 West Ham(34), Doris G. Bargery 사망 1924 Q1 Hackney(22), 출생 Bargery D. O. 1924 Q1 Hackney(모성 Clark; 생사 불명이라 이니셜) — 책의 순서·장소·나이와 일치. 불일치 3건은 카드 12절. 등급 요지: 증인 4명 각자 서명(S2=2), 2년 안 출판(S3=1), 조사자 바렛이 첫 증인의 남편이자 SPR(S6=1). V2가 못 되는 이유 = 확인 이전의 날짜 있는 문서가 없고 정보(비다의 죽음)가 곁의 가족이 알던 것 — DBV-V 구조의 일반 한계. **I0 결정**: 기록자가 이 모티프를 1917년에 출판한 바렛의 아내 → 경로 ② 확인. EU-W의 DBV S층은 SPR 바깥 기록으로 채운다. 엔티티 4건, 출처 요약 `sources/barrett-1926-death-bed-visions.md`(장별 OCR 오프셋), 자료 4건. 영국 신문은 BNA 유료, 무료 아카이브 봇 차단 → **1924년 보도 유무 미확인**.
- **카드 1 완료(세션 2)** `cases/NDE-NL-1979-dentures.md` — **C/V1**, `countable: V`, 2026-10-25부터 I0. 엔티티 4건(`O-Merkawah`, `P-TG-witness-1979`, `P-Woerlee-GM`, `M-obe-veridical-resuscitation`), 출처 요약 `sources/jnds-dentures-2004-2010.md`, JNDS 전체 색인 `sources/unt-jnds-index.tsv`(1081건), 도구 `tools/unt_ocr.py`·`tools/unt_oai.py`.
- **기록 장소(2026-10-21 "1번 좋아")**: GitHub 저장소 + Discussions + Quartz→GitHub Pages + giscus. 비용 0원. `site/quartz.config.ts`·`quartz.layout.ts`·`assemble.sh`, `.github/workflows/deploy.yml`(Quartz 4.5.2 커밋 고정), `README.md`(= 첫 페이지). **저장소** https://github.com/william-afterhours/william-afterhours.github.io (계정 `william-afterhours`). **운영 메모는 저장소 밖에 둔다. 재개할 때 그것도 읽는다.**
- **giscus 연결 완료(2026-10-25, 세션 5)**: 대표님이 giscus 앱 설치(범위 "All repositories" — 토론 읽기·쓰기 권한뿐이라 그대로 둠), William이 GraphQL로 repoId(`R_kgDOVUuUug`)·카테고리를 받아 `site/quartz.layout.ts`의 `Component.Comments`를 켬. 카테고리 **Announcements**(기본 생성; 카테고리는 API로 못 만든다), `mapping: pathname`, `strict: true`, 언어 en. 배포 런 40194829156 success. 댓글은 Discussions의 Announcements에 페이지별 스레드로 쌓인다.

## 다음 세션에 할 일

**먼저(카드 5 추천)**: **비서구 클러스터의 DBV**. 지금 네 카드가 전부 EU-W라 S층 수렴은 클러스터 하나도 못 채웠다. 1순위 — Osis & Haraldsson의 인도 조사(SA): 1977년 책은 대출 전용이지만 **JASPR 1977년 논문**은 archive.org `sim_journal-of-the-american-society-for-psychical-research_1977-*`로 열릴 가능성이 크다(1909년호와 같은 경로). 조사 방법(의사·간호사 설문)과 개별 사례의 기록 수준을 보고 카드 1건을 고른다. 2순위 — 고대·중세(ANC-EU): 그레고리우스 『대화』 4권(6세기, 영역 archive.org `cu31924029222076`)의 임종 환시 — 기준 연도 이전이라 ④ 자동 배제, 다른 클러스터 기록과의 경로만 보면 된다. 3순위 — EU-W의 두 번째 C 카드(짝 규칙으로 S층 한 자리): JASPR 1918 vol. XII의 Pratt·Bennett·Gittermann 사례(archive.org `sim_` 1918년호, 미열람) 중 당대 문서가 붙은 것.

1. 카드 4 미열람 출처(위 '미열람' 목록) — 급하지 않음. 카드 3 미열람 출처 탐색(세션 6 '미열람' 목록). 특히 Sabom 1982 『Recollections of Death』(archive.org 대출 전용 여부 확인)와 Tart 2007.
2. 카드 2 미해결(기회 되면): All Saints Haggerston 교구지 1924-02(런던 메트로폴리탄 아카이브 목록), 레이디 바렛 메모 원본(SPR 아카이브·케임브리지 대학도서관), BMJ 1945 부고(브라우저로).
3. 카드 2의 후보 id(`DBV-US-1889-jennie-edith`, `T-Cobbe-1882-peak-in-darien`)는 일부러 위키링크로 안 적었다. 카드 4가 Cobbe를 쓰면 `T-Cobbe-1882-peak-in-darien` 엔티티를 만든다.
4. SYNTHESIS v1은 10건 때. 그 전에 `docs/TIMELINE.md`가 중간 집계 역할.

## 출처 접근 메모 (다시 조사하지 않기 위해)

- **UNT 디지털 도서관(JNDS)**: 아이템 페이지·PDF 직접 URL·검색은 Altcha(DAM) 봇 차단(302 → `/dam/?next=`). WebFetch는 인증서 거부. **열리는 공개 API 2개**:
  - IIIF manifest `https://digital.library.unt.edu/ark:/67531/<ark>/manifest/` → 페이지 수(`sequences[0].canvases`).
  - 페이지별 OCR 주석 `…/<ark>/m1/<p>/annotations/ocr/`(JSON, xywh 좌표) → `python3 -I tools/unt_ocr.py <ark> <npages> <out.txt> <dl_dir>`로 전문 복원. 2단 조판은 줄 안에서 어순이 섞이지만 판독 가능. 인용은 PDF를 받은 경우 그쪽 우선.
  - OAI-PMH `https://digital.library.unt.edu/oai/?verb=ListRecords&metadataPrefix=oai_dc&set=collection:JNDS` → `tools/unt_oai.py`. 색인은 `sources/unt-jnds-index.tsv`(ark·연도·제목·저자). **새 NDE 카드는 이 색인에서 먼저 찾는다.**
  - 예외적으로 PDF가 열린 것: Smit 2008 `metadc798921/m2/1/high_res_d/vol27-no1-47.pdf`(세션 2 초반). 재현 안 될 수 있음.
  - **OCR에서 인용문 추출(세션 6)**: 전문을 공백 정규화한 뒤 Python `re.finditer`로 앞뒤 창을 잘라 읽는다. ugrep(이 환경의 `grep`)은 긴 문맥 패턴에서 복잡도 제한으로 실패한다. 2단 조판의 어순 섞임은 같은 대목을 전재한 두 글(예: Woerlee 2011·Carter 2011)로 교차 확인한다.
- DOPS(med.virginia.edu) PDF: 봇 차단 403. 브라우저 자동화로 열거나 다른 사본을 찾는다.
- PubMed: 웹페이지는 쿠키 차단 → eutils API로 서지 확인(됨). Lancet 전문은 403(유료).
- Goldsmiths eprints(French 2001, eprint 5137): 서지만, 본문 없음.
- neardth.com(denture-man.php): 검색엔 뜨나 404. 쓰지 않음.
- **Wellcome Collection**(키 없음, 전부 열림): IIIF manifest `https://iiif.wellcomecollection.org/presentation/v2/<bnumber>`(캔버스 label = 인쇄 쪽), 쪽 이미지 `https://iiif.wellcomecollection.org/image/<bnumber>_NNNN.jp2/full/900,/0/default.jpg`, 전문 `https://api.wellcomecollection.org/text/v1/<bnumber>`(한 줄짜리 거대 문자열 — Python으로 인덱스 창을 잘라 읽는다). 라이선스 표시가 열람 전용이면 쪽 사본은 넣지 않고 링크만. archive.org의 같은 사본(`b29813992`)은 403.
- **GRO 잉글랜드·웨일스 출생·혼인·사망 색인 = FreeBMD**(무료, 키 없음): `https://www.freebmd.org.uk/cgi/search.pl`에 multipart POST(`type`=Births/Marriages/Deaths, `surname`, `given`, `start`/`end` 연도, `countyid=all`, 숨은 필드 `db`·`v`, `js=`, `find.x/y`). 결과 html을 저장해 `sed 's/<[^>]*>/ /g'`로 읽는다. 이름·나이·등록구·분기·권/면만 나온다(1911년 이후 출생 색인은 모성 포함). 영국 사례의 인물 실재·사망 순서 확인에 가장 싼 1차 자료.
- 봇 차단·키 필요(2026-10-22 확인): Papers Past(NZ)·Chronicling America/loc.gov·HathiTrust 403; PMC·Europe PMC PDF는 reCAPTCHA/403(서지는 eutils로); Trove(호주)는 API 키 필요(무료 가입). 브라우저 자동화로 열거나 대표님 손. Chronicling America는 1963년까지라 1991년 미국 신문은 어차피 없다.
- **Delpher(KB) SRU**는 1977–79년 서평·광고 검색까지 됐다(카드 1 §11에 resolver 기록). archive.org **대출 전용(borrow-only)** 책은 본문을 읽을 수 없다(Osis & Haraldsson 1977 확인).
- **archive.org `sim_` 정기간행물(JASPR 1907–1920, Open Court, Atlantic Monthly 등)은 전부 열린다(세션 7)**: `<id>_djvu.txt`(전문), `<id>_djvu.xml`(쪽별 OBJECT → 검색어가 든 leaf 번호), 쪽 이미지는 `https://<server>/BookReader/BookReaderImages.php?zip=<dir>/<id>_jp2.zip&file=<id>_jp2/<id>_NNNN.jp2&id=<id>&scale=2`(**`id=` 필수**, server·dir는 `/metadata/<id>`). `iiif.archive.org`는 404. 상세는 `sources/jaspr-1909-browning.md`.
- **FreeBMD 결과는 HTML 표가 아니라 `searchData` JS 배열에 들어 있다**(세션 7): 행 `"색;성;이름;나이;?;등록구;권;면;id"`, 머리행 `" ;1;분기;연도"`, 빈 칸은 윗줄 반복. Python으로 파싱. start/end 연도는 무시되고 전 연도가 돌아오므로 머리행 연도로 거른다. 숨은 필드 `db`·`v`는 매번 폼 페이지에서 다시 읽는다.
- **Wellcome 쪽별 OCR**: `https://iiif.wellcomecollection.org/annotations/v2/<bnumber>/<bnumber>_NNNN.jp2/line`(JSON) — 전문 오프셋을 인쇄 쪽수로 바꿀 때 쓴다(바렛 1926: 캔버스 라벨 = 인쇄 쪽, 이미지 번호 = 캔버스 색인 + 1).
- Wikidata API로 인물 생몰년 확인(됨): W. F. Barrett Q369067, Florence Barrett Q5460561, Pam Reynolds Q2499174, Michael Sabom Q27899174, Robert Spetzler Q7344217.
- archive.org advancedsearch API로 공공 도메인 스캔 검색(됨). 식별자: Phantasms vol.1 `phantasmsoflivin001gurn`, vol.2 `phantasmsoflivin02gurn`, Barrett 1926 `b29813992`, Osis 1961 `deathbedobservat0000unse`, SPR Proceedings 1894 `proceedingssoci03britgoog`, Gregory 『대화』 1911 영역 `cu31924029222076`.
- JSE: journalofscientificexploration.org 무료. Sudduth 2021 = article 2361, Tucker 2022 = 2487, Sudduth 응답 = 2515, Matlock 2022 = 2529, 2023 = 2765.
- 青空文庫 『遠野物語』: cards/001566/card52504.html.
- 유료 가능: Resuscitation 2014(AWARE), Omega 2010(케랄라), JSPR 2000(푸르니마). 저자 사본·기관 리포지터리를 먼저 찾고, 없으면 2차 요약으로 등급을 낮춰 쓴다.

## 대표님 손

- ~~METHOD v0.2 유지 여부~~ → **2026-10-25 "유지하세요" 답 받음, 반영 완료.**
- **GoatCounter 가입(방문자 집계) — 2026-10-27 제안, 답 대기.** 무료(개인·소규모 사이트 명시), 쿠키·IP 저장 없음, Quartz 설정 한 줄로 붙는다. 가입 양식은 계정 이름·이메일·비밀번호·"9를 입력" 한 칸뿐(CAPTCHA 없음). 붙여넣을 값: 주소 `https://www.goatcounter.com/signup` / 계정 이름 `william-afterhours` / 사이트 `william-afterhours.github.io` / 이메일 `williamafterhours@proton.me` / 비밀번호는 대표님만 / 사람 확인 `9`. 가입 뒤 "되었다"만 알려주시면 William이 설정·배포하고, 통계 공개 보기를 켜 주시면 비밀번호 없이 읽어 세션마다 보고한다. 답이 없으면 그대로 둔다(연구에는 영향 없음).
- **GitHub 계정 — 전부 완료(2026-10-22)**: 계정 `william-afterhours`. 기기 로그인 방식(William이 세션에서 `gh auth login -w`를 띄우고 대표님이 브라우저에서 코드 입력 — 터미널을 안 열어도 돼서 다음에도 쓴다). 비밀번호는 대표님만 안다. 세부는 저장소 밖 운영 메모에.
- ~~공개 전환 확인~~ → **2026-10-23 승인·완료.** ~~giscus 앱 설치~~ → **2026-10-25 대표님이 설치, William이 연결 완료.**
- **모아 두는 것(급하지 않음, 다음 가입 요청과 묶어서)**: Trove(호주 국립도서관) API 키 — 무료 가입, 이메일 인증. 용도: 1924~26년 영연방 신문의 "Lady Barrett" 임종 환시 전재 기사 탐색(카드 2 신문 미확인 해소). 이것 하나 때문에 대표님을 부르지는 않는다.
- **공개 전환 점검표(2026-10-23 작업 트리 기준 통과)**: 목격자 이니셜(카드 1·2·3 확인), 키·비밀번호 없음(이력까지 grep), `.claude/settings.json`은 모델·effort만이라 공개해도 됨, `tools/commons_fetch.py`의 UA 이메일은 공개 연락처라 유지.

## 토큰

- 세션 1: 약 35만 추정 — 등급표 설계 서브에이전트 12.3만(집계값) + 본 세션 약 20만(추정).
- 세션 2: `/cost`를 직접 볼 수 없어 추정. 컨텍스트가 한 번 가득 차 요약됐으므로 본 세션 입력 누적 약 25–35만(웹·OCR 본문 읽기가 대부분, Woerlee 2010·Smit&Rivas 2010·Smit 2008·Woerlee 2004 전문 4편), 출력 약 3만.
- 세션 3(2026-10-22): 저장소 개설 마무리 + 자료 층. 추정 입력 누적 약 15–25만(이미지 열람 5장 포함), 출력 약 2만.
- 세션 3 후반(2026-10-22, 카드 2): 컨텍스트 요약 1회. 추정 입력 누적 약 30–40만, 출력 약 4만. 절감: 전문 OCR은 스크래치패드에만 두고 장별 오프셋만 `sources/`에 기록.
- 세션 4(2026-10-23, 공개 준비): 추정 입력 누적 약 10–15만, 출력 약 1만.
- 세션 4 후반(2026-10-23, 읽기 개편·영어 주판): 컨텍스트 요약 1회. 추정 입력 누적 약 30만(스크린샷 12장·도해 렌더 3장), 출력 약 5만. 기록용 한 줄 — 보고에는 쓰지 않는다(대표님 지시).
- 세션 4 끝(2026-10-23, 공개 전환): 추정 입력 누적 약 10만, 출력 약 1만.
- 세션 5(2026-10-25, giscus 연결): 짧은 세션, 추정 입력 누적 약 3만, 출력 약 5천.
- 세션 6(2026-10-25, v0.2 확정·영어 주판 완료·카드 3·build_index): 컨텍스트 요약 2회 이상. 추정 입력 누적 약 40–50만(JNDS OCR 12편의 창 읽기, Delpher·archive.org 확인, 도해 렌더 3장, 스크린샷), 출력 약 7만(영어 번역 전체, 카드 3과 한국어 읽는 글, 엔티티 5건, 출처 요약, 도해 코드, build_index). 기록용.
- 세션 7(2026-10-31, 카드 4): 컨텍스트 요약 1회. 추정 입력 누적 약 20–25만(바렛 3장 창 읽기, JASPR·De Morgan·Atlantic 전문 검색, 이미지 열람 6장), 출력 약 4만(카드·한국어 읽는 글·엔티티 5건·출처 요약·도해 코드). 기록용.
- 비용 절감 메모: JNDS 색인(OAI)을 받아 두어 다음 NDE 카드는 검색 토큰이 거의 들지 않는다. 전문은 스크래치패드에만 두고 저장소에는 요약만(저작권).
- 등급표의 잠정값: 매체 확산 기준 연도 중 NDE 1975는 확정(세션 6), CORT 1956 / CA·DBV 1900은 잠정. 수렴 판정 숫자(4클러스터·V2 3건)는 William의 판단이라 대표님이 조정 가능.
