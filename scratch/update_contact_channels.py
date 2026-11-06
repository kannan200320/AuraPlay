with open('contact.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_channels = """        <!-- Quick Contact Channels -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 text-xs font-bold max-w-3xl mx-auto">
          <div class="p-4 rounded-2xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md">
            <div class="text-cyan-500 text-lg mb-1">📞</div>
            <div class="text-black dark:text-white">+1 (800) 555-AURA</div>
            <div class="text-[11px] text-black dark:text-slate-400">24/7 Direct Hotline</div>
          </div>
          <div class="p-4 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm">
            <div class="text-purple-500 text-lg mb-1">💬</div>
            <div class="text-black dark:text-white">discord.gg/auraplay</div>
            <div class="text-[11px] text-black dark:text-slate-400">&lt; 2 Min Staff Response</div>
          </div>
          <div class="p-4 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm">
            <div class="text-emerald-500 text-lg mb-1">📍</div>
            <div class="text-black dark:text-white">42 Blossom Valley Way</div>
            <div class="text-[11px] text-black dark:text-slate-400">Sunnyvale, CA 94087</div>
          </div>
        </div>"""

new_channels = """        <!-- Quick Contact Channels -->
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 text-xs font-bold max-w-3xl mx-auto">
          <div class="p-4 rounded-2xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md">
            <div class="text-cyan-500 text-lg mb-1">📞</div>
            <div class="text-slate-950 dark:text-white font-extrabold text-sm">+1 (800) 555-AURA</div>
            <div class="text-[11px] text-slate-700 dark:text-slate-300 font-semibold">24/7 Direct Hotline</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md">
            <div class="text-purple-500 text-lg mb-1">💬</div>
            <div class="text-slate-950 dark:text-white font-extrabold text-sm">discord.gg/auraplay</div>
            <div class="text-[11px] text-slate-700 dark:text-slate-300 font-semibold">&lt; 2 Min Staff Response</div>
          </div>
          <div class="p-4 rounded-2xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 shadow-md">
            <div class="text-emerald-500 text-lg mb-1">📍</div>
            <div class="text-slate-950 dark:text-white font-extrabold text-sm">42 Blossom Valley Way</div>
            <div class="text-[11px] text-slate-700 dark:text-slate-300 font-semibold">Sunnyvale, CA 94087</div>
          </div>
        </div>"""

if old_channels in c:
    c = c.replace(old_channels, new_channels, 1)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated contact channels successfully!')
else:
    print('Warning: old_channels not found in contact.html')
