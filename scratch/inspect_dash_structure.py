with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(50, 150):
    print(f"{i+1}: {lines[i].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
