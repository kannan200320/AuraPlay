with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Valve Index 144Hz')
print(repr(c[idx:idx+350]))
