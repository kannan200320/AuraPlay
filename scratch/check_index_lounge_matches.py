import re

for p in ['index.html', 'player-lounge.html']:
    content = open(p, encoding='utf-8').read()
    print(f"=== {p} ===")
    bg_m = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', content, re.DOTALL)
    print("  BG match:", bool(bg_m))
    p_m = re.search(r'<p class="[^"]*hero-subtitle-boosted[^"]*">.*?</p>', content, re.DOTALL)
    print("  Subtitle match:", bool(p_m))
    if p_m:
        print("    P tag length:", len(p_m.group(0)))
