import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in ["dashboard.html", "dashboard-packs.html", "dashboard-history.html", "dashboard-payments.html", "dashboard-settings.html"]:
    c = open(f, encoding="utf-8").read()
    btns = re.findall(r'<button[^>]*>(.*?)</button>', c, re.DOTALL)
    print(f"\n=== {f} ({len(btns)} buttons) ===")
    for b in btns:
        # clean html inside button
        clean = re.sub(r'<[^>]*>', '', b).strip()
        print(f"  - [{clean}]")
