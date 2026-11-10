import sys
sys.stdout.reconfigure(encoding='utf-8')

games = open('games.html', encoding='utf-8').read()

idx1 = games.find('Pro Peripherals Vault')
sec1_start = games.rfind('<section', 0, idx1)
sec1_end = games.find('</section>', idx1) + len('</section>')
print("=== PRO PERIPHERALS VAULT FULL SECTION ===")
print(games[sec1_start:sec1_end])

idx2 = games.find('Kernel-Level Anti-Cheat')
sec2_start = games.rfind('<section', 0, idx2)
sec2_end = games.find('</section>', idx2) + len('</section>')
print("\n=== KERNEL-LEVEL ANTI-CHEAT FULL SECTION ===")
print(games[sec2_start:sec2_end])
