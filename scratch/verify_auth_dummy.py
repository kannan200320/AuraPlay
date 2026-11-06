for f in ['login.html', 'register.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    print(f"{f}: has 'alert': {'alert' in txt}")
    print(f"{f}: has 'dashboard.html': {'dashboard.html' in txt}")
