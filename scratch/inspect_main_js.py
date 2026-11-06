with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    txt = f.read()

import re
print("Mobile menu js logic:")
for line in txt.splitlines():
    if any(k in line.lower() for k in ['mobile-menu', 'mobile-dropdown', 'mobiledropdown', 'theme-toggle', 'rtl-toggle']):
        print(line[:100])
