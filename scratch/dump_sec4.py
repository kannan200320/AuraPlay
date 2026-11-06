with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(447, 564):
    print(lines[i].encode('ascii', 'backslashreplace').decode('ascii'), end='')
