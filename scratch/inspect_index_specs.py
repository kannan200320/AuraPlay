with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Fanatec Podium DD2 25Nm Force' in line:
        start = max(0, i - 50)
        end = min(len(lines), i + 60)
        for j in range(start, end):
            ascii_line = lines[j].encode('ascii', 'backslashreplace').decode('ascii')
            print(f"{j+1}: {ascii_line}", end='')
        break
