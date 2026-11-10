import sys
sys.stdout.reconfigure(encoding='utf-8')

games = open('games.html', encoding='utf-8').read()

idx1 = games.find('HALL EFFECT KEYBOARDS')
print("HALL EFFECT KEYBOARDS at:", idx1)
sec_start = games.rfind('<section', 0, idx1)
print(games[sec_start:idx1+1200])

idx2 = games.find('KERNEL-LEVEL ANTI-CHEAT')
print("\nKERNEL-LEVEL ANTI-CHEAT at:", idx2)
sec_start2 = games.rfind('<section', 0, idx2)
print(games[sec_start2:idx2+1200])
