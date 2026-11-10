import sys
sys.stdout.reconfigure(encoding='utf-8')

index = open('index.html', encoding='utf-8').read()

old_tournaments = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm hover:shadow-xl transition-all">
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-full text-xs font-black bg-cyan-100 dark:bg-cyan-950 text-cyan-700 dark:text-cyan-400">THIS SATURDAY • 6 PM</span>
              <span class="text-sm font-extrabold text-amber-500">$1,500 Cash</span>
            </div>
            <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mb-2">Valorant 5v5 Open LAN</h3>
            <p class="text-xs text-black dark:text-slate-400 mb-6 leading-relaxed">Double elimination bracket. 16 team cap. Casted on official AuraPlay Twitch with live spectator screens.</p>
            <div class="flex items-center justify-between pt-4 border-t border-slate-100 dark:border-darkslate-border">
              <span class="text-xs font-bold text-black dark:text-slate-400">12 / 16 Teams Registered</span>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white">Register Squad</a>
            </div>
          </div>

          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm hover:shadow-xl transition-all">
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-full text-xs font-black bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-400">SUNDAY • 4 PM</span>
              <span class="text-sm font-extrabold text-amber-500">$800 Cash</span>
            </div>
            <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mb-2">Tekken 8 Clash of Iron</h3>
            <p class="text-xs text-black dark:text-slate-400 mb-6 leading-relaxed">1v1 double bracket on 65" OLED lounges with official Sanwa arcade fight sticks provided or bring your own.</p>
            <div class="flex items-center justify-between pt-4 border-t border-slate-100 dark:border-darkslate-border">
              <span class="text-xs font-bold text-black dark:text-slate-400">28 / 32 Players</span>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white">Enter Bracket</a>
            </div>
          </div>

          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm hover:shadow-xl transition-all">
            <div class="flex items-center justify-between mb-4">
              <span class="px-3 py-1 rounded-full text-xs font-black bg-pink-100 dark:bg-pink-950 text-pink-700 dark:text-pink-400">WEDNESDAY • 8 PM</span>
              <span class="text-sm font-extrabold text-amber-500">$500 + Gear</span>
            </div>
            <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mb-2">Sim Racing Apex Sprint</h3>
            <p class="text-xs text-black dark:text-slate-400 mb-6 leading-relaxed">Spa-Francorchamps hotlap shootout in the Fanatec DD2 motion bays. Top 3 walk away with prizes.</p>
            <div class="flex items-center justify-between pt-4 border-t border-slate-100 dark:border-darkslate-border">
              <span class="text-xs font-bold text-black dark:text-slate-400">Open Qualifiers</span>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white">Book Lap Time</a>
            </div>
          </div>
        </div>"""

new_tournaments = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 items-stretch">
          <div class="h-full rounded-3xl p-5 sm:p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
            <div class="flex-1 flex flex-col">
              <div class="flex items-center justify-between mb-4 gap-2">
                <span class="px-3 py-1 rounded-full text-[11px] font-black bg-cyan-100 dark:bg-cyan-950 text-cyan-700 dark:text-cyan-400 shrink-0">THIS SATURDAY • 6 PM</span>
                <span class="text-sm font-extrabold text-amber-500 shrink-0">$1,500 Cash</span>
              </div>
              <h3 class="text-xl sm:text-2xl font-black font-display uppercase text-black dark:text-white mb-2 min-h-[3.5rem] flex items-center leading-tight">Valorant 5v5 Open LAN</h3>
              <p class="text-xs text-black dark:text-slate-400 mb-6 leading-relaxed flex-1">Double elimination bracket. 16 team cap. Casted on official AuraPlay Twitch with live spectator screens.</p>
            </div>
            <div class="pt-4 mt-auto border-t border-slate-100 dark:border-darkslate-border flex items-center justify-between gap-2">
              <span class="text-xs font-bold text-black dark:text-slate-400 shrink-0">12 / 16 Teams</span>
              <a href="book-slot.html" class="px-3.5 sm:px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white whitespace-nowrap shrink-0 text-center shadow-md transition-all">Register Squad</a>
            </div>
          </div>

          <div class="h-full rounded-3xl p-5 sm:p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
            <div class="flex-1 flex flex-col">
              <div class="flex items-center justify-between mb-4 gap-2">
                <span class="px-3 py-1 rounded-full text-[11px] font-black bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-400 shrink-0">SUNDAY • 4 PM</span>
                <span class="text-sm font-extrabold text-amber-500 shrink-0">$800 Cash</span>
              </div>
              <h3 class="text-xl sm:text-2xl font-black font-display uppercase text-black dark:text-white mb-2 min-h-[3.5rem] flex items-center leading-tight">Tekken 8 Clash of Iron</h3>
              <p class="text-xs text-black dark:text-slate-400 mb-6 leading-relaxed flex-1">1v1 double bracket on 65" OLED lounges with official Sanwa arcade fight sticks provided or bring your own.</p>
            </div>
            <div class="pt-4 mt-auto border-t border-slate-100 dark:border-darkslate-border flex items-center justify-between gap-2">
              <span class="text-xs font-bold text-black dark:text-slate-400 shrink-0">28 / 32 Players</span>
              <a href="book-slot.html" class="px-3.5 sm:px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white whitespace-nowrap shrink-0 text-center shadow-md transition-all">Enter Bracket</a>
            </div>
          </div>

          <div class="h-full rounded-3xl p-5 sm:p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm hover:shadow-xl transition-all flex flex-col justify-between">
            <div class="flex-1 flex flex-col">
              <div class="flex items-center justify-between mb-4 gap-2">
                <span class="px-3 py-1 rounded-full text-[11px] font-black bg-pink-100 dark:bg-pink-950 text-pink-700 dark:text-pink-400 shrink-0">WEDNESDAY • 8 PM</span>
                <span class="text-sm font-extrabold text-amber-500 shrink-0">$500 + Gear</span>
              </div>
              <h3 class="text-xl sm:text-2xl font-black font-display uppercase text-black dark:text-white mb-2 min-h-[3.5rem] flex items-center leading-tight">Sim Racing Apex Sprint</h3>
              <p class="text-xs text-black dark:text-slate-400 mb-6 leading-relaxed flex-1">Spa-Francorchamps hotlap shootout in the Fanatec DD2 motion bays. Top 3 walk away with prizes.</p>
            </div>
            <div class="pt-4 mt-auto border-t border-slate-100 dark:border-darkslate-border flex items-center justify-between gap-2">
              <span class="text-xs font-bold text-black dark:text-slate-400 shrink-0">Open Qualifiers</span>
              <a href="book-slot.html" class="px-3.5 sm:px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white whitespace-nowrap shrink-0 text-center shadow-md transition-all">Book Lap Time</a>
            </div>
          </div>
        </div>"""

index_norm = index.replace('\r\n', '\n')
old_tournaments_norm = old_tournaments.replace('\r\n', '\n')
new_tournaments_norm = new_tournaments.replace('\r\n', '\n')

assert old_tournaments_norm in index_norm, "old_tournaments not found in index.html!"
index_norm = index_norm.replace(old_tournaments_norm, new_tournaments_norm)

open('index.html', 'w', encoding='utf-8').write(index_norm)
print("SUCCESS: Updated index.html tournaments CTA alignment!")
