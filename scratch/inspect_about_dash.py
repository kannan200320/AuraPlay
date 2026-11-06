import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('about.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("=== about.html lines 810-845 ===")
for i in range(810, min(845, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("\n=== dashboard.html lines 190-230 ===")
for i in range(190, min(230, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
