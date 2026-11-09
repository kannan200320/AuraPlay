import re, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. dashboard-history.html
hist = open('dashboard-history.html', encoding='utf-8').read()
# Replace alert for receipts
hist = re.sub(
    r'onclick="alert\(\'Viewing receipt for Session ([^\']+)\'\);"',
    r'onclick="window.showAuraPopup(\'Session Receipt\', \'Viewing receipt for Session \1\', true);"',
    hist
)
# Next page button
hist = hist.replace(
    '<button class="px-3 py-1 rounded-lg bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white font-bold transition-colors">Next Page →</button>',
    '<button onclick="window.showAuraPopup(\'History Records\', \'Loaded archive session records (Page 2).\', true);" class="px-3 py-1 rounded-lg bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white font-bold transition-colors">Next Page →</button>'
)
# Previous button
hist = hist.replace(
    '<button class="px-4 py-2 rounded-xl text-xs bg-slate-100 dark:bg-darkslate-lighter text-black dark:text-slate-400 font-bold cursor-not-allowed" disabled>Previous</button>',
    '<button onclick="window.showAuraPopup(\'History Records\', \'Already viewing latest session records (Page 1).\', true);" class="px-4 py-2 rounded-xl text-xs bg-slate-100 dark:bg-darkslate-lighter text-black dark:text-slate-400 font-bold hover:bg-slate-200">Previous</button>'
)
open('dashboard-history.html', 'w', encoding='utf-8').write(hist)
print("Updated dashboard-history.html alerts and pagination")

# 2. dashboard-payments.html
pay = open('dashboard-payments.html', encoding='utf-8').read()
pay = re.sub(
    r'onclick="alert\(\'Downloading PDF Invoice #([^\']+)\'\);"',
    r'onclick="window.showAuraPopup(\'Invoice Downloaded\', \'Downloading PDF Invoice #\1\', true);"',
    pay
)
open('dashboard-payments.html', 'w', encoding='utf-8').write(pay)
print("Updated dashboard-payments.html alerts")

# 3. dashboard-settings.html
sett = open('dashboard-settings.html', encoding='utf-8').read()
sett = sett.replace(
    "onclick=\"alert('Choose custom avatar from AuraPlay Vault.');\"",
    "onclick=\"window.showAuraPopup('Avatar Vault', 'Choose custom avatar from AuraPlay Vault.', true);\""
)
sett = sett.replace(
    "onclick=\"alert('Manage 2FA Authenticator keys and recovery codes.');\"",
    "onclick=\"window.showAuraPopup('Two-Factor Security', 'Manage 2FA Authenticator keys and recovery codes.', true);\""
)
open('dashboard-settings.html', 'w', encoding='utf-8').write(sett)
print("Updated dashboard-settings.html alerts")
