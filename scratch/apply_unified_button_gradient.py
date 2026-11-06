# Script to apply unified button gradient to all pages
import glob
import re

GRADIENT_BTN = "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white"

# We will define precise replacements for each button
replacements = [
    # Multi-gradient variants
    ("bg-gradient-to-r from-cyan-500 via-purple-600 to-pink-500 hover:from-cyan-400 hover:to-purple-500 text-white", GRADIENT_BTN),
    ("bg-gradient-to-r from-cyan-500 via-purple-600 to-pink-500 hover:from-cyan-400 hover:to-purple-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-purple-600 via-pink-600 to-cyan-500 hover:from-purple-500 hover:to-cyan-400 text-white", GRADIENT_BTN),
    ("bg-gradient-to-r from-purple-600 via-pink-600 to-cyan-500 hover:from-purple-500 hover:to-cyan-400", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:from-purple-500 hover:to-pink-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-purple-600 to-pink-600", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-400 hover:to-pink-400 text-white", GRADIENT_BTN),
    ("bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-400 hover:to-pink-400", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-400 hover:to-purple-500 text-white", GRADIENT_BTN),
    ("bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-400 hover:to-purple-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-pink-500 to-purple-600", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-cyan-400 via-cyan-500 to-purple-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-cyan-400 to-purple-400", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-cyan-400 to-cyan-500 hover:from-cyan-300 hover:to-cyan-400", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("bg-gradient-to-r from-cyan-400 to-cyan-500", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),

    # Solid cyan button variants
    ("text-white bg-cyan-600 hover:bg-cyan-500", GRADIENT_BTN),
    ("bg-cyan-600 hover:bg-cyan-500 text-white", GRADIENT_BTN),
    ("bg-cyan-600 hover:bg-cyan-500", GRADIENT_BTN),
    ("bg-cyan-500 text-black hover:bg-cyan-400", GRADIENT_BTN),
    ("bg-cyan-500 hover:bg-cyan-400 text-black", GRADIENT_BTN),
    ("bg-cyan-500 hover:bg-cyan-400", "bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500"),
    ("text-black bg-cyan-400 hover:bg-cyan-300", GRADIENT_BTN),
    ("bg-cyan-400 hover:bg-cyan-300 text-black", GRADIENT_BTN),
    ("bg-cyan-400 hover:bg-cyan-300", GRADIENT_BTN),

    # Solid purple button variants
    ("bg-purple-600 text-white hover:bg-purple-500", GRADIENT_BTN),
    ("text-white bg-purple-600 hover:bg-purple-500", GRADIENT_BTN),
    ("bg-purple-600 hover:bg-purple-500 text-white", GRADIENT_BTN),
    ("bg-purple-600 hover:bg-purple-500", GRADIENT_BTN),
    ("bg-purple-600 text-white", GRADIENT_BTN),

    # Solid pink button variants
    ("bg-pink-600 text-white hover:bg-pink-500", GRADIENT_BTN),
    ("text-white bg-pink-600 hover:bg-pink-500", GRADIENT_BTN),
    ("bg-pink-600 hover:bg-pink-500 text-white", GRADIENT_BTN),
    ("bg-pink-600 hover:bg-pink-500", GRADIENT_BTN),
    ("bg-pink-600 text-white", GRADIENT_BTN),

    # Solid amber button variants
    ("bg-amber-500 text-black hover:bg-amber-400", GRADIENT_BTN),
    ("bg-amber-500 hover:bg-amber-400 text-black", GRADIENT_BTN),
    ("bg-amber-500 hover:bg-amber-400", GRADIENT_BTN),
    ("bg-amber-400 hover:bg-amber-300 text-black", GRADIENT_BTN),
    ("bg-amber-400 hover:bg-amber-300", GRADIENT_BTN),

    # Solid emerald button variants
    ("text-black bg-emerald-400 hover:bg-emerald-300", GRADIENT_BTN),
    ("bg-emerald-400 hover:bg-emerald-300 text-black", GRADIENT_BTN),
    ("bg-emerald-400 hover:bg-emerald-300", GRADIENT_BTN),
    ("bg-emerald-500 hover:bg-emerald-400 text-white", GRADIENT_BTN),
    ("bg-emerald-500 hover:bg-emerald-400", GRADIENT_BTN),
    ("bg-emerald-600 hover:bg-emerald-500 text-white", GRADIENT_BTN),
    ("bg-emerald-600 hover:bg-emerald-500", GRADIENT_BTN),
    ("bg-emerald-600 text-white", GRADIENT_BTN),
]

html_files = sorted(glob.glob('*.html'))
total_changed = 0

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    orig = c
    for old, new in replacements:
        if old in c:
            c = c.replace(old, new)
    
    # Fix any accidental duplicate text-white or text-black left behind on buttons
    # E.g. "text-black bg-gradient-to-r ... text-white" -> replace text-black
    c = re.sub(r'text-black\s+(bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white)', r'\1', c)
    c = re.sub(r'text-white\s+(bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white)', r'\1', c)

    if c != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(c)
        total_changed += 1
        print(f"Updated buttons in: {f}")

print(f"Finished. Total files updated: {total_changed}")
