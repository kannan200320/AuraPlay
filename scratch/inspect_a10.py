import sys
sys.stdout.reconfigure(encoding='utf-8')

c = open('book-slot.html', encoding='utf-8').read()
idx = c.find('data-seat="A10"')
print(c[idx:idx+600])
