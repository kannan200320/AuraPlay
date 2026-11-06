with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect Section 1 exactly
sec1_start = c.find('<!-- ================= SECTION 1: HERO - NEON ARENA ================= -->')
sec1_end = c.find('<!-- ================= SECTION 2: LIVE FLOOR STATUS & SPECS ================= -->')

print("Old Section 1 Length:", sec1_end - sec1_start)
sec1_old = c[sec1_start:sec1_end]

# Let's verify our targeted replacements
print("Has old min-h-[90vh] py-16 lg:py-24:", 'min-h-[90vh] flex items-center overflow-hidden py-16 lg:py-24' in sec1_old)
