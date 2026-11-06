import re

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    s1_match = re.search(r'(<!--\s*(?:=+)?\s*SECTION\s+1[^>]*-->\s*<section\b[^>]*>)(.*?)(</section>)', c, re.DOTALL)
    if s1_match:
        s1 = s1_match.group(2)
        print(f"=== {p} ===")
        # find bg div
        bg_div = re.search(r'<div class="absolute inset-0 z-0[^>]*>.*?</div>\s*</div>', s1, re.DOTALL)
        if bg_div:
            print("BG:\n" + bg_div.group(0).strip())
        h1 = re.search(r'<h1\b[^>]*>.*?</h1>', s1, re.DOTALL)
        if h1:
            print("H1:\n" + h1.group(0)[:150] + "...")
        p_tag = re.search(r'<p\b[^>]*>.*?</p>', s1, re.DOTALL)
        if p_tag:
            print("P:\n" + p_tag.group(0)[:150] + "...")
        print()
