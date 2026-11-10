import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()
idx = about.find('grid grid-cols-1 md:grid-cols-3 gap-6 mb-10 items-stretch')
idx_end = about.find('Apply For An Open Role Today', idx)
print("=== EXACT SECTION 4 FROM ABOUT.HTML ===")
print(repr(about[idx:idx_end]))
