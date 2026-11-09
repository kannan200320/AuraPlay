import re, sys
sys.stdout.reconfigure(encoding='utf-8')

packs = open('dashboard-packs.html', encoding='utf-8').read()
matches = re.findall(r'<button[^>]*>[^<]*Purchase Now[^<]*</button>', packs, re.IGNORECASE)
for m in matches:
    print(m)
