import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    if "dropdown-toggle" in content:
        matches = re.findall(r'<div class="relative group[^"]*"', content)
        print(f"{f}: {len(matches)} dropdown container(s)")
