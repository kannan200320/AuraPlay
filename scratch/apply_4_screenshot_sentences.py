import re

files = ['book-slot.html', 'membership.html', 'blog.html', 'contact.html']

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace font-medium hero-subtitle with font-bold hero-subtitle-boosted
    old_cls = 'font-medium hero-subtitle'
    new_cls = 'font-bold hero-subtitle-boosted'
    
    if old_cls in content:
        content = content.replace(old_cls, new_cls, 1)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {p} to use {new_cls}!")
    else:
        print(f"Warning: '{old_cls}' not found in {p}")
