import re, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update dashboard.html
dash = open('dashboard.html', encoding='utf-8').read()
# Pause Time button
dash = re.sub(
    r'<button([^>]*>)\s*Pause Time\s*</button>',
    r'<button onclick="window.showAuraPopup(\'Session Paused\', \'Station timer paused. Station is held reserved for 15 minutes.\', true);" \1Pause Time</button>',
    dash
)
# +1 Hr Extend
dash = re.sub(
    r'<button onclick="showAuraToast\([^)]*\)" class="([^"]*)">\s*\+1 Hr Extend\s*</button>',
    r'<button onclick="window.showAuraPopup(\'Time Extended\', \'+1 Hour added to active battlestation session. NFC updated.\', true);" class="\1">+1 Hr Extend</button>',
    dash
)
# Sync Hardware Presets
dash = re.sub(
    r'<button onclick="showAuraToast\([^)]*\)" class="([^"]*)">\s*🔄 Sync Hardware Presets\s*</button>',
    r'<button onclick="window.showAuraPopup(\'Hardware Synced\', \'DPI, polling rate, and keybind presets synced to station.\', true);" class="\1">🔄 Sync Hardware Presets</button>',
    dash
)
# Claim Daily +100 XP
dash = re.sub(
    r'<button onclick="showAuraToast\([^)]*\)" class="([^"]*)">\s*🎁 Claim Daily \+100 XP\s*</button>',
    r'<button onclick="window.showAuraPopup(\'XP Claimed!\', \'+100 Daily Aura XP claimed and banked to your tier.\', true);" class="\1">🎁 Claim Daily +100 XP</button>',
    dash
)
# QR Ticket
dash = re.sub(
    r'<button onclick="showAuraToast\([^)]*\)" class="([^"]*)">\s*QR Ticket\s*</button>',
    r'<button onclick="window.showAuraPopup(\'NFC & QR Ticket\', \'Scan this terminal pass at the battlestation reader.\', true);" class="\1">QR Ticket</button>',
    dash
)
# Manage
dash = re.sub(
    r'<button onclick="showAuraToast\([^)]*\)" class="([^"]*)">\s*Manage\s*</button>',
    r'<button onclick="window.showAuraPopup(\'Reservation Hub\', \'Managing active station booking.\', true);" class="\1">Manage</button>',
    dash
)
open('dashboard.html', 'w', encoding='utf-8').write(dash)
print("Updated dashboard.html buttons")

# 2. Update dashboard-history.html
hist = open('dashboard-history.html', encoding='utf-8').read()
# Replace alert(...) on receipts with showAuraPopup
hist = re.sub(
    r'onclick="alert\(\'Downloading official tax invoice PDF for session ([^\']+)\'\);"',
    r'onclick="window.showAuraPopup(\'Receipt Downloaded\', \'Official tax invoice PDF for session \1 downloaded.\', true);"',
    hist
)
# Previous button
hist = re.sub(
    r'<button class="([^"]*)" aria-label="Previous page">\s*Previous\s*</button>',
    r'<button onclick="window.showAuraPopup(\'Session History\', \'Already viewing latest session records (Page 1).\', true);" class="\1" aria-label="Previous page">Previous</button>',
    hist
)
# Next Page button
hist = re.sub(
    r'<button class="([^"]*)" aria-label="Next page">\s*Next Page →\s*</button>',
    r'<button onclick="window.showAuraPopup(\'Session History\', \'Loaded archive session records (Page 2).\', true);" class="\1" aria-label="Next page">Next Page →</button>',
    hist
)
open('dashboard-history.html', 'w', encoding='utf-8').write(hist)
print("Updated dashboard-history.html buttons")

# 3. Update dashboard-payments.html
pay = open('dashboard-payments.html', encoding='utf-8').read()
# Add Funds to Wallet button
pay = re.sub(
    r'onclick="document\.getElementById\(\'instant-reload-section\'\)\.scrollIntoView\(\{behavior: \'smooth\'\}\);"',
    r'onclick="document.getElementById(\'instant-reload-section\').scrollIntoView({behavior: \'smooth\'}); window.showAuraPopup(\'Wallet Top-Up\', \'Select an instant reload amount or custom balance below.\', true);"',
    pay
)
# Replace alert(...) on Download PDF
pay = re.sub(
    r'onclick="alert\(\'Downloading official tax invoice PDF for receipt ([^\']+)\'\);"',
    r'onclick="window.showAuraPopup(\'Invoice Downloaded\', \'Official billing receipt PDF for \1 downloaded.\', true);"',
    pay
)
open('dashboard-payments.html', 'w', encoding='utf-8').write(pay)
print("Updated dashboard-payments.html buttons")

# 4. Update dashboard-settings.html
sett = open('dashboard-settings.html', encoding='utf-8').read()
# Save All Changes
sett = re.sub(
    r'onclick="showAuraToast\(\'Profile settings saved successfully!\', \'success\'\);"',
    r'onclick="window.showAuraPopup(\'Profile Saved\', \'Your gamer profile, battle tag, and preferences have been updated.\', true);"',
    sett
)
# Change Avatar
sett = re.sub(
    r'onclick="alert\(\'Gamer avatar vault selector opened\. Choose your new profile image\.\'\);"',
    r'onclick="window.showAuraPopup(\'Avatar Vault\', \'Gamer avatar vault opened. Choose your profile emblem.\', true);"',
    sett
)
# Update Password
sett = re.sub(
    r'onclick="showAuraToast\(\'Password updated securely!\', \'success\'\);"',
    r'onclick="window.showAuraPopup(\'Security Notice\', \'Password updated successfully!\', true);"',
    sett
)
# Manage 2FA
sett = re.sub(
    r'onclick="alert\(\'Redirecting to two-factor hardware key & authenticator management console\.\.\.\'\);"',
    r'onclick="window.showAuraPopup(\'Two-Factor Security\', \'Two-factor hardware key console initialized.\', true);"',
    sett
)
open('dashboard-settings.html', 'w', encoding='utf-8').write(sett)
print("Updated dashboard-settings.html buttons")
