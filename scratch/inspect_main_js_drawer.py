with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = False
for i, line in enumerate(lines):
    if 'mobileMenuBtn' in line:
        for j in range(max(0, i - 5), min(len(lines), i + 70)):
            print(f"{j+1}: {lines[j].encode('ascii', 'backslashreplace').decode('ascii')}", end='')
        break
