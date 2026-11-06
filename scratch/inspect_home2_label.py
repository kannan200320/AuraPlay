with open('player-lounge.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(235, 252):
    print(f"{i+1}: {repr(lines[i])}")
