import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    txt = f.read()

matches = re.findall(r'<li[^>]*><span class="([^"]*)">([^<]*)</span><span class="[^"]*">([^<]*)</span>', txt)
classes = set(m[0] for m in matches)
print("Unique classes:", classes)
