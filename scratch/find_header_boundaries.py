import re

files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    # Find position of <aside and what comes after </header>
    aside_pos = c.find('<aside')
    header_end = c.find('</header>')
    after_header = c[header_end:header_end+150] if header_end != -1 else "NOT FOUND"
    print(f"=== {f} ===")
    print(f"aside_pos: {aside_pos}, header_end: {header_end}")
    print(f"after_header: {repr(after_header)}")
