import glob
import re

html_files = sorted(glob.glob('*.html'))

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # Find all <button ...>...</button>
    btns = re.findall(r'<button\b([^>]*)>(.*?)</button>', c, re.DOTALL)
    colored_btns = []
    for attrs, inner in btns:
        cls_match = re.search(r'class=["\']([^"\']+)["\']', attrs)
        if cls_match:
            cls = cls_match.group(1)
            if any(skip in cls for skip in ['theme-toggle-btn', 'rtl-toggle-btn', 'pwd-toggle-btn', 'sidebar-toggle-btn', 'mobile-dropdown-btn', 'dashboard-sidebar-close', 'mobile-menu-close']):
                continue
            if any(bg in cls for bg in ['bg-gradient', 'bg-pink', 'bg-purple', 'bg-amber', 'bg-emerald', 'bg-cyan', 'bg-rose', 'bg-blue', 'bg-indigo']):
                inner_text = re.sub(r'<[^>]+>', '', inner).strip()
                colored_btns.append(('BUTTON', inner_text[:30], cls))

    # Find all <a ...>...</a> that look like CTA buttons
    links = re.findall(r'<a\b([^>]*)>(.*?)</a>', c, re.DOTALL)
    for attrs, inner in links:
        cls_match = re.search(r'class=["\']([^"\']+)["\']', attrs)
        if cls_match:
            cls = cls_match.group(1)
            if any(bg in cls for bg in ['bg-gradient', 'bg-pink', 'bg-purple', 'bg-amber', 'bg-emerald', 'bg-cyan', 'bg-rose', 'bg-blue', 'bg-indigo']):
                if 'dash-nav-link' in cls or 'nav-link' in cls or 'rounded-full px-3 py-1' in cls or 'text-[10px]' in cls:
                    continue
                inner_text = re.sub(r'<[^>]+>', '', inner).strip()
                colored_btns.append(('LINK-BTN', inner_text[:30], cls))

    if colored_btns:
        print(f"=== {f} ({len(colored_btns)} buttons) ===")
        for btype, text, cls in colored_btns:
            bgs = [k for k in cls.split() if k.startswith('bg-') or k.startswith('from-') or k.startswith('to-') or k.startswith('via-') or k.startswith('hover:from-') or k.startswith('hover:to-') or k.startswith('hover:bg-')]
            line = f"  {btype} [{text}]: {' '.join(bgs)}"
            print(line.encode('ascii', 'backslashreplace').decode('ascii'))
