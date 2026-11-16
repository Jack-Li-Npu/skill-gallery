"""Validate catalog paths, skill identities, and local Markdown references."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

root = Path(__file__).resolve().parents[1]
catalog = json.loads((root / "catalog.json").read_text())
assert catalog["schema_version"] == 1
ids = set()
for skill in catalog["skills"]:
    sid = skill["id"]
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid), sid
    assert sid not in ids, f"Duplicate skill: {sid}"
    ids.add(sid)
    for key in ("path", "example", "preview"):
        target = (root / skill[key]).resolve()
        assert target.is_relative_to(root) and target.exists(), (sid, key)
    entry = root / skill["path"] / "SKILL.md"
    text = entry.read_text()
    assert text.startswith("---\n"), entry
    frontmatter = text.split("---", 2)[1]
    assert re.search(r"^name: *" + re.escape(sid) + r" *$", frontmatter, re.M), entry
    assert re.search(r"^description: *\S", frontmatter, re.M), entry
    assert re.fullmatch(r"\d+\.\d+\.\d+", skill["version"]), sid
    assert skill["inputs"] and skill["outputs"] and skill["requirements"], sid

for file in root.rglob("*.md"):
    if ".git" in file.parts:
        continue
    text = file.read_text()
    links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text)
    links += re.findall(r'(?:src|href)="([^"]+)"', text)
    for link in links:
        if urlparse(link).scheme or link.startswith("#"):
            continue
        relative = unquote(link.split("#", 1)[0])
        target = (file.parent / relative).resolve()
        assert target.is_relative_to(root) and target.exists(), (file, link)

skill_dirs = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
assert ids == skill_dirs, (ids, skill_dirs)
print(f"Validated {len(ids)} skill(s): catalog, identity, versions, and local references")
