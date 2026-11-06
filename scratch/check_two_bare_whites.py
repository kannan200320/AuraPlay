with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Your Console & Sim')
if idx != -1:
    print("player-lounge.html:")
    print(repr(c[idx-250:idx+250]))

with open('about.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

idx2 = c2.find('Ready To Play On The Best Rigs')
if idx2 != -1:
    print("about.html:")
    print(repr(c2[idx2-250:idx2+250]))
