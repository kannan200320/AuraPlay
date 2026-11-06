import glob
import re

dash_files = sorted(glob.glob('dashboard*.html'))

for f in dash_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    matches = re.findall(r'<(?:button|a)[^>]+class=["\']([^"\']+)["\'][^>]*>(.*?)</(?:button|a)>', c, re.DOTALL)
    print(f"=== {f} ===")
    for cls, inner in matches:
        if any(skip in cls for skip in ['theme-toggle-btn', 'rtl-toggle-btn', 'sidebar-toggle-btn', 'dashboard-sidebar-close', 'dash-nav-link']):
            continue
        if any(bg in cls for bg in ['bg-', 'from-']):
            txt = re.sub(r'<[^>]+>', '', inner).strip()[:35]
            if txt:
                bgs = [k for k in cls.split() if k.startswith('bg-') or k.startswith('from-') or k.startswith('to-') or k.startswith('via-') or k.startswith('hover:from-') or k.startswith('hover:to-') or k.startswith('hover:bg-')]
                line = f"  [{txt}]: {' '.join(bgs)}"
                print(line.encode('ascii', 'backslashreplace').decode('ascii'))
