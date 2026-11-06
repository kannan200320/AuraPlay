import glob
import re

html_files = sorted(glob.glob('*.html'))
gradient_elements = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    matches = re.findall(r'<(?:button|a)[^>]+class=["\']([^"\']*bg-gradient-to-[^"\']*)["\'][^>]*>', c)
    for m in matches:
        gradient_elements.append((f, m))

print(f"Total gradient buttons/links: {len(gradient_elements)}")
unique_grads = set()
for f, m in gradient_elements:
    # Extract gradient tokens
    tokens = [t for t in m.split() if t.startswith('from-') or t.startswith('to-') or t.startswith('via-') or t.startswith('bg-gradient-')]
    unique_grads.add(' '.join(tokens))

for g in sorted(unique_grads):
    print("  GRAD:", g)
