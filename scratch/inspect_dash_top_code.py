with open('dashboard.html', 'r', encoding='utf-8') as f:
    txt = f.read()

body_idx = txt.find('<body')
main_idx = txt.find('<main')
lines = txt[body_idx:main_idx].splitlines()
for i in range(min(20, len(lines))):
    print(f"Top {i+1}: {lines[i][:90].encode('ascii', 'backslashreplace').decode('ascii')}")
print("...")
for i in range(max(0, len(lines)-20), len(lines)):
    print(f"Bottom {i+1}: {lines[i][:90].encode('ascii', 'backslashreplace').decode('ascii')}")
