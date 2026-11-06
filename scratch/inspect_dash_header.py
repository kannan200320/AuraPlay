with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(130, 186):
    print(f"{i+1}: {lines[i].encode('ascii', 'backslashreplace').decode('ascii')}", end='')
