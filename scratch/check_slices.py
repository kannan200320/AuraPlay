files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    aside_pos = c.find('<aside')
    before_aside = c[aside_pos-100:aside_pos]
    header_end = c.find('</header>') + len('</header>')
    after_header = c[header_end:header_end+80]
    print(f"=== {f} ===")
    print("BEFORE ASIDE:", repr(before_aside))
    print("AFTER HEADER:", repr(after_header))
