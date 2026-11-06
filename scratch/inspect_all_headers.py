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
    'blog-detail.html',
    'blog-detail-cs2-subtick.html',
    'blog-detail-direct-drive-sim.html',
    'blog-detail-wooting-rapid-trigger.html',
    'blog-detail-zero-bufferbloat.html'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    has_drawer = 'mobile-menu-drawer' in txt or 'mobile-drawer' in txt
    has_header = '</header>' in txt
    print(f"{p}: has_header={has_header}, has_drawer={has_drawer}")
