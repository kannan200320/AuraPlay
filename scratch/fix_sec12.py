# -*- coding: utf-8 -*-
import re

with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

# Fix Section 12 (Arena Floor Plan & Zones cards inner text alignment & plain horizontal line)
old_sec12_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">.*?<!-- Zone A -->.*?<!-- Zone D -->.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_sec12_html = '''<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 items-stretch">
          
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
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(about_content)
    print("PASS: about.html Section 12 updated successfully!")
else:
    print("WARN: old_sec12_pattern still did not match!")
