c = open('games.html', 'rb').read()
c = c.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
open('games.html', 'wb').write(c)

c2 = open('book-slot.html', 'rb').read()
c2 = c2.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
open('book-slot.html', 'wb').write(c2)

c3 = open('player-lounge.html', 'rb').read()
c3 = c3.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
open('player-lounge.html', 'wb').write(c3)
print("Normalized line endings to CRLF")
