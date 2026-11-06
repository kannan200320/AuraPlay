with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_chips_index = """            <!-- Hardware Spec Chips -->
            <div class="flex flex-wrap gap-2.5 justify-center lg:justify-start rtl:lg:justify-end pt-2">
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-cyan-500">⚡</span>
                <span>NVIDIA RTX 4090 24GB</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-purple-500">🖥️</span>
                <span>360Hz OLED Displays</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-emerald-500">🌐</span>
                <span>Dual 10Gbps Dedicated Fiber</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-pink-500">💺</span>
                <span>Herman Miller Embody Chairs</span>
              </span>
            </div>"""

new_chips_index = """            <!-- Hardware Spec Chips -->
            <div class="flex flex-wrap gap-2.5 justify-center lg:justify-start rtl:lg:justify-end pt-2">
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-cyan-500">⚡</span>
                <span>NVIDIA RTX 4090 24GB</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-purple-500">🖥️</span>
                <span>360Hz OLED Displays</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-emerald-500">🌐</span>
                <span>Dual 10Gbps Dedicated Fiber</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-pink-500">💺</span>
                <span>Herman Miller Embody Chairs</span>
              </span>
            </div>"""

if old_chips_index in c:
    c = c.replace(old_chips_index, new_chips_index, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated index.html spec chips!")
else:
    print("Warning: old_chips_index not found in index.html")

with open('player-lounge.html', 'r', encoding='utf-8') as f:
    pl = f.read()

old_chips_lounge = """            <div class="flex flex-wrap gap-2.5 justify-center lg:justify-start rtl:lg:justify-end pt-2">
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-purple-500">🎮</span>
                <span>Custom PS5 Pro Pods</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-pink-500">🏎️</span>
                <span>Fanatec Direct-Drive Sims</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-amber-500">🥽</span>
                <span>Wireless VR Arenas</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-slate-200 shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-cyan-500">🍸</span>
                <span>Artisan Gamer Refreshments</span>
              </span>
            </div>"""

new_chips_lounge = """            <div class="flex flex-wrap gap-2.5 justify-center lg:justify-start rtl:lg:justify-end pt-2">
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-purple-500">🎮</span>
                <span>Custom PS5 Pro Pods</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-pink-500">🏎️</span>
                <span>Fanatec Direct-Drive Sims</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-amber-500">🥽</span>
                <span>Wireless VR Arenas</span>
              </span>
              <span class="px-3 py-1.5 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-slate-950 dark:text-white shadow-md flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-cyan-500">🍸</span>
                <span>Artisan Gamer Refreshments</span>
              </span>
            </div>"""

if old_chips_lounge in pl:
    pl = pl.replace(old_chips_lounge, new_chips_lounge, 1)
    with open('player-lounge.html', 'w', encoding='utf-8') as f:
        f.write(pl)
    print("Updated player-lounge.html spec chips!")
else:
    print("Warning: old_chips_lounge not found in player-lounge.html")
