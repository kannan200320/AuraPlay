import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    c = f.read()

tags = re.findall(r'<(?:button|a)\b[^>]+class=["\']([^"\']+)["\'][^>]*>(.*?)</(?:button|a)>', c, re.DOTALL)
for cls, inner in tags:
    if any(skip in cls for skip in ['theme-toggle-btn', 'rtl-toggle-btn', 'mobile-dropdown-btn', 'mobile-menu-close', 'dash-nav-link']):
        continue
    if 'nav-link' in cls or 'text-[10px]' in cls or 'text-[11px]' in cls:
        continue
    has_btn = any(p in cls for p in ['px-', 'py-', 'btn'])
    has_col = any(k in cls for k in ['bg-', 'from-']) and not any(k in cls for k in ['bg-slate', 'bg-darkslate', 'bg-transparent', 'bg-white'])
    if has_btn and has_col:
        txt = re.sub(r'<[^>]+>', '', inner).strip()
        txt = ' '.join(txt.split())[:35]
        line = f"[{txt}]: {cls}"
        print(line.encode('ascii', 'backslashreplace').decode('ascii'))
