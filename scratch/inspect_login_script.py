with open('login.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(250, len(lines)):
    print(f"{i+1}: {lines[i].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
