---
title: Materials (photos · scans · diagrams)
updated: 2026-10-23
---

# 자료 목록

*Every photograph, document scan, map and diagram used on the site, with its source and licence. This list is in Korean for now; an English version is in progress. File names, links and licence names are the same in any language.*

사건 카드와 항목에 붙는 사진·기록 사본·신문·삽화·도해를 모아 둔다. 규칙은 [[METHOD]] 9절 "시각 자료 규칙". 핵심만 다시 적으면:

- **사진은 이해를 돕는 것이지 증거가 아니다.** 등급(R·V·I)에 영향이 없다. 예외는 1차 문서의 스캔(기록 사본)으로, 그것은 출처의 '열람 확인' 근거가 된다.
- **공개 저장소에 올라가므로 퍼블릭 도메인·CC0·CC BY·CC BY-SA·정부 저작물만.** 저작권이 있는 논문·책·사진은 넣지 않고 링크한다. 저작권 있는 그림을 "다시 그려서" 넣지도 않는다 — 표현을 베끼면 여전히 2차 저작물이고, 무엇보다 그렇게 만든 그림은 기록이 아니라 지어낸 그림이다. 대신 **사실**(순서·배치·수치·지도)은 도해로 다시 그린다. 그것은 합법이고 이 연구에 쓸모가 있다.
- **모든 자료는 열어서 보고 넣는다.** 캡션은 사진이 실제로 보여주는 것만. 사건 장소·당사자가 아닌 것은 "참고".
- **신문**은 가장 좋은 기록 사본이다(사건 직후 기록). 아카이브·신문명·날짜·면·기사 URL을 다 적는다. 찾았으나 없으면 그것도 카드 13절에 적는다.
- 쓰지 않는 것: 생성형 이미지, 재연 사진, 출처 불명 이미지, 살아 있거나 생사 불명인 목격자·당사자의 얼굴.
- 파일명 `<카드 또는 항목 id>--<slug>.<ext>`, 긴 변 1600px 이하·400KB 이하.

도구: `tools/commons_fetch.py`(Wikimedia Commons에서 라이선스 확인·메타데이터·축소본 받기), `tools/diagrams/<id>.py`(도해 생성 코드, SVG 출력).

## 목록

| 파일 | 카드·항목 | 종류 | 무엇 | 출처 | 저자·연도 | 라이선스 | 열람·확인 |
|---|---|---|---|---|---|---|---|
| `NDE-NL-1979-dentures--canisius-hospital-1960.jpg` | [[NDE-NL-1979-dentures]] | ② 장소 | 네이메헌 성 카니시우스 병원 본관과 정문. 1926~1992년 St. Annastraat에 있던 건물로, 1979년 소생이 이뤄진 병원(건물 이력은 nl.wikipedia "Canisius-Wilhelmina Ziekenhuis") | [Commons](https://commons.wikimedia.org/wiki/File:Het_hoofdgebouw_met_hoofdingang_van_het_St._Canisius_Ziekenhuis_F12159.jpeg) · Regionaal Archief Nijmegen F12159 | Fotopersbureau Gelderland · 1960 | CC BY-SA 4.0 | 2026-10-22 William 열람. 정면 간판 "ST. CANISIUS ZIEKENHUIS" 확인 |
| `NDE-NL-1979-dentures--ooij-waal-winter.jpg` | [[NDE-NL-1979-dentures]] | ② 장소(참고) | 오이(Ooij) 근처 발(Waal)강 범람원의 겨울 풍경. **사건 장소가 아닌 지역 참고 사진** | [Commons](https://commons.wikimedia.org/wiki/File:Typical_Dutch_winter_riverscape_of_the_Waal.jpg) | Lendskaip · 2021-02-11 | CC0 | 2026-10-22 열람. 눈 덮인 제방과 언 범람원 |
| `NDE-NL-1979-dentures--crash-cart-example.jpg` | [[NDE-NL-1979-dentures]] | ② 물건(참고) | 오늘날의 크래시 카트(심정지 카트) 예, 스페인. **1979년 카니시우스의 카트는 병원 기술진이 그 방을 위해 만든 것으로 사진이 없다** | [Commons](https://commons.wikimedia.org/wiki/File:Carro_de_paradas.jpeg) | Manuel Ramallo · 2014-06-12 | CC0 | 2026-10-22 열람. 서랍 3단, 위에 제세동기 |
| `NDE-NL-1979-dentures--sequence.svg` · `--sequence-ko.svg` | [[NDE-NL-1979-dentures]] | ④ 도해 | 사건 순서 6단계, 확인된 정보 4가지, "이렇게도 설명된다" 3가지와 등급. 영어판은 영어 카드에, `-ko`판은 `ko/` 읽는 글에 들어간다(같은 사실, 글자만 다름) | 카드 3·6·7절 | William · 2026-10-23(영어판 추가) | 이 저장소와 같음 | 생성 코드 `tools/diagrams/NDE-NL-1979-dentures.py en` / `ko` |
| `DBV-GB-1924-doris--timeline.svg` · `--timeline-ko.svg` | [[DBV-GB-1924-doris]] | ④ 도해 | 연표(혼인→비다 사망→숨김→출산·환시·사망→진술서→책), 발화 ①~⑦을 누가 들었나, 비다의 죽음을 알던 사람, 기록의 사슬과 등급. 영어판·`-ko`판 | 카드 3·4·6절 | William · 2026-10-23(영어판 추가) | 이 저장소와 같음 | 생성 코드 `tools/diagrams/DBV-GB-1924-doris.py en` / `ko` |
| `DBV-GB-1924-doris--florence-barrett.jpg` | [[DBV-GB-1924-doris]] · [[P-Barrett-Florence]] | ③ 인물 | 레이디 플로렌스 바렛(1867–1945), 첫 기록자·증인. 좌상 초상, 촬영 연도 미상 | [Commons](https://commons.wikimedia.org/wiki/File:Portrait_of_Florence_Barrett_Wellcome_L0004411.jpg) · Wellcome Collection L0004411 | Wellcome Images · 연도 미상 | CC BY 4.0 | 2026-10-22 William 열람. 검은 드레스, 레이스 소매, 앉은 자세. 1400px·q70으로 축소(원본 1600px은 400KB 초과) |
| `DBV-GB-1924-doris--william-barrett-1907.png` | [[DBV-GB-1924-doris]] · [[P-Barrett-WF]] | ③ 인물 | 윌리엄 F. 바렛 경(1844–1925), 수집·출판자. 1907년 출판물 초상 | [Commons](https://commons.wikimedia.org/wiki/File:William_F._Barrett_the_psychical_researcher.png) | James Creelman · 1907 | 퍼블릭 도메인 | 2026-10-22 열람. 흰 수염의 흉상 초상(311×373, 원본 크기 그대로) |
| `DBV-GB-1924-doris--mothers-hospital-clapton-2018.jpg` | [[DBV-GB-1924-doris]] · [[L-Mothers-Hospital-Clapton]] | ② 장소 | Mothers' Hospital(런던 Lower Clapton Rd) 정면 건물, 2018년. 1824년 주택을 병원 정면으로 썼고 병동은 뒤편. 1986년 폐원 후 주거 단지(Mothers' Square). **1924년 당시 사진이 아님** | [Commons](https://commons.wikimedia.org/wiki/File:The_Salvation_Army_Mothers%27_Hospital,_Front_Buildings,_Lower_Clapton_Rd.jpg) | Paul the Archivist · 2018-05-05 | CC BY-SA 4.0 | 2026-10-22 열람. 아치에 "THE MOTHERS' SQUARE AND MAITLAND HOUSE" |
| `DBV-GB-1924-doris--london-1920-map.jpg` | [[DBV-GB-1924-doris]] · [[L-Mothers-Hospital-Clapton]] | ② 장소(지도) | 1920년 베이컨 런던 포켓 지도의 동북부(클랩턴·해크니·해거스턴·스트랫퍼드·웨스트햄·하이버리)를 잘라낸 것. ① Mothers' Hospital(Lower Clapton Rd) ② 웨스트햄(비다 사망지) ③ 해거스턴 올 세인츠 일대(1923 혼인) ④ 하이버리(어머니 주소) 번호 표시와 오른쪽 아래 설명 상자(영어)는 **William이 덧붙인 것으로 대략의 위치**(지도 원본에는 없음). 1280px·q80. 생성 코드는 스크래치패드에만(크롭 좌표: 원본 축소본의 동북부 768×460, 표시 ①(360,125) ②(640,275) ③(255,262) ④(165,95)) | [Commons](https://commons.wikimedia.org/wiki/File:1920_Bacon_Pocket_Map_of_London,_England_and_Environs_-_Geographicus_-_London-bacon-1920.jpg) · Geographicus Rare Antique Maps | George Washington Bacon · 1920 | 퍼블릭 도메인(1920년 간행, 작가 1922년 사망) | 2026-10-23 William 열람. 지명 Clapton·Hackney Downs·Haggerston·West Ham·Highbury 확인 후 표시 |

## 찾았으나 쓰지 않은 것

| 카드 | 무엇 | 이유 |
|---|---|---|
| NDE-NL-1979-dentures | JNDS 논문 쪽(UNT 디지털 도서관, Smit 2008 등 4편) | ⓒ IANDS(UNT 메타데이터 `rights: (c) 2008 IANDS`). 카드 4절에서 링크만 |
| NDE-NL-1979-dentures | Lancet 2001 van Lommel 논문 쪽 | ⓒ Elsevier, 전문 유료. 링크만 |
| NDE-NL-1979-dentures | Commons "Nieuwbouw St.Canisius-ziekenhuis F70524"(1971) | 열어 보니 건축 모형 사진. 사건과 무관 |
| NDE-NL-1979-dentures | Thumper(기계식 심장마사지기) 사진 | Commons에 없음(2026-10-22 검색 "Michigan Instruments Thumper", "mechanical chest compression device") |
| NDE-NL-1979-dentures | 1979년 지역 신문 보도 | Delpher에 De Gelderlander 1979년치 없음. 카드 13절 탐색 기록 참조 |
| DBV-GB-1924-doris | Barrett 1926 『Death-bed Visions』 pp.10–14 쪽 스캔(Wellcome b29813992) | 저자 1925년 사망으로 본문은 PD이나 Wellcome 메타데이터가 저작권 표시·열람 전용. 카드 4절에서 IIIF 쪽 주소로 링크만 |
| DBV-GB-1924-doris | archive.org `b29813992` 사본 | 권리 표시가 "possibly in copyright"(InC)라 링크만(2026-10-23 확인). 파일 내려받기도 403(printdisabled 컬렉션) |
| DBV-GB-1924-doris | 1924년 1~2월 신문 보도·전재 기사 | BNA(영국)는 유료. Papers Past·Chronicling America(loc.gov)·HathiTrust는 봇 차단, Trove는 API 키 필요 → **미확인**. 카드 13절 탐색 기록 |
| DBV-GB-1924-doris | 1920년대 Mothers' Hospital 사진 | Commons에 없음(2026-10-22 검색). 2018년 정면 사진으로 대신하고 캡션에 명시 |
| DBV-GB-1924-doris | BMJ 1945-08-18 레이디 바렛 부고(PMC2059597) | PMC·Europe PMC 봇 차단으로 본문 미열람. 저작권도 BMJ |
