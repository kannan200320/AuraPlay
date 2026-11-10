import re, sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()

terms = [
    "Zero Latency",
    "Hardware Sandbox",
    "Apex Shadows",
    "System Engineer"
]

for t in terms:
    m = re.search(re.escape(t), about, re.IGNORECASE)
    if m:
        idx = m.start()
        sec_start = about.rfind('<section', 0, idx)
        sec_end = about.find('</section>', idx) + len('</section>')
        print(f"=== FOUND '{t}' ===")
        print(about[sec_start:sec_end])
        print("="*60 + "\n")
    else:
        print(f"NOT FOUND: '{t}'")
