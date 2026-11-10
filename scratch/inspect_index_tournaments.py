import re, sys
sys.stdout.reconfigure(encoding='utf-8')

index = open('index.html', encoding='utf-8').read()

m = re.search(r'VALORANT 5V5 OPEN LAN', index, re.IGNORECASE)
if m:
    idx = m.start()
    sec_start = index.rfind('<section', 0, idx)
    sec_end = index.find('</section>', idx) + len('</section>')
    print("=== TOURNAMENTS SECTION IN INDEX.HTML ===")
    print(index[sec_start:sec_end])
else:
    print("Not found in index.html")
