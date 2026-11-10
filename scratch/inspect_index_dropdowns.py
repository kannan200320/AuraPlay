import re, sys
sys.stdout.reconfigure(encoding='utf-8')

c = open('index.html', encoding='utf-8').read()
matches = re.finditer(r'<div class="relative group[^"]*".*?</div>\s*</div>', c, re.DOTALL)
for i, m in enumerate(matches):
    print(f"--- Dropdown {i+1} ---")
    print(m.group(0)[:400])
