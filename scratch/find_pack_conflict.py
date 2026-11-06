with open('dashboard-packs.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
match = re.search(r'sidebar.*?toggle', c, re.DOTALL)
if match:
    idx = match.start()
    print(repr(c[idx-50:idx+250]))
else:
    print("No regex match")
