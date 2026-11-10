import re, sys
sys.stdout.reconfigure(encoding='utf-8')

book = open('book-slot.html', encoding='utf-8').read()
matches = re.findall(r'<button[^>]*class="[^"]*seat-btn[^"]*"[^>]*>.*?</button>', book)
print(f"Total seat buttons: {len(matches)}")
for m in matches[:15]:
    print(m)

# Find JS
idx = book.find('data-seat')
if idx != -1:
    idx2 = book.find('data-seat', idx + 500)
    while idx2 != -1:
        idx = idx2
        idx2 = book.find('data-seat', idx + 500)
    print("Last data-seat occurrence near:")
    print(book[idx-100:idx+600])
