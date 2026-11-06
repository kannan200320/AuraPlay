with open('login.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(50, 110):
    print(f"{i+1}: {lines[i].encode('ascii', 'backslashreplace').decode('ascii')}", end='')
