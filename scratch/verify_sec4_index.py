with open('index.html', 'r', encoding='utf-8') as f:
    txt = f.read()

# Check Section 4 in index.html
import re
print("Section 4 span colors before:")
for m in re.findall(r'<li[^>]*><span class="([^"]*)">.*?</span><span class="[^"]*">([^<]*)</span>', txt):
    if any(k in m[1] for k in ['Intel Core', 'AMD Ryzen', 'Fanatec', 'PlayStation 5']):
        print(m[0], "-->", m[1])
