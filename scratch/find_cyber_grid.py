import glob
import re

html_files = sorted(glob.glob('*.html'))
for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    count = c.count('cyber-grid')
    if count:
        print(f"{f}: {count} occurrences of cyber-grid")
