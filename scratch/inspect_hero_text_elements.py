import re

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    content = open(p, encoding='utf-8').read()
    m = re.search(r'<!--\s*(?:={2,}\s*)?SECTION 1:.*?<section([^>]*)>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    if m:
        sec = m.group(2)
        # extract badge, title, subtitle
        badge = re.search(r'<div[^>]*class="[^"]*(?:inline-flex|badge)[^"]*"[^>]*>.*?</div>', sec, re.DOTALL)
        title = re.search(r'<h1[^>]*>.*?</h1>', sec, re.DOTALL)
        p_tag = re.search(r'<p[^>]*class="[^"]*hero-subtitle[^"]*"[^>]*>.*?</p>', sec, re.DOTALL)
        if not p_tag:
            p_tag = re.search(r'<p[^>]*class="[^"]*text-(?:base|sm|lg)[^"]*"[^>]*>.*?</p>', sec, re.DOTALL)
            
        print(f"=== {p} ===")
        if badge:
            b_text = re.sub(r'<[^>]+>', ' ', badge.group(0))
            print("Badge:", re.sub(r'\s+', ' ', b_text).strip()[:70])
        if title:
            t_text = re.sub(r'<[^>]+>', ' ', title.group(0))
            print("Title:", re.sub(r'\s+', ' ', t_text).strip()[:70])
        if p_tag:
            p_text = re.sub(r'<[^>]+>', ' ', p_tag.group(0))
            print("Subtitle tag:", p_tag.group(0)[:120])
            print("Subtitle text:", re.sub(r'\s+', ' ', p_text).strip()[:100])
        print()
