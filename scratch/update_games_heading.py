games = open('games.html', encoding='utf-8').read()
target = 'class="text-4xl sm:text-5xl font-black font-display uppercase tracking-tight text-white">\n          Reserve Your Station & Launch Any Title in Seconds'
target_crlf = 'class="text-4xl sm:text-5xl font-black font-display uppercase tracking-tight text-white">\r\n          Reserve Your Station & Launch Any Title in Seconds'

replacement_crlf = 'style="color: #ffffff !important;" class="text-4xl sm:text-5xl font-black font-display uppercase tracking-tight text-white">\r\n          Reserve Your Station & Launch Any Title in Seconds'

if target_crlf in games:
    games = games.replace(target_crlf, replacement_crlf)
    open('games.html', 'w', encoding='utf-8').write(games)
    print("Updated games.html with CRLF")
elif target in games:
    games = games.replace(target, replacement_crlf)
    open('games.html', 'w', encoding='utf-8').write(games)
    print("Updated games.html with LF")
else:
    print("Target not found!")
