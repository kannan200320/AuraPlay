import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=== dashboard-payments.html lines 245-275 ===")
with open('dashboard-payments.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(244, min(275, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')

print("\n=== dashboard-packs.html lines 430-460 ===")
with open('dashboard-packs.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(430, min(460, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')
