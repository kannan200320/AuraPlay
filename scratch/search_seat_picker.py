import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    if "A01" in content or "Seat" in content or "Floor" in content or "A03" in content:
        matches = re.findall(r'.{0,30}(?:A01|Seat Picker|Arena Floor|Available|Occupied).{0,30}', content, re.IGNORECASE)
        if any("A01" in m or "A03" in m or "Arena Floor" in m for m in matches):
            print(f"Found in {f}:")
            for m in matches[:5]:
                print("  ", m.strip())
