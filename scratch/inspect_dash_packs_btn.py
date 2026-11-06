for f in ['dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        if 'Website' in line:
            print(f"=== {f} line {i+1} ===")
            for j in range(max(0, i-2), min(len(lines), i+4)):
                print(f"{j+1}: {repr(lines[j])}")
            break
