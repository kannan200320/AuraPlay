with open('book-slot.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Floor Map' in line or 'floor map' in line.lower() or 'station-btn' in line:
        print(f"Line {i+1}: {line.strip()[:80].encode('ascii', 'backslashreplace').decode('ascii')}")
