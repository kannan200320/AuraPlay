import sys

sys.stdout.reconfigure(encoding='utf-8')

dash_payments = open('dashboard-payments.html', encoding='utf-8').read()
idx1 = dash_payments.find('<!-- Method 1: Visa -->')
print(dash_payments[idx1:idx1+2500])
