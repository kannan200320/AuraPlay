import os
import re

css_path = 'assets/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Pattern for the entire background engine block
bg_engine_pattern = r'/\* ========================================================\s*THEME-ADAPTIVE PAGE BACKGROUND ENGINE.*?body\.bg-page-pricing::before\s*\{[^}]*\}'

match = re.search(bg_engine_pattern, css_content, re.DOTALL)
if match:
    css_content = css_content[:match.start()].rstrip() + '\n'
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Successfully removed THEME-ADAPTIVE PAGE BACKGROUND ENGINE from style.css!")
else:
    print("Warning: THEME-ADAPTIVE PAGE BACKGROUND ENGINE not found in style.css")
