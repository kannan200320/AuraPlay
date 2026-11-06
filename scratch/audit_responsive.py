import os, re

html_files = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]

print("Scanning for tables without overflow-x-auto:")
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    # Check tables
    table_pos = [m.start() for m in re.finditer(r'<table', txt)]
    for pos in table_pos:
        preceding = txt[max(0, pos-200):pos]
        if 'overflow-x-auto' not in preceding and 'overflow-auto' not in preceding:
            line_no = txt[:pos].count('\n') + 1
            print(f"  {f}:{line_no} <table> might lack overflow wrapper")

print("\nScanning for fixed min-w over 280px that might cause 320px overflow:")
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    for m in re.finditer(r'min-w-\[(\d+)px\]', txt):
        val = int(m.group(1))
        if val > 280:
            line_no = txt[:m.start()].count('\n') + 1
            # Check if inside an overflow container
            preceding = txt[max(0, m.start()-300):m.start()]
            if 'overflow' not in preceding:
                print(f"  {f}:{line_no} min-w-[{val}px] without obvious overflow container")
