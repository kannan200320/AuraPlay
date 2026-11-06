pages = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    has_mobile_hdr = 'flex lg:hidden items-center justify-between' in c
    has_lap_hdr = 'hidden lg:flex items-center justify-between' in c
    has_docked_sidebar = 'lg:translate-x-0' in c
    has_docked_offset = 'lg:pl-64' in c
    print(f"[{p}]: mobile_hdr={has_mobile_hdr}, lap_hdr={has_lap_hdr}, docked_sidebar={has_docked_sidebar}, docked_offset={has_docked_offset}")
