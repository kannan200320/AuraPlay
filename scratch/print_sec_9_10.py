with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx9 = c.find('IMMERSION HOLODECK')
sec9_start = c.rfind('<section', 0, idx9)
idx10 = c.find('PRO SIM TELEMETRY')
sec10_start = c.rfind('<section', 0, idx10)
sec11_start = c.find('<section', sec10_start + 10)

print("=== SECTION 9 ===")
print(c[sec9_start:sec10_start].encode('ascii', 'backslashreplace').decode('ascii'))

print("=== SECTION 10 ===")
print(c[sec10_start:sec11_start].encode('ascii', 'backslashreplace').decode('ascii'))
