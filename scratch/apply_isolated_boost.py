import re

# 1. Update style.css
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

target_css = """.hero-subtitle {
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

replacement_css = """/* Standard Hero Subtitle for all pages */
.hero-subtitle {
  color: #000000 !important;
  text-shadow: none !important;
}

html.dark .hero-subtitle {
  color: #ffffff !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.95), 0 2px 14px rgba(0, 0, 0, 0.9) !important;
}

/* Specifically intensified text color for the 5 screenshot sentences in light mode */
.hero-subtitle-boosted {
  color: #000000 !important;
  font-weight: 700 !important;
  -webkit-text-stroke: 0.35px #000000;
  text-shadow: 0 0 1px #000000 !important;
}

html.dark .hero-subtitle-boosted {
  color: #ffffff !important;
  font-weight: 500 !important;
  -webkit-text-stroke: 0px transparent !important;
  text-shadow: 0 1px 6px rgba(0, 0, 0, 0.95), 0 2px 14px rgba(0, 0, 0, 0.9) !important;
}"""

if target_css in css:
    css = css.replace(target_css, replacement_css, 1)
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated assets/css/style.css successfully!")
else:
    print("Warning: target_css not found in style.css!")

# 2. Update the 5 screenshot pages to use hero-subtitle-boosted
boosted_pages = ['index.html', 'player-lounge.html', 'about.html', 'games.html', 'pricing.html']
for p in boosted_pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    # Replace hero-subtitle with hero-subtitle-boosted on these 5 pages
    if 'hero-subtitle' in content and 'hero-subtitle-boosted' not in content:
        content = content.replace('hero-subtitle', 'hero-subtitle-boosted')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Applied hero-subtitle-boosted to {p}")
    else:
        print(f"{p} already has hero-subtitle-boosted or no hero-subtitle")

# 3. Ensure other pages keep regular hero-subtitle and font-medium
other_pages = ['membership.html', 'blog.html', 'contact.html', 'book-slot.html']
for p in other_pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    # Ensure they have standard hero-subtitle and font-medium (not boosted)
    content = content.replace('hero-subtitle-boosted', 'hero-subtitle')
    content = content.replace('font-bold hero-subtitle', 'font-medium hero-subtitle')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Verified standard styling on {p}")
