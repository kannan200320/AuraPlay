import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== index.html lines 560-620 (Section 3 Cards) ===")
for i in range(560, 620):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')

print("\n=== index.html lines 1110-1155 (Section 15 Pro Stage) ===")
for i in range(1110, 1155):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
