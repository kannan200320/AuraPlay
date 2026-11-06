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
    # Find mobile drawer location
    drawer_start = txt.find('<!-- ================= MOBILE MENU DRAWER ================= -->')
    if drawer_start == -1:
        drawer_start = txt.find('id="mobile-drawer"')
        if drawer_start == -1:
            drawer_start = txt.find('id="mobile-menu-drawer"')
    main_start = txt.find('<main')
    print(f"{p}: drawer_start={drawer_start}, main_start={main_start}")
