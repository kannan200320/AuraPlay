import glob
import re

html_files = sorted(glob.glob('*.html'))
faint_light_text = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # Check for bare text-slate-300, text-slate-400, text-gray-300, text-gray-400 on p or span or div
    matches = re.findall(r'<(?:p|span|div|h1|h2|h3|h4|li)\b[^>]*class=["\']([^"\']+)["\'][^>]*>(.*?)</(?:p|span|div|h1|h2|h3|h4|li)>', c, re.DOTALL)
    for cls, inner in matches:
        tokens = cls.split()
        for t in tokens:
            if t in ['text-slate-300', 'text-slate-400', 'text-gray-300', 'text-gray-400']:
                # Is there a dark:text- token? If not, it means this faint text applies in light mode too!
                has_dark = any(tok.startswith('dark:text-') for tok in tokens)
                if not has_dark:
                    # check if inside a permanent dark container
                    txt = re.sub(r'<[^>]+>', '', inner).strip()
                    txt = ' '.join(txt.split())[:35]
                    if txt:
                        faint_light_text.append((f, t, txt, cls))

print(f"Total bare faint text found: {len(faint_light_text)}")
for f, t, txt, cls in faint_light_text[:20]:
    line = f"[{f}] {t}: {txt}"
    print(line.encode('ascii', 'backslashreplace').decode('ascii'))
