import re

dash_files = [
    'dashboard.html',
    'dashboard-packs.html',
    'dashboard-history.html',
    'dashboard-payments.html',
    'dashboard-settings.html'
]

# Match the entire <a> block containing "Website" linking to index.html in header
pattern = re.compile(
    r'\s*(?:<!--\s*Back to Arena Website\s*-->\s*)?<a href="index\.html"[^>]*class="[^"]*hidden sm:inline-flex[^"]*"[^>]*>.*?Website.*?</a>',
    re.DOTALL
)

for f in dash_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    new_content, count = pattern.subn('', content)
    if count > 0:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        print(f"Removed Website button from {f} (count={count})")
    else:
        print(f"No match in {f}")
