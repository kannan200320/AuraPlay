import glob
import re

html_files = sorted(glob.glob('*.html'))
btn_color_patterns = [
    r'bg-gradient-to-[a-z]+[^\s"\'<>]+',
    r'bg-(?:pink|rose|amber|yellow|emerald|green|teal|indigo|purple|violet|red|orange|cyan|blue)-[0-9]+',
]

findings = {}

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # Find all buttons and links styled as buttons
    # E.g. <button ...> and <a ... class="... py- ... px- ...">
    elements = re.findall(r'<(?:button|a)[^>]+class=["\']([^"\']+)["\'][^>]*>', c)
    for cls in elements:
        # Check if it looks like a colored CTA button (not a simple icon or transparent link)
        if any(term in cls for term in ['px-', 'py-', 'btn', 'rounded-']) and ('bg-' in cls):
            for bg in cls.split():
                if bg.startswith('bg-') and not bg.startswith('bg-slate') and not bg.startswith('bg-darkslate') and not bg.startswith('bg-white') and not bg.startswith('bg-transparent') and not bg.startswith('bg-black'):
                    findings.setdefault(bg, 0)
                    findings[bg] += 1

print("Found button/badge background classes:")
for bg, count in sorted(findings.items(), key=lambda x: -x[1])[:40]:
    print(f"  {bg}: {count}")
