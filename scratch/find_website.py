import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
                if 'Website' in txt:
                    for i, line in enumerate(txt.splitlines()):
                        if 'Website' in line:
                            out = f"{p}:{i+1}: {line.strip()[:100]}"
                            print(out.encode('ascii', 'backslashreplace').decode('ascii'))
