import re

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    content = open(p, encoding='utf-8').read()
    m = re.search(r'(<div[^>]*hero-bg-container[^>]*>.*?</div>\s*</div>)', content, re.DOTALL)
    if m:
        print(f"=== {p} ===")
        print(m.group(1))
        print()
