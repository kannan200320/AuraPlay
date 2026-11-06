import os

for f in sorted(os.listdir('.')):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
            if 'mobile-menu-drawer' in txt:
                print(f"{f}: has mobile-menu-drawer")
            else:
                print(f"{f}: NO mobile-menu-drawer")
