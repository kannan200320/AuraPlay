import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    matches = re.findall(r'<a href="login\.html"[^>]*hidden sm:inline-flex[^>]*>', content)
    if matches:
        print(f"{f}: found {len(matches)} match")
