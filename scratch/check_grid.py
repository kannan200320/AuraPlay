import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()
idx = about.find('Rig & System Engineer')
grid_idx = about.rfind('<div class=', 0, idx)
grid_idx2 = about.rfind('<div class=', 0, grid_idx)
print("grid_idx2:", repr(about[grid_idx2:idx]))
