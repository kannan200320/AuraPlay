import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()
idx = about.find('Rig & System Engineer')
print(about[idx-300:idx+800])
