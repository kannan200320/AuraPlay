import sys
sys.stdout.reconfigure(encoding='utf-8')

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html']

for p in pages:
    print(f"\n==================== {p} HERO SECTION ====================")
    with open(p, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    hero_start = -1
    hero_end = -1
    for idx, l in enumerate(lines):
        if 'SECTION 1:' in l or 'SECTION 1 ' in l or 'hero' in l.lower() and '<section' in l:
            if hero_start == -1:
                hero_start = idx
        if hero_start != -1 and ('SECTION 2:' in l or 'SECTION 2 ' in l):
            hero_end = idx
            break
    
    if hero_start != -1 and hero_end != -1:
        for i in range(hero_start, min(hero_end + 1, len(lines))):
            print(f"{i+1}: {lines[i]}", end='')
    else:
        print(f"Could not cleanly find hero bounds: start={hero_start}, end={hero_end}")
