with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(830, 865):
    print(f"{i+1}: {lines[i].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
