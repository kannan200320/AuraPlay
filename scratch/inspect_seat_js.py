import sys
sys.stdout.reconfigure(encoding='utf-8')

book = open('book-slot.html', encoding='utf-8').read()
idx = book.find('seat-btn')
print("Seats in book-slot.html:")
idx_js = book.find('seat-btn', idx + 1000)
if idx_js != -1:
    print(book[idx_js-100:idx_js+800])
else:
    # search script for seat
    import re
    for m in re.finditer(r'<script.*?</script>', book, re.DOTALL):
        if 'seat' in m.group(0).lower():
            print("Found script:")
            print(m.group(0)[:1000])
