import sys
sys.stdout.reconfigure(encoding='utf-8')

pay = open('dashboard-payments.html', encoding='utf-8').read()
idx = pay.find('window.selectPaymentMethod')
print(pay[idx:idx+1600])
