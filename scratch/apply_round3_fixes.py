# -*- coding: utf-8 -*-
import re

# ==============================================================================
# 1. FIX membership.html: Proper color without mixed colors in comparison table
# ==============================================================================
with open('membership.html', 'r', encoding='utf-8') as f:
    membership_content = f.read()

old_membership_table_pattern = re.compile(
    r'<div class="overflow-x-auto rounded-3xl border border-slate-200 dark:border-darkslate-border bg-slate-50 dark:bg-darkslate-deep shadow-xl">\s*<table class="w-full text-left text-xs sm:text-sm whitespace-nowrap">.*?</table>\s*</div>',
    re.DOTALL
)

new_membership_table_html = '''<div class="overflow-x-auto rounded-3xl border border-slate-200 dark:border-darkslate-border bg-slate-50 dark:bg-darkslate-deep shadow-xl">
          <table class="w-full text-left text-xs sm:text-sm whitespace-nowrap">
            <thead class="bg-slate-100 dark:bg-darkslate-card text-xs font-bold uppercase tracking-wider border-b border-slate-200 dark:border-darkslate-border">
              <tr>
                <th class="p-5 text-slate-500 dark:text-slate-400">Feature & Privilege</th>
                <th class="p-5 text-center text-black dark:text-white font-extrabold">Bronze</th>
                <th class="p-5 text-center text-black dark:text-white font-extrabold">Silver</th>
                <th class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">
                  Champion VIP <span class="ml-1 text-[10px] font-bold text-cyan-500 bg-cyan-500/10 px-1.5 py-0.5 rounded">Popular</span>
                </th>
                <th class="p-5 text-center text-black dark:text-white font-extrabold">Pro Clan</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 dark:divide-darkslate-border text-slate-700 dark:text-slate-300 font-medium text-xs sm:text-sm">
              <tr class="hover:bg-slate-100/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="p-5 font-bold text-black dark:text-white">Included Gaming Hours / Mo</td>
                <td class="p-5 text-center">10 Hours</td>
                <td class="p-5 text-center">25 Hours</td>
                <td class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">60 Hours</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">180 Hours (Pool)</td>
              </tr>
              <tr class="hover:bg-slate-100/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="p-5 font-bold text-black dark:text-white">Seat Availability Guarantee</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center">15 Minutes</td>
                <td class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">5 Minutes Guarantee</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">Immediate Pod Lock</td>
              </tr>
              <tr class="hover:bg-slate-100/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="p-5 font-bold text-black dark:text-white">RTX 4090 Arena Station Access</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">✓</td>
                <td class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">✓</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">✓</td>
              </tr>
              <tr class="hover:bg-slate-100/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="p-5 font-bold text-black dark:text-white">Fanatec Direct Drive Sim Racing</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">50% Off Rates</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">✓ Included</td>
              </tr>
              <tr class="hover:bg-slate-100/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="p-5 font-bold text-black dark:text-white">Weekly Cash Cup Tournament Entry</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center">1 Entry / Mo</td>
                <td class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">All 4 Entries Free</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">All 5 Players Free</td>
              </tr>
              <tr class="hover:bg-slate-100/50 dark:hover:bg-darkslate-card/50 transition-colors">
                <td class="p-5 font-bold text-black dark:text-white">Personal Keyless Smart Locker</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center text-slate-400 dark:text-slate-600">—</td>
                <td class="p-5 text-center text-cyan-600 dark:text-cyan-400 font-black">✓ Dedicated</td>
                <td class="p-5 text-center font-bold text-black dark:text-white">✓ Team Locker</td>
              </tr>
            </tbody>
          </table>
        </div>'''

if old_membership_table_pattern.search(membership_content):
    membership_content = old_membership_table_pattern.sub(new_membership_table_html, membership_content)
    with open('membership.html', 'w', encoding='utf-8') as f:
        f.write(membership_content)
    print("PASS: membership.html comparison table updated with unified proper color!")
else:
    print("WARN: old_membership_table_pattern did not match in membership.html")


# ==============================================================================
# 2 & 3. FIX blog-detail*.html (QD-OLED Alpha row fix + Recommended Reads alignment)
# ==============================================================================
blog_detail_files = [
    'blog-detail.html',
    'blog-detail-cs2-subtick.html',
    'blog-detail-direct-drive-sim.html',
    'blog-detail-wooting-rapid-trigger.html',
    'blog-detail-zero-bufferbloat.html'
]

old_bench_row_pattern = re.compile(
    r'<tr class="bg-cyan-50/70 dark:bg-cyan-950/30 text-cyan-950 dark:text-cyan-200 font-bold border-l-4 border-cyan-500">.*?Championship Tier.*?</tr>',
    re.DOTALL
)

new_bench_row_html = '''<tr class="bg-cyan-500/10 dark:bg-cyan-500/10 border-l-4 border-cyan-500 font-semibold transition-colors">
                      <td class="p-3.5 font-bold text-black dark:text-white">QD-OLED (AuraPlay Alpha)</td>
                      <td class="p-3.5 font-black text-cyan-600 dark:text-cyan-400">360 Hz</td>
                      <td class="p-3.5 font-mono text-black dark:text-slate-200">2.77 ms</td>
                      <td class="p-3.5 text-black dark:text-slate-200 font-medium">0.03 ms True GtG</td>
                      <td class="p-3.5 font-mono font-bold text-cyan-600 dark:text-cyan-400">4.1 ms</td>
                      <td class="p-3.5 whitespace-nowrap"><span class="inline-flex items-center px-2.5 py-1 rounded-full bg-cyan-500 text-black text-[10px] font-black uppercase tracking-wider whitespace-nowrap shadow-sm">Championship Tier</span></td>
                    </tr>'''

old_rec_reads_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6">\s*<div class="p-6 rounded-3xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-md space-y-4">.*?Read Analysis →</a>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

for bfile in blog_detail_files:
    with open(bfile, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 2. Fix the QD-OLED Alpha row (if present in file)
    if old_bench_row_pattern.search(content):
        content = old_bench_row_pattern.sub(new_bench_row_html, content)
        print(f"PASS: {bfile} benchmark row updated!")

    # 3. Fix Recommended Esports Reads alignment
    # Determine the 3 articles for this file
    m_reads = old_rec_reads_pattern.search(content)
    if m_reads:
        matched_block = m_reads.group(0)
        # Parse each card in the block and inject alignment classes
        cards = re.findall(r'<div class="p-6 rounded-3xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-md space-y-4">(.*?)</div>', matched_block, re.DOTALL)
        if len(cards) == 3:
            aligned_cards = []
            for c in cards:
                # Extract badge, title, desc, link
                badge_m = re.search(r'(<span class="px-2\.5 py-1 rounded text-\[10px\].*?</span>)', c)
                title_m = re.search(r'<h4 class="text-lg font-bold font-display uppercase text-black dark:text-white">(.*?)</h4>', c)
                desc_m = re.search(r'<p class="text-xs text-black dark:text-slate-400 leading-relaxed">(.*?)</p>', c)
                link_m = re.search(r'(<a href="[^"]+" class="[^"]+">Read Analysis →</a>)', c)

                badge_html = badge_m.group(1) if badge_m else ''
                title_text = title_m.group(1) if title_m else ''
                desc_text = desc_m.group(1) if desc_m else ''
                link_html = link_m.group(1) if link_m else ''

                aligned_card = f'''<div class="p-6 rounded-3xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-md flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col">
              <div class="mb-3">
                {badge_html}
              </div>
              <h4 class="text-lg font-bold font-display uppercase text-black dark:text-white min-h-[56px] leading-snug">{title_text}</h4>
              <p class="text-xs text-black dark:text-slate-400 leading-relaxed min-h-[44px] mt-2">{desc_text}</p>
            </div>
            <div class="pt-3 mt-4 border-t border-slate-100 dark:border-darkslate-border/80">
              {link_html}
            </div>
          </div>'''
                aligned_cards.append(aligned_card)

            new_reads_html = f'''<div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
          {aligned_cards[0]}

          {aligned_cards[1]}

          {aligned_cards[2]}
        </div>
      </section>'''
            content = content[:m_reads.start()] + new_reads_html + content[m_reads.end():]
            print(f"PASS: {bfile} Recommended Reads aligned!")
        else:
            print(f"WARN: {bfile} found {len(cards)} cards instead of 3")

    with open(bfile, 'w', encoding='utf-8') as f:
        f.write(content)


# ==============================================================================
# 4. FIX contact.html: Scrim Pod & Venue Hire Inner Text Alignment
# ==============================================================================
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

old_venue_pattern = re.compile(
    r'<div class="grid grid-cols-1 md:grid-cols-2 gap-8">\s*<div class="p-8 rounded-3xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border space-y-4">.*?From \$45 / Hour.*?From \$450 / Hour.*?</div>\s*</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_venue_html = '''<div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch">
          
          <div class="p-8 rounded-3xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <span class="text-xs font-bold px-3 py-1 rounded-full bg-cyan-100 dark:bg-cyan-950/60 text-cyan-600 dark:text-cyan-400 uppercase">Tier 1 Scrim Pod</span>
                <h3 class="text-2xl font-bold font-display uppercase text-black dark:text-white mt-3">Private 5-Player Team Room</h3>
                <p class="text-xs text-black dark:text-slate-400 leading-relaxed mt-2 min-h-[64px]">
                  Equipped with 5x RTX 4090 battlestations, 360Hz QD-OLED monitors, Herman Miller Embody ergonomic seating, sound-dampened acoustic walls, and coach tactical whiteboard.
                </p>
              </div>
            </div>
            <div class="pt-4 mt-6 border-t border-slate-200 dark:border-darkslate-border">
              <div class="text-xs font-bold text-cyan-500">From $45 / Hour • Includes Dedicated 10Gbps VLAN</div>
            </div>
          </div>

          <div class="p-8 rounded-3xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex flex-col justify-between h-full">
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <span class="text-xs font-bold px-3 py-1 rounded-full bg-purple-100 dark:bg-purple-950/60 text-purple-600 dark:text-purple-400 uppercase">Full Venue Takeover</span>
                <h3 class="text-2xl font-bold font-display uppercase text-black dark:text-white mt-3">70-Station Arena Buyout</h3>
                <p class="text-xs text-black dark:text-slate-400 leading-relaxed mt-2 min-h-[64px]">
                  Exclusive access to all 70 PCs, Sim Racing pods, PS5 Pro lounges, live shoutcaster stage, broadcast production switchers, and dedicated floor staff for up to 120 guests.
                </p>
              </div>
            </div>
            <div class="pt-4 mt-6 border-t border-slate-200 dark:border-darkslate-border">
              <div class="text-xs font-bold text-purple-500">From $450 / Hour • Custom Tournament Production Packages</div>
            </div>
          </div>

        </div>
      </div>
    </section>'''

if old_venue_pattern.search(contact_content):
    contact_content = old_venue_pattern.sub(new_venue_html, contact_content)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(contact_content)
    print("PASS: contact.html venue buyout cards updated with aligned inner text!")
else:
    print("WARN: old_venue_pattern did not match in contact.html")


# ==============================================================================
# 5. FIX dashboard-settings.html: Remove "Remote Station Sign-Out & Emergency Flush"
# ==============================================================================
with open('dashboard-settings.html', 'r', encoding='utf-8') as f:
    settings_content = f.read()

old_remote_signout_pattern = re.compile(
    r'\s*<!-- Remote Force Sign-Out -->\s*<div class="pt-6 border-t border-slate-100 dark:border-darkslate-border flex flex-col sm:flex-row sm:items-center justify-between gap-4">\s*<div>\s*<div class="text-xs font-bold text-rose-500">Remote Station Sign-Out & Emergency Flush</div>.*?Emergency Remote Logout\s*</button>\s*</div>',
    re.DOTALL
)

if old_remote_signout_pattern.search(settings_content):
    settings_content = old_remote_signout_pattern.sub('', settings_content)
    with open('dashboard-settings.html', 'w', encoding='utf-8') as f:
        f.write(settings_content)
    print("PASS: dashboard-settings.html Remote Station Sign-Out completely removed!")
else:
    print("WARN: old_remote_signout_pattern did not match in dashboard-settings.html")
