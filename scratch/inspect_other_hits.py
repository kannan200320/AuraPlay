import glob, re

for f in ['index.html', 'about.html', 'games.html', 'player-lounge.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    sections = list(re.finditer(r'(<!--\s*(?:=+)?\s*SECTION\s+\d+[^>]*-->\s*<section\b[^>]*>)(.*?)(</section>)', c, re.DOTALL))
    for idx, s in enumerate(sections, 1):
        header = s.group(1).strip().split('\n')[0]
        s_text = s.group(2)
        if 'inset-0' in s_text and '<img' in s_text and idx != 1:
            print(f"--- {f} Section {idx} ({header}) ---")
            # find all tags containing inset-0 and nearby img
            for m in re.finditer(r'<[^>]*inset-0[^>]*>', s_text):
                print("Tag:", m.group(0))
