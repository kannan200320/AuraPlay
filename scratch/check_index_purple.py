with open('index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'text-purple-500 font-bold' in line:
            print(f"{i+1}: {line.strip().encode('ascii', 'backslashreplace').decode('ascii')}")
