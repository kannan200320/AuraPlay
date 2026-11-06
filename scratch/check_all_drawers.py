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
    hdr_end = txt.find('</header>')
    main_start = txt.find('<main')
    snippet = txt[hdr_end + len('</header>'):main_start].strip()
    first_line = snippet.splitlines()[0] if snippet else 'NONE'
    print(f"{p}: length={len(snippet)}, first_line={first_line}")
