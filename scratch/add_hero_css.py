css_addon = """
/* ========================================================
   HIGH-CONTRAST HERO TYPOGRAPHY & VISIBILITY ENGINE
   Guarantees maximum text pop and razor-sharp readability
   over vivid hero background imagery in both light and dark modes
   ======================================================== */
.hero-headline {
  color: #020617;
  text-shadow: 0 1px 3px rgba(255, 255, 255, 0.9), 0 0 18px rgba(255, 255, 255, 0.75);
}

html.dark .hero-headline {
  color: #ffffff !important;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95), 0 4px 25px rgba(0, 0, 0, 0.95);
}

.hero-subtitle {
  color: #020617;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
}

html.dark .hero-subtitle {
  color: #f8fafc !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.95), 0 2px 14px rgba(0, 0, 0, 0.9);
}

.hero-badge-glass {
  background-color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-color: rgba(203, 213, 225, 0.9);
  color: #020617;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

html.dark .hero-badge-glass {
  background-color: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-color: rgba(51, 65, 85, 0.9);
  color: #f8fafc;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
}
"""

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

if 'HIGH-CONTRAST HERO TYPOGRAPHY & VISIBILITY ENGINE' not in content:
    content = content.rstrip() + '\n' + css_addon
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added hero typography engine to assets/css/style.css")
else:
    print("Hero typography engine already exists in assets/css/style.css")
