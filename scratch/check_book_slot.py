with open('book-slot.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'floor-map' in line or 'rig-card' in line or 'Station 01' in line or 'grid grid-cols' in line:
        print(f"book-slot.html:{i+1}: {line.strip()[:100]}")
        if 'grid grid-cols' in line and i < 400:
            for j in range(max(0, i-2), min(len(lines), i+8)):
                print(f"   {j+1}: {lines[j].strip()[:90]}")
            break
