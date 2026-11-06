with open('pricing.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'grid grid-cols' in line:
        print(f"pricing.html line {i+1}: {line.strip()[:90]}")
