with open('book-slot.html', 'r', encoding='utf-8') as f:
    c = f.read()
import re
print("section tags:", len(re.findall(r'<section', c)))
print("data-section tags:", len(re.findall(r'data-section', c)))
