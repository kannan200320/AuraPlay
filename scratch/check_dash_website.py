import os, re

dash_files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in dash_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    m = re.findall(r'<!-- Back to Arena Website -->\s*<a href="index\.html"[^>]*>.*?</a>', txt, re.DOTALL)
    print(f"{f}: found {len(m)} matches")
