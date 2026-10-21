"""Harvest UNT OAI-PMH records for a collection set -> TSV (ark, date, title, creators).
usage: unt_oai.py <set e.g. collection:JNDS> <out.tsv> <dl_dir>
"""
import sys, os, re, time, urllib.request, urllib.parse
import xml.etree.ElementTree as ET

setspec, out, dl = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(dl, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}
base = "https://digital.library.unt.edu/oai/"
ns = {"oai": "http://www.openarchives.org/OAI/2.0/", "dc": "http://purl.org/dc/elements/1.1/",
      "oai_dc": "http://www.openarchives.org/OAI/2.0/oai_dc/"}
rows, token, page = [], None, 0
while True:
    q = f"?verb=ListRecords&resumptionToken={urllib.parse.quote(token)}" if token else f"?verb=ListRecords&metadataPrefix=oai_dc&set={setspec}"
    f = os.path.join(dl, f"oai_{page}.xml")
    if not os.path.exists(f):
        with urllib.request.urlopen(urllib.request.Request(base + q, headers=UA), timeout=120) as r:
            open(f, "wb").write(r.read())
        time.sleep(1)
    root = ET.parse(f).getroot()
    for rec in root.iter("{http://www.openarchives.org/OAI/2.0/}record"):
        ident = rec.findtext("oai:header/oai:identifier", "", ns)
        ark = re.sub(r".*/(metadc\d+).*", r"\1", ident)
        md = rec.find("oai:metadata/oai_dc:dc", ns)
        if md is None:
            continue
        title = " | ".join(t.text or "" for t in md.findall("dc:title", ns))
        date = " | ".join(t.text or "" for t in md.findall("dc:date", ns))
        creators = "; ".join(t.text or "" for t in md.findall("dc:creator", ns))
        src = " | ".join(t.text or "" for t in md.findall("dc:source", ns) + md.findall("dc:relation", ns))
        rows.append((ark, date, title, creators, src))
    tok = root.find("oai:ListRecords/oai:resumptionToken", ns)
    token = tok.text if tok is not None and tok.text else None
    page += 1
    if not token:
        break
with open(out, "w") as fh:
    for r in rows:
        fh.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in r) + "\n")
print(len(rows), "records,", page, "pages ->", out)
