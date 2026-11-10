import sys
sys.stdout.reconfigure(encoding='utf-8')

index = open('index.html', encoding='utf-8').read()
idx = index.find('Weekly LAN Tournaments')
sec_start = index.rfind('<section', 0, idx)
sec_end = index.find('</section>', idx) + len('</section>')
print("=== TOURNAMENTS SECTION ===")
print(index[sec_start:sec_end])
