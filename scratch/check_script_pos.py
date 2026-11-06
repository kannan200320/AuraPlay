files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    script_pos = c.rfind('<script')
    print(f"=== {f} ===")
    print(repr(c[script_pos-100:script_pos]))
