import re

# 1. Update login.html
with open('login.html', 'r', encoding='utf-8') as f:
    login_txt = f.read()

# Remove window.location.href='dashboard.html'
login_txt = login_txt.replace("window.location.href='dashboard.html'", "event.preventDefault()")
# Remove alert(...)
login_txt = re.sub(r"alert\([^)]*\);\s*", "", login_txt)

# Ensure form onsubmit is purely preventDefault
login_txt = re.sub(r'onsubmit="[^"]*"', 'onsubmit="event.preventDefault(); return false;"', login_txt)

with open('login.html', 'w', encoding='utf-8') as f:
    f.write(login_txt)
print("login.html updated: all submit & social buttons are now dummy, no alerts, no navigation.")

# 2. Update register.html
with open('register.html', 'r', encoding='utf-8') as f:
    reg_txt = f.read()

# Remove window.location.href='dashboard.html'
reg_txt = reg_txt.replace("window.location.href='dashboard.html'", "event.preventDefault()")
# Remove alert(...)
reg_txt = re.sub(r"alert\([^)]*\);\s*", "", reg_txt)

# Ensure form onsubmit is purely preventDefault
reg_txt = re.sub(r'onsubmit="[^"]*"', 'onsubmit="event.preventDefault(); return false;"', reg_txt)

with open('register.html', 'w', encoding='utf-8') as f:
    f.write(reg_txt)
print("register.html updated: all submit & social buttons are now dummy, no alerts, no navigation.")
