---
title: "Ji Yun, Yuewei caotang biji (1789–1798) and East Asian deathbed records: how the sources were reached"
updated: 2026-11-02
---

# Ji Yun's notebooks and East Asian deathbed records — access notes

Notes for card [[DBV-CN-1793-zhang]] (session 8, 2026-11-02). What was opened, how, and what failed, so that nothing has to be searched for twice.

## 1. The text: Chinese Wikisource

- 《閱微草堂筆記》 is on Chinese Wikisource as 24 pages `閱微草堂筆記/卷1` … `/卷24` plus `/序`, `/附`. Fetched as wikitext with the MediaWiki API (`action=query&prop=revisions&rvprop=content&rvslots=main`), about 1.1 million characters in all.
- Chapter map: ch. 1–6 《灤陽消夏錄》, 7–10 《如是我聞》, 11–14 《槐西雜志》, 15–18 《姑妄聽之》 (preface at the head of ch. 15, dated 乾隆癸丑七月二十五日 = 1793), 19–24 《灤陽續錄》.
- The same API worked for other collections, fetched by page-name prefix (`list=prefixsearch`): 《子不語》 (27 pages), 《續子不語》, 《夷堅志》 (101 pages, partial), 《池北偶談》, 《庸閑齋筆記》, 《右台仙館筆記》, 《耳食錄》, 《夜譚隨錄》, 《諧鐸》.
- Search method: regular expressions over the downloaded text, a deathbed term (臨終, 病革, 疾革, 將死, 垂死, 疾篤, 病篤, 屬纊, 彌留 …) within about 150 characters of a fetching term (來迎, 迎我, 接我, 來導, 招我 …) or a dead-kin term (亡妻, 亡母, 先亡, 亡媳 …). Twelve windows came out of about 3.7 million characters; the card's entry was the only one with a named witness who was present.
- ctext.org's API requires a key or a registered IP (refused, 2026-11-02). Not needed.

## 2. The scan: archive.org, CADAL copies from Peking University Library

- A Qing woodblock edition is on archive.org as 17 items `02099113.cn` … `02099129.cn` (titles 閱微艸堂筆記(一) … (十七)), sponsor China-America Digital Academic Library, scanning centre Peking University Library, 600 ppi. The date of the edition is not in the metadata.
- **The archive.org OCR is useless** (simplified-script Tesseract on a traditional woodblock page). Do not search it.
- These items have **no `_jp2.zip`**, so the BookReader image URL used for the `sim_` serials does not work. Use the per-item `<id>_tif.zip` (about 7–10 MB, one TIFF per image, 1900 × 3000 px) and convert with `sips -s format jpeg -Z <px>`.
- Volume ↔ chapter, found by reading first pages: vol. 11 (`02099123.cn`) begins ch. 15 with the 《姑妄聽之》 preface (images 2–3); vol. 13 (`02099125.cn`) is ch. 17, and the Lady Zhang entry is the last leaf (leaf 38), image 76 of 78; vol. 14 (`02099126.cn`) begins ch. 18; vol. 15 (`02099127.cn`) begins ch. 19 (preface of 《灤陽續錄》 dated 嘉慶戊午 = 1798).
- To find a passage in the scan: locate it in the Wikisource chapter, take its relative position in the chapter, open the images at that fraction of the volume, and compare the first and last characters.

## 3. Route checks

- **Christian books in Chinese (route ②):** 《四庫全書總目提要》 卷125 on Chinese Wikisource contains the catalogue notes on 天主實義 (1603), 畸人十篇 (1608), 七克, 靈言蠡勺, 西學凡; 卷134 on 天學初函. Lives of saints and deathbed manuals in Chinese were **not** searched; that is the open part of route ②.
- **Buddhist canon (route ③):** CBETA XML on GitHub, `https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T13/T13n0412.xml` (Taishō 412). Chapter headings are `<cb:mulu>` elements; strip tags and whitespace before searching. Any Taishō text: `T/T<vol>/T<vol>n<no>.xml`.

## 4. Searches that failed or were set aside

- **Osis & Haraldsson 1977 (South Asia):** archive.org has JASPR issues for 1909–1920 and 1960–1961, but for 1970–1990 only contents and index volumes (advancedsearch, 2026-11-02). *At the Hour of Death* is borrow-only. Haraldsson's university pages are gone; the Wayback copy of `notendur.hi.is/erlendur/english/svid.htm` lists the 1977 paper without a full-text link (other papers there do have PDFs: Haraldsson 1987 JSPR on the Iyengar–Kirti case; 1988–89 Omega survey; 2009 J Parapsychol; 2012 terminal lucidity).
- **Korean Classics DB (한국고전종합DB, db.itkc.or.kr):** open without login. `https://db.itkc.or.kr/search/group?q=query†<words>` returns HTML with result counts and snippets (script `$S/x/itkc_search.py` in the session scratchpad, not kept). The search is loose (it matched every "데리러 왔" in court records), so deathbed passages need tighter terms in the original Classical Chinese. Not used for a card.
- **Japan (NDL Lab, 次世代デジタルライブラリー):** `https://lab.ndl.go.jp/dl/api/book/search?keyword=<phrase>&size=<n>` returns JSON with `hit` and per-book OCR `highlights`. It works for **one phrase**, not for several words (space-separated keywords return 0). The OCR uses old character forms (來, not 来). Example hit: Hirata Atsutane, 《古今妖魅考》, on visions at death being the work of demons. Japanese Wikisource has none of the Edo essay collections tried (耳嚢, 甲子夜話, 兎園小説, 譚海 …).

## 5. Ji Yun's own statements about his sources (preface of 1793, scan)

追錄舊聞 ("writing down old things I heard"); 多得諸傳聞 ("much of it came from hearsay"); 大旨期不乖於風教 ("the main aim is not to run against moral teaching"); 五十以後，領修秘籍 ("after fifty I led the editing of the palace books"); 適盛子松雲欲為剞劂 ("Sheng Songyun wished to have it cut on blocks").
