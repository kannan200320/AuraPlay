with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Step inside our acoustically padded')
if idx != -1:
    s = c[idx-300:idx+400]
    print("HOLODECK SECTION:")
    print(s.encode('ascii', 'backslashreplace').decode('ascii'))

idx2 = c.find('Experience authentic motorsport')
if idx2 != -1:
    s2 = c[idx2-300:idx2+400]
    print("\nSIM COCKPITS SECTION:")
    print(s2.encode('ascii', 'backslashreplace').decode('ascii'))
