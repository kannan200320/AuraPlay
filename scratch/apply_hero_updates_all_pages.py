import re

# Update index.html
def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update hero-bg-container
    old_bg = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', content, re.DOTALL).group(0)
    new_bg = '''<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">
        <img src="assets/images/hero-bg-home1.png" alt="AuraPlay Arena Setup" class="hero-bg-img w-full h-full object-cover object-center transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-white/40 via-white/15 to-transparent dark:from-black/60 dark:via-black/30 dark:to-transparent pointer-events-none"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/25 via-transparent to-white/35 dark:from-black/35 dark:via-transparent dark:to-black/45 pointer-events-none"></div>
      </div>'''
    content = content.replace(old_bg, new_bg)

    # 2. Add badge above h1 if not present
    old_h1_block = re.search(r'(<div class="lg:col-span-7 space-y-3.5 lg:space-y-4 text-center lg:text-left rtl:lg:text-right">\s*)(<h1)', content, re.DOTALL)
    if old_h1_block:
        new_h1_block = old_h1_block.group(1) + '''<!-- Hero Reference Badge -->
            <div class="inline-flex items-center space-x-2 rtl:space-x-reverse px-4 py-1.5 rounded-full hero-badge-glass text-xs font-black uppercase tracking-widest shadow-md mb-2">
              <span class="w-2 h-2 rounded-full bg-cyan-500 animate-pulse"></span>
              <span>NOW LIVE: 360HZ LIQUID-COOLED ARENA</span>
            </div>\n\n            ''' + old_h1_block.group(2)
        content = content.replace(old_h1_block.group(0), new_h1_block)

    # 3. Wrap subtitle p in .hero-capsule
    old_p = re.search(r'<p class="text-sm sm:text-base lg:text-base xl:text-lg text-black dark:text-white max-w-2xl mx-auto lg:mx-0 font-bold leading-normal sm:leading-relaxed hero-subtitle-boosted">.*?Step into the ultimate competitive gaming arena.*?</p>', content, re.DOTALL).group(0)
    new_p = '''<!-- Hero Subtitle Reference Capsule -->
            <div class="hero-capsule rounded-2xl sm:rounded-3xl p-4 sm:p-5 max-w-2xl mx-auto lg:mx-0">
              <p class="text-sm sm:text-base leading-relaxed hero-subtitle-boosted text-center lg:text-left rtl:lg:text-right">
                Step into the ultimate competitive gaming arena. Custom liquid-cooled RTX 4090 battlestations, 360Hz QD-OLED monitors, zero-jitter 10 Gbps dedicated fiber, and an elite PC lounge built for champions.
              </p>
            </div>'''
    content = content.replace(old_p, new_p)

    with open('index.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content)
    print("index.html updated successfully!")

# Update player-lounge.html
def update_lounge():
    with open('player-lounge.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update hero-bg-container
    old_bg = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', content, re.DOTALL).group(0)
    new_bg = '''<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">
        <img src="assets/images/hero-bg-lounge.png" alt="AuraPlay Lounge Suite" class="hero-bg-img w-full h-full object-cover object-center transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-white/40 via-white/15 to-transparent dark:from-black/60 dark:via-black/30 dark:to-transparent pointer-events-none"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/25 via-transparent to-white/35 dark:from-black/35 dark:via-transparent dark:to-black/45 pointer-events-none"></div>
      </div>'''
    content = content.replace(old_bg, new_bg)

    # 2. Add badge above h1 if not present
    old_h1_block = re.search(r'(<div class="lg:col-span-7 space-y-3.5 lg:space-y-4 text-center lg:text-left rtl:lg:text-right">\s*)(<h1)', content, re.DOTALL)
    if old_h1_block:
        new_h1_block = old_h1_block.group(1) + '''<!-- Hero Reference Badge -->
            <div class="inline-flex items-center space-x-2 rtl:space-x-reverse px-4 py-1.5 rounded-full hero-badge-glass text-xs font-black uppercase tracking-widest shadow-md mb-2">
              <span class="w-2 h-2 rounded-full bg-purple-500 animate-pulse"></span>
              <span>CASUAL & COUCH CO-OP SANCTUARY • 65" OLED BAYS</span>
            </div>\n\n            ''' + old_h1_block.group(2)
        content = content.replace(old_h1_block.group(0), new_h1_block)

    # 3. Wrap subtitle p in .hero-capsule
    old_p = re.search(r'<p class="text-sm sm:text-base lg:text-base xl:text-lg text-black dark:text-white max-w-2xl mx-auto lg:mx-0 font-bold leading-normal sm:leading-relaxed hero-subtitle-boosted">.*?Forget cramped sofas and small televisions.*?</p>', content, re.DOTALL).group(0)
    new_p = '''<!-- Hero Subtitle Reference Capsule -->
            <div class="hero-capsule rounded-2xl sm:rounded-3xl p-4 sm:p-5 max-w-2xl mx-auto lg:mx-0">
              <p class="text-sm sm:text-base leading-relaxed hero-subtitle-boosted text-center lg:text-left rtl:lg:text-right">
                Forget cramped sofas and small televisions. Immerse yourself in 65" LG OLED couch suites, tactile Fanatec direct drive cockpits, room-scale wireless VR pods, and craft mocktails with your squad.
              </p>
            </div>'''
    content = content.replace(old_p, new_p)

    with open('player-lounge.html', 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content)
    print("player-lounge.html updated successfully!")

# Update centered hero pages
def update_centered_page(filepath, img_src, img_alt):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update hero-bg-container
    old_bg = re.search(r'<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">.*?</div>\s*</div>', content, re.DOTALL).group(0)
    new_bg = f'''<div class="absolute inset-0 z-0 pointer-events-none overflow-hidden hero-bg-container">
        <img src="{img_src}" alt="{img_alt}" class="hero-bg-img w-full h-full object-cover object-center transform scale-105">
        <div class="absolute inset-0 bg-white/20 dark:bg-black/35 pointer-events-none"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-white/30 via-transparent to-white/40 dark:from-black/40 dark:via-transparent dark:to-black/50 pointer-events-none"></div>
      </div>'''
    content = content.replace(old_bg, new_bg)

    # 2. Update subtitle p
    old_p_match = re.search(r'(<!--\s*Subtitle\s*-->\s*)?<p class="[^"]*hero-subtitle-boosted[^"]*">\s*(.*?)\s*</p>', content, re.DOTALL)
    if old_p_match:
        sub_text = old_p_match.group(2).strip()
        new_capsule = f'''<!-- Hero Subtitle Reference Capsule -->
        <div class="hero-capsule rounded-2xl sm:rounded-3xl p-4 sm:p-5 sm:px-6 max-w-2xl sm:max-w-3xl mx-auto">
          <p class="text-sm sm:text-base leading-relaxed hero-subtitle-boosted text-center">
            {sub_text}
          </p>
        </div>'''
        content = content.replace(old_p_match.group(0), new_capsule)

    # 3. Ensure badges have hero-badge-glass class
    content = re.sub(r'class="inline-flex items-center space-x-2 rtl:space-x-reverse px-4 py-1\.5 rounded-full bg-white/95 dark:bg-slate-900/90[^"]*"',
                     'class="inline-flex items-center space-x-2 rtl:space-x-reverse px-4 py-1.5 rounded-full hero-badge-glass text-xs font-black uppercase tracking-widest shadow-md"',
                     content)
    content = re.sub(r'class="inline-flex items-center px-4 py-1\.5 rounded-full bg-white/95 dark:bg-slate-900/90[^"]*"',
                     'class="inline-flex items-center px-4 py-1.5 rounded-full hero-badge-glass text-xs font-black uppercase tracking-widest shadow-md"',
                     content)

    with open(filepath, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content)
    print(f"{filepath} updated successfully!")

update_index()
update_lounge()
update_centered_page('about.html', 'assets/images/hero-bg-about.jpg', 'AuraPlay Hardware Lab')
update_centered_page('games.html', 'assets/images/hero-bg-games.jpg', 'AuraPlay Games Arena')
update_centered_page('pricing.html', 'assets/images/hero-bg-pricing.png', 'AuraPlay Pricing Hardware')
update_centered_page('membership.html', 'assets/images/hero-bg-membership.png', 'AuraPlay VIP Memberships & Lounge Setup')
update_centered_page('book-slot.html', 'assets/images/tour-pc-arena-wide.jpg', 'AuraPlay PC Arena Station Floor')
update_centered_page('blog.html', 'assets/images/hero-bg-blog.png', 'AuraPlay Esports Engineering & Hardware Lab')
update_centered_page('contact.html', 'assets/images/hero-bg-contact.png', 'AuraPlay 24/7 Welcome Desk & Support Center')
