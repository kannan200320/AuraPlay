import re

# 1. Update index.html hero headline
with open('index.html', 'r', encoding='utf-8') as f:
    txt = f.read()
txt = txt.replace(
    'text-3xl sm:text-5xl lg:text-5xl xl:text-6xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline',
    'text-2xl xs:text-3xl sm:text-5xl lg:text-5xl xl:text-6xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline'
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated index.html responsive headline.")

# 2. Update player-lounge.html hero headline
with open('player-lounge.html', 'r', encoding='utf-8') as f:
    txt = f.read()
txt = txt.replace(
    'text-3xl sm:text-5xl lg:text-5xl xl:text-6xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline',
    'text-2xl xs:text-3xl sm:text-5xl lg:text-5xl xl:text-6xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline'
)
with open('player-lounge.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated player-lounge.html responsive headline.")

# 3. Update pricing.html grid progression for 1024px & 768px
with open('pricing.html', 'r', encoding='utf-8') as f:
    txt = f.read()
txt = txt.replace(
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 items-stretch',
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 items-stretch'
)
with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated pricing.html grid progression.")

# 4. Update book-slot.html floor map container padding for 320px
with open('book-slot.html', 'r', encoding='utf-8') as f:
    txt = f.read()
txt = txt.replace(
    'p-6 sm:p-8 rounded-3xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm',
    'p-3.5 sm:p-8 rounded-3xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border shadow-sm'
)
with open('book-slot.html', 'w', encoding='utf-8') as f:
    f.write(txt)
print("Updated book-slot.html floor map padding.")

# 5. Update dashboard files: header toggles and sidebar mobile settings
dash_files = [
    'dashboard.html',
    'dashboard-packs.html',
    'dashboard-history.html',
    'dashboard-payments.html',
    'dashboard-settings.html'
]

sidebar_settings_snippet = '''          <!-- Mobile Settings Controls inside Dashboard Sidebar -->
          <div class="mt-3 pt-3 border-t border-slate-200 dark:border-darkslate-border flex items-center justify-between sm:hidden">
            <span class="text-xs font-bold text-slate-700 dark:text-slate-300">Settings:</span>
            <div class="flex items-center space-x-2 rtl:space-x-reverse">
              <button type="button" class="theme-toggle-btn w-8 h-8 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center justify-center text-slate-800 dark:text-slate-200 hover:border-cyan-500 transition-colors shadow-sm" aria-label="Toggle dark mode">
                <svg class="theme-sun-icon w-4 h-4 text-amber-400 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/></svg>
                <svg class="theme-moon-icon w-4 h-4 text-slate-800 dark:text-slate-200" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
              </button>
              <button type="button" class="rtl-toggle-btn px-2.5 h-8 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center space-x-1 rtl:space-x-reverse text-xs font-bold text-slate-900 dark:text-white hover:border-cyan-500 transition-colors shadow-sm" title="Switch text direction">
                <span class="rtl-arrow text-xs">\u2190</span>
                <span class="rtl-status-text">RTL</span>
              </button>
            </div>
          </div>\n'''

for df in dash_files:
    with open(df, 'r', encoding='utf-8') as f:
        txt = f.read()
    
    # Hide header RTL and Theme toggles on small mobile (< sm)
    txt = re.sub(
        r'<button type="button" class="rtl-toggle-btn px-3 py-2 text-xs font-bold rounded-xl border border-slate-200 dark:border-darkslate-border bg-slate-100 dark:bg-darkslate-card text-black dark:text-slate-300 hover:border-cyan-500 hover:text-cyan-600 transition-all flex items-center space-x-1 rtl:space-x-reverse"',
        '<button type="button" class="rtl-toggle-btn hidden sm:inline-flex px-3 py-2 text-xs font-bold rounded-xl border border-slate-200 dark:border-darkslate-border bg-slate-100 dark:bg-darkslate-card text-black dark:text-slate-300 hover:border-cyan-500 hover:text-cyan-600 transition-all items-center space-x-1 rtl:space-x-reverse"',
        txt
    )
    txt = re.sub(
        r'<button type="button" class="theme-toggle-btn p-2 rounded-xl border border-slate-200 dark:border-darkslate-border bg-slate-100 dark:bg-darkslate-card text-black dark:text-slate-300 hover:border-purple-500 hover:text-purple-600 transition-all"',
        '<button type="button" class="theme-toggle-btn hidden sm:inline-flex p-2 rounded-xl border border-slate-200 dark:border-darkslate-border bg-slate-100 dark:bg-darkslate-card text-black dark:text-slate-300 hover:border-purple-500 hover:text-purple-600 transition-all"',
        txt
    )
    
    # Add settings controls inside sidebar if not already present
    if 'Mobile Settings Controls inside Dashboard Sidebar' not in txt:
        # insert right after user profile card closes (line with </a>\n        </div>\n      </div>)
        target = '</a>\n        </div>\n      </div>'
        if target in txt:
            txt = txt.replace(target, '</a>\n        </div>\n' + sidebar_settings_snippet + '      </div>', 1)
        else:
            # fallback
            target_simple = '</a>\n            </div>\n          </div>'
            if target_simple in txt:
                txt = txt.replace(target_simple, '</a>\n            </div>\n' + sidebar_settings_snippet + '          </div>', 1)

    with open(df, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f"Updated {df} responsive header and sidebar settings.")

print("All responsive layout refinements applied successfully!")
