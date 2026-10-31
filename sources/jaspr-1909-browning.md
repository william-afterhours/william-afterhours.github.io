---
title: JASPR 1909, the Browning letter, and archive.org serials
updated: 2026-10-31
---

# Source summary — *Journal of the ASPR*, July 1909, pp. 422–423 ("Vision of the Dying"), and how archive.org serials open (so it need not be worked out again)

Everything from the source that the card needs is in `cases/DBV-GB-1883-browning.md` §3 with source numbers. This page keeps the access route, what the pages contain beyond the card, and the two anecdotes from 1863 and 1879 that were checked and not carded.

## Access (confirmed 2026-10-31)

- **archive.org `sim_` serial items** (Serials in Microfilm): the 1907–1920 run of the *Journal of the American Society for Psychical Research* is split by issue, e.g. `sim_journal-of-the-american-society-for-psychical-research_1909-07_3_7` (year-month_volume_issue). Found with the advancedsearch API: `title:("journal of the american society for psychical research") AND date:[1909-01-01 TO 1909-12-31]`.
  - Full text: `https://archive.org/download/<id>/<id>_djvu.txt` (opens without a key; 1909-07 ≈ 165 KB).
  - Page-level text: `<id>_djvu.xml` — one `<OBJECT>` per leaf; the leaf index that contains a string gives the page image to fetch.
  - Page image: `https://<server>/BookReader/BookReaderImages.php?zip=<dir>/<id>_jp2.zip&file=<id>_jp2/<id>_NNNN.jp2&id=<id>&scale=2&rotate=0`, where `server` and `dir` come from `https://archive.org/metadata/<id>`. **The `id=` parameter is required** (404 without it). `scale=2` gives ≈1200×1800 px. The IIIF endpoint `iiif.archive.org/iiif/3/<id>$<leaf>` returns 404 for these items. The PDF also downloads; macOS can render a page with a short Swift/PDFKit script if ever needed (not needed here).
  - The 1909 volume is a United States publication of 1909 → public domain; page scans may be kept in `assets/`.
- Same route works for *The Open Court* (`sim_open-court_<date>_<vol>_<iss>`) and *The Atlantic Monthly* (`sim_atlantic_1879-03_43_257`).
- The Wellcome per-page OCR of Barrett 1926: `https://iiif.wellcomecollection.org/annotations/v2/b29813992/b29813992_NNNN.jp2/line` (JSON annotation list; `resources[].resource.chars`). Canvas index + 1 = image number; printed page = canvas label (p. 44 = `_0060`).

## What pp. 422–423 contain (beyond the card)

- The item sits in the "Incidents" department, after a cablegram-and-letter coincidence case (K. D., Dedham, March 1909) and before a "Premonitory Dream" (E. F. B—, Boston, 1907, sworn deposition sent by Prescott F. Hall).
- Hyslop's bracketed note: provenance chain Church → editor of *The Open Court* → David P. Abbott (author of *Behind the Scenes with the Mediums*) → Hyslop, "with the letter that accompanied it"; "Inquiry of the writer, who is connected with the 'Army and Navy Journal'"; description of the paper (yellow, black edges, stamp of a hand holding a sword, motto "Fortune de guerre"); "The letter may be interpreted as documentary evidence."
- The letter: heading "Egmont, Bracknell, Berks, Nov. 5th, 1883"; "Dear Capt. Ericsson"; the full paragraph quoted in the card; then "She was quite prepared to go, and I really think it a happy release; for recently she has, as I before told you, been so weak and helpless, in fact a perfect skeleton from diabetes from which she has suffered for many years. * * * * * * * Yours very sincerely, ELLEN CHUTE." The asterisks mark Hyslop's omission ("incidents in the letter that have a personal character").
- Church's covering letter: "New York, Aug. 17th, 1908. Editor of the Open Court, Chicago, Ill." — identifies the persons; postscript: "Lady Chute was the wife of General Sir Trevor Chute of the British Service, K.C.B., and one of the Chutes of 'Chute Hall,' England. Mrs. John Ericsson died July, 1867." Signed "WM. CONANT CHURCH".

## Civil index (FreeBMD, 2026-10-31)

- The search form (`/cgi/search.pl`) returns results inside a JavaScript array `searchData` (not an HTML table): rows `"<colour>;<Surname>;<Given>;<Age>;<?>;<District>;<Vol>;<Page>;<id>"` under header rows `" ;1;<quarter>;<year>"`; a blank surname or given name repeats the row above. Parse with Python, not `sed`. The start/end year fields were ignored in these runs (all years returned), so filter by the header year.
- Deaths, Dec quarter 1883: Browning, Louisa, 78, Kensington, 1a 11. Deaths, Sep quarter 1867: Ericsson, Amelia Jane, 50, Marylebone, 1a 376.

## Checked and not carded (Barrett 1926 ch. III, pre-1882 dates)

- **De Morgan 1863**, *From Matter to Spirit*, pp. 184–185 (archive.org `frommattertospir00demorich`, djvu text at offset ≈333,600): the dying boy "John L—" of "M—" replies to an unseen questioner, then "Mother, here is grandmother come! you must see her! And she is with such a great company, and they say that they are come to take me away with them"; told by the mother to the narrator, who wrote to the author. Anonymous, undated, second-hand → D. The narrator's gloss ("a holy assembly of ministering spirits") shows the spiritualist frame of the collection.
- ***Atlantic Monthly* March 1879**, "Ghost Stories", p. 289 (archive.org `sim_atlantic_1879-03_43_257`, djvu text at offset ≈61,200): "Mrs. G—", daughters Minnie and Ada, smallpox after a move to London; Ada: "there is Minnie! She has come for me!"; the mother hears "soft, sweet music" and a voice "Come, dear Ada; I am waiting for you!"; the mother had overheard the children agree that whoever died first would fetch the other. Anonymous literary anecdote; Barrett himself notes the mother's expectancy → D.
- **Pearson 1864** (Proc. SPR VI p. 20; recorded 1889): a collective apparition seen by relatives at a deathbed, not the dying person's own vision; twenty-five years late → not this motif's best case.
- **Daisy Dryden 1864** (JASPR 1918 vol. XII no. 6; mother's memoir): long after the event; a candidate for the EU-W (US) cluster if the mother's original dated notes exist — not opened.
