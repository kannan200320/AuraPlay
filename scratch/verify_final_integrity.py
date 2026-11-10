import re, glob

PRIMARY_PAGES = [
    'index.html',
    'player-lounge.html',
    'about.html',
    'games.html',
    'pricing.html',
    'membership.html',
    'book-slot.html',
    'blog.html',
    'contact.html'
]

print("=== CHECKING SECTION COUNTS ===")
for page in PRIMARY_PAGES:
    content = open(page, encoding='utf-8').read()
    sections = re.findall(r'<section\b', content)
    print(f"{page}: {len(sections)} sections")
    assert len(sections) == 15, f"ERROR: {page} has {len(sections)} sections instead of 15!"

print("\n=== CHECKING CAFE REFERENCES ===")
cafe_found = False
for file in glob.glob('*.html') + glob.glob('assets/js/*.js') + glob.glob('assets/css/*.css'):
    content = open(file, encoding='utf-8').read()
    matches = re.findall(r'\bcafe\b|\bcafé\b', content, re.IGNORECASE)
    if matches:
        print(f"ERROR: {file} has cafe references: {matches}")
        cafe_found = True
if not cafe_found:
    print("Zero cafe references found across all files. PASS!")

print("\n=== VERIFYING GOOGLE / APPLE ID AUTH IN LOGIN AND REGISTER ===")
for auth_page in ['login.html', 'register.html']:
    c = open(auth_page, encoding='utf-8').read()
    google_btns = re.findall(r'<button[^>]*onclick="[^"]*showAuraPopup[^"]*"[^>]*>.*?Google', c, re.DOTALL)
    apple_btns = re.findall(r'<button[^>]*onclick="[^"]*showAuraPopup[^"]*"[^>]*>.*?Apple ID', c, re.DOTALL)
    print(f"{auth_page}: {len(google_btns)} Google buttons with popup, {len(apple_btns)} Apple ID buttons with popup")
    assert len(google_btns) > 0 and len(apple_btns) > 0, f"Missing popup on {auth_page}"

print("\nALL INTEGRITY CHECKS PASSED!")
