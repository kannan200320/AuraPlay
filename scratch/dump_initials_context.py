import os, re

files_to_check = [
    'index.html',
    'player-lounge.html',
    'about.html',
    'games.html',
    'pricing.html',
    'membership.html',
    'book-slot.html',
    'blog.html',
    'contact.html',
    'blog-detail.html',
    'dashboard.html',
    'dashboard-settings.html'
]

for f in files_to_check:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        # Match initials in rounded-full or rounded-xl
        m = re.search(r'<(?:div|span)[^>]*rounded-(?:full|xl|2xl|3xl)[^>]*>\s*([A-Z]{2})\s*<\/(?:div|span)>', line)
        if m:
            print(f"=== {f} line {i+1} : {m.group(1)} ===")
            start = max(0, i - 4)
            end = min(len(lines), i + 8)
            for j in range(start, end):
                print(f"  {j+1}: {lines[j].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
