import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== CHECKING DASHBOARD BUTTONS IN MAIN.JS & HTML ===")
main_js = open("assets/js/main.js", encoding="utf-8").read()

dash_files = [
    "dashboard.html",
    "dashboard-packs.html",
    "dashboard-history.html",
    "dashboard-payments.html",
    "dashboard-settings.html"
]

for df in dash_files:
    content = open(df, encoding="utf-8").read()
    print(f"\n--- {df} ---")
    # Check head script for dark glitch
    has_head_script = "localStorage.getItem('color-theme')" in content[:1500]
    html_tag = re.search(r'<html[^>]*>', content)
    print("html tag:", html_tag.group(0) if html_tag else "None")
    print("head theme script in first 1500 chars:", has_head_script)
    
    # Check buttons
    btns = re.findall(r'<button[^>]*>([^<]{1,30})</button>', content)
    print("Sample buttons in HTML:", btns[:5])

print("\n=== CHECKING IF main.js ATTACHES POPUPS TO DASHBOARD BUTTONS ===")
for term in ["PURCHASE NOW", "BUY CUSTOM HOURS", "Update Password", "dashboard-payments", "Make Default", "Default", "Reload Amount"]:
    print(f"Term '{term}' in main.js:", term.lower() in main_js.lower())

