with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace High-Contrast Typography & Hero Capsule Block
start_str = '/* ========================================================\n   HIGH-CONTRAST HERO TYPOGRAPHY & VISIBILITY ENGINE'
end_str = '/* ========================================================\n   FAQ ACCORDION & DROPDOWN COMPONENT'

start_idx = css.find(start_str)
end_idx = css.find(end_str)

assert start_idx != -1, "start_str not found!"
assert end_idx != -1, "end_str not found!"

new_hero_css = '''/* ========================================================
   UNIFIED HERO TYPOGRAPHY & VISIBILITY ENGINE (BOTH MODES)
   Light mode hero section features the exact same dark mode
   text styling (brilliant white with drop shadow, dark glass capsule)
   and deep, vibrant, highly visible background image.
   ======================================================== */
.hero-headline,
.hero-headline span,
.hero-headline *,
html.dark .hero-headline,
html.dark .hero-headline span,
html.dark .hero-headline * {
  color: #ffffff !important;
  -webkit-text-fill-color: #ffffff !important;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95), 0 4px 25px rgba(0, 0, 0, 0.95) !important;
  filter: none !important;
}

/* Standard Hero Subtitle for all pages */
.hero-subtitle,
html.dark .hero-subtitle,
.hero-subtitle-boosted,
html.dark .hero-subtitle-boosted {
  color: rgba(255, 255, 255, 0.95) !important;
  font-weight: 500 !important;
  text-shadow: 0 1px 4px rgba(0, 0, 0, 0.9) !important;
  -webkit-text-stroke: 0px transparent !important;
}

.hero-badge-glass,
html.dark .hero-badge-glass {
  background-color: rgba(15, 23, 42, 0.85) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(56, 189, 248, 0.45) !important;
  color: #38bdf8 !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5) !important;
}

/* ========================================================
   HERO SUBTITLE REFERENCE CAPSULE COMPONENT
   Matches the reference hero design with a sleek, translucent
   pill-card container and fine border for maximum legibility
   over vibrant, highly visible background imagery in both themes.
   ======================================================== */
.hero-capsule,
html.dark .hero-capsule {
  background-color: rgba(0, 0, 0, 0.5) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(255, 255, 255, 0.22) !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45) !important;
  transition: all 0.25s ease;
}

.hero-capsule p,
.hero-capsule .hero-subtitle,
.hero-capsule .hero-subtitle-boosted,
html.dark .hero-capsule p,
html.dark .hero-capsule .hero-subtitle,
html.dark .hero-capsule .hero-subtitle-boosted {
  color: rgba(255, 255, 255, 0.95) !important;
  font-weight: 500 !important;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.85) !important;
  -webkit-text-stroke: 0px transparent !important;
  margin: 0 !important;
}

'''

css = css[:start_idx] + new_hero_css + css[end_idx:]

# Update Background Image Clarity Block
bg_start_str = '/* ========================================================\n   HERO BACKGROUND IMAGE CLARITY & VISIBILITY'
bg_end_str = '/* ========================================================\n   DESKTOP DROPDOWN FREEZE-ON-CLICK'

bg_start_idx = css.find(bg_start_str)
bg_end_idx = css.find(bg_end_str)

assert bg_start_idx != -1, "bg_start_str not found!"
assert bg_end_idx != -1, "bg_end_str not found!"

new_bg_css = '''/* ========================================================
   HERO BACKGROUND IMAGE CLARITY & VISIBILITY (BOTH MODES)
   Ensures the hero background image is vibrant, rich, sharp,
   and fully visible across the entire section in both light
   and dark modes, exactly matching dark mode richness.
   ======================================================== */
.hero-bg-container {
  background-color: #090D16 !important;
}

.hero-bg-img,
.hero-bg-container img,
section:first-of-type .absolute.inset-0 > img {
  opacity: 0.95 !important;
  filter: saturate(1.25) contrast(1.1) brightness(0.96) !important;
  -webkit-filter: saturate(1.25) contrast(1.1) brightness(0.96) !important;
}

'''

css = css[:bg_start_idx] + new_bg_css + css[bg_end_idx:]

with open('assets/css/style.css', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(css)

print("assets/css/style.css successfully updated for unified hero visibility!")
