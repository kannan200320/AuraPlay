# -*- coding: utf-8 -*-
import re

# ==========================================
# 1. FIX index.html (Hardware Tiers Alignment)
# ==========================================
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Replace the hardware tiers section in index.html
old_tiers_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">.*?<!-- Rig Tier 1 -->.*?<!-- Rig Tier 4 -->.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_tiers_html = '''<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 items-stretch">
          
          <!-- Rig Tier 1 -->
          <div class="rounded-2xl p-6 bg-slate-50 dark:bg-darkslate-deep border-2 border-cyan-500 shadow-lg relative flex flex-col justify-between h-full">
            <div class="absolute -top-3.5 right-4 px-3 py-1 bg-cyan-500 text-black text-xs font-black uppercase tracking-wider rounded-full">
              Flagship
            </div>
            <div class="flex-1 flex flex-col">
              <div class="text-xs font-bold uppercase tracking-wider text-cyan-600 dark:text-cyan-400">Tier 1: Alpha Beast</div>
              <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mt-1 mb-4">RTX 4090 Arena</h3>
              <ul class="space-y-3 text-xs sm:text-sm text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Intel Core i9-14900KS 6.2GHz</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">ASUS ROG Strix RTX 4090 24GB</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">64GB DDR5 7200MHz RAM</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Alienware 27" 360Hz QD-OLED</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Wooting 60HE Hall-Effect Keyboard</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Logitech G Pro X Superlight 2</span></li>
              </ul>
            </div>
            <div class="mt-8 pt-4 border-t border-slate-200 dark:border-darkslate-border flex items-center justify-between">
              <div>
                <span class="text-2xl font-black text-black dark:text-white">$7.50</span>
                <span class="text-xs text-black dark:text-slate-400">/ hour</span>
              </div>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-cyan-600 hover:bg-cyan-500">Book Alpha</a>
            </div>
          </div>

          <!-- Rig Tier 2 -->
          <div class="rounded-2xl p-6 bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border shadow-sm flex flex-col justify-between h-full hover:border-purple-500 transition-colors">
            <div class="flex-1 flex flex-col">
              <div class="text-xs font-bold uppercase tracking-wider text-purple-600 dark:text-purple-400">Tier 2: Esports Pro</div>
              <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mt-1 mb-4">RTX 4080 Super</h3>
              <ul class="space-y-3 text-xs sm:text-sm text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-purple-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">AMD Ryzen 7 7800X3D V-Cache</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-purple-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">GeForce RTX 4080 Super 16GB</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-purple-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">32GB DDR5 6000MHz Low-Latency</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-purple-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">BenQ Zowie XL2566K 360Hz DyAc+</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-purple-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">SteelSeries Apex Pro TKL</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-purple-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Razer Viper V3 Pro Wireless</span></li>
              </ul>
            </div>
            <div class="mt-8 pt-4 border-t border-slate-200 dark:border-darkslate-border flex items-center justify-between">
              <div>
                <span class="text-2xl font-black text-black dark:text-white">$5.50</span>
                <span class="text-xs text-black dark:text-slate-400">/ hour</span>
              </div>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-purple-600 hover:bg-purple-500">Book Pro</a>
            </div>
          </div>

          <!-- Rig Tier 3 -->
          <div class="rounded-2xl p-6 bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border shadow-sm flex flex-col justify-between h-full hover:border-pink-500 transition-colors">
            <div class="flex-1 flex flex-col">
              <div class="text-xs font-bold uppercase tracking-wider text-pink-600 dark:text-pink-400">Tier 3: Sim Cockpit</div>
              <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mt-1 mb-4">Fanatec DD2 Bay</h3>
              <ul class="space-y-3 text-xs sm:text-sm text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-pink-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Fanatec Podium DD2 25Nm Force</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-pink-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Triple 4K 144Hz 55" Curved Wraparound</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-pink-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Hydraulic Loadcell Inverted Pedals</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-pink-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">NextLevel Racing GT Elite Motion Pod</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-pink-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Buttkicker Haptic Feedback Transducer</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-pink-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">iRacing & Assetto Corsa Pro Telemetry</span></li>
              </ul>
            </div>
            <div class="mt-8 pt-4 border-t border-slate-200 dark:border-darkslate-border flex items-center justify-between">
              <div>
                <span class="text-2xl font-black text-black dark:text-white">$9.00</span>
                <span class="text-xs text-black dark:text-slate-400">/ hour</span>
              </div>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-pink-600 hover:bg-pink-500">Book Sim</a>
            </div>
          </div>

          <!-- Rig Tier 4 -->
          <div class="rounded-2xl p-6 bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border shadow-sm flex flex-col justify-between h-full hover:border-emerald-500 transition-colors">
            <div class="flex-1 flex flex-col">
              <div class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Tier 4: Console Pod</div>
              <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mt-1 mb-4">PS5 Pro & OLED</h3>
              <ul class="space-y-3 text-xs sm:text-sm text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-emerald-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Sony PlayStation 5 Pro Edition</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-emerald-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">65" LG G4 4K 144Hz OLED TV</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-emerald-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">DualSense Edge Pro Wireless Gamepads</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-emerald-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Dolby Atmos 7.1 Immersive Soundbar</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-emerald-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Premium Italian Leather Recliner</span></li>
                <li class="flex items-start space-x-2.5 rtl:space-x-reverse"><span class="text-emerald-500 font-bold shrink-0 mt-0.5 select-none text-sm">✔</span><span class="flex-1 leading-snug">Split-Screen & 4-Player Local Support</span></li>
              </ul>
            </div>
            <div class="mt-8 pt-4 border-t border-slate-200 dark:border-darkslate-border flex items-center justify-between">
              <div>
                <span class="text-2xl font-black text-black dark:text-white">$6.00</span>
                <span class="text-xs text-black dark:text-slate-400">/ hour</span>
              </div>
              <a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-emerald-600 hover:bg-emerald-500">Book Console</a>
            </div>
          </div>

        </div>
      </div>
    </section>'''

if old_tiers_pattern.search(index_content):
    index_content = old_tiers_pattern.sub(new_tiers_html, index_content)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("PASS: index.html updated successfully!")
else:
    print("WARN: old_tiers_pattern did not match in index.html")


# ==============================================================================
# 2. FIX player-lounge.html (VIP Pod Stories Alignment & Plain Horizontal Line)
# ==============================================================================
with open('player-lounge.html', 'r', encoding='utf-8') as f:
    lounge_content = f.read()

old_lounge_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">.*?SUITE 03.*?SIM BAY 02.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_lounge_html = '''<div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto items-stretch">
          
          <!-- Testimonial 1 -->
          <div class="p-8 rounded-3xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border shadow-sm hover:border-purple-500 transition-all duration-300 flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <div class="flex text-amber-400 text-sm">★★★★★</div>
                  <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-purple-50 dark:bg-purple-950/60 text-purple-700 dark:text-purple-300 border border-purple-500/20">
                    SUITE 03 • 6-PLAYER CO-OP
                  </span>
                </div>
                <p class="text-sm sm:text-base italic text-black dark:text-slate-300 leading-relaxed min-h-[96px] flex items-center">
                  "We booked Suite 3 for a 4-hour FIFA tournament with 6 friends. The couches are insanely comfortable, food delivery was prompt, and the 65-inch OLED made every goal look unreal."
                </p>
              </div>
            </div>

            <!-- Plain horizontal line -->
            <div class="w-full border-t border-slate-300 dark:border-slate-700 my-5"></div>

            <div class="flex items-center space-x-3 rtl:space-x-reverse">
              <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-purple-600 to-pink-500 text-white font-bold flex items-center justify-center text-sm shadow-md shrink-0">
                DS
              </div>
              <div class="flex-1 min-w-0">
                <strong class="text-sm font-bold text-black dark:text-white block truncate">— Daniel & Squad</strong>
                <span class="text-xs text-black dark:text-slate-400 font-normal block truncate">Console Lounge Regulars • EA FC 25 Squad</span>
              </div>
            </div>
          </div>

          <!-- Testimonial 2 -->
          <div class="p-8 rounded-3xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border shadow-sm hover:border-pink-500 transition-all duration-300 flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-4">
                  <div class="flex text-amber-400 text-sm">★★★★★</div>
                  <span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-pink-50 dark:bg-pink-950/60 text-pink-700 dark:text-pink-300 border border-pink-500/20">
                    SIM BAY 02 • DIRECT-DRIVE
                  </span>
                </div>
                <p class="text-sm sm:text-base italic text-black dark:text-slate-300 leading-relaxed min-h-[96px] flex items-center">
                  "The direct drive racing cockpit is so good it ruined playing racing games on my home desk forever. The force feedback and pedal vibration give you real goosebumps."
                </p>
              </div>
            </div>

            <!-- Plain horizontal line -->
            <div class="w-full border-t border-slate-300 dark:border-slate-700 my-5"></div>

            <div class="flex items-center space-x-3 rtl:space-x-reverse">
              <div class="w-11 h-11 rounded-full bg-gradient-to-tr from-pink-500 to-cyan-500 text-white font-bold flex items-center justify-center text-sm shadow-md shrink-0">
                TC
              </div>
              <div class="flex-1 min-w-0">
                <strong class="text-sm font-bold text-black dark:text-white block truncate">— Tyler Chen</strong>
                <span class="text-xs text-black dark:text-slate-400 font-normal block truncate">iRacing GT3 Driver • Spa-Francorchamps Sim Record</span>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>'''

if old_lounge_pattern.search(lounge_content):
    lounge_content = old_lounge_pattern.sub(new_lounge_html, lounge_content)
    with open('player-lounge.html', 'w', encoding='utf-8') as f:
        f.write(lounge_content)
    print("PASS: player-lounge.html updated successfully!")
else:
    print("WARN: old_lounge_pattern did not match in player-lounge.html")


# ==============================================================================
# 3, 4, 5. FIX about.html (Remove Partner strip, Align Zones & Line, Align Careers Perks)
# ==============================================================================
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# 3. Replace Section 8 (Hardware Partners) with Fair Play Standards section
old_sec8_pattern = re.compile(
    r'<!-- ================= SECTION 8: HARDWARE PARTNERS ================= -->.*?Official Hardware & Peripherals Partners.*?</section>',
    re.DOTALL
)

new_sec8_html = '''<!-- ================= SECTION 8: FAIR PLAY & TOURNAMENT INTEGRITY ================= -->
    <section class="py-16 bg-white dark:bg-darkslate-card border-y border-slate-200 dark:border-darkslate-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center max-w-3xl mx-auto mb-10 space-y-2">
          <span class="text-xs font-extrabold uppercase tracking-widest text-cyan-600 dark:text-cyan-400">Competitive Integrity</span>
          <h3 class="text-2xl sm:text-3xl font-black font-display uppercase tracking-tight text-black dark:text-white">
            The AuraPlay Fair-Play & Anti-Cheat Standard
          </h3>
          <p class="text-xs sm:text-sm text-black dark:text-slate-300 leading-relaxed">
            Every competitive battlestation is monitored by kernel-level isolation, proctored tournament environments, and tamper-evident peripheral verification.
          </p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
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
        </div>
      </div>
    </section>'''

if old_sec8_pattern.search(about_content):
    about_content = old_sec8_pattern.sub(new_sec8_html, about_content)
    print("PASS: about.html Section 8 replaced!")
else:
    print("WARN: old_sec8_pattern did not match in about.html")

# 4. Fix Section 12 (Arena Floor Plan & Zones cards inner text alignment & plain horizontal line)
old_sec12_pattern = re.compile(
    r'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">.*?ZONE A.*?ZONE D.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_sec12_html = '''<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 items-stretch">
          
          <!-- Zone A -->
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 transition-all duration-300 group flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 border border-cyan-500/20">
                    ZONE A • 48 STATIONS
                  </span>
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </div>
                <h3 class="text-lg font-black font-display uppercase text-black dark:text-white group-hover:text-cyan-500 transition-colors">
                  PC Master Battlestations
                </h3>
                <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed min-h-[52px]">
                  Liquid-cooled RTX 4090 rigs, i9-14900KS, 360Hz QD-OLED monitors, and tournament sound-dampened partitions.
                </p>
              </div>
            </div>

            <!-- Plain horizontal line -->
            <div class="w-full border-t border-slate-300 dark:border-slate-700 my-4"></div>

            <div class="space-y-2 text-[11px] font-semibold text-black dark:text-slate-400">
              <div class="flex justify-between items-center"><span>Display:</span><strong class="text-black dark:text-white">360Hz QD-OLED 0.03ms</strong></div>
              <div class="flex justify-between items-center"><span>Network:</span><strong class="text-cyan-500">Dual 10Gbps Dedicated</strong></div>
              <div class="flex justify-between items-center"><span>Status:</span><strong class="text-emerald-500">Live & Available</strong></div>
            </div>
          </div>

          <!-- Zone B -->
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border hover:border-purple-500 transition-all duration-300 group flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-purple-500/10 text-purple-600 dark:text-purple-400 border border-purple-500/20">
                    ZONE B • 12 PODS
                  </span>
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </div>
                <h3 class="text-lg font-black font-display uppercase text-black dark:text-white group-hover:text-purple-500 transition-colors">
                  PS5 Pro Couch Suites
                </h3>
                <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed min-h-[52px]">
                  Sony PlayStation 5 Pro consoles connected to calibrated 65" LG OLED displays with 7.1 Dolby Atmos soundbars.
                </p>
              </div>
            </div>

            <!-- Plain horizontal line -->
            <div class="w-full border-t border-slate-300 dark:border-slate-700 my-4"></div>

            <div class="space-y-2 text-[11px] font-semibold text-black dark:text-slate-400">
              <div class="flex justify-between items-center"><span>Display:</span><strong class="text-black dark:text-white">65" 4K 120Hz VRR OLED</strong></div>
              <div class="flex justify-between items-center"><span>Audio:</span><strong class="text-purple-500">Dolby Atmos Surround</strong></div>
              <div class="flex justify-between items-center"><span>Seating:</span><strong class="text-emerald-500">Custom Squad Couches</strong></div>
            </div>
          </div>

          <!-- Zone C -->
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border hover:border-pink-500 transition-all duration-300 group flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-pink-500/10 text-pink-600 dark:text-pink-400 border border-pink-500/20">
                    ZONE C • 6 RIGS
                  </span>
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </div>
                <h3 class="text-lg font-black font-display uppercase text-black dark:text-white group-hover:text-pink-500 transition-colors">
                  Direct-Drive Sim Cockpits
                </h3>
                <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed min-h-[52px]">
                  Fanatec Podium DD2 25Nm wheelbases, hydraulic load-cell inverted pedals, and active D-BOX 4-axis motion chassis.
                </p>
              </div>
            </div>

            <!-- Plain horizontal line -->
            <div class="w-full border-t border-slate-300 dark:border-slate-700 my-4"></div>

            <div class="space-y-2 text-[11px] font-semibold text-black dark:text-slate-400">
              <div class="flex justify-between items-center"><span>Wheelbase:</span><strong class="text-black dark:text-white">25Nm Direct Drive</strong></div>
              <div class="flex justify-between items-center"><span>Motion:</span><strong class="text-pink-500">D-BOX 4-Axis G-Force</strong></div>
              <div class="flex justify-between items-center"><span>View:</span><strong class="text-emerald-500">Triple 32" Curved 240Hz</strong></div>
            </div>
          </div>

          <!-- Zone D -->
          <div class="p-6 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border hover:border-amber-500 transition-all duration-300 group flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-3">
                  <span class="px-2.5 py-1 rounded-md text-[11px] font-black uppercase tracking-wider bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">
                    ZONE D • PRO LAB
                  </span>
                  <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                </div>
                <h3 class="text-lg font-black font-display uppercase text-black dark:text-white group-hover:text-amber-500 transition-colors">
                  Hardware Tuning Lab
                </h3>
                <p class="text-xs text-black dark:text-slate-400 mt-2 leading-relaxed min-h-[52px]">
                  Hardware customization desk with rapid-trigger analog switches, 8000Hz polling mice, glass mousepads, and audiophile DACs.
                </p>
              </div>
            </div>

            <!-- Plain horizontal line -->
            <div class="w-full border-t border-slate-300 dark:border-slate-700 my-4"></div>

            <div class="space-y-2 text-[11px] font-semibold text-black dark:text-slate-400">
              <div class="flex justify-between items-center"><span>Switches:</span><strong class="text-black dark:text-white">0.1mm Rapid Trigger</strong></div>
              <div class="flex justify-between items-center"><span>Sensors:</span><strong class="text-amber-500">8,000Hz HyperPolling</strong></div>
              <div class="flex justify-between items-center"><span>Access:</span><strong class="text-emerald-500">Free With Any Pass</strong></div>
            </div>
          </div>

        </div>
      </div>
    </section>'''

if old_sec12_pattern.search(about_content):
    about_content = old_sec12_pattern.sub(new_sec12_html, about_content)
    print("PASS: about.html Section 12 updated!")
else:
    print("WARN: old_sec12_pattern did not match in about.html")

# 5. Fix Section 14 (Careers perks inner text alignment)
old_sec14_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">.*?FULL TIME • HARDWARE.*?FULL / PART TIME.*?</div>\s*</div>',
    re.DOTALL
)

new_sec14_html = '''<div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10 items-stretch">
          
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

        </div>'''

if old_sec14_pattern.search(about_content):
    about_content = old_sec14_pattern.sub(new_sec14_html, about_content)
    print("PASS: about.html Section 14 updated!")
else:
    print("WARN: old_sec14_pattern did not match in about.html")

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)
print("PASS: about.html saved!")
