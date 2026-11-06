for f in ['404.html', 'coming-soon.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    print(f"=== {f} ({len(lines)} lines) ===")
    for i in range(min(50, len(lines))):
        if 'header' in lines[i].lower() or 'nav' in lines[i].lower():
            print(f"{i+1}: {lines[i].strip()[:80]}")
