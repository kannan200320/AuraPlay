import glob, re

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    hits = re.findall(r'href=["\'](login\.html[^"\']*|register\.html[^"\']*)["\']', c)
    if hits:
        print(f"{p}: {len(hits)} auth links -> {hits[:2]}")
