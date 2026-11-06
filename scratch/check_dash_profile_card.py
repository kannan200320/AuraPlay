with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(104, 125):
    print(f"{i+1}: {lines[i].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
