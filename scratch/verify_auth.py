for page in ['login.html', 'register.html']:
    with open(page, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {page} ===")
    print("has alert:", 'alert(' in c)
    print("has dashboard.html:", 'dashboard.html' in c)
    print("buttons count:", c.count('<button'))
    print("forms count:", c.count('<form'))
    import re
    buttons = re.findall(r'<button[^>]*>.*?</button>', c, re.DOTALL)
    for b in buttons:
        print("  BTN:", b.strip()[:100].replace('\n', ' '))
