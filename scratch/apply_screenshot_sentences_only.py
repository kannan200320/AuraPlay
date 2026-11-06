import re

# 1. Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_subtitle_css = """.hero-subtitle {
  color: #000000 !important;
  font-weight: 600 !important;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.6), 0 1px 2px rgba(255, 255, 255, 0.5) !important;
}

html.dark .hero-subtitle {
  color: #ffffff !important;
  font-weight: 500 !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.95), 0 2px 14px rgba(0, 0, 0, 0.9) !important;
}"""

new_subtitle_css = """.hero-subtitle {
  color: #000000 !important;
  font-weight: 700 !important;
  -webkit-text-stroke: 0.35px #000000;
  text-shadow: 0 0 1px #000000 !important;
}

html.dark .hero-subtitle {
  color: #ffffff !important;
  font-weight: 500 !important;
  -webkit-text-stroke: 0px transparent !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.95), 0 2px 14px rgba(0, 0, 0, 0.9) !important;
}"""

if old_subtitle_css in css:
    css = css.replace(old_subtitle_css, new_subtitle_css, 1)
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css with intensified text color stroke for hero-subtitle!")
else:
    print("Warning: old_subtitle_css not found in style.css")

# 2. Revert scrims back to vivid background visibility on all pages
pages = [
    'index.html',
    'player-lounge.html',
    'about.html',
    'games.html',
    'pricing.html',
    'membership.html',
    'book-slot.html',
    'blog.html',
    'contact.html'
]

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Restore scrims
    c = c.replace('from-slate-50/82 via-slate-50/55 to-transparent', 'from-slate-50/75 via-slate-50/45 to-transparent')
    c = c.replace('from-slate-50/72 via-slate-50/50 to-slate-50', 'from-slate-50/60 via-slate-50/35 to-slate-50')
    
    # For the 5 screenshot pages, ensure font-bold is set on the subtitle
    if p in ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html']:
        c = c.replace('font-semibold sm:font-bold', 'font-bold')
        c = c.replace('font-medium', 'font-bold')
    else:
        # For other pages, keep font-medium as original
        c = c.replace('font-semibold sm:font-bold', 'font-medium')
        
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Processed {p} successfully!")

print("All tasks completed!")
