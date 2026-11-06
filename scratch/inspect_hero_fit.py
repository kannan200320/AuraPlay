with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

with open('player-lounge.html', 'r', encoding='utf-8') as f:
    lounge_content = f.read()

import re

def get_sec1(html):
    start = html.find('<section')
    end = html.find('</section>', start) + len('</section>')
    return html[start:end]

print("=== INDEX.HTML SECTION 1 OPENING & PADDING ===")
sec1_idx = get_sec1(idx_content)
# print first 15 lines of sec1_idx
for line in sec1_idx.splitlines()[:25]:
    print(line)

print("\n=== PLAYER-LOUNGE.HTML SECTION 1 OPENING & PADDING ===")
sec1_lounge = get_sec1(lounge_content)
for line in sec1_lounge.splitlines()[:25]:
    print(line)
