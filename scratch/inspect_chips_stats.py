import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

m = re.search(r'<!-- Hardware Spec Chips -->.*?<!-- Fast Stats -->.*?</div>\s*</div>', idx_content, re.DOTALL)
if m:
    print("=== index.html Chips & Stats ===")
    print(m.group(0))
