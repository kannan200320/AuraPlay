with open('pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(120, 180):
    print(f"{i+1}: {lines[i].encode('ascii', 'backslashreplace').decode('ascii')}", end='')
