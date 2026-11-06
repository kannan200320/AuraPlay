import re

# 1. Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the hero typography engine in style.css
old_css_pattern = r'/\* ========================================================\s*HIGH-CONTRAST HERO TYPOGRAPHY & VISIBILITY ENGINE.*?box-shadow: 0 8px 20px rgba\(0, 0, 0, 0\.5\);\s*\}'

new_hero_css = """/* ========================================================
   HIGH-CONTRAST HERO TYPOGRAPHY & VISIBILITY ENGINE
   - Light mode: Pure 100% solid black text without white color or shadow
   - Dark mode: Pure 100% white text with deep contrast drop-shadow
   ======================================================== */
.hero-headline,
.hero-headline span,
.hero-headline * {
  color: #000000 !important;
  -webkit-text-fill-color: #000000 !important;
  text-shadow: none !important;
  filter: none !important;
}

html.dark .hero-headline,
html.dark .hero-headline span,
html.dark .hero-headline * {
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95), 0 4px 25px rgba(0, 0, 0, 0.95) !important;
}

.hero-subtitle {
  color: #000000 !important;
  text-shadow: none !important;
}

html.dark .hero-subtitle {
  color: #ffffff !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.95), 0 2px 14px rgba(0, 0, 0, 0.9) !important;
}

.hero-badge-glass {
  background-color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-color: rgba(203, 213, 225, 0.9);
  color: #000000 !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

html.dark .hero-badge-glass {
  background-color: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-color: rgba(51, 65, 85, 0.9);
  color: #ffffff !important;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
}"""

match = re.search(old_css_pattern, css, re.DOTALL)
if match:
    css = css[:match.start()] + new_hero_css
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css hero typography successfully!")
else:
    print("Warning: old_css_pattern not matched in style.css")
