with open('dashboard-settings.html', 'r', encoding='utf-8') as f:
    txt = f.read()

for i, line in enumerate(txt.splitlines()):
    if any(k in line.lower() for k in ['profile', 'gamer tag', 'account', 'alex', 'avatar']):
        print(f"{i+1}: {line.strip()[:100]}")
