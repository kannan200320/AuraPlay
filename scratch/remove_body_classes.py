import re

html_files = [
    ('index.html', 'bg-page-home1 '),
    ('player-lounge.html', 'bg-page-home2 '),
    ('about.html', 'bg-page-about '),
    ('games.html', 'bg-page-games '),
    ('pricing.html', 'bg-page-pricing '),
]

for filename, cls_to_remove in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if cls_to_remove in content:
        content = content.replace(cls_to_remove, '', 1)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed {cls_to_remove.strip()} from {filename}")
    else:
        print(f"Warning: {cls_to_remove.strip()} not found in {filename}")
