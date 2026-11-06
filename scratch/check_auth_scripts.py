for p in ['login.html', 'register.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    s_idx = c.rfind('<script>')
    print(f"=== {p} SCRIPT ===")
    print(c[s_idx:])
