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
    print(f"==================== {p} ====================")
    # find section 1
    m = re.search(r'<!--\s*(?:={2,}\s*)?SECTION 1:[^>]*-->\s*<section([^>]*)>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    if m:
        sec_body = m.group(2)
        # find title
        title_m = re.search(r'<h1[^>]*>(.*?)</h1>', sec_body, re.DOTALL)
        # find subtitle p
        p_m = re.search(r'<p[^>]*class="[^"]*(?:hero-subtitle|leading-relaxed|max-w-2xl)[^"]*"[^>]*>(.*?)</p>', sec_body, re.DOTALL)
        # find badge
        badge_m = re.search(r'<(?:div|span)[^>]*class="[^"]*(?:inline-flex|badge|rounded-full)[^"]*"[^>]*>.*?</(?:div|span)>', sec_body, re.DOTALL)
        
        print("TITLE HTML:", title_m.group(0).strip() if title_m else "None")
        print("SUBTITLE HTML:", p_m.group(0).strip() if p_m else "None")
        print()
