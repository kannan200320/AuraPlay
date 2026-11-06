with open('dashboard-packs.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = "sidebar.classList.toggle('hidden')"
idx = c.find(target)
if idx != -1:
    script_open = c.rfind('<script', 0, idx)
    script_close = c.find('</script>', idx) + len('</script>')
    c = c[:script_open].rstrip() + '\n' + c[script_close:].lstrip()
    with open('dashboard-packs.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Cleaned script block from dashboard-packs.html")
else:
    print("Target not found.")
