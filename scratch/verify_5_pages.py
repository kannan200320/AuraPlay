import re

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    s1 = re.search(r'(<!--\s*(?:=+)?\s*SECTION\s+1[^>]*-->\s*<section\b[^>]*>)(.*?)(</section>)', c, re.DOTALL).group(2)
    p_tag = re.search(r'<p\b[^>]*hero-subtitle[^>]*>(.*?)</p>', s1, re.DOTALL).group(0).strip()
    scrim = re.search(r'<div class="absolute inset-0 bg-gradient-to-[^>]*>', s1).group(0)
    print(f"=== {p} ===")
    print("Scrim:", scrim)
    print("P:", p_tag)
    print()
