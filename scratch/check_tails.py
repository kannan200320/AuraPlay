files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    # Check closing tags before </body>
    idx_body = c.find('</body>')
    tail = c[idx_body-300:idx_body]
    print(f"=== {f} ===")
    print(repr(tail))
