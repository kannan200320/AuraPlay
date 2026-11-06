import re

files = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'blog.html', 'contact.html', 'book-slot.html']
for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.findall(r'<p[^>]*class="([^"]*)"[^>]*>(.*?)</p>', content, re.DOTALL)
    for cls, text in m[:3]:
        clean_text = ' '.join(text.split())[:70]
        if 'hero-subtitle' in cls or 'text-black' in cls or 'text-slate' in cls or 'hero' in cls:
            print(f"{p}: class='{cls}' | text: '{clean_text}'")
