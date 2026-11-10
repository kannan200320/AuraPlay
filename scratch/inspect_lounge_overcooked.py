import sys
sys.stdout.reconfigure(encoding='utf-8')

lounge = open('player-lounge.html', encoding='utf-8').read()
idx = lounge.find('Overcooked!')
sec_start = lounge.rfind('<section', 0, idx)
sec_end = lounge.find('</section>', idx) + len('</section>')
print("=== OVERCOOKED SECTION IN PLAYER-LOUNGE.HTML ===")
print(lounge[sec_start:sec_end])
