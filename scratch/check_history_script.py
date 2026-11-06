with open('dashboard-history.html', 'r', encoding='utf-8') as f:
    c = f.read()
script_pos = c.rfind('<script>')
if script_pos == -1:
    script_pos = c.rfind('<script ')
print(c[script_pos:])
