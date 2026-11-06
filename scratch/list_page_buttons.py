import glob
import re

html_files = sorted(glob.glob('*.html'))

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    btns = re.findall(r'<button\b[^>]*class=["\']([^"\']+)["\'][^>]*>(.*?)</button>', c, re.DOTALL)
    links = re.findall(r'<a\b[^>]*class=["\']([^"\']+)["\'][^>]*>(.*?)</a>', c, re.DOTALL)

    colored = []
    for cls, inner in btns + links:
        if any(skip in cls for skip in ['theme-toggle-btn', 'rtl-toggle-btn', 'pwd-toggle-btn', 'sidebar-toggle-btn', 'mobile-dropdown-btn', 'dashboard-sidebar-close', 'mobile-menu-close', 'dash-nav-link']):
            continue
        has_btn_shape = any(p in cls for p in ['px-', 'py-', 'btn', 'rounded-xl', 'rounded-2xl', 'rounded-lg'])
        has_color = any(c_name in cls for c_name in [
            'from-', 'to-', 'via-', 'bg-pink', 'bg-rose', 'bg-amber', 'bg-emerald', 'bg-purple', 'bg-cyan', 'bg-violet', 'bg-blue'
        ])
        if has_btn_shape and has_color:
            txt = re.sub(r'<[^>]+>', '', inner).strip()
            txt = ' '.join(txt.split())[:35]
            if txt and not any(tag in txt for tag in ['Lv 28', 'Arena Online', 'Ping:']):
                colored.append((txt, cls))

    if colored:
        print(f"=== {f} ({len(colored)}) ===")
        for txt, cls in colored[:15]:
            bgs = [k for k in cls.split() if any(k.startswith(p) for p in ['bg-', 'from-', 'to-', 'via-', 'hover:from-', 'hover:to-', 'hover:bg-'])]
            line = f"  [{txt}]: {' '.join(bgs)}"
            print(line.encode('ascii', 'backslashreplace').decode('ascii'))
        if len(colored) > 15:
            print(f"  ... and {len(colored) - 15} more")
