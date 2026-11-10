import sys
sys.stdout.reconfigure(encoding='utf-8')

games = open('games.html', encoding='utf-8').read()

# 1. Update Pro Peripherals Vault section
old_peripherals = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border space-y-4">
            <div class="w-12 h-12 rounded-xl bg-cyan-100 dark:bg-cyan-950/50 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-bold text-xl">⌨️</div>
            <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white">Hall Effect Keyboards</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed">
              Equipped with Wooting 60HE+ and DrunkDeer rapid-trigger switches for instantaneous counter-strafing with 0.1mm actuation points.
            </p>
            <span class="inline-block text-xs font-bold text-cyan-500">50 Units in Vault</span>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border space-y-4">
            <div class="w-12 h-12 rounded-xl bg-purple-100 dark:bg-purple-950/50 text-purple-600 dark:text-purple-400 flex items-center justify-center font-bold text-xl">🖱️</div>
            <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white">8000Hz Optical Mice</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed">
              Logitech G Pro X Superlight 2, Razer Viper V3 Pro, and Finalmouse UltralightX with sub-0.125ms tracking response times.
            </p>
            <span class="inline-block text-xs font-bold text-purple-500">75 Units in Vault</span>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border space-y-4">
            <div class="w-12 h-12 rounded-xl bg-pink-100 dark:bg-pink-950/50 text-pink-600 dark:text-pink-400 flex items-center justify-center font-bold text-xl">🎧</div>
            <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white">Spatial Audio Headsets</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed">
              HyperX Cloud III Wireless and SteelSeries Arctis Nova Pro with planar magnetic drivers tuned for pinpoint directional footstep queues.
            </p>
            <span class="inline-block text-xs font-bold text-pink-500">70 Units in Vault</span>
          </div>
        </div>"""

new_peripherals = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between shadow-sm">
            <div class="flex flex-col flex-1">
              <div class="w-12 h-12 rounded-xl bg-cyan-100 dark:bg-cyan-950/50 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-bold text-xl mb-4 shrink-0">⌨️</div>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white min-h-[3.5rem] flex items-center mb-2 leading-tight">Hall Effect Keyboards</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">
                Equipped with Wooting 60HE+ and DrunkDeer rapid-trigger switches for instantaneous counter-strafing with 0.1mm actuation points.
              </p>
            </div>
            <div class="pt-3 mt-4 border-t border-slate-100 dark:border-darkslate-border/50 flex items-center">
              <span class="inline-block text-xs font-bold text-cyan-500">50 Units in Vault</span>
            </div>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between shadow-sm">
            <div class="flex flex-col flex-1">
              <div class="w-12 h-12 rounded-xl bg-purple-100 dark:bg-purple-950/50 text-purple-600 dark:text-purple-400 flex items-center justify-center font-bold text-xl mb-4 shrink-0">🖱️</div>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white min-h-[3.5rem] flex items-center mb-2 leading-tight">8000Hz Optical Mice</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">
                Logitech G Pro X Superlight 2, Razer Viper V3 Pro, and Finalmouse UltralightX with sub-0.125ms tracking response times.
              </p>
            </div>
            <div class="pt-3 mt-4 border-t border-slate-100 dark:border-darkslate-border/50 flex items-center">
              <span class="inline-block text-xs font-bold text-purple-500">75 Units in Vault</span>
            </div>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between shadow-sm">
            <div class="flex flex-col flex-1">
              <div class="w-12 h-12 rounded-xl bg-pink-100 dark:bg-pink-950/50 text-pink-600 dark:text-pink-400 flex items-center justify-center font-bold text-xl mb-4 shrink-0">🎧</div>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white min-h-[3.5rem] flex items-center mb-2 leading-tight">Spatial Audio Headsets</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">
                HyperX Cloud III Wireless and SteelSeries Arctis Nova Pro with planar magnetic drivers tuned for pinpoint directional footstep queues.
              </p>
            </div>
            <div class="pt-3 mt-4 border-t border-slate-100 dark:border-darkslate-border/50 flex items-center">
              <span class="inline-block text-xs font-bold text-pink-500">70 Units in Vault</span>
            </div>
          </div>
        </div>"""

# 2. Update Kernel-Level Anti-Cheat section
old_anti_cheat = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold">🛡️</div>
            <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white">Kernel-Level Anti-Cheat Integrity</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed">Riot Vanguard, Valve Anti-Cheat, and Easy Anti-Cheat are natively certified with secure boot and TPM 2.0 active.</p>
          </div>
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-3">
            <div class="w-10 h-10 rounded-xl bg-cyan-100 dark:bg-cyan-950/60 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-bold">🔒</div>
            <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white">Strict Hardware Sandboxing</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed">No unauthorized third-party background utilities or macros. Only certified driver suites (Synapse, G HUB) are permitted.</p>
          </div>
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-3">
            <div class="w-10 h-10 rounded-xl bg-purple-100 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400 flex items-center justify-center font-bold">⚖️</div>
            <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white">Referees & Match Arbiters</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed">Weekly tournaments feature live staff arbiters ensuring tournament fairness, clean pause protocols, and instant review.</p>
          </div>
        </div>"""

new_anti_cheat = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-stretch">
          <div class="h-full p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center font-bold mb-3 shrink-0">🛡️</div>
            <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center mb-2 leading-tight">Kernel-Level Anti-Cheat Integrity</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">Riot Vanguard, Valve Anti-Cheat, and Easy Anti-Cheat are natively certified with secure boot and TPM 2.0 active.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="w-10 h-10 rounded-xl bg-cyan-100 dark:bg-cyan-950/60 text-cyan-600 dark:text-cyan-400 flex items-center justify-center font-bold mb-3 shrink-0">🔒</div>
            <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center mb-2 leading-tight">Strict Hardware Sandboxing</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">No unauthorized third-party background utilities or macros. Only certified driver suites (Synapse, G HUB) are permitted.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="w-10 h-10 rounded-xl bg-purple-100 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400 flex items-center justify-center font-bold mb-3 shrink-0">⚖️</div>
            <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center mb-2 leading-tight">Referees & Match Arbiters</h3>
            <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">Weekly tournaments feature live staff arbiters ensuring tournament fairness, clean pause protocols, and instant review.</p>
          </div>
        </div>"""

# Normalize
games_norm = games.replace('\r\n', '\n')
old_peripherals_norm = old_peripherals.replace('\r\n', '\n')
new_peripherals_norm = new_peripherals.replace('\r\n', '\n')
old_anti_cheat_norm = old_anti_cheat.replace('\r\n', '\n')
new_anti_cheat_norm = new_anti_cheat.replace('\r\n', '\n')

assert old_peripherals_norm in games_norm, "old_peripherals not found!"
assert old_anti_cheat_norm in games_norm, "old_anti_cheat not found!"

games_norm = games_norm.replace(old_peripherals_norm, new_peripherals_norm)
games_norm = games_norm.replace(old_anti_cheat_norm, new_anti_cheat_norm)

open('games.html', 'w', encoding='utf-8').write(games_norm)
print("Successfully updated games.html alignment for both sections!")
