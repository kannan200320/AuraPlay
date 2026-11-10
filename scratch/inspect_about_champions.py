import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()
idx = about.find('Apex Shadows')
sec_start = about.rfind('<section', 0, idx)
sec_end = about.find('</section>', idx) + len('</section>')
print("=== WALL OF CHAMPIONS SECTION ===")
print(about[sec_start:sec_end])
