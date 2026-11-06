import glob, re

pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    s1 = re.search(r'(<!--\s*(?:=+)?\s*SECTION\s+1[^>]*-->\s*<section\b[^>]*>)(.*?)(</section>)', c, re.DOTALL).group(2)
    
    # Check if any element in s1 has text-white without dark: prefix
    # E.g. class="... text-white ..." without dark:text-white
    # Ignore CTA button that has text-white on gradient bg if needed
    for tag in re.finditer(r'<([a-zA-Z0-9]+)\b([^>]*)>', s1):
        tag_name = tag.group(1)
        attrs = tag.group(2)
        if 'class=' in attrs:
            classes = re.search(r'class=["\']([^"\']+)["\']', attrs).group(1)
            # check for text-white not preceded by dark:
            has_bare_text_white = bool(re.search(r'(?<!dark:)text-white\b', classes))
            if has_bare_text_white and tag_name not in ['a', 'button']:
                print(f"{p} has bare text-white on <{tag_name}>: {classes[:80]}")
