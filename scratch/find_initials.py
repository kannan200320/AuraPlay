import os, re

for root, dirs, files in os.walk('.'):
    for f in sorted(files):
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
            # Look for 2 uppercase letters inside rounded-full
            initials_matches = re.findall(r'<div[^>]*rounded-full[^>]*>\s*([A-Z]{2})\s*</div>', txt)
            # Also search for "feedback", "testimonial", "review", "avatar", "profile"
            if initials_matches:
                print(f"{p}: found initials {initials_matches}")
            # Also search for avatar placeholder or SVGs used as avatars
            svg_avatars = re.findall(r'<div[^>]*rounded-full[^>]*>\s*<svg[^>]*>.*?</svg>\s*</div>', txt, re.DOTALL)
            if svg_avatars:
                print(f"{p}: found {len(svg_avatars)} SVG rounded-full containers")
