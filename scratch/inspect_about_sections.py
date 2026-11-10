import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()

print("=== ABOUT.HTML SECTION 1: ZERO LATENCY ===")
idx1 = about.find('ZERO LATENCY')
sec1_start = about.rfind('<section', 0, idx1)
sec1_end = about.find('</section>', idx1) + len('</section>')
print(about[sec1_start:sec1_end])

print("\n=== ABOUT.HTML SECTION 2: HARDWARE SANDBOX ISOLATION ===")
idx2 = about.find('HARDWARE SANDBOX ISOLATION')
sec2_start = about.rfind('<section', 0, idx2)
sec2_end = about.find('</section>', idx2) + len('</section>')
print(about[sec2_start:sec2_end])

print("\n=== ABOUT.HTML SECTION 3: TEAM APEX SHADOWS ===")
idx3 = about.find('TEAM APEX SHADOWS')
sec3_start = about.rfind('<section', 0, idx3)
sec3_end = about.find('</section>', idx3) + len('</section>')
print(about[sec3_start:sec3_end])

print("\n=== ABOUT.HTML SECTION 4: RIG & SYSTEM ENGINEER ===")
idx4 = about.find('RIG & SYSTEM ENGINEER')
sec4_start = about.rfind('<section', 0, idx4)
sec4_end = about.find('</section>', idx4) + len('</section>')
print(about[sec4_start:sec4_end])
