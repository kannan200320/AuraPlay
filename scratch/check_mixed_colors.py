import os, re

for f in sorted(os.listdir('.')):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
        # look for checkmark spans with mixed colors
        matches = re.findall(r'<span class="([^"]*(?:purple|pink|emerald|amber)[^"]*font-bold[^"]*)">.*?</span>', txt)
        if matches:
            print(f"{f}: {len(matches)} matches: {set(matches)}")
