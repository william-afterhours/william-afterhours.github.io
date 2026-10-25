---
title: Barrett 1926, Death-bed Visions
updated: 2026-10-25
---

# Source summary — Barrett 1926, *Death-bed Visions* (so it need not be read again)

The full OCR (about 177,000 characters) was kept in the session scratchpad only and is not in the repository (the Wellcome metadata carries a rights statement). All facts were moved into `cases/DBV-GB-1924-doris.md` with source numbers. This page holds only the access route, the structure of the book and details not used in the card.

## Access (confirmed 2026-10-22)

- **Wellcome Collection, b29813992** — everything opens without a key.
  - IIIF manifest `https://iiif.wellcomecollection.org/presentation/v2/b29813992` — 144 canvases; the canvas `label` is the printed page number. Image number = canvas index + 1 (printed p. 10 = `_0026`).
  - Page image `https://iiif.wellcomecollection.org/image/b29813992_NNNN.jp2/full/900,/0/default.jpg` (width 900 works).
  - Full text `https://api.wellcomecollection.org/text/v1/b29813992` — one enormous single-line string. Do not `grep -n`; cut index windows with Python.
  - The metadata rights statement is view-only (the author died in 1925 so the text is public domain, but the scan follows the Wellcome statement: link only).
- archive.org `b29813992` (printdisabled collection): file download 403. Other copies are borrow-only.

## Structure of the book (by OCR offset)

| Chapter | Title (original) | OCR start offset | Card candidates |
|---|---|---|---|
| I | Introduction | 6,044 | Quotes Sidgwick ("no single case can justify the ghost hypothesis") — the same spirit as METHOD |
| II | Visions seen by the dying of persons by them unknown to be dead | 16,626 | **DBV-V storehouse.** First case Doris (pp. 10–14) → Jennie & Edith, United States 1889 (pp. 14–16, Savage → Hyslop) → the rest not read |
| III | Visions seen by the dying of persons known by them to be dead, and deathbed visions … | 38,885 | Many DBV (S layer) candidates. Not read |
| IV | Visions seen by the dying of living persons at a distance — in some cases reciprocal | 112,510 | Borderline CA/DBV cases. Not read |
| V | Music heard at the time of death by the dying or by persons present at a death | 132,592 | Out of scope (structure not defined) |
| VI | Visions of the spirit of a dying person leaving the body | 143,262 | Out of scope |

## Details not used in the card

- At the head of chapter II Barrett writes that Richet too regards this evidence as inexplicable by cryptesthesia — Richet's text not checked.
- Chapter II, Jennie & Edith (June 1889, a "neighbouring city" in the United States, diphtheria): the parents and the physician hid Jennie's death from Edith, and shortly before dying Edith chose two photographs to send to Jennie (evidence that she did not know). Barrett reprints from Hyslop's book and notes that Savage "gave the names and address to Hyslop". To card it, Hyslop's original (book title unverified) and Savage's original record are needed.
- Footnote on Hyslop: professor of ethics and logic at Columbia, at first a sceptic, died of overwork as treasurer, secretary and researcher of the ASPR (1920).

## To open next

- Extract the list of cases in chapter III to pick DBV S-layer candidates (those with records before 1882). OCR offsets 38,885–112,510.
- The deathbed-vision chapter of *On the Threshold of the Unseen* (1917) — search archive.org for a public-domain copy.
- Cobbe 1882 is now opened (see `entities/M-dbv-visitor-unknown-dead.md`): Barrett's chapter II title repeats Cobbe's definition, so the SPR collection and Cobbe's anecdotes are one English lineage.
