from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load hero-bg-about.jpg
bg = Image.open('assets/images/hero-bg-about.jpg').convert('RGBA')

# Create a subtle scrim: dark:bg-black/35 + subtle top/bottom vignette
overlay = Image.new('RGBA', bg.size, (0, 0, 0, int(255 * 0.35)))
bg_scrim = Image.alpha_composite(bg, overlay)

# Save simulated dark hero
bg_scrim.convert('RGB').save('scratch/simulated_dark_hero.jpg')
print("Simulated dark hero saved successfully!")
