import sys
sys.stdout.reconfigure(encoding='utf-8')

content = open('games.html', encoding='utf-8').read()
idx = content.find('Reserve Your Station & Launch Any Title in Seconds')
if idx != -1:
    print(content[idx-300:idx+300])
