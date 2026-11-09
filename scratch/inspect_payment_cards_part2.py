import sys
sys.stdout.reconfigure(encoding='utf-8')

dash = open('dashboard-payments.html', encoding='utf-8').read()
idx = dash.find('id="label-mc"')
print(dash[idx:idx+2500])
