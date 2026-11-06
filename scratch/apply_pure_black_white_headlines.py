import re

# 1. index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace H1 and P
old_h1_index = """            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-slate-950 dark:text-white uppercase leading-none hero-headline">
              Play Hard. <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-purple-600 to-pink-600 dark:from-cyan-400 dark:via-purple-400 dark:to-pink-400">
                Win Big. Repeat.
              </span>
            </h1>

            <p class="text-base sm:text-xl text-slate-950 dark:text-slate-100 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed hero-subtitle">"""

new_h1_index = """            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline">
              Play Hard. <br>
              <span>Win Big. Repeat.</span>
            </h1>

            <p class="text-base sm:text-xl text-black dark:text-white max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed hero-subtitle">"""

if old_h1_index in c:
    c = c.replace(old_h1_index, new_h1_index, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated index.html H1 & P!")
else:
    print("Warning: old_h1_index not found in index.html")

# 2. player-lounge.html
with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_lounge = """            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-slate-950 dark:text-white uppercase leading-none hero-headline">
              Your Living Room, <br>
              <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 via-pink-600 to-amber-600 dark:from-purple-400 dark:via-pink-400 dark:to-amber-400">
                Radically Upgraded.
              </span>
            </h1>

            <p class="text-base sm:text-xl text-slate-950 dark:text-slate-100 max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed hero-subtitle">"""

new_h1_lounge = """            <h1 class="text-4xl sm:text-6xl xl:text-7xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline">
              Your Living Room, <br>
              <span>Radically Upgraded.</span>
            </h1>

            <p class="text-base sm:text-xl text-black dark:text-white max-w-2xl mx-auto lg:mx-0 font-medium leading-relaxed hero-subtitle">"""

if old_h1_lounge in c:
    c = c.replace(old_h1_lounge, new_h1_lounge, 1)
    with open('player-lounge.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated player-lounge.html H1 & P!")
else:
    print("Warning: old_h1_lounge not found in player-lounge.html")

# 3. about.html
with open('about.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_about = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Born From Passion. <br>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-purple-600 to-pink-600 dark:from-cyan-400 dark:via-purple-400 dark:to-pink-400">
            Engineered For Champions.
          </span>
        </h1>

        <!-- Subtitle -->
        <p class="text-base sm:text-lg text-slate-950 dark:text-slate-100 leading-relaxed max-w-2xl mx-auto font-medium hero-subtitle">"""

new_h1_about = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          Born From Passion. <br>
          <span>Engineered For Champions.</span>
        </h1>

        <!-- Subtitle -->
        <p class="text-base sm:text-lg text-black dark:text-white leading-relaxed max-w-2xl mx-auto font-medium hero-subtitle">"""

if old_h1_about in c:
    c = c.replace(old_h1_about, new_h1_about, 1)
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated about.html H1 & P!")
else:
    print("Warning: old_h1_about not found in about.html")

# 4. games.html
with open('games.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_games = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Zero Downloads. <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Instant Launch.</span> Maximum FPS.
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

new_h1_games = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          Zero Downloads. <span>Instant Launch.</span> Maximum FPS.
        </h1>
        <p class="text-black dark:text-white text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

if old_h1_games in c:
    c = c.replace(old_h1_games, new_h1_games, 1)
    with open('games.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated games.html H1 & P!")
else:
    print("Warning: old_h1_games not found in games.html")

# 5. pricing.html
with open('pricing.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_pricing = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Pay For What You Play. <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 to-purple-600 dark:from-cyan-400 dark:to-purple-400">Zero Hidden Fees.</span>
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto font-medium hero-subtitle">"""

new_h1_pricing = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          Pay For What You Play. <span>Zero Hidden Fees.</span>
        </h1>
        <p class="text-black dark:text-white text-base sm:text-lg max-w-2xl mx-auto font-medium hero-subtitle">"""

if old_h1_pricing in c:
    c = c.replace(old_h1_pricing, new_h1_pricing, 1)
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated pricing.html H1 & P!")
else:
    print("Warning: old_h1_pricing not found in pricing.html")

# 6. membership.html
with open('membership.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_membership = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Level Up Your Play With <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 via-indigo-600 to-cyan-600 dark:from-purple-400 dark:via-indigo-400 dark:to-cyan-400">Aura Memberships</span>
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

new_h1_membership = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          Level Up Your Play With <span>Aura Memberships</span>
        </h1>
        <p class="text-black dark:text-white text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

if old_h1_membership in c:
    c = c.replace(old_h1_membership, new_h1_membership, 1)
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated membership.html H1 & P!")
else:
    print("Warning: old_h1_membership not found in membership.html")

# 7. book-slot.html
with open('book-slot.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_book = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          Reserve Your <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Battle Station</span> In Advance
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

new_h1_book = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          Reserve Your <span>Battle Station</span> In Advance
        </h1>
        <p class="text-black dark:text-white text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

if old_h1_book in c:
    c = c.replace(old_h1_book, new_h1_book, 1)
    with open('book-slot.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated book-slot.html H1 & P!")
else:
    print("Warning: old_h1_book not found in book-slot.html")

# 8. blog.html
with open('blog.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_blog = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          The AuraPlay <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Esports Engineering</span> Journal
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

new_h1_blog = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          The AuraPlay <span>Esports Engineering</span> Journal
        </h1>
        <p class="text-black dark:text-white text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

if old_h1_blog in c:
    c = c.replace(old_h1_blog, new_h1_blog, 1)
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated blog.html H1 & P!")
else:
    print("Warning: old_h1_blog not found in blog.html")

# 9. contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_h1_contact = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-slate-950 dark:text-white leading-tight hero-headline">
          We Are Always Ready For <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-600 via-indigo-600 to-purple-600 dark:from-cyan-400 dark:via-indigo-400 dark:to-purple-400">Your Next Match</span>
        </h1>
        <p class="text-slate-950 dark:text-slate-100 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

new_h1_contact = """        <h1 class="text-4xl sm:text-6xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-tight hero-headline">
          We Are Always Ready For <span>Your Next Match</span>
        </h1>
        <p class="text-black dark:text-white text-base sm:text-lg max-w-2xl mx-auto leading-relaxed font-medium hero-subtitle">"""

if old_h1_contact in c:
    c = c.replace(old_h1_contact, new_h1_contact, 1)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated contact.html H1 & P!")
else:
    print("Warning: old_h1_contact not found in contact.html")
