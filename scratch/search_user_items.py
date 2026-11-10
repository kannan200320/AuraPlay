import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== TASK 1: SEAT PICKER SEARCH ===")
for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    if "INTERACTIVE SEAT PICKER" in content or "SELECT YOUR STATION" in content:
        print(f"Found in {f}")

print("\n=== TASK 2: GAMES PAGE PERIPHERALS & INTEGRITY SEARCH ===")
games = open("games.html", encoding="utf-8").read()
for term in ["Pro Peripherals", "HALL EFFECT KEYBOARDS", "KERNEL-LEVEL ANTI-CHEAT", "REFEREES & MATCH ARBITERS"]:
    print(f"Term '{term}' in games.html: {term.lower() in games.lower()}")

print("\n=== TASK 3: OVERCOOKED! SEARCH ===")
for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    if "Overcooked!" in content:
        print(f"Found in {f}")

print("\n=== TASK 4: HOME DROPDOWN SEARCH ===")
index = open("index.html", encoding="utf-8").read()
idx = index.find('nav class="hidden')
if idx != -1:
    print(index[idx:idx+1200])
else:
    # search for Home in nav
    for m in re.finditer(r'<nav[^>]*>.*?</nav>', index, re.DOTALL):
        print(m.group(0)[:800])
