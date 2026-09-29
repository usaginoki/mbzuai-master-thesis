"""Integrity check: required properties, questions<->q/ tag agreement, wikilinks and embeds resolve."""
import re, glob, os, sys
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(VAULT)
notes = {os.path.basename(p)[:-3] for p in glob.glob("**/*.md", recursive=True) if not p.startswith((".", "_tools"))}
files = {os.path.basename(p) for p in glob.glob("**/*", recursive=True) if os.path.isfile(p)}
REQ = ["title", "authors", "year", "published", "venue", "peer_reviewed", "url", "pdf", "questions", "relevance", "tags"]
problems = []
for p in sorted(glob.glob("Papers/*.md") + glob.glob("Questions/*.md") + glob.glob("Sessions/*.md") + ["Backlog.md"]):
    if not os.path.exists(p): continue
    s = open(p).read()
    if p.startswith("Papers/"):
        fm = s.split("---")[1]
        for k in REQ:
            if not re.search(rf"^{k}:", fm, re.M): problems.append(f"{p}: missing property {k}")
        qs = re.search(r"^questions:\s*\[(.*)\]", fm, re.M)
        qs = {q.strip() for q in qs.group(1).split(",")} if qs else set()
        tags = {t.replace("-", ".").upper() for t in re.findall(r"q/([\d-]+)", fm)}
        if {q.upper() for q in qs} != {"Q" + t for t in tags}: problems.append(f"{p}: questions {sorted(qs)} vs q/ tags {sorted(tags)}")
    s = re.sub(r"`[^`\n]*`", "", s)  # links inside inline code are not links
    for emb, tgt in re.findall(r"(!?)\[\[([^\]|#]+)", s):
        tgt = tgt.strip().rstrip("\\").strip()  # "\|" is an escaped alias pipe inside tables
        ok = tgt in notes or tgt in files or os.path.basename(tgt) in files or tgt + ".md" in files
        if not ok: problems.append(f"{p}: unresolved {'embed' if emb else 'link'} [[{tgt}]]")
print("\n".join(problems) or "OK: no problems")
print(f"{len(glob.glob('Papers/*.md'))} paper notes checked")
