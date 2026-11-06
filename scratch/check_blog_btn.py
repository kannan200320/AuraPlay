with open('blog.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Read Article')
if idx != -1:
    s = c[idx-150:idx+150]
    print(s.encode('ascii', 'backslashreplace').decode('ascii'))
