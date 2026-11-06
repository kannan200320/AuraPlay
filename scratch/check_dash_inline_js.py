import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
                if 'sidebar-toggle-btn' in txt:
                    for i, line in enumerate(txt.splitlines()):
                        if 'sidebar-toggle-btn' in line:
                            print(f"{p}:{i+1}: {line.strip()[:80]}")
