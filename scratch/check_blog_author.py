with open('blog-detail.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Eric Lin' in line or 'Author' in line or 'Lead Systems' in line:
        print(f"Line {i+1}: {line.strip()[:90]}")
        for j in range(max(0, i-3), min(len(lines), i+6)):
            print(f"  {j+1}: {lines[j].strip()[:80]}")
        break
