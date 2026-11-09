import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for f in ["dashboard.html", "dashboard-packs.html", "dashboard-history.html", "dashboard-payments.html", "dashboard-settings.html"]:
    c = open(f, encoding="utf-8").read()
    buttons = re.findall(r'<button([^>]*)>(.*?)</button>', c, re.DOTALL)
    print(f"\n================ {f} ({len(buttons)} buttons) ================")
    for attrs, body in buttons:
        clean_body = re.sub(r'<[^>]*>', '', body).strip().replace('\n', ' ')
        has_onclick = 'onclick=' in attrs
        onclick_val = re.search(r'onclick=["\']([^"\']*)["\']', attrs)
        val = onclick_val.group(1) if onclick_val else "NO ONCLICK"
        print(f"[{clean_body[:30]:30}] -> {val[:60]}")
