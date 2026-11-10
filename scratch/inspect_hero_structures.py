import re

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    content = open(p, encoding='utf-8').read()
    # Find Section 1
    m = re.search(r'<!--\s*(?:={2,}\s*)?SECTION 1:.*?<section([^>]*)>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
    if m:
        sec_tag = m.group(1)
        sec_body = m.group(2)
        # Find all img tags in sec_body
        imgs = re.findall(r'<img[^>]+>', sec_body)
        # Find all background overlays
        divs = re.findall(r'<div[^>]+hero-bg-container[^>]*>.*?</div>\s*</div>', sec_body, re.DOTALL)
        if not divs:
            divs = re.findall(r'<div[^>]+absolute inset-0[^>]*>', sec_body)
        print(f"=== {p} ===")
        print("Section tag attributes:", sec_tag[:100])
        print("Images found:", len(imgs))
        for img in imgs[:3]:
            print("  IMG:", img[:120])
        print("Overlays found:", len(divs))
        for d in divs[:3]:
            print("  DIV:", d.strip().replace('\n', ' ')[:150])
        print()
