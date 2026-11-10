import sys
sys.stdout.reconfigure(encoding='utf-8')

book = open('book-slot.html', encoding='utf-8').read()
idx = book.find('Step 2: Interactive Seat Picker')
print(book[idx-200:idx+2500])
