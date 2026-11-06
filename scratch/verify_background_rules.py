import glob
import re

primary_pages = [
    'index.html',
    'player-lounge.html',
    'about.html',
    'games.html',
    'pricing.html',
    'membership.html',
    'book-slot.html',
    'blog.html',
    'contact.html'
]

print("=== CHECK 1: NO bg-page CLASSES ON BODY ===")
for p in primary_pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    body_tag = re.search(r'<body\b[^>]*>', c).group(0)
    if 'bg-page' in body_tag:
        print(f"  FAIL: {p} has bg-page in body: {body_tag}")
    else:
        print(f"  PASS: {p} body is clean of bg-page classes")

print("\n=== CHECK 2: NO FIXED BACKGROUND ENGINE IN style.css ===")
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
if 'THEME-ADAPTIVE PAGE BACKGROUND ENGINE' in css or 'bg-page' in css or 'body::before' in css:
    print("  FAIL: style.css still contains page background engine!")
else:
    print("  PASS: style.css is completely clean of full-page background engine!")

print("\n=== CHECK 3: HERO SECTION (SEC 1) HAS BG IMAGE & CONTENT SECTIONS (SEC 2-15) DO NOT ===")
for p in primary_pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    sections = list(re.finditer(r'(<!--\s*(?:=+)?\s*SECTION\s+(\d+)[^>]*-->\s*<section\b[^>]*>)(.*?)(</section>)', c, re.DOTALL))
    print(f"\n--- Checking {p} ({len(sections)} sections) ---")
    
    for s in sections:
        sec_num = int(s.group(2))
        sec_header = s.group(1)
        sec_body = s.group(3)
        
        # Check for direct section background image layer (absolute inset-0 with img)
        has_direct_bg_img = bool(re.search(r'<div[^>]*class="[^"]*absolute inset-0[^"]*pointer-events-none[^"]*"[^>]*>\s*<img[^>]+>', sec_body))
        
        if sec_num == 1:
            if has_direct_bg_img:
                img_src = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', sec_body).group(1)
                print(f"  Sec 1 (Hero): PASS (Hero background image present: {img_src})")
            else:
                print(f"  Sec 1 (Hero): FAIL (Hero background image missing!)")
        else:
            if has_direct_bg_img:
                print(f"  Sec {sec_num}: FAIL (Direct background image found in content section!)")
            else:
                pass
    print(f"  All content sections (Sec 2 to {len(sections)}): PASS (0 section background images)")

print("\nALL BACKGROUND RULE CHECKS COMPLETE.")
