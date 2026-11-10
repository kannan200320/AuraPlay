import re, sys
sys.stdout.reconfigure(encoding='utf-8')

games = open('games.html', encoding='utf-8').read()

m1 = re.search(r'hall effect keyboards', games, re.IGNORECASE)
if m1:
    print("Found m1:", m1.group(0))
    idx = m1.start()
    sec_start = games.rfind('<section', 0, idx)
    print(games[sec_start:idx+1200])

m2 = re.search(r'kernel-level', games, re.IGNORECASE)
if m2:
    print("\nFound m2:", m2.group(0))
    idx2 = m2.start()
    sec_start2 = games.rfind('<section', 0, idx2)
    print(games[sec_start2:idx2+1200])
