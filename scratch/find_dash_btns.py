import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

for f in ["dashboard.html", "dashboard-packs.html", "dashboard-history.html", "dashboard-payments.html", "dashboard-settings.html"]:
    c = open(f, encoding="utf-8").read()
    for term in ["Purchase Now", "Buy Custom Hours", "Update Password"]:
        if term.lower() in c.lower():
            idx = c.lower().find(term.lower())
            print(f"{f} found '{term}':\n", c[max(0, idx-100):min(len(c), idx+150)], "\n" + "-"*40)
