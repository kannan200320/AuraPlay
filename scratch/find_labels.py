for f in ['index.html', 'player-lounge.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        if 'RIGS AVAILABLE' in line or 'THE SOCIAL GAMING SANCTUARY' in line:
            start = max(0, i - 4)
            end = min(len(lines), i + 6)
            print(f"=== {f} line {i+1} ===")
            for j in range(start, end):
                print(f"{j+1}: {lines[j].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
