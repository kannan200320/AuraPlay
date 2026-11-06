import glob
import re

html_files = sorted(glob.glob('*.html'))

# Replacement rules: (regex_pattern, replacement_str)
# Note: "only change the button colour."
# Target color: bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white

replacements = [
    # 1. 3-color gradient navbar & CTA buttons
    ('bg-gradient-to-r from-cyan-500 via-purple-600 to-pink-500 hover:from-cyan-400 hover:to-purple-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-purple-600 via-pink-600 to-cyan-500 hover:from-purple-500 hover:to-cyan-400',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:from-purple-500 hover:to-pink-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-purple-600 to-pink-600',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-400 hover:to-pink-400',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-pink-500 to-purple-600 hover:from-pink-400 hover:to-purple-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-pink-500 to-purple-600',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-cyan-400 via-cyan-500 to-purple-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-cyan-400 to-purple-400',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-cyan-400 to-cyan-500 hover:from-cyan-300 hover:to-cyan-400',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
    ('bg-gradient-to-r from-cyan-400 to-cyan-500',
     'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500'),
]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    match_count = 0
    for old, new in replacements:
        cnt = c.count(old)
        if cnt:
            match_count += cnt
    if match_count:
        print(f"{f}: {match_count} gradient matches")
