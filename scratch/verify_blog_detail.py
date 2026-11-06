with open('blog-detail.html', 'r', encoding='utf-8') as f:
    txt = f.read()

import re
print("Benchmark row in blog-detail.html:")
row = re.search(r'<tr class="[^"]*">\s*<td[^>]*>QD-OLED.*?</tr>', txt, re.DOTALL)
if row:
    ascii_row = row.group(0).encode('ascii', 'backslashreplace').decode('ascii')
    print(ascii_row)
else:
    print("Row not found!")

print("\nRecommended Reads in blog-detail.html:")
recs = re.search(r'<!-- RECOMMENDED ARTICLES GRID -->.*?</div>\s*</div>\s*</div>', txt, re.DOTALL)
if recs:
    print(recs.group(0)[:600].encode('ascii', 'backslashreplace').decode('ascii'))
