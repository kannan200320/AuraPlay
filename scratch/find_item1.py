import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    matches = re.findall(r'.{0,30}(?:RESERVE YOUR STATION|LAUNCH ANY TITLE).{0,30}', content, re.IGNORECASE)
    if matches:
        print(f, matches)
