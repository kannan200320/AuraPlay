with open('dashboard-packs.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = "sidebar.classList.toggle('hidden')"
idx = c.find(target)
print("Index:", idx)
if idx != -1:
    print(repr(c[idx-100:idx+150]))
