from PIL import Image
import numpy as np, glob

imgs = [
    'assets/images/hero-bg-home1.png',
    'assets/images/hero-bg-lounge.png',
    'assets/images/hero-bg-about.jpg',
    'assets/images/hero-bg-games.jpg',
    'assets/images/hero-bg-pricing.png',
    'assets/images/hero-bg-membership.png',
    'assets/images/tour-pc-arena-wide.jpg',
    'assets/images/hero-bg-blog.png',
    'assets/images/hero-bg-contact.png'
]

for p in imgs:
    im = Image.open(p)
    arr = np.array(im.convert('RGB'))
    print(f"{p}: size={im.size}, mean RGB={arr.mean(axis=(0,1)).round(1)}")
