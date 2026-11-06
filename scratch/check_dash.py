import re

files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    has_aside = '<aside id="dashboard-sidebar"' in c
    has_head = '<header' in c
    has_toggle = 'sidebar-toggle-btn' in c
    print(f"{f}: len={len(c)}, aside={has_aside}, head={has_head}, toggle={has_toggle}")
