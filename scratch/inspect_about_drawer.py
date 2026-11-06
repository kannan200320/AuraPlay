with open('about.html', 'r', encoding='utf-8') as f:
    txt = f.read()

hdr_end = txt.find('</header>')
main_start = txt.find('<main')
print("Between header and main in about.html:")
print(txt[hdr_end:main_start][:500].encode('ascii', 'backslashreplace').decode('ascii'))
