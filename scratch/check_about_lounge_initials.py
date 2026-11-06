for f in ['about.html', 'player-lounge.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        if any(initial in line for initial in ['SP', 'JR', 'DS', 'TC']):
            print(f"=== {f} line {i+1} ===")
            start = max(0, i - 4)
            end = min(len(lines), i + 8)
            for j in range(start, end):
                print(f"  {j+1}: {lines[j].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
