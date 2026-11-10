c = open('about.html', 'rb').read()
c = c.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
open('about.html', 'wb').write(c)

c2 = open('index.html', 'rb').read()
c2 = c2.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
open('index.html', 'wb').write(c2)
print("Normalized line endings on about.html and index.html")
