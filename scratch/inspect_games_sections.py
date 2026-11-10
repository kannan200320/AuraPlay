import sys
sys.stdout.reconfigure(encoding='utf-8')

games = open('games.html', encoding='utf-8').read()

print("=== SECTION: PRO PERIPHERALS VAULT ===")
idx1 = games.find('HALL EFFECT KEYBOARDS')
sec1_start = games.rfind('<section', 0, idx1)
sec1_end = games.find('</section>', idx1)
print(games[sec1_start:sec1_start+1500])

print("\n=== SECTION: KERNEL-LEVEL ANTI-CHEAT INTEGRITY ===")
idx2 = games.find('KERNEL-LEVEL ANTI-CHEAT')
sec2_start = games.rfind('<section', 0, idx2)
sec2_end = games.find('</section>', idx2)
print(games[sec2_start:sec2_start+1500])
