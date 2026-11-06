with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Ready To Play On The Best Rigs')
sec_start = c.rfind('<section', 0, idx)
sec_tag_end = c.find('>', sec_start)
print("Section tag:", repr(c[sec_start:sec_tag_end+1]))
