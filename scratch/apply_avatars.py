import re

# 1. index.html
with open('index.html', 'r', encoding='utf-8') as f:
    txt = f.read()

txt = re.sub(
    r'<div class="w-10 h-10 rounded-full bg-cyan-500 text-white font-bold flex items-center justify-center">MK</div>',
    '<img src="assets/images/avatar-1.jpg" alt="Marcus \'Kryptic\' Vance" class="w-10 h-10 rounded-full object-cover shrink-0 border border-cyan-500/30 shadow-md">',
    txt
)
txt = re.sub(
    r'<div class="w-10 h-10 rounded-full bg-pink-500 text-white font-bold flex items-center justify-center">SR</div>',
    '<img src="assets/images/avatar-2.jpg" alt="Sophia Rodriguez" class="w-10 h-10 rounded-full object-cover shrink-0 border border-pink-500/30 shadow-md">',
    txt
)
txt = re.sub(
    r'<div class="w-10 h-10 rounded-full bg-purple-500 text-white font-bold flex items-center justify-center">AL</div>',
    '<img src="assets/images/avatar-4.jpg" alt="Alexandre Lim" class="w-10 h-10 rounded-full object-cover shrink-0 border border-purple-500/30 shadow-md">',
    txt
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated index.html avatars.")

# 2. about.html
with open('about.html', 'r', encoding='utf-8') as f:
    txt = f.read()

txt = re.sub(
    r'<div class="w-10 h-10 rounded-full bg-gradient-to-tr from-cyan-500 to-purple-600 text-white font-bold flex items-center justify-center text-sm shadow-md">\s*SP\s*</div>',
    '<img src="assets/images/avatar-3.jpg" alt="Samira Patel" class="w-10 h-10 rounded-full object-cover shrink-0 border border-cyan-500/30 shadow-md">',
    txt
)
txt = re.sub(
    r'<div class="w-10 h-10 rounded-full bg-gradient-to-tr from-purple-600 to-pink-500 text-white font-bold flex items-center justify-center text-sm shadow-md">\s*JR\s*</div>',
    '<img src="assets/images/avatar-5.jpg" alt="Jonas Richter" class="w-10 h-10 rounded-full object-cover shrink-0 border border-purple-500/30 shadow-md">',
    txt
)
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated about.html avatars.")

# 3. player-lounge.html
with open('player-lounge.html', 'r', encoding='utf-8') as f:
    txt = f.read()

txt = re.sub(
    r'<div class="w-11 h-11 rounded-full bg-gradient-to-tr from-purple-600 to-pink-500 text-white font-bold flex items-center justify-center text-sm shadow-md shrink-0">\s*DS\s*</div>',
    '<img src="assets/images/avatar-4.jpg" alt="Daniel & Squad" class="w-11 h-11 rounded-full object-cover shrink-0 border border-purple-500/30 shadow-md">',
    txt
)
txt = re.sub(
    r'<div class="w-11 h-11 rounded-full bg-gradient-to-tr from-pink-500 to-cyan-500 text-white font-bold flex items-center justify-center text-sm shadow-md shrink-0">\s*TC\s*</div>',
    '<img src="assets/images/avatar-1.jpg" alt="Tyler Chen" class="w-11 h-11 rounded-full object-cover shrink-0 border border-pink-500/30 shadow-md">',
    txt
)
with open('player-lounge.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated player-lounge.html avatars.")

# 4. membership.html
with open('membership.html', 'r', encoding='utf-8') as f:
    txt = f.read()

txt = re.sub(
    r'<div class="w-9 h-9 rounded-full bg-cyan-500/20 text-cyan-500 flex items-center justify-center font-bold text-xs">\s*VA\s*</div>',
    '<img src="assets/images/avatar-5.jpg" alt="ViperAim_" class="w-9 h-9 rounded-full object-cover shrink-0 border border-cyan-500/30 shadow-md">',
    txt
)
txt = re.sub(
    r'<div class="w-9 h-9 rounded-full bg-purple-500/20 text-purple-500 flex items-center justify-center font-bold text-xs">\s*KX\s*</div>',
    '<img src="assets/images/avatar-1.jpg" alt="KronoX_CS" class="w-9 h-9 rounded-full object-cover shrink-0 border border-purple-500/30 shadow-md">',
    txt
)
txt = re.sub(
    r'<div class="w-9 h-9 rounded-full bg-amber-500/20 text-amber-500 flex items-center justify-center font-bold text-xs">\s*ZL\s*</div>',
    '<img src="assets/images/avatar-2.jpg" alt="ZeroLag_Sim" class="w-9 h-9 rounded-full object-cover shrink-0 border border-amber-500/30 shadow-md">',
    txt
)
with open('membership.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated membership.html avatars.")

# 5. blog.html
with open('blog.html', 'r', encoding='utf-8') as f:
    txt = f.read()

txt = re.sub(
    r'<div class="w-10 h-10 rounded-full bg-gradient-to-tr from-cyan-500 to-purple-600 flex items-center justify-center text-white font-bold text-xs">\s*EL\s*</div>',
    '<img src="assets/images/avatar-1.jpg" alt="Dr. Eric Lin" class="w-10 h-10 rounded-full object-cover shrink-0 border border-cyan-500/30 shadow-md">',
    txt
)
with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated blog.html avatars.")

# 6. blog-detail pages
blog_detail_files = [
    'blog-detail.html',
    'blog-detail-cs2-subtick.html',
    'blog-detail-direct-drive-sim.html',
    'blog-detail-wooting-rapid-trigger.html',
    'blog-detail-zero-bufferbloat.html'
]

for bf in blog_detail_files:
    with open(bf, 'r', encoding='utf-8') as f:
        txt = f.read()
    # Author image
    txt = re.sub(
        r'<img\s+src="https://images\.unsplash\.com/[^"]*"\s+alt="Dr\.\s*Eric\s*Lin"[^>]*>',
        '<img src="assets/images/avatar-1.jpg" alt="Dr. Eric Lin" class="w-11 h-11 rounded-full object-cover ring-2 ring-cyan-500/50 shadow-md shrink-0">',
        txt
    )
    # Comments
    txt = re.sub(
        r'<div class="w-8 h-8 rounded-full bg-cyan-500/20 text-cyan-500 flex items-center justify-center font-bold text-xs">\s*RM\s*</div>',
        '<img src="assets/images/avatar-2.jpg" alt="RazeMain99" class="w-8 h-8 rounded-full object-cover shrink-0 border border-cyan-500/30 shadow-sm">',
        txt
    )
    txt = re.sub(
        r'<div class="w-8 h-8 rounded-full bg-amber-500/20 text-amber-500 flex items-center justify-center font-bold text-xs">\s*CS\s*</div>',
        '<img src="assets/images/avatar-4.jpg" alt="CS2_Veteran" class="w-8 h-8 rounded-full object-cover shrink-0 border border-amber-500/30 shadow-sm">',
        txt
    )
    txt = re.sub(
        r'<div class="w-8 h-8 rounded-full bg-pink-500/20 text-pink-500 flex items-center justify-center font-bold text-xs">\s*TK\s*</div>',
        '<img src="assets/images/avatar-3.jpg" alt="TekkenKing_SF" class="w-8 h-8 rounded-full object-cover shrink-0 border border-pink-500/30 shadow-sm">',
        txt
    )
    with open(bf, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"Updated {bf} avatars.")

# 7. Dashboard files
dash_files = [
    'dashboard.html',
    'dashboard-packs.html',
    'dashboard-history.html',
    'dashboard-payments.html',
    'dashboard-settings.html'
]

for df in dash_files:
    with open(df, 'r', encoding='utf-8') as f:
        txt = f.read()
    # Sidebar avatar
    txt = re.sub(
        r'<div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-purple-600 flex items-center justify-center font-black text-white text-sm shadow-md">\s*PA\s*</div>',
        '<img src="assets/images/avatar-5.jpg" alt="PhoenixAim" class="w-10 h-10 rounded-xl object-cover shrink-0 shadow-md border border-cyan-500/30">',
        txt
    )
    # Settings main profile card avatar
    txt = re.sub(
        r'<div class="w-24 h-24 rounded-3xl bg-gradient-to-tr from-cyan-500 via-purple-600 to-pink-500 flex items-center justify-center font-black text-white text-3xl shadow-xl shadow-cyan-500/20">\s*PA\s*</div>',
        '<img src="assets/images/avatar-5.jpg" alt="PhoenixAim" class="w-24 h-24 rounded-3xl object-cover shadow-xl shadow-cyan-500/20 border-2 border-cyan-500/40">',
        txt
    )
    with open(df, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"Updated {df} avatars.")

print("All avatar replacements applied successfully!")
