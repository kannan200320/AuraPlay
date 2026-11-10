import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update section tag
c = re.sub(r'<section class="relative min-h-\[calc\(100vh-5rem\)\] flex items-center overflow-hidden py-6 sm:py-8 lg:py-10 bg-[^"]*"',
           '<section class="relative min-h-[calc(100vh-5rem)] flex items-center overflow-hidden py-6 sm:py-8 lg:py-10 bg-darkslate-deep text-white"',
           c)

# Update hero-bg-container
old_bg_index = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', c, re.DOTALL).group(0)
new_bg_index = '''<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container bg-darkslate-deep">
        <img src="assets/images/hero-bg-home1.png" alt="AuraPlay Arena Setup" class="hero-bg-img w-full h-full object-cover object-center transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-black/60 via-black/30 to-transparent pointer-events-none"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-black/35 via-transparent to-black/45 pointer-events-none"></div>
      </div>'''
c = c.replace(old_bg_index, new_bg_index)

# Update Hardware Spec Chips in index.html to dark glass
c = re.sub(r'bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-black dark:text-white',
           'bg-slate-900/80 backdrop-blur-md border border-white/20 text-xs font-bold text-white',
           c)

# Update Fast stats labels and border
c = c.replace('border-t border-slate-200 dark:border-darkslate-border max-w-lg mx-auto lg:mx-0',
              'border-t border-white/15 max-w-lg mx-auto lg:mx-0')
c = re.sub(r'text-\[11px\] sm:text-xs text-black dark:text-slate-400 font-semibold uppercase',
           'text-[11px] sm:text-xs text-slate-300 font-semibold uppercase',
           c)

# Update secondary CTA button in hero
c = re.sub(r'<a href="games\.html" class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl text-sm sm:text-base font-bold text-black dark:text-slate-200 dark:text-white bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border hover:bg-slate-100 dark:hover:bg-darkslate-lighter transition-all text-center flex items-center justify-center space-x-2 rtl:space-x-reverse">',
           '<a href="games.html" class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl text-sm sm:text-base font-bold text-white bg-slate-900/80 hover:bg-slate-800 border border-white/20 backdrop-blur-md transition-all text-center flex items-center justify-center space-x-2 rtl:space-x-reverse">',
           c)

with open('index.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(c)
print("index.html updated successfully!")


# 2. Update player-lounge.html
with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Update section tag
c = re.sub(r'<section class="relative min-h-\[calc\(100vh-5rem\)\] flex items-center overflow-hidden py-6 sm:py-8 lg:py-10 bg-[^"]*"',
           '<section class="relative min-h-[calc(100vh-5rem)] flex items-center overflow-hidden py-6 sm:py-8 lg:py-10 bg-darkslate-deep text-white"',
           c)

# Update hero-bg-container
old_bg_lounge = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', c, re.DOTALL).group(0)
new_bg_lounge = '''<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container bg-darkslate-deep">
        <img src="assets/images/hero-bg-lounge.png" alt="AuraPlay Lounge Suite" class="hero-bg-img w-full h-full object-cover object-center transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-black/60 via-black/30 to-transparent pointer-events-none"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-black/35 via-transparent to-black/45 pointer-events-none"></div>
      </div>'''
c = c.replace(old_bg_lounge, new_bg_lounge)

# Update Experience chips in player-lounge.html to dark glass
c = re.sub(r'bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-black dark:text-white',
           'bg-slate-900/80 backdrop-blur-md border border-white/20 text-xs font-bold text-white',
           c)

# Update secondary CTA button in hero
c = re.sub(r'<a href="#lounge-bays" class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl text-sm sm:text-base font-bold text-black dark:text-slate-200 dark:text-white bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border hover:bg-slate-100 dark:hover:bg-darkslate-lighter transition-all text-center">',
           '<a href="#lounge-bays" class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl text-sm sm:text-base font-bold text-white bg-slate-900/80 hover:bg-slate-800 border border-white/20 backdrop-blur-md transition-all text-center">',
           c)

with open('player-lounge.html', 'w', encoding='utf-8', newline='\r\n') as f:
    f.write(c)
print("player-lounge.html updated successfully!")


# 3. Update centered hero pages
def update_centered(filepath, img_src, img_alt):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    # Update section tag: ensure bg-darkslate-deep text-white
    c = re.sub(r'(<!--\s*={2,}\s*SECTION 1:.*?-->\s*<section class="[^"]*?)(?:bg-slate-100(?:/90)?\s+dark:bg-darkslate-deep(?:/90)?)([^"]*?)">',
               r'\1bg-darkslate-deep text-white\2">',
               c, flags=re.DOTALL)

    # Update hero-bg-container: pure rich dark mode scrim in both modes
    old_bg = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', c, re.DOTALL).group(0)
    new_bg = f'''<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container bg-darkslate-deep">
        <img src="{img_src}" alt="{img_alt}" class="hero-bg-img w-full h-full object-cover object-center transform scale-105">
        <div class="absolute inset-0 bg-black/35 pointer-events-none"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-black/40 via-transparent to-black/50 pointer-events-none"></div>
      </div>'''
    c = c.replace(old_bg, new_bg)

    # If about.html, update pillars and secondary button
    if filepath == 'about.html':
        c = re.sub(r'class="p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm space-y-2"',
                   'class="p-5 rounded-2xl bg-slate-900/80 backdrop-blur-md border border-white/15 shadow-sm space-y-2"',
                   c)
        c = re.sub(r'<h3 class="font-black text-sm uppercase text-black dark:text-white font-display">',
                   '<h3 class="font-black text-sm uppercase text-white font-display">',
                   c)
        c = re.sub(r'<p class="text-xs text-black dark:text-slate-400 leading-relaxed">',
                   '<p class="text-xs text-slate-300 leading-relaxed">',
                   c)
        c = re.sub(r'<a href="pricing\.html" class="w-full sm:w-auto px-7 py-3\.5 rounded-xl font-bold text-xs uppercase tracking-wider text-black dark:text-slate-200 dark:text-white bg-white dark:bg-darkslate-card hover:bg-slate-50 dark:hover:bg-darkslate-lighter border border-slate-200 dark:border-darkslate-border transition-all">',
                   '<a href="pricing.html" class="w-full sm:w-auto px-7 py-3.5 rounded-xl font-bold text-xs uppercase tracking-wider text-white bg-slate-900/80 hover:bg-slate-800 border border-white/20 backdrop-blur-md transition-all">',
                   c)

    with open(filepath, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(c)
    print(f"{filepath} updated successfully!")

update_centered('about.html', 'assets/images/hero-bg-about.jpg', 'AuraPlay Hardware Lab')
update_centered('games.html', 'assets/images/hero-bg-games.jpg', 'AuraPlay Games Arena')
update_centered('pricing.html', 'assets/images/hero-bg-pricing.png', 'AuraPlay Pricing Hardware')
update_centered('membership.html', 'assets/images/hero-bg-membership.png', 'AuraPlay VIP Memberships & Lounge Setup')
update_centered('book-slot.html', 'assets/images/tour-pc-arena-wide.jpg', 'AuraPlay PC Arena Station Floor')
update_centered('blog.html', 'assets/images/hero-bg-blog.png', 'AuraPlay Esports Engineering & Hardware Lab')
update_centered('contact.html', 'assets/images/hero-bg-contact.png', 'AuraPlay 24/7 Welcome Desk & Support Center')
