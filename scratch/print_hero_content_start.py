import re

for p in ['games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html', 'index.html', 'player-lounge.html']:
    c = open(p, encoding='utf-8').read()
    m = re.search(r'<!--\s*(?:={2,}\s*)?SECTION 1:.*?<section([^>]*)>(.*?)</section>', c, re.DOTALL | re.IGNORECASE)
    if m:
        sec = m.group(2)
        # remove hero-bg-container
        clean_sec = re.sub(r'<div[^>]*hero-bg-container.*?</div>\s*</div>', '', sec, flags=re.DOTALL)
        print(f"=== {p} ===")
        # print first 500 chars of clean_sec
        lines = [l.strip() for l in clean_sec.strip().splitlines() if l.strip()]
        for l in lines[:10]:
            print(" ", l[:100])
        print()
