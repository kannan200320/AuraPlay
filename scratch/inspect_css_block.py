with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's see the current hero section styles
start_idx = css.find('/* ========================================================\n   HIGH-CONTRAST HERO TYPOGRAPHY')
end_idx = css.find('/* ========================================================\n   FAQ ACCORDION & DROPDOWN COMPONENT')

print("Found block between start_idx and end_idx:")
print(css[start_idx:end_idx])
