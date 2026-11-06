with open('dashboard-history.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Next Page')
if idx != -1:
    s = repr(c[idx-100:idx+100])
    print("dashboard-history.html Next Page:", s.encode('ascii', 'backslashreplace').decode('ascii'))

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

idx2 = c2.find('Claim Daily')
if idx2 != -1:
    s2 = repr(c2[idx2-100:idx2+100])
    print("dashboard.html Claim Daily:", s2.encode('ascii', 'backslashreplace').decode('ascii'))
