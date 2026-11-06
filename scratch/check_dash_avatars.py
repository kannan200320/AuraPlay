import os, re

dash_files = ['dashboard.html', 'dashboard-packs.html', 'dashboard-history.html', 'dashboard-payments.html', 'dashboard-settings.html']
for f in dash_files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    # Search for "Alex" or "Viper" or "Profile" or "avatar" or user profile
    for i, line in enumerate(txt.splitlines()):
        if any(k in line.lower() for k in ['avatar', 'profile photo', 'profile picture', 'alex_viper', 'viper99', 'pro gamer', 'gamer tag', 'rounded-full']):
            if 'w-' in line or 'h-' in line or 'img' in line:
                print(f"{f}:{i+1}: {line.strip()[:100]}")
