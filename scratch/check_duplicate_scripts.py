import sys
sys.stdout.reconfigure(encoding='utf-8')

dash = open('dashboard-payments.html', encoding='utf-8').read()
count = dash.count('let selectedReload = 50;')
print(f"Count of 'let selectedReload = 50;' in dashboard-payments.html: {count}")

packs = open('dashboard-packs.html', encoding='utf-8').read()
count_packs = packs.count('window.handlePackBuy')
print(f"Count of 'window.handlePackBuy' in dashboard-packs.html: {count_packs}")
