with open('dashboard-packs.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = "sidebar.classList.toggle('hidden')"
idx = c.find(target)
print(repr(c[idx-250:idx+150]))
