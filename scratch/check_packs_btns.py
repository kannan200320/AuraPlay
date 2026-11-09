import re, sys
sys.stdout.reconfigure(encoding='utf-8')

packs = open('dashboard-packs.html', encoding='utf-8').read()
for m in re.finditer(r'<button[^>]*>.*?Purchase Now.*?</button>', packs, re.DOTALL | re.IGNORECASE):
    print(m.group(0))

for m in re.finditer(r'<button[^>]*>.*?Buy Custom Hours.*?</button>', packs, re.DOTALL | re.IGNORECASE):
    print(m.group(0))
