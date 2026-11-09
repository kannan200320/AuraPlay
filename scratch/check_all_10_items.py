import glob
import re

print("="*60)
print("ITEM 1: RESERVE YOUR STATION & LAUNCH ANY TITLE IN SECONDS")
print("="*60)
for f in glob.glob("*.html"):
    content = open(f, encoding="utf-8").read()
    if "RESERVE YOUR STATION" in content:
        for line in content.splitlines():
            if "RESERVE YOUR STATION" in line:
                print(f, line.strip())

print("\n" + "="*60)
print("ITEM 2: LOGIN CREDENTIALS EMPTY")
print("="*60)
login = open("login.html", encoding="utf-8").read()
for line in login.splitlines():
    if 'id="login-email"' in line or 'id="login-pass"' in line or 'name="email"' in line or 'name="password"' in line or 'phoenix.aim' in line:
        print(line.strip())

print("\n" + "="*60)
print("ITEM 3: GAMES BENCHMARKS RIG COLORS")
print("="*60)
games = open("games.html", encoding="utf-8").read()
for m in re.finditer(r'<td[^>]*>(?:<span[^>]*>)?(RTX 4090[^<]*|PS5 Pro Suite[^<]*|Sim Triple 4K Rig[^<]*)', games):
    print(m.group(0))

print("\n" + "="*60)
print("ITEM 4: GAMES PAGE FILTER TABS (All Titles (15)...)")
print("="*60)
if "All Titles (15)" in games:
    print("Found 'All Titles (15)' in games.html!")
    for line in games.splitlines():
        if "All Titles (15)" in line:
            print(line.strip()[:120])
else:
    print("'All Titles (15)' NOT in games.html (already removed/hidden)")

print("\n" + "="*60)
print("ITEM 5: CONTACT FORM VALIDATION & SUCCESS/ERROR TOASTS")
print("="*60)
main_js = open("assets/js/main.js", encoding="utf-8").read()
if "showToast" in main_js:
    print("showToast found in main.js")
for m in re.finditer(r'function validateContactForm|setupContactForm|contact-form', main_js):
    print("Found contact form logic in main.js at pos", m.start())

contact_html = open("contact.html", encoding="utf-8").read()
for line in contact_html.splitlines():
    if '<form' in line or 'id="contact' in line:
        print(line.strip()[:120])

print("\n" + "="*60)
print("ITEM 6, 7, 8: DASHBOARD BUTTONS TOAST")
print("="*60)
for m in re.finditer(r'PURCHASE NOW|BUY CUSTOM HOURS|Update Password', main_js):
    print("Found in main.js:", m.group(0))

print("\n" + "="*60)
print("ITEM 9: DASHBOARD PAYMENTS SELECTION")
print("="*60)
dash_pay = open("dashboard-payments.html", encoding="utf-8").read()
if 'class="payment-card' in dash_pay or 'set-default' in dash_pay or 'make-default' in dash_pay or 'reload-btn' in dash_pay or 'Instant Reload' in dash_pay:
    print("Found payment card / reload handlers in dashboard-payments.html")

print("\n" + "="*60)
print("ITEM 10: HEADER SIGN IN BUTTON ON TABLET AND LAPTOP (1024px)")
print("="*60)
for f in ["index.html", "about.html", "games.html", "pricing.html"]:
    c = open(f, encoding="utf-8").read()
    for m in re.finditer(r'<a href="login\.html"[^>]*>', c):
        print(f, m.group(0))
