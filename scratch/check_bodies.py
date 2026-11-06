pages = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    b_idx = c.find('<body')
    b_end = c.find('>', b_idx)
    print(p, ':', c[b_idx:b_end+1])
