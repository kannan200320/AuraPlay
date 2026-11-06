# -*- coding: utf-8 -*-
import re

# ==============================================================================
# 1, 2, 3. UPDATE pricing.html
# ==============================================================================
with open('pricing.html', 'r', encoding='utf-8') as f:
    pricing_content = f.read()

# --- 1. Fix Section 3: 5 Core Hour Packs (Pricing Cards Inner Text Alignment) ---
old_sec3_cards_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">.*?<!-- Plan 1: 1 Hour -->.*?<!-- Plan 5: Monthly Membership -->.*?</div>\s*</div>\s*<!-- Fast Gamer Dashboard Top-Up Banner -->',
    re.DOTALL
)

new_sec3_cards_html = '''<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 items-stretch">
          
          <!-- Plan 1: 1 Hour -->
          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full hover:border-cyan-500 transition-all shadow-md">
            <div class="flex-1 flex flex-col">
              <span class="px-2.5 py-1 rounded text-[11px] font-bold bg-slate-100 dark:bg-darkslate-deep text-black dark:text-slate-400 uppercase w-fit">Quick Match</span>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white mt-3">1 Hour</h3>
              <div class="mt-4 flex items-baseline">
                <span class="text-4xl font-black font-display text-black dark:text-white">$6</span>
                <span class="text-xs text-black dark:text-slate-400 ml-1">/hour</span>
              </div>
              <p class="text-xs text-black dark:text-slate-400 mt-3 leading-relaxed min-h-[50px]">Ideal for warm-ups, aim routine training, or quick 1v1 scrims before tournaments.</p>
              
              <ul class="mt-6 space-y-3 text-xs text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Standard Arena PC Rig</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">360Hz Display Access</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">All Pre-Installed Games</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse text-slate-400 dark:text-slate-500"><span class="text-slate-400 dark:text-slate-500 font-bold shrink-0 mt-0.5 select-none text-sm">✗</span><span class="flex-1 leading-snug">No Minute Rollover</span></li>
              </ul>
            </div>
            <a href="book-slot.html" class="mt-8 block w-full py-2.5 rounded-xl text-center text-xs font-bold bg-slate-100 dark:bg-darkslate-deep hover:bg-cyan-500 hover:text-black text-black dark:text-slate-200 transition-all">
              Select 1 Hour
            </a>
          </div>

          <!-- Plan 2: 3 Hours Combo (Popular) -->
          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border-2 border-cyan-500 dark:border-cyan-500 flex flex-col justify-between h-full relative shadow-xl">
            <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-3 py-1 rounded-full bg-cyan-500 text-black font-black text-[10px] uppercase tracking-wider">
              Most Popular
            </div>
            <div class="flex-1 flex flex-col">
              <span class="px-2.5 py-1 rounded text-[11px] font-bold bg-cyan-100 dark:bg-cyan-950 text-cyan-700 dark:text-cyan-300 uppercase w-fit">Squad Combo</span>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white mt-3">3 Hours</h3>
              <div class="mt-4 flex items-baseline">
                <span class="text-4xl font-black font-display text-black dark:text-white">$15</span>
                <span class="text-xs text-black dark:text-slate-400 ml-1">($5.00/hr)</span>
              </div>
              <p class="text-xs text-black dark:text-slate-400 mt-3 leading-relaxed min-h-[50px]">The sweet spot for full ranked queues, Premier match grinds, and custom lobbies.</p>
              
              <ul class="mt-6 space-y-3 text-xs text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Standard & VIP Rigs</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">1-Month Minute Rollover</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Free Peripheral Swaps</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">+300 AuraPlay XP</span></li>
              </ul>
            </div>
            <a href="book-slot.html" class="mt-8 block w-full py-2.5 rounded-xl text-center text-xs font-black bg-cyan-500 hover:bg-cyan-400 text-black transition-all shadow-md">
              Select 3 Hours
            </a>
          </div>

          <!-- Plan 3: Day Pass -->
          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full hover:border-purple-500 transition-all shadow-md">
            <div class="flex-1 flex flex-col">
              <span class="px-2.5 py-1 rounded text-[11px] font-bold bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-300 uppercase w-fit">12-Hour Marathon</span>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white mt-3">Day Pass</h3>
              <div class="mt-4 flex items-baseline">
                <span class="text-4xl font-black font-display text-black dark:text-white">$35</span>
                <span class="text-xs text-black dark:text-slate-400 ml-1">(12 Hours)</span>
              </div>
              <p class="text-xs text-black dark:text-slate-400 mt-3 leading-relaxed min-h-[50px]">Full 12-hour session from 10 AM to 10 PM. Jump between PC, Sim Rigs, and PS5 Pro.</p>
              
              <ul class="mt-6 space-y-3 text-xs text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Full Venue Platform Hopping</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Includes 1 Hr Sim Cockpit</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Private Locker Storage</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">+1,000 AuraPlay XP</span></li>
              </ul>
            </div>
            <a href="book-slot.html" class="mt-8 block w-full py-2.5 rounded-xl text-center text-xs font-bold bg-slate-100 dark:bg-darkslate-deep hover:bg-purple-600 hover:text-white text-black dark:text-slate-200 transition-all">
              Select Day Pass
            </a>
          </div>

          <!-- Plan 4: Night Pass -->
          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full hover:border-pink-500 transition-all shadow-md">
            <div class="flex-1 flex flex-col">
              <span class="px-2.5 py-1 rounded text-[11px] font-bold bg-pink-100 dark:bg-pink-950 text-pink-700 dark:text-pink-300 uppercase w-fit">11 PM – 8 AM</span>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white mt-3">Night Pass</h3>
              <div class="mt-4 flex items-baseline">
                <span class="text-4xl font-black font-display text-black dark:text-white">$28</span>
                <span class="text-xs text-black dark:text-slate-400 ml-1">(9 Hours)</span>
              </div>
              <p class="text-xs text-black dark:text-slate-400 mt-3 leading-relaxed min-h-[50px]">The legendary graveyard lock-in. Minimal network congestion, pure competitive focus.</p>
              
              <ul class="mt-6 space-y-3 text-xs text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Guaranteed Station Lock</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Peak Fiber Routing (&lt;4ms)</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Dim Ambient Night Lights</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">+800 AuraPlay XP</span></li>
              </ul>
            </div>
            <a href="book-slot.html" class="mt-8 block w-full py-2.5 rounded-xl text-center text-xs font-bold bg-slate-100 dark:bg-darkslate-deep hover:bg-pink-600 hover:text-white text-black dark:text-slate-200 transition-all">
              Select Night Pass
            </a>
          </div>

          <!-- Plan 5: Monthly Membership -->
          <div class="rounded-3xl p-6 bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full hover:border-amber-500 transition-all shadow-md">
            <div class="flex-1 flex flex-col">
              <span class="px-2.5 py-1 rounded text-[11px] font-bold bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-300 uppercase w-fit">VIP Elite</span>
              <h3 class="text-xl font-bold font-display uppercase text-black dark:text-white mt-3">Monthly Pass</h3>
              <div class="mt-4 flex items-baseline">
                <span class="text-4xl font-black font-display text-black dark:text-white">$149</span>
                <span class="text-xs text-black dark:text-slate-400 ml-1">/month</span>
              </div>
              <p class="text-xs text-black dark:text-slate-400 mt-3 leading-relaxed min-h-[50px]">Unlimited arena hours, reserved personal rig configuration, and free tournament entry.</p>
              
              <ul class="mt-6 space-y-3 text-xs text-black dark:text-slate-300 flex-1">
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Unlimited Arena Gaming</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Permanent SSD Cache Slot</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">Free Weekly In-House Entry</span></li>
                <li class="flex items-start space-x-2 rtl:space-x-reverse"><span class="text-cyan-500 font-bold shrink-0 mt-0.5 select-none text-sm">✓</span><span class="flex-1 leading-snug">VIP Lounge Keycard Access</span></li>
              </ul>
            </div>
            <a href="membership.html" class="mt-8 block w-full py-2.5 rounded-xl text-center text-xs font-bold bg-slate-100 dark:bg-darkslate-deep hover:bg-amber-500 hover:text-black text-black dark:text-slate-200 transition-all">
              Join Monthly VIP
            </a>
          </div>

        </div>
        <!-- Fast Gamer Dashboard Top-Up Banner -->'''

if old_sec3_cards_pattern.search(pricing_content):
    pricing_content = old_sec3_cards_pattern.sub(new_sec3_cards_html, pricing_content)
    print("PASS: pricing.html Section 3 cards updated!")
else:
    print("WARN: old_sec3_cards_pattern did not match!")


# --- 2. Fix Section 5: Comparison Table (Proper Unified Colour Without Mixed Colours) ---
old_table_pattern = re.compile(
    r'<div class="overflow-x-auto">\s*<table class="w-full text-left border-collapse text-xs sm:text-sm">.*?</table>\s*</div>',
    re.DOTALL
)

new_table_html = '''<div class="overflow-x-auto">
          <table class="w-full text-left border-collapse text-xs sm:text-sm">
            <thead>
              <tr class="border-b-2 border-slate-200 dark:border-darkslate-border">
                <th class="py-4 px-4 font-bold text-slate-500 dark:text-slate-400 uppercase text-xs">Features</th>
                <th class="py-4 px-4 font-black text-black dark:text-white uppercase tracking-wider">Arena Standard</th>
                <th class="py-4 px-4 font-black text-cyan-600 dark:text-cyan-400 uppercase tracking-wider">
                  Pro VIP Stage <span class="ml-1 text-[10px] font-bold text-cyan-500 bg-cyan-500/10 px-1.5 py-0.5 rounded">Popular</span>
                </th>
                <th class="py-4 px-4 font-black text-black dark:text-white uppercase tracking-wider">Sim Racing Pod</th>
                <th class="py-4 px-4 font-black text-black dark:text-white uppercase tracking-wider">PS5 Pro Couch</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 dark:divide-darkslate-border">
              <tr class="hover:bg-slate-50/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="py-4 px-4 font-bold text-black dark:text-white">Graphics Processing</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">RTX 4080 Super 16GB</td>
                <td class="py-4 px-4 font-bold text-cyan-600 dark:text-cyan-400">RTX 4090 24GB Liquid</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">RTX 4090 Triple Display</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">PS5 Pro PSSR AI Upscaling</td>
              </tr>
              <tr class="hover:bg-slate-50/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="py-4 px-4 font-bold text-black dark:text-white">Display & Refresh</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">27" 240Hz Fast IPS</td>
                <td class="py-4 px-4 font-bold text-cyan-600 dark:text-cyan-400">27" 360Hz QD-OLED</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">Triple 32" Curved 165Hz</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">65" LG C4 OLED 120Hz</td>
              </tr>
              <tr class="hover:bg-slate-50/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="py-4 px-4 font-bold text-black dark:text-white">Input Peripherals</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">Logitech G Pro + G513</td>
                <td class="py-4 px-4 font-bold text-cyan-600 dark:text-cyan-400">Wooting 60HE + 4K Mouse</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">Fanatec DD2 25Nm Wheel</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">DualSense Edge Custom</td>
              </tr>
              <tr class="hover:bg-slate-50/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="py-4 px-4 font-bold text-black dark:text-white">Ergonomic Seating</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">Secretlab Titan Evo</td>
                <td class="py-4 px-4 font-bold text-cyan-600 dark:text-cyan-400">Herman Miller Embody</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">Sparco FIA Bucket Seat</td>
                <td class="py-4 px-4 text-slate-700 dark:text-slate-300">Plush Italian Leather Recliner</td>
              </tr>
              <tr class="bg-slate-50/70 dark:bg-darkslate-deep/50 hover:bg-slate-100/70 dark:hover:bg-darkslate-deep/80 transition-colors">
                <td class="py-4 px-4 font-black text-black dark:text-white">Hourly Rate</td>
                <td class="py-4 px-4 font-mono font-bold text-black dark:text-white">$6.00 / hr</td>
                <td class="py-4 px-4 font-mono font-black text-cyan-600 dark:text-cyan-400 text-sm">$8.50 / hr</td>
                <td class="py-4 px-4 font-mono font-bold text-black dark:text-white">$12.00 / hr</td>
                <td class="py-4 px-4 font-mono font-bold text-black dark:text-white">$10.00 / hr (Whole Suite)</td>
              </tr>
            </tbody>
          </table>
        </div>'''

if old_table_pattern.search(pricing_content):
    pricing_content = old_table_pattern.sub(new_table_html, pricing_content)
    print("PASS: pricing.html Section 5 table updated with unified colors!")
else:
    print("WARN: old_table_pattern did not match!")


# --- 3. Fix Section 10: Peripheral Addon Cards Inner Text Alignment ---
old_addons_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-4 gap-6">.*?Wooting 60HE\+.*?Sennheiser HD 560S.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_addons_html = '''<div class="grid grid-cols-1 md:grid-cols-4 gap-6 items-stretch">
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="text-[11px] font-bold text-cyan-500 block uppercase">Hall Effect Keyboard</span>
              <h4 class="font-bold text-black dark:text-white text-base mt-1">Wooting 60HE+</h4>
              <p class="text-xs text-black dark:text-slate-400 mt-2 min-h-[48px] leading-relaxed">Adjustable actuation from 0.1mm to 4.0mm with Rapid Trigger mode.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-white">Free With Pass</div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="text-[11px] font-bold text-purple-500 block uppercase">Sub-50g Wireless</span>
              <h4 class="font-bold text-black dark:text-white text-base mt-1">Logitech Superlight 2</h4>
              <p class="text-xs text-black dark:text-slate-400 mt-2 min-h-[48px] leading-relaxed">Lightforce hybrid optical-mechanical switches, 4,000Hz wireless polling.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-white">Free With Pass</div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="text-[11px] font-bold text-pink-500 block uppercase">Japanese Glass-Coated</span>
              <h4 class="font-bold text-black dark:text-white text-base mt-1">Artisan Hayate Otsu</h4>
              <p class="text-xs text-black dark:text-slate-400 mt-2 min-h-[48px] leading-relaxed">Premium porous foam base with consistent dynamic friction for micro-adjustments.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-white">+$2.00 / Session</div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="text-[11px] font-bold text-amber-500 block uppercase">Studio Monitoring</span>
              <h4 class="font-bold text-black dark:text-white text-base mt-1">Sennheiser HD 560S</h4>
              <p class="text-xs text-black dark:text-slate-400 mt-2 min-h-[48px] leading-relaxed">Open-back acoustic design with custom tuned DAC amp for accurate audio cue distance.</p>
            </div>
            <div class="mt-4 pt-3 border-t border-slate-200 dark:border-darkslate-border text-xs font-bold text-black dark:text-white">+$3.00 / Session</div>
          </div>
        </div>
      </div>
    </section>'''

if old_addons_pattern.search(pricing_content):
    pricing_content = old_addons_pattern.sub(new_addons_html, pricing_content)
    print("PASS: pricing.html Section 10 gear addons updated!")
else:
    print("WARN: old_addons_pattern did not match!")

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(pricing_content)
print("PASS: pricing.html saved successfully!")


# ==============================================================================
# 4, 5. UPDATE book-slot.html
# ==============================================================================
with open('book-slot.html', 'r', encoding='utf-8') as f:
    book_content = f.read()

# --- 4. Interactive Shift & Duration Selection in HTML & JS ---
# Update Step 3 (Shift Cards) with data attributes
old_shifts_html = '''        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div class="shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all">
            <span class="text-xs font-bold text-black dark:text-slate-400 block">Morning Shift</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">08:00 AM – 01:00 PM</span>
            <span class="text-xs text-emerald-500 font-bold block mt-2">Off-Peak Rates (15% Off)</span>
          </div>
          <div class="shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all">
            <span class="text-xs font-bold text-black dark:text-slate-400 block">Afternoon Grind</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">01:00 PM – 06:00 PM</span>
            <span class="text-xs text-cyan-500 font-bold block mt-2">Standard Gaming Rate</span>
          </div>
          <div class="shift-card p-5 rounded-2xl border-2 border-cyan-500 bg-cyan-50 dark:bg-cyan-950/40 cursor-pointer shadow-md">
            <span class="text-xs font-bold text-cyan-600 dark:text-cyan-400 block">Prime Time Arena</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">06:00 PM – 11:00 PM</span>
            <span class="text-xs text-purple-500 font-bold block mt-2">Tournaments & Scrims Active</span>
          </div>
          <div class="shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all">
            <span class="text-xs font-bold text-black dark:text-slate-400 block">Night Owl Lock-In</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">11:00 PM – 08:00 AM</span>
            <span class="text-xs text-emerald-500 font-bold block mt-2">Flat Rate Pass Available</span>
          </div>
        </div>'''

new_shifts_html = '''        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4" id="shifts-container">
          <div class="shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all" data-shift="Morning Shift (08:00 AM - 01:00 PM)">
            <span class="shift-badge text-xs font-bold text-black dark:text-slate-400 block">Morning Shift</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">08:00 AM – 01:00 PM</span>
            <span class="text-xs text-emerald-500 font-bold block mt-2">Off-Peak Rates (15% Off)</span>
          </div>
          <div class="shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all" data-shift="Afternoon Grind (01:00 PM - 06:00 PM)">
            <span class="shift-badge text-xs font-bold text-black dark:text-slate-400 block">Afternoon Grind</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">01:00 PM – 06:00 PM</span>
            <span class="text-xs text-cyan-500 font-bold block mt-2">Standard Gaming Rate</span>
          </div>
          <div class="shift-card p-5 rounded-2xl border-2 border-cyan-500 bg-cyan-50 dark:bg-cyan-950/40 cursor-pointer shadow-md" data-shift="Prime Time Arena (06:00 PM - 11:00 PM)">
            <span class="shift-badge text-xs font-bold text-cyan-600 dark:text-cyan-400 block">Prime Time Arena</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">06:00 PM – 11:00 PM</span>
            <span class="text-xs text-purple-500 font-bold block mt-2">Tournaments & Scrims Active</span>
          </div>
          <div class="shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all" data-shift="Night Owl Lock-In (11:00 PM - 08:00 AM)">
            <span class="shift-badge text-xs font-bold text-black dark:text-slate-400 block">Night Owl Lock-In</span>
            <span class="text-lg font-black text-black dark:text-white font-display block mt-1">11:00 PM – 08:00 AM</span>
            <span class="text-xs text-emerald-500 font-bold block mt-2">Flat Rate Pass Available</span>
          </div>
        </div>'''

if old_shifts_html in book_content:
    book_content = book_content.replace(old_shifts_html, new_shifts_html)
    print("PASS: book-slot.html Shift cards updated!")
else:
    print("WARN: old_shifts_html exact match failed, using regex fallback")
    book_content = re.sub(
        r'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">\s*<div class="shift-card.*?</div>\s*</div>\s*</div>\s*</section>',
        new_shifts_html + '\n      </div>\n    </section>',
        book_content,
        flags=re.DOTALL
    )

# Update Step 4 (Duration Buttons)
old_duration_html = '''        <div class="grid grid-cols-2 sm:grid-cols-5 gap-4">
          <button class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all" data-hours="1">
            1 Hour
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$6.00</span>
          </button>
          <button class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all" data-hours="2">
            2 Hours
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$12.00</span>
          </button>
          <button class="duration-btn py-4 rounded-2xl border-2 border-purple-500 bg-purple-50 dark:bg-purple-950/40 font-display text-lg font-black text-black dark:text-white shadow-md" data-hours="3">
            3 Hours Combo
            <span class="block text-xs font-bold text-purple-600 dark:text-purple-400 mt-0.5">$16.00 (Save $2)</span>
          </button>
          <button class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all" data-hours="5">
            5 Hours Pack
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$25.00 (Save $5)</span>
          </button>
          <button class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all col-span-2 sm:col-span-1" data-hours="10">
            Day Pass (10h)
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$45.00 Unlimited</span>
          </button>
        </div>'''

new_duration_html = '''        <div class="grid grid-cols-2 sm:grid-cols-5 gap-4" id="durations-container">
          <button type="button" class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all" data-hours="1" data-label="1 Hour" data-price="$6.00">
            1 Hour
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$6.00</span>
          </button>
          <button type="button" class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all" data-hours="2" data-label="2 Hours" data-price="$12.00">
            2 Hours
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$12.00</span>
          </button>
          <button type="button" class="duration-btn py-4 rounded-2xl border-2 border-purple-500 bg-purple-50 dark:bg-purple-950/40 font-display text-lg font-black text-black dark:text-white shadow-md" data-hours="3" data-label="3 Hours Combo Pack" data-price="$16.00">
            3 Hours Combo
            <span class="block text-xs font-bold text-purple-600 dark:text-purple-400 mt-0.5">$16.00 (Save $2)</span>
          </button>
          <button type="button" class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all" data-hours="5" data-label="5 Hours Pack" data-price="$25.00">
            5 Hours Pack
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$25.00 (Save $5)</span>
          </button>
          <button type="button" class="duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all col-span-2 sm:col-span-1" data-hours="10" data-label="Day Pass (10 Hours Unlimited)" data-price="$45.00">
            Day Pass (10h)
            <span class="block text-xs font-normal text-black dark:text-slate-400 mt-0.5">$45.00 Unlimited</span>
          </button>
        </div>'''

if old_duration_html in book_content:
    book_content = book_content.replace(old_duration_html, new_duration_html)
    print("PASS: book-slot.html Duration buttons updated!")
else:
    print("WARN: old_duration_html exact match failed, using regex fallback")
    book_content = re.sub(
        r'<div class="grid grid-cols-2 sm:grid-cols-5 gap-4">\s*<button class="duration-btn.*?</div>\s*</div>\s*</section>',
        new_duration_html + '\n      </div>\n    </section>',
        book_content,
        flags=re.DOTALL
    )

# Add IDs to summary rows in Section 8 Order Summary
old_summary_shift = '''            <div class="flex justify-between text-black dark:text-slate-400">
              <span>Shift Window:</span>
              <span class="font-bold text-black dark:text-white">Prime Time Arena (06:00 PM - 09:00 PM)</span>
            </div>
            <div class="flex justify-between text-black dark:text-slate-400">
              <span>Duration:</span>
              <span class="font-bold text-black dark:text-white">3 Hours Combo Pack</span>
            </div>'''

new_summary_shift = '''            <div class="flex justify-between text-black dark:text-slate-400">
              <span>Shift Window:</span>
              <span id="summary-shift" class="font-bold text-black dark:text-white">Prime Time Arena (06:00 PM - 11:00 PM)</span>
            </div>
            <div class="flex justify-between text-black dark:text-slate-400">
              <span>Duration:</span>
              <span id="summary-duration" class="font-bold text-black dark:text-white">3 Hours Combo Pack</span>
            </div>'''

if old_summary_shift in book_content:
    book_content = book_content.replace(old_summary_shift, new_summary_shift)
    print("PASS: book-slot.html Order Summary IDs added!")


# --- 5. Fix Section 10: Hardware Specifications Cards Alignment ---
old_sec10_specs = '''        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6 text-xs">
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-2">
            <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Processor</span>
            <span class="text-black dark:text-white font-bold text-sm block">AMD Ryzen 7 7800X3D</span>
            <span class="text-emerald-500 block">96MB 3D V-Cache • 5.0GHz All-Core Boost</span>
            <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed">Engineered specifically for peak 1% low frames in Valorant, CS2, and Apex Legends.</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-2">
            <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Graphics Accelerator</span>
            <span class="text-black dark:text-white font-bold text-sm block">GeForce RTX 4090 24GB</span>
            <span class="text-emerald-500 block">Custom EKWB Loop • 450W Power Target</span>
            <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed">Delivers locked 360+ FPS at native 1440p with zero thermal throttling or fan noise.</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-2">
            <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Memory & Storage</span>
            <span class="text-black dark:text-white font-bold text-sm block">64GB DDR5 6000MHz</span>
            <span class="text-cyan-500 block">CL30 Low-Latency • 10Gbps NVMe Flash</span>
            <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed">Instant game loads directly from our redundant all-flash Enterprise SAN cluster.</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-2">
            <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Tournament Monitor</span>
            <span class="text-black dark:text-white font-bold text-sm block">27" 360Hz QD-OLED</span>
            <span class="text-purple-500 block">0.03ms Response • G-Sync Compatible</span>
            <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed">Infinite contrast ratio and zero motion blur blur-free tracking for fast flick shots.</p>
          </div>
        </div>'''

new_sec10_specs = '''        <div class="grid grid-cols-2 sm:grid-cols-4 gap-6 text-xs items-stretch">
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Processor</span>
              <span class="text-black dark:text-white font-bold text-sm block mt-1">AMD Ryzen 7 7800X3D</span>
              <span class="text-emerald-500 block text-xs mt-1 min-h-[36px] flex items-center leading-snug">96MB 3D V-Cache • 5.0GHz All-Core Boost</span>
              <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed mt-2 min-h-[44px]">Engineered specifically for peak 1% low frames in Valorant, CS2, and Apex Legends.</p>
            </div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Graphics Accelerator</span>
              <span class="text-black dark:text-white font-bold text-sm block mt-1">GeForce RTX 4090 24GB</span>
              <span class="text-emerald-500 block text-xs mt-1 min-h-[36px] flex items-center leading-snug">Custom EKWB Loop • 450W Power Target</span>
              <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed mt-2 min-h-[44px]">Delivers locked 360+ FPS at native 1440p with zero thermal throttling or fan noise.</p>
            </div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Memory & Storage</span>
              <span class="text-black dark:text-white font-bold text-sm block mt-1">64GB DDR5 6000MHz</span>
              <span class="text-cyan-500 block text-xs mt-1 min-h-[36px] flex items-center leading-snug">CL30 Low-Latency • 10Gbps NVMe Flash</span>
              <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed mt-2 min-h-[44px]">Instant game loads directly from our redundant all-flash Enterprise SAN cluster.</p>
            </div>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <span class="font-bold text-black dark:text-slate-400 block uppercase tracking-wider text-[11px]">Tournament Monitor</span>
              <span class="text-black dark:text-white font-bold text-sm block mt-1">27" 360Hz QD-OLED</span>
              <span class="text-purple-500 block text-xs mt-1 min-h-[36px] flex items-center leading-snug">0.03ms Response • G-Sync Compatible</span>
              <p class="text-[11px] text-black dark:text-slate-400 leading-relaxed mt-2 min-h-[44px]">Infinite contrast ratio and blur-free motion clarity for sub-millisecond flick shots.</p>
            </div>
          </div>
        </div>'''

if old_sec10_specs in book_content:
    book_content = book_content.replace(old_sec10_specs, new_sec10_specs)
    print("PASS: book-slot.html Section 10 specs cards updated!")
else:
    print("WARN: old_sec10_specs exact match failed, using regex fallback")
    book_content = re.sub(
        r'<div class="grid grid-cols-2 sm:grid-cols-4 gap-6 text-xs">.*?Tournament Monitor.*?</div>\s*</div>\s*</div>\s*</section>',
        new_sec10_specs + '\n      </div>\n    </section>',
        book_content,
        flags=re.DOTALL
    )

# --- Update Script in book-slot.html to make Shift and Duration Selection Interactive ---
old_script = '''    document.addEventListener('DOMContentLoaded', () => {
      const seatBtns = document.querySelectorAll('.seat-btn:not([disabled])');
      const seatLabel = document.getElementById('selected-seat-label');
      const confirmBtn = document.getElementById('confirm-booking-btn');
      const bookingModal = document.getElementById('booking-modal');

      seatBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          seatBtns.forEach(b => {
            b.classList.remove('border-2', 'border-cyan-500', 'bg-cyan-500', 'text-black', 'shadow-md');
            b.classList.add('border-slate-300', 'dark:border-darkslate-border', 'bg-slate-50', 'dark:bg-darkslate-deep', 'text-slate-900', 'dark:text-white');
          });
          btn.classList.add('border-2', 'border-cyan-500', 'bg-cyan-500', 'text-black', 'shadow-md');
          btn.classList.remove('border-slate-300', 'dark:border-darkslate-border', 'bg-slate-50', 'dark:bg-darkslate-deep', 'text-slate-900', 'dark:text-white');
          if (seatLabel) {
            seatLabel.textContent = `Station ${btn.getAttribute('data-seat')} (Zone Alpha - 360Hz QD-OLED)`;
          }
        });
      });

      if (confirmBtn && bookingModal) {
        confirmBtn.addEventListener('click', () => {
          bookingModal.classList.remove('hidden');
        });
      }
    });'''

new_script = '''    document.addEventListener('DOMContentLoaded', () => {
      // 1. Interactive Seat Selection
      const seatBtns = document.querySelectorAll('.seat-btn:not([disabled])');
      const seatLabel = document.getElementById('selected-seat-label');
      const assignedStationSummary = document.querySelector('#selected-seat-label') || document.querySelector('.flex.justify-between.text-black.dark\\\\:text-slate-400 .text-cyan-500');

      seatBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          seatBtns.forEach(b => {
            b.classList.remove('border-2', 'border-cyan-500', 'bg-cyan-500', 'text-black', 'shadow-md');
            b.classList.add('border-slate-300', 'dark:border-darkslate-border', 'bg-slate-50', 'dark:bg-darkslate-deep', 'text-slate-900', 'dark:text-white');
          });
          btn.classList.add('border-2', 'border-cyan-500', 'bg-cyan-500', 'text-black', 'shadow-md');
          btn.classList.remove('border-slate-300', 'dark:border-darkslate-border', 'bg-slate-50', 'dark:bg-darkslate-deep', 'text-slate-900', 'dark:text-white');
          const seatNum = btn.getAttribute('data-seat');
          if (seatLabel) {
            seatLabel.textContent = `Station ${seatNum} (Zone Alpha - 360Hz QD-OLED)`;
          }
          const summaryStation = document.querySelector('.order-station-text');
          if (summaryStation) {
            summaryStation.textContent = `Station ${seatNum} (Zone Alpha)`;
          }
        });
      });

      // 2. Interactive Shift Selection (User Can Choose Any Shift)
      const shiftCards = document.querySelectorAll('.shift-card');
      const summaryShift = document.getElementById('summary-shift');

      shiftCards.forEach(card => {
        card.addEventListener('click', () => {
          shiftCards.forEach(c => {
            c.className = "shift-card p-5 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep cursor-pointer transition-all";
            const badge = c.querySelector('.shift-badge');
            if (badge) {
              badge.className = "shift-badge text-xs font-bold text-black dark:text-slate-400 block";
            }
          });
          card.className = "shift-card p-5 rounded-2xl border-2 border-cyan-500 bg-cyan-50 dark:bg-cyan-950/40 cursor-pointer shadow-md";
          const activeBadge = card.querySelector('.shift-badge');
          if (activeBadge) {
            activeBadge.className = "shift-badge text-xs font-bold text-cyan-600 dark:text-cyan-400 block";
          }
          const shiftVal = card.getAttribute('data-shift');
          if (summaryShift && shiftVal) {
            summaryShift.textContent = shiftVal;
          }
        });
      });

      // 3. Interactive Duration Selection (User Can Choose Any Duration)
      const durationBtns = document.querySelectorAll('.duration-btn');
      const summaryDuration = document.getElementById('summary-duration');
      const receiptTotal = document.getElementById('receipt-total');

      durationBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          durationBtns.forEach(b => {
            const isColSpan = b.classList.contains('col-span-2');
            b.className = `duration-btn py-4 rounded-2xl border border-slate-200 dark:border-darkslate-border hover:border-purple-500 bg-white dark:bg-darkslate-card font-display text-lg font-bold text-black dark:text-white transition-all ${isColSpan ? 'col-span-2 sm:col-span-1' : ''}`;
            const sub = b.querySelector('span');
            if (sub) {
              sub.className = "block text-xs font-normal text-black dark:text-slate-400 mt-0.5";
            }
          });
          const isColSpan = btn.classList.contains('col-span-2');
          btn.className = `duration-btn py-4 rounded-2xl border-2 border-purple-500 bg-purple-50 dark:bg-purple-950/40 font-display text-lg font-black text-black dark:text-white shadow-md ${isColSpan ? 'col-span-2 sm:col-span-1' : ''}`;
          const activeSub = btn.querySelector('span');
          if (activeSub) {
            activeSub.className = "block text-xs font-bold text-purple-600 dark:text-purple-400 mt-0.5";
          }
          const durLabel = btn.getAttribute('data-label');
          const durPrice = btn.getAttribute('data-price');
          if (summaryDuration && durLabel) {
            summaryDuration.textContent = durLabel;
          }
          if (receiptTotal && durPrice) {
            receiptTotal.textContent = durPrice;
          }
        });
      });

      // 4. Modal Confirmation
      const confirmBtn = document.getElementById('confirm-booking-btn');
      const bookingModal = document.getElementById('booking-modal');
      if (confirmBtn && bookingModal) {
        confirmBtn.addEventListener('click', () => {
          bookingModal.classList.remove('hidden');
        });
      }
    });'''

if old_script in book_content:
    book_content = book_content.replace(old_script, new_script)
    print("PASS: book-slot.html Script updated with shift and duration interactivity!")
else:
    print("WARN: old_script exact match failed, using regex fallback")
    book_content = re.sub(
        r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\',\s*\(\)\s*=>\s*\{.*?\}\);\s*</script>',
        f'<script>\n{new_script}\n  </script>',
        book_content,
        flags=re.DOTALL
    )

with open('book-slot.html', 'w', encoding='utf-8') as f:
    f.write(book_content)
print("PASS: book-slot.html saved successfully!")
