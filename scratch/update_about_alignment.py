import sys
sys.stdout.reconfigure(encoding='utf-8')

about = open('about.html', encoding='utf-8').read()

# 1. Update The AuraPlay Standards (Image 1)
old_sec1 = """        <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border">
            <div class="text-3xl mb-3">⚡</div>
            <h4 class="text-lg font-bold font-display uppercase text-black dark:text-white">Zero Latency</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed">No packet loss. No frame drops. No excuses. We test every station with hardware probes every morning.</p>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border">
            <div class="text-3xl mb-3">🤝</div>
            <h4 class="text-lg font-bold font-display uppercase text-black dark:text-white">Zero Toxicity</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed">Competitive passion is encouraged; hate and harassment are strictly banned. Everyone plays with dignity.</p>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border">
            <div class="text-3xl mb-3">🧼</div>
            <h4 class="text-lg font-bold font-display uppercase text-black dark:text-white">Hospital-Grade Clean</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed">Keyboards, mice, and desk mats undergo continuous cleaning cycles throughout every shift.</p>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border">
            <div class="text-3xl mb-3">💡</div>
            <h4 class="text-lg font-bold font-display uppercase text-black dark:text-white">Community First</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed">Every member is family. We host beginner workshops, collegiate scrims, and fun community mixers.</p>
          </div>
        </div>"""

new_sec1 = """        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 items-stretch">
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="text-3xl mb-3 shrink-0">⚡</div>
            <h4 class="text-base sm:text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center leading-tight">Zero Latency</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed flex-1">No packet loss. No frame drops. No excuses. We test every station with hardware probes every morning.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="text-3xl mb-3 shrink-0">🤝</div>
            <h4 class="text-base sm:text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center leading-tight">Zero Toxicity</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed flex-1">Competitive passion is encouraged; hate and harassment are strictly banned. Everyone plays with dignity.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="text-3xl mb-3 shrink-0">🧼</div>
            <h4 class="text-base sm:text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center leading-tight">Hospital-Grade Clean</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed flex-1">Keyboards, mice, and desk mats undergo continuous cleaning cycles throughout every shift.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-start shadow-sm">
            <div class="text-3xl mb-3 shrink-0">💡</div>
            <h4 class="text-base sm:text-lg font-bold font-display uppercase text-black dark:text-white min-h-[3.25rem] flex items-center leading-tight">Community First</h4>
            <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed flex-1">Every member is family. We host beginner workshops, collegiate scrims, and fun community mixers.</p>
          </div>
        </div>"""

# 2. Update Fair-Play & Anti-Cheat Standard (Image 2)
old_sec2 = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-3">
                <div class="w-10 h-10 rounded-xl bg-cyan-500/10 text-cyan-500 flex items-center justify-center font-bold text-lg shrink-0">🛡️</div>
                <h4 class="text-sm font-bold font-display uppercase text-black dark:text-white">Hardware Sandbox Isolation</h4>
              </div>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed">Disk images are re-flashed via PXE boot between player sessions, wiping local memory and eliminating background scripts.</p>
            </div>
          </div>
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-3">
                <div class="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-500 flex items-center justify-center font-bold text-lg shrink-0">⚖️</div>
                <h4 class="text-sm font-bold font-display uppercase text-black dark:text-white">Tournament Referee Sanctioning</h4>
              </div>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed">Live match arbiters verify all user peripheral configs, rapid-trigger actuations, and enforce sanctioned rulebooks.</p>
            </div>
          </div>
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div>
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-3">
                <div class="w-10 h-10 rounded-xl bg-pink-500/10 text-pink-500 flex items-center justify-center font-bold text-lg shrink-0">⚡</div>
                <h4 class="text-sm font-bold font-display uppercase text-black dark:text-white">Sub-Millisecond Ping Parity</h4>
              </div>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed">Enterprise fiber switches equalize routing hops so every station competes on identical 4ms local gateway latency.</p>
            </div>
          </div>
        </div>"""

new_sec2 = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full shadow-sm">
            <div class="flex flex-col flex-1">
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-3 min-h-[3.75rem]">
                <div class="w-10 h-10 rounded-xl bg-cyan-500/10 text-cyan-500 flex items-center justify-center font-bold text-lg shrink-0">🛡️</div>
                <h4 class="text-sm font-bold font-display uppercase text-black dark:text-white leading-tight">Hardware Sandbox Isolation</h4>
              </div>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">Disk images are re-flashed via PXE boot between player sessions, wiping local memory and eliminating background scripts.</p>
            </div>
          </div>
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full shadow-sm">
            <div class="flex flex-col flex-1">
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-3 min-h-[3.75rem]">
                <div class="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-500 flex items-center justify-center font-bold text-lg shrink-0">⚖️</div>
                <h4 class="text-sm font-bold font-display uppercase text-black dark:text-white leading-tight">Tournament Referee Sanctioning</h4>
              </div>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">Live match arbiters verify all user peripheral configs, rapid-trigger actuations, and enforce sanctioned rulebooks.</p>
            </div>
          </div>
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full shadow-sm">
            <div class="flex flex-col flex-1">
              <div class="flex items-center space-x-3 rtl:space-x-reverse mb-3 min-h-[3.75rem]">
                <div class="w-10 h-10 rounded-xl bg-pink-500/10 text-pink-500 flex items-center justify-center font-bold text-lg shrink-0">⚡</div>
                <h4 class="text-sm font-bold font-display uppercase text-black dark:text-white leading-tight">Sub-Millisecond Ping Parity</h4>
              </div>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">Enterprise fiber switches equalize routing hops so every station competes on identical 4ms local gateway latency.</p>
            </div>
          </div>
        </div>"""

# 3. Update Hall of Champions (Image 3)
old_sec3 = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">🥇</div>
            <h4 class="font-bold font-display uppercase text-black dark:text-white">Team Apex Shadows</h4>
            <div class="text-xs text-amber-500 font-bold">2025 Regional LAN Champions</div>
            <p class="text-xs text-black dark:text-slate-400 mt-2">Trained 400+ hours inside AuraPlay Bootcamp Suite 01 before qualifying for Nationals.</p>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">🏎️</div>
            <h4 class="font-bold font-display uppercase text-black dark:text-white">Liam 'Apex' Sterling</h4>
            <div class="text-xs text-pink-500 font-bold">Sim Hotlap World Record #4</div>
            <p class="text-xs text-black dark:text-slate-400 mt-2">Achieved a 1:41.22 lap at Spa-Francorchamps on our Fanatec DD2 motion rig.</p>
          </div>
          <div class="p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center">
            <div class="text-3xl mb-2">🥊</div>
            <h4 class="font-bold font-display uppercase text-black dark:text-white">Kenji Sato</h4>
            <div class="text-xs text-cyan-500 font-bold">Tekken 8 Summer Brawler Winner</div>
            <p class="text-xs text-black dark:text-slate-400 mt-2">Undefeated 18-match streak in our Sunday Fighter lounge competitions.</p>
          </div>
        </div>"""

new_sec3 = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between shadow-sm">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">🥇</div>
              <h4 class="font-bold font-display uppercase text-black dark:text-white min-h-[2rem] flex items-center justify-center leading-snug">Team Apex Shadows</h4>
              <div class="text-xs text-amber-500 font-bold min-h-[2.5rem] flex items-center justify-center leading-tight mt-1">2025 Regional LAN Champions</div>
            </div>
            <p class="text-xs text-black dark:text-slate-400 mt-3 pt-3 border-t border-slate-100 dark:border-darkslate-border/50 leading-relaxed flex-1 flex items-center justify-center">Trained 400+ hours inside AuraPlay Bootcamp Suite 01 before qualifying for Nationals.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between shadow-sm">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">🏎️</div>
              <h4 class="font-bold font-display uppercase text-black dark:text-white min-h-[2rem] flex items-center justify-center leading-snug">Liam 'Apex' Sterling</h4>
              <div class="text-xs text-pink-500 font-bold min-h-[2.5rem] flex items-center justify-center leading-tight mt-1">Sim Hotlap World Record #4</div>
            </div>
            <p class="text-xs text-black dark:text-slate-400 mt-3 pt-3 border-t border-slate-100 dark:border-darkslate-border/50 leading-relaxed flex-1 flex items-center justify-center">Achieved a 1:41.22 lap at Spa-Francorchamps on our Fanatec DD2 motion rig.</p>
          </div>
          <div class="h-full p-6 rounded-2xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border text-center flex flex-col justify-between shadow-sm">
            <div class="w-full flex flex-col items-center">
              <div class="text-3xl mb-2 shrink-0">🥊</div>
              <h4 class="font-bold font-display uppercase text-black dark:text-white min-h-[2rem] flex items-center justify-center leading-snug">Kenji Sato</h4>
              <div class="text-xs text-cyan-500 font-bold min-h-[2.5rem] flex items-center justify-center leading-tight mt-1">Tekken 8 Summer Brawler Winner</div>
            </div>
            <p class="text-xs text-black dark:text-slate-400 mt-3 pt-3 border-t border-slate-100 dark:border-darkslate-border/50 leading-relaxed flex-1 flex items-center justify-center">Undefeated 18-match streak in our Sunday Fighter lounge competitions.</p>
          </div>
        </div>"""

# 4. Update Careers / Open Positions (Image 4)
old_sec4 = """        <!-- 3 Role Opportunity Badges -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10 items-stretch">
          
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <div class="mb-3">
                <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 border border-cyan-500/20">
                  FULL TIME • HARDWARE
                </span>
              </div>
              <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white mb-2">Rig & System Engineer</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed min-h-[48px]">
                Maintain custom water loops, diagnose GPU overclocking stability, and manage 10Gbps PXE network image deployment.
              </p>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-200 dark:border-darkslate-border/80">
              <div class="text-xs font-bold text-cyan-500 flex items-center justify-between">
                <span>Competitive Pay</span>
                <span class="text-slate-400 dark:text-slate-600 font-normal">•</span>
                <span>Unlimited Playtime</span>
              </div>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <div class="mb-3">
                <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-purple-500/10 text-purple-600 dark:text-purple-400 border border-purple-500/20">
                  PART TIME • EVENTS
                </span>
              </div>
              <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white mb-2">Tournament Arbiter</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed min-h-[48px]">
                Manage live Challengers brackets, resolve in-game disputes, arbitrate LAN matches, and stream match scores on Twitch.
              </p>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-200 dark:border-darkslate-border/80">
              <div class="text-xs font-bold text-purple-500 flex items-center justify-between">
                <span>Weekend Shifts</span>
                <span class="text-slate-400 dark:text-slate-600 font-normal">•</span>
                <span>Gear Allowance</span>
              </div>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <div class="mb-3">
                <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-pink-500/10 text-pink-600 dark:text-pink-400 border border-pink-500/20">
                  FULL / PART TIME
                </span>
              </div>
              <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white mb-2">Lounge Concierge</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed min-h-[48px]">
                Welcome players, manage station check-ins, guide gamers on hardware tuning, and ensure pristine station cleanliness.
              </p>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-200 dark:border-darkslate-border/80">
              <div class="text-xs font-bold text-pink-500 flex items-center justify-between">
                <span>Flexible Hours</span>
                <span class="text-slate-400 dark:text-slate-600 font-normal">•</span>
                <span>Free Shift Snacks</span>
              </div>
            </div>
          </div>
        </div>"""

new_sec4 = """        <!-- 3 Role Opportunity Badges -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10 items-stretch">
          
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full shadow-sm">
            <div class="flex-1 flex flex-col">
              <div class="mb-3 shrink-0">
                <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 border border-cyan-500/20">
                  FULL TIME • HARDWARE
                </span>
              </div>
              <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white mb-2 min-h-[3.25rem] flex items-center leading-tight">Rig & System Engineer</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">
                Maintain custom water loops, diagnose GPU overclocking stability, and manage 10Gbps PXE network image deployment.
              </p>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-200 dark:border-darkslate-border/80">
              <div class="text-xs font-bold text-cyan-500 flex items-center justify-between">
                <span>Competitive Pay</span>
                <span class="text-slate-400 dark:text-slate-600 font-normal">•</span>
                <span>Unlimited Playtime</span>
              </div>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full shadow-sm">
            <div class="flex-1 flex flex-col">
              <div class="mb-3 shrink-0">
                <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-purple-500/10 text-purple-600 dark:text-purple-400 border border-purple-500/20">
                  PART TIME • EVENTS
                </span>
              </div>
              <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white mb-2 min-h-[3.25rem] flex items-center leading-tight">Tournament Arbiter</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">
                Manage live Challengers brackets, resolve in-game disputes, arbitrate LAN matches, and stream match scores on Twitch.
              </p>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-200 dark:border-darkslate-border/80">
              <div class="text-xs font-bold text-purple-500 flex items-center justify-between">
                <span>Weekend Shifts</span>
                <span class="text-slate-400 dark:text-slate-600 font-normal">•</span>
                <span>Gear Allowance</span>
              </div>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full shadow-sm">
            <div class="flex-1 flex flex-col">
              <div class="mb-3 shrink-0">
                <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-pink-500/10 text-pink-600 dark:text-pink-400 border border-pink-500/20">
                  FULL / PART TIME
                </span>
              </div>
              <h3 class="text-lg font-bold font-display uppercase text-black dark:text-white mb-2 min-h-[3.25rem] flex items-center leading-tight">Lounge Concierge</h3>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed flex-1">
                Welcome players, manage station check-ins, guide gamers on hardware tuning, and ensure pristine station cleanliness.
              </p>
            </div>
            <div class="pt-4 mt-4 border-t border-slate-200 dark:border-darkslate-border/80">
              <div class="text-xs font-bold text-pink-500 flex items-center justify-between">
                <span>Flexible Hours</span>
                <span class="text-slate-400 dark:text-slate-600 font-normal">•</span>
                <span>Free Shift Snacks</span>
              </div>
            </div>
          </div>
        </div>"""

about_norm = about.replace('\r\n', '\n')
old_sec1_norm = old_sec1.replace('\r\n', '\n')
new_sec1_norm = new_sec1.replace('\r\n', '\n')
old_sec2_norm = old_sec2.replace('\r\n', '\n')
new_sec2_norm = new_sec2.replace('\r\n', '\n')
old_sec3_norm = old_sec3.replace('\r\n', '\n')
new_sec3_norm = new_sec3.replace('\r\n', '\n')
old_sec4_norm = old_sec4.replace('\r\n', '\n')
new_sec4_norm = new_sec4.replace('\r\n', '\n')

assert old_sec1_norm in about_norm, "old_sec1 not found!"
assert old_sec2_norm in about_norm, "old_sec2 not found!"
assert old_sec3_norm in about_norm, "old_sec3 not found!"
assert old_sec4_norm in about_norm, "old_sec4 not found!"

about_norm = about_norm.replace(old_sec1_norm, new_sec1_norm)
about_norm = about_norm.replace(old_sec2_norm, new_sec2_norm)
about_norm = about_norm.replace(old_sec3_norm, new_sec3_norm)
about_norm = about_norm.replace(old_sec4_norm, new_sec4_norm)

open('about.html', 'w', encoding='utf-8').write(about_norm)
print("Successfully updated all 4 sections in about.html!")
