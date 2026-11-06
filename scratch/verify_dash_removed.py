for f in ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    if 'hidden sm:inline-flex' in txt and 'Website' in txt:
        print(f"STILL PRESENT in {f}")
    else:
        print(f"VERIFIED REMOVED in {f}")
