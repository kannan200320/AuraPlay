import sys
sys.stdout.reconfigure(encoding='utf-8')

c = open('dashboard-packs.html', encoding='utf-8').read()
idx = c.find('checkout-modal')
print(c[idx:idx+1500])
