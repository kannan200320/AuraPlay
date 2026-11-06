with open('pricing.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_badges = """        <!-- Quick Guarantee Badges -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 text-xs font-bold text-slate-950 dark:text-white">
          <div class="p-3 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-cyan-500 text-sm">⏱</span>
            <span>Pause Time Any Time</span>
          </div>
          <div class="p-3 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-purple-500 text-sm">🔁</span>
            <span>30-Day Minute Rollover</span>
          </div>
          <div class="p-3 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-emerald-500 text-sm">⚡</span>
            <span>Instant Cloud Station Lock</span>
          </div>
          <div class="p-3 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-amber-500 text-sm">🛡</span>
            <span>Zero Queue For Pass Holders</span>
          </div>
        </div>"""

new_badges = """        <!-- Quick Guarantee Badges -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 text-xs font-bold text-slate-950 dark:text-white">
          <div class="p-3 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-cyan-500 text-sm">⏱</span>
            <span>Pause Time Any Time</span>
          </div>
          <div class="p-3 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-purple-500 text-sm">🔁</span>
            <span>30-Day Minute Rollover</span>
          </div>
          <div class="p-3 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-emerald-500 text-sm">⚡</span>
            <span>Instant Cloud Station Lock</span>
          </div>
          <div class="p-3 rounded-xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md flex items-center justify-center space-x-2 rtl:space-x-reverse">
            <span class="text-amber-500 text-sm">🛡</span>
            <span>Zero Queue For Pass Holders</span>
          </div>
        </div>"""

if old_badges in c:
    c = c.replace(old_badges, new_badges, 1)
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated pricing guarantee badges!")
else:
    print("Warning: old_badges not found in pricing.html")
