import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()
idx = about.find('Rig & System Engineer')
grid_idx = about.rfind('grid-cols', 0, idx)
div_start = about.rfind('<div', 0, grid_idx)
print(about[div_start:div_start+300])
