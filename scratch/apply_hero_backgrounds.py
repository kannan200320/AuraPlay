import os

def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        c = f.read()
    
    old_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/bg-home1-arena.png" alt="" class="w-full h-full object-cover object-center opacity-30 dark:opacity-40 filter dark:brightness-75 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/95 via-slate-50/90 to-slate-50/80 dark:from-darkslate-deep/95 dark:via-darkslate-deep/90 dark:to-darkslate-deep/80"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>'''

    new_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-home1.png" alt="AuraPlay Arena Setup" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/88 via-slate-50/75 to-slate-50/60 dark:from-darkslate-deep/90 dark:via-darkslate-deep/75 dark:to-darkslate-deep/60 backdrop-blur-[1px]"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>'''

    if old_target in c:
        c = c.replace(old_target, new_target)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated index.html hero background successfully!")
    else:
        print("Warning: old_target not found in index.html")

def update_player_lounge():
    with open('player-lounge.html', 'r', encoding='utf-8') as f:
        c = f.read()

    old_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/bg-home2-lounge.png" alt="" class="w-full h-full object-cover object-center opacity-30 dark:opacity-40 filter dark:brightness-75 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/95 via-slate-50/90 to-slate-50/80 dark:from-darkslate-deep/95 dark:via-darkslate-deep/90 dark:to-darkslate-deep/80"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>'''

    new_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-lounge.png" alt="AuraPlay Lounge Suite" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/88 via-slate-50/75 to-slate-50/60 dark:from-darkslate-deep/90 dark:via-darkslate-deep/75 dark:to-darkslate-deep/60 backdrop-blur-[1px]"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>'''

    if old_target in c:
        c = c.replace(old_target, new_target)
        with open('player-lounge.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated player-lounge.html hero background successfully!")
    else:
        print("Warning: old_target not found in player-lounge.html")

def update_about():
    with open('about.html', 'r', encoding='utf-8') as f:
        c = f.read()

    old_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/bg-about-lab.jpg" alt="" class="w-full h-full object-cover object-center opacity-25 dark:opacity-35 filter dark:brightness-75 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/90 via-slate-50/95 to-slate-50 dark:from-darkslate-deep/90 dark:via-darkslate-deep/95 dark:to-darkslate-deep"></div>
      </div>'''

    new_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-about.jpg" alt="AuraPlay Hardware Lab" class="w-full h-full object-cover object-center opacity-40 dark:opacity-50 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>'''

    if old_target in c:
        c = c.replace(old_target, new_target)
        with open('about.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated about.html hero background successfully!")
    else:
        print("Warning: old_target not found in about.html")

def update_games():
    with open('games.html', 'r', encoding='utf-8') as f:
        c = f.read()

    old_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/bg-games-arena.jpg" alt="" class="w-full h-full object-cover object-center opacity-25 dark:opacity-35 filter dark:brightness-75 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/92 via-slate-50/95 to-slate-50 dark:from-darkslate-deep/90 dark:via-darkslate-deep/95 dark:to-darkslate-deep"></div>
      </div>'''

    new_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-games.jpg" alt="AuraPlay Games Arena" class="w-full h-full object-cover object-center opacity-40 dark:opacity-50 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>'''

    if old_target in c:
        c = c.replace(old_target, new_target)
        with open('games.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated games.html hero background successfully!")
    else:
        print("Warning: old_target not found in games.html")

def update_pricing():
    with open('pricing.html', 'r', encoding='utf-8') as f:
        c = f.read()

    old_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/bg-pricing-showcase.png" alt="" class="w-full h-full object-cover object-center opacity-30 dark:opacity-40 filter dark:brightness-75 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/90 via-slate-50/95 to-slate-50 dark:from-darkslate-deep/90 dark:via-darkslate-deep/95 dark:to-darkslate-deep"></div>
      </div>'''

    new_target = '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-pricing.png" alt="AuraPlay Pricing Hardware" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>'''

    if old_target in c:
        c = c.replace(old_target, new_target)
        with open('pricing.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated pricing.html hero background successfully!")
    else:
        print("Warning: old_target not found in pricing.html")

update_index()
update_player_lounge()
update_about()
update_games()
update_pricing()
