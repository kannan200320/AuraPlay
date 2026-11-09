import sys
sys.stdout.reconfigure(encoding='utf-8')

dash = open('dashboard-payments.html', encoding='utf-8').read()
idx = dash.find('let selectedReload')
print(dash[idx-100:])
