import glob
import re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    sections = list(re.finditer(r'(<!--\s*(?:=+)?\s*SECTION\s+\d+[^>]*-->\s*<section\b[^>]*>)(.*?)(</section>)', c, re.DOTALL))
    for idx, s in enumerate(sections, 1):
        header = s.group(1)
        s_text = s.group(2)
        # Check if the section itself has a background image layer as a direct child of section or general backdrop
        # Let's find all occurrences of <img in this section
        imgs = re.findall(r'<img[^>]+>', s_text)
        bg_imgs = [img for img in imgs if 'object-cover' in img and ('inset-0' in s_text or 'opacity-' in img)]
        # Also check direct child divs with absolute inset-0
        direct_bg = re.findall(r'<div[^>]*class="[^"]*absolute inset-0[^"]*"[^>]*>\s*<img[^>]+>', s_text)
        if direct_bg:
            sec_comment = header.strip().split('\n')[0]
            print(f"{f} | Section {idx} | {sec_comment}")
            for dbg in direct_bg:
                print(f"   Direct BG layer: {dbg}")
