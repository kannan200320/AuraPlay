import sys
sys.stdout.reconfigure(encoding='utf-8')

book = open('book-slot.html', encoding='utf-8').read()
idx = book.find('seat-btn')
js_idx = book.find('querySelectorAll(\'.seat-btn\')')
print(book[js_idx:js_idx+1200])
