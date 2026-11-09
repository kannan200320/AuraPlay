import sys
sys.stdout.reconfigure(encoding='utf-8')

c = open('dashboard-history.html', encoding='utf-8').read()
idx = c.find('Previous')
print(c[idx-50:idx+350])
