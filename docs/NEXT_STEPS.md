# NEXT_STEPS — 재개할 때 이것부터

## 현재 상태 (2026-10-22, 세션 3)

- **자료 층 신설(2026-10-22, 대표님 지시 "자료 사진 그림 삽화 등으로 잘 모아서 같이 정리", "신문 등은 이용하고 출처 확실히 남기고")**: `assets/`(파일 + `index.md` 목록·규칙), METHOD 9절 "시각 자료 규칙"(13절 "자료" 칸 추가), 카드·템플릿 13절, `tools/commons_fetch.py`(Commons 라이선스 확인·받기), `tools/diagrams/<id>.py`(도해 생성). 카드 1에 4건 적용(병원 1960 사진 CC BY-SA, 오이 범람원 참고 CC0, 크래시 카트 참고 CC0, 사건 순서 도해 SVG). 로컬 Quartz 빌드로 이미지·자료 페이지 확인됨.
  - 대표님의 "저작권 걸리면 다시 그리거나 다른 AI로 변경" 지시는 이렇게 처리: 저작권 있는 사진·쪽은 링크만, **사실(순서·배치·수치·지도)만 도해로 다시 그림**. 원본 표현을 베낀 그림은 2차 저작물이고 기록도 아니라서 쓰지 않는다(`assets/index.md`에 적음).
  - 신문: Delpher(KB) SRU API `https://jsru.kb.nl/sru/sru?x-collection=DDD_artikel&query=…`가 열린다(무료, 키 없음). 1979년 지역지 De Gelderlander는 미수록. 다음 카드부터 사건 직후 신문을 먼저 찾는다(Chronicling America·Trove·Papers Past·Delpher는 전부 무료·PD).
  - Wikimedia 축소본 URL은 API가 주는 폭(예 960·1280)만 받아들인다(임의 폭은 400). `commons_fetch.py`가 처리.
- **단계**: 조사 진행 중. 카드 1 `cases/NDE-NL-1979-dentures.md` 완료(**C/V1**, `countable: V`). 엔티티 4건(`O-Merkawah`, `P-TG-witness-1979`, `P-Woerlee-GM`, `M-obe-veridical-resuscitation`), 출처 요약 `sources/jnds-dentures-2004-2010.md`, JNDS 전체 색인 `sources/unt-jnds-index.tsv`(1081건), 도구 `tools/unt_ocr.py`·`tools/unt_oai.py`.
- **METHOD v0.2**(이번 세션, 내 결정, 대표님께 보고·거부 가능): NDE "요소 2개 이상"은 S층 집계에만. V층 입장 = 생명 위기 + 체외 시점 + V요소. `countable: no/S/V/SV`. 거부되면 v0.1로 되돌리고 카드 1은 "유사 사례"로 둔다(10절에 기록).
- **기록 장소 확정(2026-10-21 "1번 좋아")**: GitHub 저장소(이 저장소 그대로) + Discussions(토론) + Quartz로 GitHub Pages(읽기용 사이트, 위키링크·백링크·그래프·검색) + giscus(페이지 댓글을 Discussions로 모음). 비용 0원. 지금은 **비공개**로 올리고 **공개 전환은 SYNTHESIS v1(10건) 시점에 대표님 확인**(되돌릴 수 없는 공개 발언). 무료 계정의 Pages·giscus는 공개 저장소에서만 되므로 사이트는 공개 전환 때 켜진다.
  - 준비 완료: `site/quartz.config.ts`·`quartz.layout.ts`·`assemble.sh`, `.github/workflows/deploy.yml`(Quartz 4.5.2 커밋 고정, 비공개 동안 deploy 단계 생략), `README.md`(= 사이트 첫 페이지), `.gitignore`. **로컬 빌드 확인함**(Node 26, 10개 문서 → 41 파일, 위키링크·백링크 정상).
  - **저장소 개설 완료(2026-10-22)**: https://github.com/william-afterhours/william-afterhours.github.io (비공개, Discussions 켜짐, main 추적). 계정 `william-afterhours`, 이메일 `williamafterhours@proton.me`. 커밋 이메일은 GitHub noreply 주소(로컬 git config).
  - 첫 push의 Actions `Deploy site`(build만) 런 39784436279 **success** 확인(2026-10-22). 비공개라 deploy 단계는 건너뜀.
  - 공개 전환 때 할 것: Settings → Pages → Source "GitHub Actions"(API: `gh api -X POST repos/…/pages -f build_type=workflow`) → giscus 앱 설치(https://github.com/apps/giscus) → giscus.app에서 repoId·categoryId 받아 `site/quartz.layout.ts` 주석 해제 → push → 사이트 확인.

## 다음 세션에 할 일

1. 대표님 답을 반영: METHOD v0.2 유지/복귀(기록 장소는 확정·개설 완료).
2. 카드 2 `DBV-GB-1924-doris`(archive.org `b29813992`, Barrett 1926). 엔티티 Barrett, 모티프 "잘못 데려감"은 그때. **자료**: Barrett 1926은 PD → 해당 쪽 스캔(기록 사본 ①), Barrett 부부 초상(Commons, 사망 확인), Mothers' Hospital Clapton 사진, 1924년 신문(영국지는 유료 BNA라 Trove·Papers Past의 전재 기사로).
3. 카드 3 후보: `NDE-INTL-2014-aware`(V층 대조군; Resuscitation 2014 저자 사본 탐색) 또는 `NDE-US-1991-reynolds`(Sabom 1998; Woerlee 2011 반박 UNT metadc461684·461715).
4. `tools/build_index.py` — 프론트매터 → `docs/TIMELINE.md` + 깨진 `[[링크]]` 목록. 지금 깨진 링크: `NDE-INTL-2014-aware`(카드 미작성, 의도적).
5. 매체 기준 연도(NDE 1975) 근거 문헌: Moody 『Life After Life』 1975 초판·네덜란드어판 연도 확인(카드 1 독립성 ②·④가 '불명'인 이유).

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
- archive.org advancedsearch API로 공공 도메인 스캔 검색(됨). 식별자: Phantasms vol.1 `phantasmsoflivin001gurn`, vol.2 `phantasmsoflivin02gurn`, Barrett 1926 `b29813992`, Osis 1961 `deathbedobservat0000unse`, SPR Proceedings 1894 `proceedingssoci03britgoog`, Gregory 『대화』 1911 영역 `cu31924029222076`.
- JSE: journalofscientificexploration.org 무료. Sudduth 2021 = article 2361, Tucker 2022 = 2487, Sudduth 응답 = 2515, Matlock 2022 = 2529, 2023 = 2765.
- 青空文庫 『遠野物語』: cards/001566/card52504.html.
- 유료 가능: Resuscitation 2014(AWARE), Omega 2010(케랄라), JSPR 2000(푸르니마). 저자 사본·기관 리포지터리를 먼저 찾고, 없으면 2차 요약으로 등급을 낮춰 쓴다.

## 대표님 손

- **답 1개 남음**: METHOD v0.2(NDE V층 입장 조건) 유지 여부. 답이 없으면 유지한 채 진행하고, 거부하면 v0.1로 되돌린다.
- **GitHub 계정 — 전부 완료(2026-10-22)**: 이메일 `williamafterhours@proton.me` → GitHub `william-afterhours` 가입 → 기기 로그인(William이 세션에서 `gh auth login -w`를 띄우고 대표님이 브라우저에서 코드 입력. 이 방식이 터미널을 안 열어도 돼서 다음에도 쓴다). 비밀번호는 대표님만 안다.
- 지금 남은 대표님 손: 없음. 다음은 SYNTHESIS v1 때 공개 전환 확인.
- **공개 전환**: SYNTHESIS v1(카드 10건) 때 한 번 확인. 그때 점검표 — 목격자 이니셜, 키·비밀번호 없음, `.claude/settings.json` 노출 여부.

## 토큰

- 세션 1: 약 35만 추정 — 등급표 설계 서브에이전트 12.3만(집계값) + 본 세션 약 20만(추정).
- 세션 3(2026-10-22): 저장소 개설 마무리 + 자료 층. 추정 입력 누적 약 15–25만(이미지 열람 5장 포함), 출력 약 2만.
- 세션 2: `/cost`를 직접 볼 수 없어 추정. 컨텍스트가 한 번 가득 차 요약됐으므로 본 세션 입력 누적 약 25–35만(웹·OCR 본문 읽기가 대부분, Woerlee 2010·Smit&Rivas 2010·Smit 2008·Woerlee 2004 전문 4편), 출력 약 3만. 대표님이 `/cost`를 치면 정확한 수치가 나온다.
- 비용 절감 메모: JNDS 색인(OAI)을 받아 두어 다음 NDE 카드는 검색 토큰이 거의 들지 않는다. 전문은 스크래치패드에만 두고 저장소에는 요약만(저작권).
- 등급표의 잠정값(1회차 조사에서 확정할 것): 매체 확산 기준 연도(NDE 1975 / CORT 1956 / CA·DBV 1900)는 근거 문헌 미확인. 수렴 판정 숫자(4클러스터·V2 3건)는 William의 판단이라 대표님이 조정 가능.
