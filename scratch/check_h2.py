with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Room-Scale Wireless')
h2_start = c.rfind('<h2', 0, idx)
print("H2 1:", repr(c[h2_start:idx+150]))

idx2 = c.find('Direct-Drive Force Feedback')
h2_start2 = c.rfind('<h2', 0, idx2)
print("H2 2:", repr(c[h2_start2:idx2+150]))
