for p in ['login.html', 'register.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    import re
    forms = re.findall(r'<form[^>]*>', c)
    print(f"=== {p} FORMS ===")
    for form in forms:
        print(form)
