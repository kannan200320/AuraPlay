import os, re

html_files = [f for f in sorted(os.listdir('.')) if f.endswith('.html')]

print("Searching for whitespace-nowrap that might cause 320px overflow:")
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    # Check for whitespace-nowrap
    matches = re.finditer(r'<[^>]*class="([^"]*whitespace-nowrap[^"]*)"', txt)
    for m in matches:
        cls = m.group(1)
        # If it's a large container or inside flex without wrap/overflow
        if 'flex' in cls and 'overflow' not in cls and 'hidden' not in cls:
            line_no = txt[:m.start()].count('\n') + 1
            print(f"  {f}:{line_no} -> {cls[:90]}")
