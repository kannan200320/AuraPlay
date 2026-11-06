files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    target = "sidebar.classList.toggle('hidden')"
    print(f"{f}: has conflict = {target in c}")
