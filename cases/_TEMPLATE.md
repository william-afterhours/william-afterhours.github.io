---
id: CODE-CC-YYYY-slug          # same as the file name, e.g. NDE-NL-1979-dentures
title: "<Short human title (Place, Year)>"   # shown on the site; e.g. "Doris sees Vida (London, 1924)"
code: CODE                     # NDE / DBV / CA / CORT / MED. Counter-evidence cards: X-CODE
variant: ""                    # V (verification claim) / S (shared) / C (collective) / F (within family) / ""
cluster: ""                    # METHOD §5 cluster code, e.g. EU-W, SA, ANC-EA
country: CC                    # ISO country code
event_year: YYYY               # year of the event; cYYYY if uncertain
record_year: YYYY              # year of the earliest record
investigator: none             # investigating body code (organisation or person); none if there was none
independence: ""               # I2 / I1 / I0 (result of §11)
scores: {S1: , S2: , S3: , S4: , S5: , S6: , S7: }
grade_R: ""                    # A / B / C / D / —
grade_V: ""                    # V2 / V1 / V0 / V—
cap: ""                        # cap rule applied, e.g. "①"; "" if none
unfavorable: []                # hypotheses graded "unfavourable", e.g. [H5, H6] (result of §8)
links: []                      # ids linked in §10, e.g. [M-taken-by-mistake-returned, O-SPR]
counter: unsearched            # best R grade among rebuttals (A–D) / none (searched, none found) / unsearched
countable: no                  # no / S / V / SV. S = R≥B ∧ I2 ∧ counter≠unsearched ∧ no cap ∧ ≥2 structural elements. V = V1 or better ∧ counter≠unsearched ∧ no cap (METHOD §1 v0.2)
status: draft                  # draft / reviewed / final
updated: YYYY-MM-DD
---

# <One-line descriptive title of the case (Place, Year)>

> (Lede. One paragraph a reader can take in at a glance: where and when, what the person said or saw, and the one fact that makes the case worth a card. Only facts that appear with a source number in the ledger below.)

## What happened

(The story told plainly, top to bottom, in past tense. Verified quotations in the original language's wording; no invented dialogue. Every fact here must appear with a `[#n]` in §3. Put each image where it belongs in the story, as a standard markdown image with alt text, followed by a one-line italic caption: what it shows · source (archive, author, year) · licence. Say "Reference" when the image is not the actual place, object or person. Say so when a diagram is William's and "not a record".)

![Alt text](../assets/CODE-CC-YYYY-slug--slug.jpg)
*What it shows · source · licence*

## How far can this record be trusted

(The R, V and I grades explained in words: who wrote, when, how many witnesses, whether anything was written before it was checked, who investigated and with what stake. No new facts.)

## Other ways to explain it

- **(Explanation in a few words.)** (Why it is live or not, from §7.)

(Close with the compatibility verdict in one or two sentences: compatible with the survival hypothesis or not, and whether the record can separate it from the others.)

---

## Investigation ledger

Everything above rests on the sources numbered below. The ledger is this study's working record: the facts with their source numbers (§3–§4), the scores behind the grades (§5), the verified information (§6), the ordinary explanations (§7), the hypotheses the record can and cannot separate (§8), counter-evidence (§9), connections (§10), cultural independence (§11), notes (§12) and the list of materials (§13). Rules in `docs/METHOD.md`.

## 1. One-line summary

(Who, when, where, what was experienced, what was confirmed. Two sentences at most. Living people, or those whose status is unknown, as initials.)

## 2. Structure checklist

(Copy the elements for this code from the METHOD §1 table and tick ☑/☐. If any required element is ☐, no code is assigned → "similar case".)

- [ ] Required 1:
- [ ] Required 2:
- [ ] Required 3:
- [ ] Optional:
- V element: present / absent —

## 3. Account

(Facts only. Every sentence carries a source number `[#n]`. No interpretation, no adjectives.)

## 4. Sources

| # | Type (primary/secondary/tertiary) | Reference | Opened | Link | Notes |
|---|---|---|---|---|---|
| 1 | | | Confirmed / Unverified | | |

## 5. Scores and grades

| Axis | Score | Reason in one line |
|---|---|---|
| S1 Source | | |
| S2 Witnesses | | |
| S3 Timing | | |
| S4 Ordinary explanations examined | | (determined by §7) |
| S5 Prior record (V axis) | | — if no V claim |
| S6 Investigator independence | | |
| S7 Original text opened | | |

Total (S1+S2+S3+S4+S6) = /10 → R grade — / cap applied: none / V grade —

## 6. Verified information (V claim)

(Write "none" if there is none. The last column is for the H2 verdict: who alive at the time knew the information.)

| Information | Who said it | When and where recorded | When and by whom verified | Normal channels investigated | Who alive at the time knew it |
|---|---|---|---|---|---|
| | | | | | |

## 7. Other ways to explain it

(Status: ruled out / partly ruled out / not ruled out / cannot assess. Criteria in METHOD §3. If any row is empty, the card is unassessed.)

| Item | Status | Reason |
|---|---|---|
| F Fraud | | |
| M Misperception | | |
| D Memory distortion, later embellishment | | |
| L Leakage, normal channels | | |
| E Cultural expectation, suggestion | | |
| N Neurophysiology, drugs, psychology | | (no deduction; recorded only) |
| C Coincidence, base rate | | |
| X Selective reporting, recorder bias | | |

## 8. Compatible hypotheses

(METHOD §4. Status: compatible / unfavourable / undetermined. "Compatible" is the default. "Unfavourable" only where this card's specific record is the ground — otherwise "undetermined".)

| Hypothesis | Status | Reason |
|---|---|---|
| H1 Survival after death | | |
| H2 Psi without survival | | |
| H3 Cultural transmission | | |
| H4 Neurophysiology, psychology | | |
| H5 Memory distortion, embellishment | | |
| H6 Fraud | | |
| H7 Chance, base rate | | |
| H8 Investigator effect | | |

## 9. Counter-evidence

Search: date / search terms / result (record "none" too)

| Source | R grade | Gist | Effect on this card |
|---|---|---|---|
| | | | |

## 10. Connections

(METHOD §6. Targets are `entities/` items or other case cards. Verdict: transmission / recurrence / neutral / undecided. Grade: confirmed / inferred / unverified. Transmission links feed the path table in §11. Record "no connections" too, with the date and method of the search.)

Search: date / method / result

| Target `[[id]]` | Relation (R-*) | Verdict | Grade | Reason |
|---|---|---|---|---|
| | | | | |

## 11. Cultural independence

Cluster: / record year vs baseline year: / investigating body:

| Path | Ruled out / unknown / confirmed | Reason (including transmission links from §10) |
|---|---|---|
| ① Direct contact | | |
| ② Translation, publication | | |
| ③ Missionary, religious transmission | | |
| ④ Mass media | | automatically ruled out if before the baseline year |
| ⑤ Same investigating body | | |

→ Independence grade: I2 / I1 / I0

## 12. Notes

(Open questions, sources to open next, information that could change a grade.)

## 13. Materials

(List of photographs, copies of records, illustrations and diagrams. The images themselves go in "What happened" above; here only the table. Rules in METHOD §9 "visual materials"; full records in `assets/index.md`. No effect on grades. Mark anything that is not the actual place, object or person "reference". If there is nothing, write "none (search: date, where, terms)".)

| File | Kind | What | Source · licence |
|---|---|---|---|
| `CODE-CC-YYYY-slug--slug.jpg` | | | |

- Not included for copyright or access reasons: (what, and where it is linked instead)
- Newspaper and archive search: (date, archive, terms, result — record 0 hits too)
- To look for next:
