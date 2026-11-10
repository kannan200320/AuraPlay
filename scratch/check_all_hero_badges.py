import re

pages = [
    'index.html',
    'player-lounge.html',
    'about.html',
    'games.html',
    'pricing.html',
    'membership.html',
    'book-slot.html',
    'blog.html',
    'contact.html'
]

for p in pages:
    content = open(p, encoding='utf-8').read()
    m = re.search(r'<!--\s*(?:={2,}\s*)?SECTION 1:.*?<section([^>]*)>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    if m:
        sec = m.group(2)
        # find badge before h1
        h1_pos = sec.find('<h1')
        before_h1 = sec[:h1_pos]
        badges = re.findall(r'<div[^>]*class="[^"]*(?:inline-flex|badge)[^"]*"[^>]*>.*?</div>', before_h1, re.DOTALL)
        print(f"=== {p} ===")
        if badges:
            for b in badges:
                clean = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', b)).strip()
                print("  Existing Badge:", clean)
        else:
            print("  No badge before h1")
