import glob
import re

html_files = sorted(glob.glob('*.html'))
remaining_colored_btns = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    btns = re.findall(r'<(?:button|a)\b[^>]+class=["\']([^"\']+)["\'][^>]*>(.*?)</(?:button|a)>', c, re.DOTALL)
    for cls, inner in btns:
        if any(skip in cls for skip in ['theme-toggle-btn', 'rtl-toggle-btn', 'pwd-toggle-btn', 'sidebar-toggle-btn', 'mobile-dropdown-btn', 'dashboard-sidebar-close', 'mobile-menu-close', 'dash-nav-link']):
            continue
        if 'nav-link' in cls or 'text-[10px]' in cls or 'text-[11px]' in cls or 'duration-btn' in cls or 'seat-btn' in cls:
            continue
        # Check if button has other colors: pink, purple (not to-purple-600), amber, emerald, red, etc.
        other_colors = []
        for token in cls.split():
            if any(token.startswith(p) for p in ['bg-pink', 'bg-amber', 'bg-emerald', 'bg-red', 'bg-orange', 'bg-purple', 'bg-rose', 'from-pink', 'from-amber', 'from-emerald', 'to-pink', 'to-amber']):
                other_colors.append(token)
            # Check if gradient is NOT from-cyan-500 to-purple-600
            if token.startswith('via-'):
                other_colors.append(token)
        if other_colors:
            txt = re.sub(r'<[^>]+>', '', inner).strip()
            txt = ' '.join(txt.split())[:35]
            remaining_colored_btns.append((f, txt, ' '.join(other_colors)))

print(f"Total remaining other-colored buttons: {len(remaining_colored_btns)}")
for f, txt, col in remaining_colored_btns:
    line = f"{f}: [{txt}] -> {col}"
    print(line.encode('ascii', 'backslashreplace').decode('ascii'))
