import os

def fix_membership():
    path = 'membership.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    old = '''              <h3 class="text-2xl font-black font-display uppercase text-black dark:text-white mt-1">Champion VIP</h3>
              <div class="mt-4 flex items-baseline space-x-1">
                <span class="text-4xl font-black font-display text-purple-400 price-value" data-monthly="$119" data-annual="$89">$119</span>
                <span class="text-xs text-black dark:text-slate-400">/ month</span>
              </div>
              <p class="text-xs text-black dark:text-slate-400 mt-2">Unlimited power user pass with zero hardware waiting.</p>
              <ul class="mt-6 space-y-3 text-xs font-semibold text-black dark:text-slate-200 border-t border-purple-800/40 pt-4">'''

    new = '''              <h3 class="text-2xl font-black font-display uppercase text-white mt-1">Champion VIP</h3>
              <div class="mt-4 flex items-baseline space-x-1">
                <span class="text-4xl font-black font-display text-purple-400 price-value" data-monthly="$119" data-annual="$89">$119</span>
                <span class="text-xs text-slate-300">/ month</span>
              </div>
              <p class="text-xs text-slate-300 mt-2">Unlimited power user pass with zero hardware waiting.</p>
              <ul class="mt-6 space-y-3 text-xs font-semibold text-slate-200 border-t border-purple-800/40 pt-4">'''

    if old in c:
        c = c.replace(old, new)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print("membership.html Tier 3 updated successfully!")
    else:
        print("Warning: old pattern not found in membership.html")

fix_membership()
