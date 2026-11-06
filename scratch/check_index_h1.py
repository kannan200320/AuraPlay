with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if '<h1' in line:
            print(f"index.html line {i+1}: {line.strip()}")
