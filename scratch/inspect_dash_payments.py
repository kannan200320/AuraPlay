import sys

sys.stdout.reconfigure(encoding='utf-8')

dash_payments = open('dashboard-payments.html', encoding='utf-8').read()
idx1 = dash_payments.find('SAVED PAYMENT METHODS')
print("=== SAVED PAYMENT METHODS SECTION ===")
print(dash_payments[idx1:idx1+2000])

idx2 = dash_payments.find('INSTANT WALLET RELOAD')
print("\n=== INSTANT WALLET RELOAD SECTION ===")
print(dash_payments[idx2:idx2+2000])
