import re

def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for Google button
    pattern_google = r'<button type="button" onclick="event\.preventDefault\(\)" class="([^"]*?)">\s*(<svg class="w-4 h-4" viewBox="0 0 24 24">.*?<span>Google</span>\s*</button>)'
    
    # We want to replace onclick with window.showAuraPopup
    replacement_google = r'''<button type="button" onclick="event.preventDefault(); if(window.showAuraPopup){window.showAuraPopup('Redirecting...', 'Connecting to Google authentication service...', true);}" class="\1">\n            \2'''

    content = re.sub(pattern_google, replacement_google, content, flags=re.DOTALL)

    # Pattern for Apple ID button
    pattern_apple = r'<button type="button" onclick="event\.preventDefault\(\)" class="([^"]*?)">\s*(<svg class="w-4 h-4 fill-current text-black dark:text-white" viewBox="0 0 24 24">.*?<span>Apple ID</span>\s*</button>)'
    replacement_apple = r'''<button type="button" onclick="event.preventDefault(); if(window.showAuraPopup){window.showAuraPopup('Redirecting...', 'Connecting to Apple ID authentication service...', true);}" class="\1">\n            \2'''

    content = re.sub(pattern_apple, replacement_apple, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content)
    print(f"Updated {path}")

update_file('login.html')
update_file('register.html')
