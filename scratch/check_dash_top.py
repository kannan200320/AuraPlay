dash_files = [
    'dashboard.html',
    'dashboard-packs.html',
    'dashboard-history.html',
    'dashboard-payments.html',
    'dashboard-settings.html'
]

for df in dash_files:
    with open(df, 'r', encoding='utf-8') as f:
        txt = f.read()
    body_idx = txt.find('<body')
    main_idx = txt.find('<main')
    print(f"=== {df} ===")
    print(f"body to main length: {main_idx - body_idx}")
