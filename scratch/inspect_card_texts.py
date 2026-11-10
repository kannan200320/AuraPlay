import sys
sys.stdout.reconfigure(encoding='utf-8')

index = open('index.html', encoding='utf-8').read()
idx = index.find('Weekly LAN Tournaments')
idx2 = index.find('</section>', idx)
sec = index[idx:idx2]

cards = sec.split('rounded-3xl p-5')[1:]
for i, c in enumerate(cards, 1):
    print(f"--- CARD {i} ---")
    print(c[:400])
