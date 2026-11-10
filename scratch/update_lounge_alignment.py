import sys
sys.stdout.reconfigure(encoding='utf-8')

lounge = open('player-lounge.html', encoding='utf-8').read()

old_hits = """        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div class="p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">🍳</div>
            <h4 class="font-bold text-black dark:text-white text-base">Overcooked! All You Can Eat</h4>
            <div class="text-xs text-black dark:text-slate-400 mt-1">4-Player Party Brawler Lounge</div>
          </div>
          <div class="p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">🥊</div>
            <h4 class="font-bold text-black dark:text-white text-base">Super Smash Bros Ultimate</h4>
            <div class="text-xs text-black dark:text-slate-400 mt-1">8-Player Local Brawler</div>
          </div>
          <div class="p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">🏎️</div>
            <h4 class="font-bold text-black dark:text-white text-base">Mario Kart 8 Deluxe</h4>
            <div class="text-xs text-black dark:text-slate-400 mt-1">4-Player Split Screen</div>
          </div>
          <div class="p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">👫</div>
            <h4 class="font-bold text-black dark:text-white text-base">It Takes Two</h4>
            <div class="text-xs text-black dark:text-slate-400 mt-1">2-Player Masterpiece</div>
          </div>
        </div>"""

new_hits = """        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6 items-stretch">
          <div class="h-full p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between items-center shadow-sm hover:border-purple-500/50 transition-all">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">🍳</div>
              <h4 class="font-bold text-black dark:text-white text-sm sm:text-base min-h-[3rem] flex items-center justify-center text-center leading-snug px-1">Overcooked! All You Can Eat</h4>
            </div>
            <div class="w-full text-xs text-black dark:text-slate-400 min-h-[2.5rem] flex items-center justify-center text-center leading-tight mt-2 pt-2 border-t border-slate-100 dark:border-darkslate-border/50">4-Player Party Brawler Lounge</div>
          </div>
          <div class="h-full p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between items-center shadow-sm hover:border-purple-500/50 transition-all">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">🥊</div>
              <h4 class="font-bold text-black dark:text-white text-sm sm:text-base min-h-[3rem] flex items-center justify-center text-center leading-snug px-1">Super Smash Bros Ultimate</h4>
            </div>
            <div class="w-full text-xs text-black dark:text-slate-400 min-h-[2.5rem] flex items-center justify-center text-center leading-tight mt-2 pt-2 border-t border-slate-100 dark:border-darkslate-border/50">8-Player Local Brawler</div>
          </div>
          <div class="h-full p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between items-center shadow-sm hover:border-purple-500/50 transition-all">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">🏎️</div>
              <h4 class="font-bold text-black dark:text-white text-sm sm:text-base min-h-[3rem] flex items-center justify-center text-center leading-snug px-1">Mario Kart 8 Deluxe</h4>
            </div>
            <div class="w-full text-xs text-black dark:text-slate-400 min-h-[2.5rem] flex items-center justify-center text-center leading-tight mt-2 pt-2 border-t border-slate-100 dark:border-darkslate-border/50">4-Player Split Screen</div>
          </div>
          <div class="h-full p-5 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between items-center shadow-sm hover:border-purple-500/50 transition-all">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">👫</div>
              <h4 class="font-bold text-black dark:text-white text-sm sm:text-base min-h-[3rem] flex items-center justify-center text-center leading-snug px-1">It Takes Two</h4>
            </div>
            <div class="w-full text-xs text-black dark:text-slate-400 min-h-[2.5rem] flex items-center justify-center text-center leading-tight mt-2 pt-2 border-t border-slate-100 dark:border-darkslate-border/50">2-Player Masterpiece</div>
          </div>
        </div>"""

lounge_norm = lounge.replace('\r\n', '\n')
old_hits_norm = old_hits.replace('\r\n', '\n')
new_hits_norm = new_hits.replace('\r\n', '\n')

assert old_hits_norm in lounge_norm, "old_hits not found in player-lounge.html"
lounge_norm = lounge_norm.replace(old_hits_norm, new_hits_norm)

open('player-lounge.html', 'w', encoding='utf-8').write(lounge_norm)
print("Successfully updated player-lounge.html couch co-op alignment!")
