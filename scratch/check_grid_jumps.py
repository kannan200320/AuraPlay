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
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    print(f"=== {p} ===")
    matches = re.finditer(r'class="([^"]*grid\s+grid-cols-[^"]*)"', txt)
    for m in matches:
        cls = m.group(1)
        # check if it lacks md: or sm: or jumps to lg:
        if ('lg:grid-cols-3' in cls or 'lg:grid-cols-4' in cls or 'lg:grid-cols-5' in cls) and 'md:grid-cols' not in cls and 'sm:grid-cols' not in cls:
            line_no = txt[:m.start()].count('\n') + 1
            print(f"  Line {line_no}: JUMPS TO LG: {cls}")
