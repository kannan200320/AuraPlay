import re, glob

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    content = open(p, encoding='utf-8').read()
    m = re.search(r'(<!--\s*={2,}\s*SECTION 1:[^>]*-->\s*<section[^>]*>.*?</section>)', content, re.DOTALL | re.IGNORECASE)
    if m:
        sec = m.group(1)
        imgs = re.findall(r'<img[^>]*src=[\'"]([^\'"]+)[\'"][^>]*', sec)
        overlays = re.findall(r'<div[^>]*class=[\'"]([^\'"]*bg-gradient[^\'"]*)[\'"]', sec)
        titles = re.findall(r'<h1[^>]*>(.*?)</h1>', sec, re.DOTALL)
        paragraphs = re.findall(r'<p[^>]*class=[\'"]([^\'"]*)[\'"][^>]*>(.*?)</p>', sec, re.DOTALL)
        hero_bg_containers = re.findall(r'<div[^>]*hero-bg-container[^>]*>.*?</div>\s*</div>', sec, re.DOTALL)
        print(f'=== {p} ===')
        print('  Images:', imgs)
        print('  Overlays:', overlays)
        if titles:
            clean_title = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', titles[0])).strip()
            print('  Title:', clean_title[:80])
        if paragraphs:
            clean_p = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', paragraphs[0][1])).strip()
            print('  P[0] class:', paragraphs[0][0])
            print('  P[0] text:', clean_p[:100])
        print()
