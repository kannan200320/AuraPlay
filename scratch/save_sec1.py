with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

def get_sec1(html):
    start = html.find('<section')
    end = html.find('</section>', start) + len('</section>')
    return html[start:end]

sec1_idx = get_sec1(idx_content)
with open('scratch/index_sec1.txt', 'w', encoding='utf-8') as out:
    out.write(sec1_idx)

with open('player-lounge.html', 'r', encoding='utf-8') as f:
    lounge_content = f.read()

sec1_lounge = get_sec1(lounge_content)
with open('scratch/lounge_sec1.txt', 'w', encoding='utf-8') as out:
    out.write(sec1_lounge)

print("Saved index_sec1.txt and lounge_sec1.txt")
