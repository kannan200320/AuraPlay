with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(68, 136):
    print(f"{i+1}: {lines[i].encode('ascii', 'backslashreplace').decode('ascii')}", end='')
