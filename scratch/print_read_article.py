with open('blog.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Read Article')
a_start = c.rfind('<a', 0, idx)
a_end = c.find('</a>', idx) + 4
print(c[a_start:a_end].encode('ascii', 'backslashreplace').decode('ascii'))
