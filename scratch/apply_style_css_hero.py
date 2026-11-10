with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update the first block to add .hero-capsule
old_block_1 = '''.hero-badge-glass {
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
}'''

new_block_1 = '''.hero-badge-glass {
  background-color: rgba(255, 255, 255, 0.92) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  border: 1px solid rgba(203, 213, 225, 0.9) !important;
  color: #000000 !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06) !important;
}

html.dark .hero-badge-glass {
  background-color: rgba(15, 23, 42, 0.85) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(56, 189, 248, 0.4) !important;
  color: #38bdf8 !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5) !important;
}

/* ========================================================
   HERO SUBTITLE REFERENCE CAPSULE COMPONENT
   Matches the reference hero design with a sleek, translucent
   pill-card container and fine border for maximum legibility
   over vibrant, highly visible background imagery in both themes.
   ======================================================== */
.hero-capsule {
  background-color: rgba(255, 255, 255, 0.88) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border: 1px solid rgba(203, 213, 225, 0.9) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08) !important;
  transition: all 0.25s ease;
}

html.dark .hero-capsule {
  background-color: rgba(0, 0, 0, 0.45) !important;
  backdrop-filter: blur(14px) !important;
  -webkit-backdrop-filter: blur(14px) !important;
  border: 1px solid rgba(255, 255, 255, 0.22) !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45) !important;
}

.hero-capsule p,
.hero-capsule .hero-subtitle,
.hero-capsule .hero-subtitle-boosted {
  color: #000000 !important;
  font-weight: 600 !important;
  text-shadow: none !important;
  -webkit-text-stroke: 0px transparent !important;
  margin: 0 !important;
}

html.dark .hero-capsule p,
html.dark .hero-capsule .hero-subtitle,
html.dark .hero-capsule .hero-subtitle-boosted {
  color: rgba(255, 255, 255, 0.95) !important;
  font-weight: 500 !important;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.75) !important;
  -webkit-text-stroke: 0px transparent !important;
}'''

assert old_block_1 in css, "old_block_1 not found!"
css = css.replace(old_block_1, new_block_1)

# 2. Update the background clarity block
old_block_2 = '''/* ========================================================
   HERO BACKGROUND IMAGE COLOR & CLARITY (LIGHT MODE ONLY)
   Slightly increases background image color, saturation,
   and sharpness in light mode so it is never washed out or blurry.
   Dark mode remains completely untouched.
   ======================================================== */
html:not(.dark) .hero-bg-img,
html:not(.dark) .hero-bg-container img,
html:not(.dark) section:first-of-type .absolute.inset-0 > img {
  opacity: 0.96 !important;
  filter: saturate(1.25) contrast(1.08) brightness(0.98) !important;
  -webkit-filter: saturate(1.25) contrast(1.08) brightness(0.98) !important;
}

html:not(.dark) .hero-bg-container div[class*="backdrop-blur"],
html:not(.dark) section:first-of-type .absolute.inset-0 > div[class*="backdrop-blur"] {
  backdrop-filter: none !important;
  -webkit-backdrop-filter: none !important;
}'''

new_block_2 = '''/* ========================================================
   HERO BACKGROUND IMAGE CLARITY & VISIBILITY (BOTH MODES)
   Ensures the hero background image is vibrant, rich, sharp,
   and fully visible across the entire section in both light
   and dark modes, exactly matching the reference design.
   ======================================================== */
.hero-bg-img,
.hero-bg-container img,
section:first-of-type .absolute.inset-0 > img {
  opacity: 0.96 !important;
  filter: saturate(1.22) contrast(1.08) brightness(1.0) !important;
  -webkit-filter: saturate(1.22) contrast(1.08) brightness(1.0) !important;
}

html.dark .hero-bg-img,
html.dark .hero-bg-container img,
html.dark section:first-of-type .absolute.inset-0 > img {
  opacity: 0.94 !important;
  filter: saturate(1.25) contrast(1.1) brightness(0.96) !important;
  -webkit-filter: saturate(1.25) contrast(1.1) brightness(0.96) !important;
}'''

assert old_block_2 in css, "old_block_2 not found!"
css = css.replace(old_block_2, new_block_2)

with open('assets/css/style.css', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(css)

print("Successfully updated assets/css/style.css with hero reference styles!")
