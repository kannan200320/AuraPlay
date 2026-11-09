import sys
sys.stdout.reconfigure(encoding='utf-8')

packs = open('dashboard-packs.html', encoding='utf-8').read()
idx = packs.find('function handlePackBuy')
if idx != -1:
    print(packs[idx:idx+1500])
else:
    idx2 = packs.find('handlePackBuy')
    print(packs[idx2:idx2+1500])
