import re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in ['login.html', 'register.html']:
    content = open(f, encoding='utf-8').read()
    print(f"=== {f} ===")
    for m in re.finditer(r'<button[^>]*>(?:(?!</button>).)*?(?:Google|Apple)(?:(?!</button>).)*?</button>', content, re.DOTALL | re.IGNORECASE):
        print(m.group(0))
    for m in re.finditer(r'<a[^>]*>(?:(?!</a>).)*?(?:Google|Apple)(?:(?!</a>).)*?</a>', content, re.DOTALL | re.IGNORECASE):
        print(m.group(0))
