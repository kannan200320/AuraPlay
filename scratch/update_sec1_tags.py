import re

for f in ['games.html', 'pricing.html', 'membership.html', 'book-slot.html', 'blog.html', 'contact.html']:
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()

    c = re.sub(r'(<!--\s*(?:={2,}\s*)?SECTION 1:.*?<section class="[^"]*?)(?:bg-slate-100(?:/90)?\s+(?:dark:)?bg-darkslate-deep(?:/90)?)([^"]*?)">',
               r'\1bg-darkslate-deep text-white\2">',
               c, flags=re.DOTALL)

    with open(f, 'w', encoding='utf-8', newline='\r\n') as file:
        file.write(c)
    print(f"Updated {f} section tag")
