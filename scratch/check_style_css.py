with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    txt = f.read()

print(f"assets/css/style.css is {len(txt)} chars, {len(txt.splitlines())} lines")
# Search for media queries in style.css
for line in txt.splitlines():
    if '@media' in line:
        print("  ", line)
