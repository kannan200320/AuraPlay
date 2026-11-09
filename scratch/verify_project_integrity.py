import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

primary_pages = [
    "index.html",
    "player-lounge.html",
    "about.html",
    "games.html",
    "pricing.html",
    "membership.html",
    "book-slot.html",
    "blog.html",
    "contact.html"
]

all_15 = True
print("=== SECTION COUNT VERIFICATION ===")
for p in primary_pages:
    content = open(p, encoding="utf-8").read()
    sections = re.findall(r'<section\b', content)
    count = len(sections)
    status = "OK (15)" if count == 15 else f"MISMATCH ({count})"
    if count != 15:
        all_15 = False
    print(f"{p:25}: {status}")

print("\n=== CAFE SCAN VERIFICATION ===")
cafe_found = False
for f in sorted(glob.glob("*.html") + glob.glob("assets/css/*.css") + glob.glob("assets/js/*.js")):
    c = open(f, encoding="utf-8", errors="ignore").read()
    # Check for cafe word (ignore uppercase/lowercase)
    m = re.findall(r'\bcafe\b|\bcafes\b|\bcafé\b|\bcafés\b', c, re.IGNORECASE)
    if m:
        print(f"FOUND CAFE in {f}: {len(m)} matches -> {m[:3]}")
        cafe_found = True

if not cafe_found:
    print("ZERO cafe mentions across all HTML, CSS, and JS files! PASS!")

if all_15 and not cafe_found:
    print("\nALL CONSTRAINTS FULLY SATISFIED!")
