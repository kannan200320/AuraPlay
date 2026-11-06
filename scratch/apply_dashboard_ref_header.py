import re

def build_dashboard_header_and_sidebar(active_page):
    is_overview = active_page == 'dashboard'
    is_slot = active_page == 'book-slot'
    is_packs = active_page == 'dashboard-packs'
    is_history = active_page == 'dashboard-history'
    is_payments = active_page == 'dashboard-payments'
    is_settings = active_page == 'dashboard-settings'

    def link_cls(active):
        if active:
            return "dash-nav-link flex items-center space-x-3 rtl:space-x-reverse px-3.5 py-2.5 rounded-xl bg-cyan-50 dark:bg-cyan-950/40 text-cyan-700 dark:text-cyan-300 font-bold transition-all shadow-sm"
        return "dash-nav-link flex items-center space-x-3 rtl:space-x-reverse px-3.5 py-2.5 rounded-xl text-black dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-darkslate-lighter transition-all"

    return f'''  <!-- Dashboard Sidebar Overlay (Active on Mobile Drawer only) -->
  <div id="dashboard-sidebar-overlay" class="fixed inset-0 bg-slate-950/70 backdrop-blur-sm z-40 opacity-0 pointer-events-none transition-opacity duration-300 lg:hidden"></div>

  <!-- ================= DASHBOARD SIDEBAR (DESKTOP DOCKED / MOBILE STICKY DRAWER) ================= -->
  <aside id="dashboard-sidebar" class="fixed inset-y-0 left-0 rtl:left-auto rtl:right-0 z-50 lg:z-30 w-72 max-w-[85vw] lg:w-64 h-full bg-white dark:bg-darkslate-card border-r rtl:border-r-0 rtl:border-l border-slate-200 dark:border-darkslate-border shadow-2xl lg:shadow-none transform -translate-x-full rtl:translate-x-full lg:translate-x-0 rtl:lg:translate-x-0 transition-transform duration-300 ease-in-out flex flex-col justify-between overflow-y-auto">
    <div>
      <!-- Drawer Top Bar: Brand Logo & Mobile Close Button -->
      <div class="h-16 sm:h-20 flex items-center justify-between px-6 border-b border-slate-200 dark:border-darkslate-border whitespace-nowrap">
        <a href="index.html" class="flex items-center space-x-3 rtl:space-x-reverse shrink-0 group whitespace-nowrap">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 via-purple-600 to-pink-500 flex items-center justify-center text-white shadow-md group-hover:scale-105 transition-transform shrink-0">
            <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M21 6H3c-1.1 0-2 .9-2 2v8c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-10 7H8v3H6v-3H3v-2h3V8h2v3h3v2zm4.5 2c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4-3c-.83 0-1.5-.67-1.5-1.5S18.67 9 19.5 9s1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
          </div>
          <span class="text-2xl font-black tracking-tight text-black dark:text-white font-display uppercase leading-none">
            Aura<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 to-purple-500">Play</span>
          </span>
        </a>
        <!-- Mobile close button (Hidden on Laptop) -->
        <button id="dashboard-sidebar-close" type="button" class="lg:hidden p-2 rounded-xl text-black dark:text-slate-400 hover:text-cyan-500 dark:hover:text-cyan-400 hover:bg-slate-100 dark:hover:bg-darkslate-deep transition-colors focus:outline-none" aria-label="Close dashboard menu">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Navigation Links -->
      <nav class="p-4 space-y-1.5 text-xs font-semibold whitespace-nowrap">
        <a href="dashboard.html" class="{link_cls(is_overview)}">
          <svg class="w-4 h-4 text-cyan-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
          <span>Dashboard Overview</span>
        </a>
        <a href="book-slot.html" class="{link_cls(is_slot)}">
          <svg class="w-4 h-4 text-purple-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          <span>Book Station Slot</span>
        </a>
        <a href="dashboard-packs.html" class="{link_cls(is_packs)}">
          <svg class="w-4 h-4 text-pink-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <span>Buy Hour Packs</span>
        </a>
        <a href="dashboard-history.html" class="{link_cls(is_history)}">
          <svg class="w-4 h-4 text-amber-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <span>Play History & Logs</span>
        </a>
        <a href="dashboard-payments.html" class="{link_cls(is_payments)}">
          <svg class="w-4 h-4 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/></svg>
          <span>Payments & Billing</span>
        </a>
        <a href="dashboard-settings.html" class="{link_cls(is_settings)}">
          <svg class="w-4 h-4 text-cyan-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          <span>Account & Settings</span>
        </a>
      </nav>
    </div>

    <!-- User Profile Card & Settings Controls in Sidebar -->
    <div class="p-4 border-t border-slate-200 dark:border-darkslate-border space-y-3">
      <div class="p-3 rounded-2xl bg-slate-50 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex items-center justify-between">
        <div class="flex items-center space-x-3 rtl:space-x-reverse">
          <img src="assets/images/avatar-5.jpg" alt="PhoenixAim" class="w-10 h-10 rounded-full object-cover shrink-0 shadow-md border border-cyan-500/30">
          <div>
            <div class="font-bold text-xs text-black dark:text-white">PhoenixAim</div>
            <div class="text-[10px] text-cyan-600 dark:text-cyan-400 font-bold">VIP Champion • Lv 28</div>
          </div>
        </div>
        <a href="login.html" class="p-1.5 rounded-lg text-black dark:text-slate-400 hover:text-rose-500 transition-colors" title="Log out">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
        </a>
      </div>

      <!-- Settings row in Sidebar (Mobile Only: In Lap View toggles are already in the top bar) -->
      <div class="pt-2 flex lg:hidden items-center justify-between border-t border-slate-200 dark:border-darkslate-border">
        <span class="text-xs font-bold text-slate-700 dark:text-slate-300">Settings:</span>
        <div class="flex items-center space-x-2 rtl:space-x-reverse">
          <button type="button" class="theme-toggle-btn w-9 h-9 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center justify-center text-slate-800 dark:text-slate-200 hover:border-cyan-500 transition-colors shadow-sm cursor-pointer" aria-label="Toggle dark mode">
            <svg class="theme-sun-icon w-4 h-4 text-amber-400 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/></svg>
            <svg class="theme-moon-icon w-4 h-4 text-slate-800 dark:text-slate-200" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
          </button>
          <button type="button" class="rtl-toggle-btn px-3 h-9 rounded-xl bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border flex items-center space-x-1 rtl:space-x-reverse text-xs font-bold text-slate-900 dark:text-white hover:border-cyan-500 transition-colors shadow-sm cursor-pointer" title="Switch text direction">
            <span class="rtl-arrow text-xs">←</span>
            <span class="rtl-status-text">RTL</span>
          </button>
        </div>
      </div>
    </div>
  </aside>

  <!-- ================= MAIN WRAPPER (DOCKED SIDEBAR OFFSET ON LAPTOP) ================= -->
  <div class="flex-1 lg:pl-64 rtl:lg:pl-0 rtl:lg:pr-64 flex flex-col min-h-screen w-full transition-all duration-300">

    <!-- ================= STICKY TOP HEADER ================= -->
    <header class="sticky top-0 z-40 w-full bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border-b border-slate-200 dark:border-darkslate-border shadow-sm transition-colors duration-300">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        <!-- MOBILE VIEW ONLY (EXACTLY MATCHING THE REFERENCE IMAGE media_1793949435352_b99113e6.png) -->
        <div class="flex lg:hidden items-center justify-between h-16 sm:h-20">
          
          <!-- Left: Rounded Hamburger Menu Button + Brand Logo -->
          <div class="flex items-center space-x-3 sm:space-x-4 rtl:space-x-reverse">
            <!-- Rounded Hamburger Toggle Button matching Reference Image -->
            <button id="sidebar-toggle-btn" type="button" class="w-10 h-10 sm:w-11 sm:h-11 rounded-2xl border border-slate-200 dark:border-darkslate-border bg-slate-50 dark:bg-darkslate-deep text-slate-800 dark:text-slate-200 hover:text-cyan-500 hover:border-cyan-500 transition-colors focus:outline-none shadow-sm flex items-center justify-center cursor-pointer" aria-label="Toggle Dashboard Menu" aria-expanded="false">
              <svg class="w-5 h-5 sm:w-6 sm:h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
              </svg>
            </button>

            <!-- Brand Logo matching Reference Layout with Circular Icon & AuraPlay Brand -->
            <a href="index.html" class="flex items-center space-x-2.5 rtl:space-x-reverse group shrink-0">
              <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-gradient-to-tr from-cyan-500 via-purple-600 to-pink-500 flex items-center justify-center text-white shadow-md group-hover:scale-105 transition-transform shrink-0">
                <svg class="w-5 h-5 sm:w-6 sm:h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M21 6H3c-1.1 0-2 .9-2 2v8c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-10 7H8v3H6v-3H3v-2h3V8h2v3h3v2zm4.5 2c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4-3c-.83 0-1.5-.67-1.5-1.5S18.67 9 19.5 9s1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/>
                </svg>
              </div>
              <span class="text-xl sm:text-2xl font-black font-display uppercase tracking-tight text-black dark:text-white leading-none">
                Aura<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 to-purple-500">Play</span>
              </span>
            </a>
          </div>

          <!-- Right: Circular Profile Avatar (Matching Reference Image Position & AuraPlay Theme) -->
          <div class="flex items-center space-x-3 rtl:space-x-reverse">
            <a href="dashboard-settings.html" class="group flex items-center focus:outline-none" title="Gamer Profile & Settings">
              <img src="assets/images/avatar-5.jpg" alt="PhoenixAim Profile" class="w-10 h-10 sm:w-11 sm:h-11 rounded-full object-cover ring-2 ring-cyan-500/40 group-hover:ring-cyan-400 shadow-md transition-all">
            </a>
          </div>

        </div>

        <!-- LAPTOP / DESKTOP VIEW ONLY (FULL DESKTOP TELEMETRY NAVBAR) -->
        <div class="hidden lg:flex items-center justify-between h-20 whitespace-nowrap">
          
          <!-- Live Status Telemetry Ticker -->
          <div class="flex items-center space-x-3 rtl:space-x-reverse text-xs font-bold whitespace-nowrap">
            <span class="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>Arena Online: 10Gbps Fiber</span>
            </span>
            <span class="text-slate-400 dark:text-slate-500">•</span>
            <span class="text-slate-600 dark:text-slate-400">Ping: <strong class="text-cyan-600 dark:text-cyan-400">3.2ms</strong></span>
            <span class="text-slate-400 dark:text-slate-500">•</span>
            <span class="text-slate-600 dark:text-slate-400">Open Rigs: <strong class="text-purple-600 dark:text-purple-400">18 / 70</strong></span>
          </div>

          <!-- Desktop Top Actions -->
          <div class="flex items-center space-x-3 rtl:space-x-reverse whitespace-nowrap shrink-0">
            <!-- Banked Hours Display -->
            <div class="flex items-center space-x-2 rtl:space-x-reverse px-3.5 py-1.5 rounded-xl bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800/50 text-xs font-bold text-purple-700 dark:text-purple-300">
              <span>⏱ Banked:</span>
              <span class="font-mono text-black dark:text-white">14h 25m</span>
            </div>

            <!-- Top-Up CTA -->
            <a href="dashboard-packs.html" class="px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white font-extrabold text-xs uppercase tracking-wider shadow-md transition-all">
              + Top-Up Hours
            </a>

            <!-- LTR / RTL Toggle -->
            <button type="button" class="rtl-toggle-btn px-3 py-2 text-xs font-bold rounded-xl border border-slate-200 dark:border-darkslate-border bg-slate-100 dark:bg-darkslate-card text-black dark:text-slate-300 hover:border-cyan-500 hover:text-cyan-600 transition-all items-center space-x-1 rtl:space-x-reverse cursor-pointer" title="Switch text direction">
              <span class="rtl-arrow text-xs">←</span>
              <span class="rtl-status-text">RTL</span>
            </button>

            <!-- Dark / Light Mode Toggle -->
            <button type="button" class="theme-toggle-btn p-2 rounded-xl border border-slate-200 dark:border-darkslate-border bg-slate-100 dark:bg-darkslate-card text-black dark:text-slate-300 hover:border-purple-500 hover:text-purple-600 transition-all cursor-pointer" aria-label="Toggle dark/light mode">
              <svg class="theme-sun-icon w-5 h-5 text-amber-400 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/></svg>
              <svg class="theme-moon-icon w-5 h-5 text-black dark:text-slate-300" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
            </button>

            <!-- Circular Profile Avatar on Desktop -->
            <a href="dashboard-settings.html" class="group flex items-center focus:outline-none" title="Gamer Profile & Settings">
              <img src="assets/images/avatar-5.jpg" alt="PhoenixAim Profile" class="w-10 h-10 rounded-full object-cover ring-2 ring-cyan-500/40 group-hover:ring-cyan-400 shadow-md transition-all">
            </a>
          </div>

        </div>

      </div>
    </header>
'''

pages = [
    ('dashboard.html', 'dashboard'),
    ('dashboard-packs.html', 'dashboard-packs'),
    ('dashboard-history.html', 'dashboard-history'),
    ('dashboard-payments.html', 'dashboard-payments'),
    ('dashboard-settings.html', 'dashboard-settings')
]

for filename, active_page in pages:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    body_idx = content.find('<body')
    body_close_bracket = content.find('>', body_idx)
    header_end_idx = content.find('</header>') + len('</header>')

    if body_idx == -1 or header_end_idx == -1:
        print(f"Error finding boundaries in {filename}")
        continue

    prefix = content[:body_close_bracket+1] + '\n\n'
    suffix = content[header_end_idx:]

    new_header_and_sidebar = build_dashboard_header_and_sidebar(active_page)
    new_content = prefix + new_header_and_sidebar + suffix

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")
