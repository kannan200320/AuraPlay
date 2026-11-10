import re

pages = ['about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    content = open(p, encoding='utf-8').read()
    print(f"=== {p} ===")
    
    # Check bg container
    bg_m = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', content, re.DOTALL)
    print("  BG match:", bool(bg_m))
    
    # Check subtitle
    p_m = re.search(r'<p class="[^"]*hero-subtitle-boosted[^"]*">.*?</p>', content, re.DOTALL)
    print("  Subtitle match:", bool(p_m))
    if p_m:
        print("    P tag length:", len(p_m.group(0)))
