with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<footer')
end = c.find('</footer>') + len('</footer>')

with open('scratch/current_footer.html', 'w', encoding='utf-8') as out:
    out.write(c[idx:end])

print("Written scratch/current_footer.html")
