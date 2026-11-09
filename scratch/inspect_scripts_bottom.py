import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== dashboard-payments.html scripts ===")
c = open('dashboard-payments.html', encoding='utf-8').read()
idx = c.find('assets/js/main.js')
print(c[idx:idx+3500])

print("\n=== dashboard-packs.html scripts ===")
c2 = open('dashboard-packs.html', encoding='utf-8').read()
idx2 = c2.find('assets/js/main.js')
print(c2[idx2:idx2+3500])
