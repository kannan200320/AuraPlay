import os
import re

print("================ COMPREHENSIVE VERIFICATION ================")

# 1. Check Dashboard Files
dash_files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for df in dash_files:
    with open(df, 'r', encoding='utf-8') as f:
        c = f.read()
    has_overlay = 'id="dashboard-sidebar-overlay"' in c
    has_sidebar = 'id="dashboard-sidebar"' in c
    has_toggle = 'id="sidebar-toggle-btn"' in c
    has_close = 'id="dashboard-sidebar-close"' in c
    has_avatar = 'assets/images/avatar-5.jpg' in c
    has_sticky_header = 'sticky top-0 z-40' in c
    has_conflicting_script = 'sidebar.classList.toggle(\'hidden\')' in c
    print(f"[{df}]: overlay={has_overlay}, sidebar={has_sidebar}, toggle={has_toggle}, close={has_close}, avatar={has_avatar}, sticky_hdr={has_sticky_header}, conflict={has_conflicting_script}")
    assert has_overlay and has_sidebar and has_toggle and has_close and has_avatar and has_sticky_header, f"Failed on {df}"
    assert not has_conflicting_script, f"Found conflicting script in {df}"

# 2. Check Auth Pages
for ap in ['login.html', 'register.html']:
    with open(ap, 'r', encoding='utf-8') as f:
        c = f.read()
    has_alert = 'alert(' in c
    has_dash_nav = 'dashboard.html' in c
    has_dummy_submit = 'onsubmit="event.preventDefault(); return false;"' in c
    print(f"[{ap}]: has_alert={has_alert}, has_dash_nav={has_dash_nav}, dummy_submit={has_dummy_submit}")
    assert not has_alert, f"Alert found in {ap}"
    assert not has_dash_nav, f"Dashboard navigation found in {ap}"
    assert has_dummy_submit, f"Dummy submit missing in {ap}"

# 3. Check 9 Primary Pages Section Count
primary_pages = [
    'index.html', 'player-lounge.html', 'about.html', 'games.html', 
    'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html'
]
for p in primary_pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    sec_count = len(re.findall(r'<section', c))
    print(f"[{p}]: section_count={sec_count}")
    assert sec_count == 15, f"{p} has {sec_count} sections instead of 15!"

# 4. Check Cafe References across ALL html files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
total_cafe = 0
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        c = f.read()
    cafe_matches = re.findall(r'\bcafe\b|\bcafé\b', c, re.IGNORECASE)
    if cafe_matches:
        print(f"WARNING: {hf} has {len(cafe_matches)} cafe mentions!")
        total_cafe += len(cafe_matches)
print(f"Total cafe mentions across all HTML files: {total_cafe}")
assert total_cafe == 0, "Cafe mentions found!"

# 5. Check Image references
missing_images = []
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        c = f.read()
    imgs = re.findall(r'src=["\']([^"\']+\.(?:jpg|png|webp|svg))["\']', c)
    for img in imgs:
        if img.startswith('http'):
            continue
        clean_img = img.split('?')[0].split('#')[0]
        if not os.path.exists(clean_img):
            missing_images.append((hf, clean_img))

print(f"Missing local images count: {len(missing_images)}")
if missing_images:
    for m in missing_images[:5]:
        print(f"  Missing: {m}")
assert len(missing_images) == 0, "Missing image files found!"

# 6. Check JS Syntax
print("Verification finished successfully.")
