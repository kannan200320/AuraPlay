for f in ['login.html', 'register.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    print(f"=== {f} ({len(lines)} lines) ===")
    for i, line in enumerate(lines):
        if any(k in line for k in ['<button', '<form', 'onsubmit', 'onclick', 'alert', 'href="dashboard']):
            print(f"  {i+1}: {line.strip()[:95]}")
