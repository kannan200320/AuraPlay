files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    has_back = 'Back to Public Arena' in c
    has_sidebar_toggles_hidden_on_lg = 'flex lg:hidden items-center justify-between border-t border-slate-200' in c
    has_desktop_toggles = 'rtl-toggle-btn' in c and 'theme-toggle-btn' in c
    print(f"[{f}]: has_back={has_back}, sidebar_toggles_hidden_on_lg={has_sidebar_toggles_hidden_on_lg}, desktop_toggles={has_desktop_toggles}")
    assert not has_back, f"Found 'Back to Public Arena' in {f}"
    assert has_sidebar_toggles_hidden_on_lg, f"Sidebar toggles not hidden on lg in {f}"
print("All specific checks passed!")
