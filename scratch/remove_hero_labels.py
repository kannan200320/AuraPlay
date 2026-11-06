import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_txt = f.read()

idx_pat = re.compile(
    r'\s*<div class="inline-flex items-center space-x-2\.5 rtl:space-x-reverse px-3\.5 py-1 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs sm:text-sm font-extrabold shadow-sm">\s*<span class="w-2\.5 h-2\.5 rounded-full bg-emerald-500 live-indicator"></span>\s*<span>AURAPLAY GAMING & PC LOUNGE.*?</span>\s*</div>',
    re.DOTALL
)

new_idx, c1 = idx_pat.subn('', idx_txt)
print(f"index.html: removed label count={c1}")
assert c1 == 1, "Failed to remove label in index.html"
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_idx)


with open('player-lounge.html', 'r', encoding='utf-8') as f:
    lounge_txt = f.read()

lounge_pat = re.compile(
    r'\s*<div class="inline-flex items-center space-x-2\.5 rtl:space-x-reverse px-3\.5 py-1 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-purple-400 dark:border-purple-500/50 text-purple-950 dark:text-purple-200 text-xs sm:text-sm font-extrabold shadow-sm">\s*<span class="w-2\.5 h-2\.5 rounded-full bg-emerald-500 live-indicator"></span>\s*<span>THE SOCIAL GAMING SANCTUARY.*?</span>\s*</div>',
    re.DOTALL
)

new_lounge, c2 = lounge_pat.subn('', lounge_txt)
print(f"player-lounge.html: removed label count={c2}")
assert c2 == 1, "Failed to remove label in player-lounge.html"
with open('player-lounge.html', 'w', encoding='utf-8') as f:
    f.write(new_lounge)

print("Successfully removed hero labels from home pages!")
