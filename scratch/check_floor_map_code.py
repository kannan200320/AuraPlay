with open('book-slot.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(341, 380):
    print(f"{i+1}: {lines[i].strip()[:90].encode('ascii', 'backslashreplace').decode('ascii')}")
