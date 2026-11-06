for f in ['dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for i, line in enumerate(lines):
        if 'Website' in line:
            start = max(0, i - 2)
            end = min(len(lines), i + 3)
            print(f"=== {f} ===")
            for j in range(start, end):
                print(f"{j+1}: {lines[j].strip().encode('ascii', 'backslashreplace').decode('ascii')}")
