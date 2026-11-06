with open('index.html', 'r', encoding='utf-8') as f:
    c1 = f.read()
with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

import re
def get_info(c):
    m_main = re.search(r'<main\b[^>]*>', c).group(0)
    m_sec = re.search(r'<section\b[^>]*>', c).group(0)
    m_col = re.search(r'<div class="lg:col-span-7\b[^>]*>', c).group(0)
    m_h1 = re.search(r'<h1\b[^>]*>', c).group(0)
    m_p = re.search(r'<p\b[^>]*hero-subtitle-boosted\b[^>]*>', c).group(0)
    return m_main, m_sec, m_col, m_h1, m_p

print('=== HOME PAGE 1 (index.html) ===')
for item in get_info(c1):
    print(' ', item)

print('\n=== HOME PAGE 2 (player-lounge.html) ===')
for item in get_info(c2):
    print(' ', item)
