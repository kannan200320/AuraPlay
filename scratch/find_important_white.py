with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '!important' in line or '#ffffff' in line or '#fff' in line or '#cbd5e1' in line:
        print(f"Line {i+1}: {line.strip()}")
