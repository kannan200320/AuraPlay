import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.js'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
                if 'sidebar-toggle-btn' in txt or 'dashboard-sidebar' in txt:
                    print(f"Found in {p}")
