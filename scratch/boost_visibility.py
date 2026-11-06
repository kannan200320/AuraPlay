import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        c = f.read()
    
    success = True
    for old, new in replacements:
        if old in c:
            c = c.replace(old, new, 1)
        else:
            print(f"FAILED to find match in {filename}:\n{old[:100]}...")
            success = False
            
    if success:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Successfully updated {filename}!")
    return success

# 1. index.html
update_file('index.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-home1.png" alt="AuraPlay Arena Setup" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/88 via-slate-50/75 to-slate-50/60 dark:from-darkslate-deep/90 dark:via-darkslate-deep/75 dark:to-darkslate-deep/60 backdrop-blur-[1px]"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-home1.png" alt="AuraPlay Arena Setup" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/75 via-slate-50/45 to-transparent dark:from-darkslate-deep/85 dark:via-darkslate-deep/50 dark:to-transparent"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>'''
    ),
    (
        '<div class="inline-flex items-center space-x-2.5 rtl:space-x-reverse px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/60 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs sm:text-sm font-bold">',
        '<div class="inline-flex items-center space-x-2.5 rtl:space-x-reverse px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs sm:text-sm font-extrabold shadow-sm">'
    ),
    (
        '''            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none">
              Play Hard. <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 via-purple-500 to-pink-500">
                Win Big. Repeat.
              </span>
            </h1>

            <p class="text-base sm:text-xl text-black dark:text-slate-300 max-w-2xl mx-auto lg:mx-0 font-normal leading-relaxed">''',
        '''            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-slate-950 dark:text-white uppercase leading-none hero-headline">
              Play Hard. <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-purple-600 to-pink-600 dark:from-cyan-400 dark:via-purple-400 dark:to-pink-400">
                Win Big. Repeat.
              </span>
            </h1>

            <p class="text-base sm:text-xl text-slate-950 dark:text-slate-100 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed hero-subtitle">'''
    )
])

# 2. player-lounge.html
update_file('player-lounge.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-lounge.png" alt="AuraPlay Lounge Suite" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/88 via-slate-50/75 to-slate-50/60 dark:from-darkslate-deep/90 dark:via-darkslate-deep/75 dark:to-darkslate-deep/60 backdrop-blur-[1px]"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-lounge.png" alt="AuraPlay Lounge Suite" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/75 via-slate-50/45 to-transparent dark:from-darkslate-deep/85 dark:via-darkslate-deep/50 dark:to-transparent"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>'''
    ),
    (
        '<div class="inline-flex items-center space-x-2.5 rtl:space-x-reverse px-4 py-1.5 rounded-full bg-purple-100 dark:bg-purple-950/60 border border-purple-300 dark:border-purple-800 text-purple-800 dark:text-purple-300 text-xs sm:text-sm font-bold">',
        '<div class="inline-flex items-center space-x-2.5 rtl:space-x-reverse px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-purple-400 dark:border-purple-500/50 text-purple-950 dark:text-purple-200 text-xs sm:text-sm font-extrabold shadow-sm">'
    ),
    (
        '''            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none">
              Your Living Room, <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-pink-500 to-amber-500">
                Radically Upgraded.
              </span>
            </h1>

            <p class="text-base sm:text-xl text-black dark:text-slate-300 max-w-2xl mx-auto lg:mx-0 font-normal leading-relaxed">''',
        '''            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-slate-950 dark:text-white uppercase leading-none hero-headline">
              Your Living Room, <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 via-pink-600 to-amber-600 dark:from-purple-400 dark:via-pink-400 dark:to-amber-400">
                Radically Upgraded.
              </span>
            </h1>

            <p class="text-base sm:text-xl text-slate-950 dark:text-slate-100 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed hero-subtitle">'''
    )
])

# 3. about.html
update_file('about.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-about.jpg" alt="AuraPlay Hardware Lab" class="w-full h-full object-cover object-center opacity-40 dark:opacity-50 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-about.jpg" alt="AuraPlay Hardware Lab" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<div class="inline-flex items-center space-x-2 rtl:space-x-reverse px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/80 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs font-bold uppercase tracking-widest shadow-sm">',
        '<div class="inline-flex items-center space-x-2 rtl:space-x-reverse px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          Born From Passion. <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 via-purple-500 to-pink-500">
            Engineered For Champions.
          </span>
        </h1>

        <!-- Subtitle -->
        <p class="text-base sm:text-lg text-black dark:text-slate-300 leading-relaxed max-w-2xl mx-auto font-normal">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Born From Passion. <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-purple-600 to-pink-600 dark:from-cyan-400 dark:via-purple-400 dark:to-pink-400">
            Engineered For Champions.
          </span>
        </h1>

        <!-- Subtitle -->
        <p class="text-base sm:text-lg text-slate-950 dark:text-slate-100 leading-relaxed max-w-2xl mx-auto font-medium hero-subtitle">'''
    )
])

# 4. games.html
update_file('games.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-games.jpg" alt="AuraPlay Games Arena" class="w-full h-full object-cover object-center opacity-40 dark:opacity-50 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-games.jpg" alt="AuraPlay Games Arena" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/60 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs font-bold uppercase tracking-widest">',
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          Zero Downloads. <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500">Instant Launch.</span> Maximum FPS.
        </h1>
        <p class="text-black dark:text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Zero Downloads. <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Instant Launch.</span> Maximum FPS.
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">'''
    )
])

# 5. pricing.html
update_file('pricing.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-pricing.png" alt="AuraPlay Pricing Hardware" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-pricing.png" alt="AuraPlay Pricing Hardware" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/60 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs font-bold uppercase tracking-widest">',
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          Pay For What You Play. <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 to-purple-500">Zero Hidden Fees.</span>
        </h1>
        <p class="text-black dark:text-slate-300 text-base sm:text-lg max-w-2xl mx-auto">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Pay For What You Play. <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 to-purple-600 dark:from-cyan-400 dark:to-purple-400">Zero Hidden Fees.</span>
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto font-medium hero-subtitle">'''
    ),
    (
        '<div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 text-xs font-bold text-black dark:text-slate-300">',
        '<div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 text-xs font-bold text-slate-950 dark:text-white">'
    ),
    (
        '<div class="p-3 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center justify-center space-x-2 rtl:space-x-reverse">',
        '<div class="p-3 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md flex items-center justify-center space-x-2 rtl:space-x-reverse">'
    )
])

# 6. membership.html
update_file('membership.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-membership.png" alt="AuraPlay VIP Memberships & Lounge Setup" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-membership.png" alt="AuraPlay VIP Memberships & Lounge Setup" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-purple-100 dark:bg-purple-950/60 border border-purple-300 dark:border-purple-800 text-purple-800 dark:text-purple-300 text-xs font-bold uppercase tracking-widest">',
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-purple-400 dark:border-purple-500/50 text-purple-950 dark:text-purple-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          Level Up Your Play With <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-500 via-indigo-500 to-cyan-500">Aura Memberships</span>
        </h1>
        <p class="text-black dark:text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Level Up Your Play With <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 via-indigo-600 to-cyan-600 dark:from-purple-400 dark:via-indigo-400 dark:to-cyan-400">Aura Memberships</span>
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">'''
    ),
    (
        '<div class="flex flex-wrap items-center justify-center gap-3 pt-2 text-xs font-bold text-black dark:text-slate-300">',
        '<div class="flex flex-wrap items-center justify-center gap-3 pt-2 text-xs font-bold text-slate-950 dark:text-white">'
    ),
    (
        'class="px-3.5 py-1.5 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm"',
        'class="px-3.5 py-1.5 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md"'
    )
])

# 7. book-slot.html
update_file('book-slot.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/tour-pc-arena-wide.jpg" alt="AuraPlay PC Arena Station Floor" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/tour-pc-arena-wide.jpg" alt="AuraPlay PC Arena Station Floor" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/60 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs font-bold uppercase tracking-widest">',
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          Reserve Your <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500">Battle Station</span> In Advance
        </h1>
        <p class="text-black dark:text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Reserve Your <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Battle Station</span> In Advance
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">'''
    ),
    (
        '<div class="flex items-center justify-center space-x-6 rtl:space-x-reverse pt-2 text-xs sm:text-sm font-semibold">',
        '<div class="inline-flex items-center justify-center space-x-6 rtl:space-x-reverse px-5 py-2.5 rounded-2xl bg-white/90 dark:bg-darkslate-card/90 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md text-xs sm:text-sm font-bold">'
    )
])

# 8. blog.html
update_file('blog.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-blog.png" alt="AuraPlay Esports Engineering & Hardware Lab" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-blog.png" alt="AuraPlay Esports Engineering & Hardware Lab" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/60 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs font-bold uppercase tracking-widest">',
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          The AuraPlay <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500">Esports Engineering</span> Journal
        </h1>
        <p class="text-black dark:text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          The AuraPlay <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Esports Engineering</span> Journal
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">'''
    )
])

# 9. contact.html
update_file('contact.html', [
    (
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-contact.png" alt="AuraPlay 24/7 Welcome Desk & Support Center" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>''',
        '''      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-contact.png" alt="AuraPlay 24/7 Welcome Desk & Support Center" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/60 via-slate-50/35 to-slate-50 dark:from-darkslate-deep/70 dark:via-darkslate-deep/45 dark:to-darkslate-deep backdrop-blur-[0.5px]"></div>
      </div>'''
    ),
    (
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-cyan-100 dark:bg-cyan-950/60 border border-cyan-300 dark:border-cyan-800 text-cyan-800 dark:text-cyan-300 text-xs font-bold uppercase tracking-widest">',
        '<span class="inline-flex items-center px-4 py-1.5 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-cyan-400 dark:border-cyan-500/50 text-cyan-950 dark:text-cyan-200 text-xs font-extrabold uppercase tracking-widest shadow-sm">'
    ),
    (
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight">
          We Are Always Ready For <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500">Your Next Match</span>
        </h1>
        <p class="text-black dark:text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed">''',
        '''        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          We Are Always Ready For <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Your Next Match</span>
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">'''
    ),
    (
        '<div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 text-xs font-bold max-w-3xl mx-auto">',
        '<div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 text-xs font-bold max-w-3xl mx-auto">'
    ),
    (
        '<div class="p-4 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm">',
        '<div class="p-4 rounded-2xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md">'
    )
])

print("\nAll files processed!")
