import re

files = [
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

for f in files:
    content = open(f, encoding='utf-8').read()
    # find hero-bg-container
    bg_m = re.search(r'(<div[^>]*hero-bg-container[^>]*>.*?</div>\s*</div>)', content, re.DOTALL)
    print(f"=== {f} ===")
    if bg_m:
        print("  Found bg container:", len(bg_m.group(1)), "chars")
    else:
        print("  WARNING: bg container NOT found!")
