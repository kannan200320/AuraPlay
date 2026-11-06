import re

pages = [
    'index.html',
    'player-lounge.html',
    'about.html',
    'games.html',
    'pricing.html',
    'book-slot.html',
    'membership.html',
    'blog.html',
    'contact.html',
    'blog-detail.html'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    rtl_m = re.search(r'<button[^>]*class="[^"]*rtl-toggle-btn[^"]*"', txt)
    theme_m = re.search(r'<button[^>]*class="[^"]*theme-toggle-btn[^"]*"', txt)
    print(f"=== {p} ===")
    if rtl_m:
        print("  RTL:", rtl_m.group(0)[:80])
    if theme_m:
        print("  Theme:", theme_m.group(0)[:80])
