for f in ['index.html', 'player-lounge.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    print(f"=== {f} Hero Section 1 ===")
    for i in range(230, 270):
        if i < len(lines):
            l = lines[i].strip()
            if l.startswith('<h1') or 'Win Big' in l or 'Radically Upgraded' in l or 'Step into' in l or 'Forget cramped' in l:
                print(f"  {i+1}: {l.encode('ascii', 'backslashreplace').decode('ascii')}")
