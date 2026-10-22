# 출처 요약 — Barrett 1926 『Death-bed Visions』 (다시 읽지 않기 위해)

전문 OCR(약 177k자)은 세션 스크래치패드에만 두었고 저장소에는 넣지 않는다(Wellcome 메타데이터가 저작권 표시). 사실은 전부 `cases/DBV-GB-1924-doris.md`에 출처 번호로 옮겼다. 여기는 접근 방법과 책의 구조, 카드에 안 쓴 세부만.

## 접근 (2026-10-22 확인)

- **Wellcome Collection, b29813992** — 키 없이 전부 열린다.
  - IIIF manifest `https://iiif.wellcomecollection.org/presentation/v2/b29813992` — 캔버스 144장, 캔버스 `label`이 인쇄 쪽 번호. 이미지 번호 = 캔버스 순번 + 1(인쇄 p.10 = `_0026`).
  - 쪽 이미지 `https://iiif.wellcomecollection.org/image/b29813992_NNNN.jp2/full/900,/0/default.jpg` (폭 900 동작).
  - 전문 텍스트 `https://api.wellcomecollection.org/text/v1/b29813992` — 한 줄짜리 거대 문자열. `grep -n`은 쓰지 말고 Python으로 인덱스 창을 잘라 읽는다.
  - 메타데이터 라이선스 표시가 열람 전용(저자 1925년 사망으로 본문은 퍼블릭 도메인이지만 스캔은 Wellcome 표시를 따라 링크만).
- archive.org `b29813992`(printdisabled 컬렉션)는 파일 내려받기 403. 다른 사본은 대출 전용.

## 책의 구조 (OCR 오프셋 기준)

| 장 | 제목(원문) | OCR 시작 오프셋 | 카드 후보 |
|---|---|---|---|
| I | Introduction | 6,044 | Sidgwick 인용("단일 사건으로는 유령 가설을 택할 수 없다") — METHOD의 정신과 같음 |
| II | Visions seen by the dying of persons by them unknown to be dead | 16,626 | **DBV-V 창고.** 첫 사례 도리스(pp.10–14) → Jennie & Edith 1889 미국(pp.14–16, Savage→Hyslop) → 이하 미열람 |
| III | Visions seen by the dying of persons known by them to be dead, and deathbed visions … | 38,885 | DBV(S층) 후보 다수. 미열람 |
| IV | Visions seen by the dying of living persons at a distance — in some cases reciprocal | 112,510 | CA와 DBV 경계 사례. 미열람 |
| V | Music heard at the time of death by the dying or by persons present at a death | 132,592 | 범위 밖(구조 미정의) |
| VI | Visions of the spirit of a dying person leaving the body | 143,262 | 범위 밖 |

## 카드에 안 쓴 세부

- 바렛은 2장 서두에서 "리셰(Richet)도 이 증거는 크립테스테지아(cryptesthesia)로 설명 불가능하다고 본다"고 쓴다 — 리셰의 원문은 미확인.
- 2장 Jennie & Edith(1889년 6월, 미국 "이웃 도시", 디프테리아): 부모와 의사가 Jennie의 죽음을 Edith에게 숨겼고, Edith는 죽기 직전 Jennie에게 보낼 사진 두 장을 골랐다(몰랐다는 증거). 바렛은 Hyslop의 책에서 전재하고 Savage가 "이름과 주소를 Hyslop에게 주었다"고 적는다. 카드화하려면 Hyslop 원문(책 제목 미확인)과 Savage의 원 기록이 필요.
- 하이슬롭 각주: 컬럼비아대 윤리·논리 교수, 처음엔 회의론자, ASPR 재무·총무·연구원으로 과로사(1920).

## 다음에 열 것

- 3장 사례 목록을 뽑아 DBV S층 후보(1882년 이전 기록이 있는 것)를 고른다. OCR 오프셋 38,885–112,510.
- 1917년 『On the Threshold of the Unseen』의 임종 환시 장 — archive.org 공공 도메인 사본 탐색.
