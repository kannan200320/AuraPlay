with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

s1_comment = '<!-- ================= SECTION 1: HERO - NEON ARENA ================= -->'
s2_comment = '<!-- ================= SECTION 2: LIVE METRICS & NETWORK TICKER ================= -->'

start = c.find(s1_comment)
end = c.find(s2_comment)

with open('scratch/current_index_sec1.html', 'w', encoding='utf-8') as out:
    out.write(c[start:end])

print("Written scratch/current_index_sec1.html. Length:", end - start)
