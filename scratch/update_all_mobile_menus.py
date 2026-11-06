import re

def build_drawer_html(page_key):
    # Active item checks
    is_home_active = page_key in ['index', 'player-lounge']
    is_neon_active = page_key == 'index'
    is_lounge_active = page_key == 'player-lounge'
    
    is_about_active = page_key == 'about'
    is_games_active = page_key == 'games'
    is_pricing_active = page_key == 'pricing'
    
    is_explore_active = page_key in ['book-slot', 'membership']
    is_book_active = page_key == 'book-slot'
    is_member_active = page_key == 'membership'
    
    is_blog_active = page_key in ['blog', 'blog-detail']
    is_contact_active = page_key == 'contact'
    is_dash_active = page_key == 'dashboard'

    def item_cls(active):
        if active:
            return "block p-3 rounded-xl text-base font-bold bg-cyan-50 dark:bg-cyan-950/70 border border-cyan-500/20 text-cyan-600 dark:text-cyan-400"
        return "block p-3 rounded-xl text-base font-bold text-black dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-darkslate-card transition-colors"

    def sub_cls(active):
        if active:
            return "block p-2.5 rounded-lg text-sm font-semibold bg-cyan-50 dark:bg-cyan-950/70 border border-cyan-500/20 text-cyan-600 dark:text-cyan-400"
        return "block p-2.5 rounded-lg text-sm font-semibold text-black dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-darkslate-card transition-colors"

    home_sub_hidden = "hidden" if not is_home_active else ""
    explore_sub_hidden = "hidden" if not is_explore_active else ""

    return f'''  <!-- ================= MOBILE MENU DRAWER ================= -->
  <div id="mobile-menu-overlay" class="fixed inset-0 bg-slate-950/70 backdrop-blur-sm z-50 opacity-0 pointer-events-none transition-opacity duration-300"></div>

  <div id="mobile-menu-drawer" class="fixed top-0 right-0 rtl:right-auto rtl:left-0 z-50 w-80 max-w-[85vw] h-full bg-white dark:bg-darkslate-card border-l rtl:border-l-0 rtl:border-r border-slate-200 dark:border-darkslate-border shadow-2xl transform translate-x-full rtl:-translate-x-full transition-transform duration-300 ease-in-out flex flex-col justify-between overflow-y-auto">
    <div>
      <!-- Drawer Top Bar: Brand Logo & Close Icon -->
      <div class="p-6 border-b border-slate-200 dark:border-darkslate-border flex items-center justify-between">
        <a href="index.html" class="flex items-center space-x-2.5 rtl:space-x-reverse">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-cyan-500 via-purple-600 to-pink-500 flex items-center justify-center text-white shadow-md">
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24"><path d="M21 6H3c-1.1 0-2 .9-2 2v8c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-10 7H8v3H6v-3H3v-2h3V8h2v3h3v2zm4.5 2c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm4-3c-.83 0-1.5-.67-1.5-1.5S18.67 9 19.5 9s1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>
          </div>
          <span class="text-xl font-black font-display uppercase tracking-tight text-black dark:text-white">Aura<span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-500 to-purple-500">Play</span></span>
        </a>
        <button id="mobile-menu-close" type="button" class="p-2 rounded-xl text-black dark:text-slate-400 hover:text-cyan-500 dark:hover:text-cyan-400 hover:bg-slate-100 dark:hover:bg-darkslate-deep transition-colors focus:outline-none" aria-label="Close mobile menu">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>

      <!-- Navigation Links (Matching Image 4) -->
      <nav class="p-5 space-y-1.5 font-bold">
        <!-- 1. Home Dropdown -->
        <div>
          <button type="button" class="mobile-dropdown-btn w-full flex items-center justify-between p-3 rounded-xl text-base font-bold text-black dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-darkslate-card transition-colors" data-target="mobile-sub-home">
            <span>Home</span>
            <svg class="mobile-arrow w-4 h-4 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div id="mobile-sub-home" class="{home_sub_hidden} pl-4 rtl:pl-0 rtl:pr-4 py-1 space-y-1">
            <a href="index.html" class="{sub_cls(is_neon_active)}">Neon Arena</a>
            <a href="player-lounge.html" class="{sub_cls(is_lounge_active)}">Player's Lounge</a>
          </div>
        </div>

        <!-- 2. About Us -->
        <a href="about.html" class="{item_cls(is_about_active)}">About Us</a>

        <!-- 3. Games -->
        <a href="games.html" class="{item_cls(is_games_active)}">Games</a>

        <!-- 4. Pricing -->
        <a href="pricing.html" class="{item_cls(is_pricing_active)}">Pricing</a>

        <!-- 5. Explore Dropdown -->
        <div>
          <button type="button" class="mobile-dropdown-btn w-full flex items-center justify-between p-3 rounded-xl text-base font-bold text-black dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-darkslate-card transition-colors" data-target="mobile-sub-explore">
            <span>Explore</span>
            <svg class="mobile-arrow w-4 h-4 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div id="mobile-sub-explore" class="{explore_sub_hidden} pl-4 rtl:pl-0 rtl:pr-4 py-1 space-y-1">
            <a href="book-slot.html" class="{sub_cls(is_book_active)}">Book Slot Page</a>
            <a href="membership.html" class="{sub_cls(is_member_active)}">Membership Passes</a>
          </div>
        </div>

        <!-- 6. Blog -->
        <a href="blog.html" class="{item_cls(is_blog_active)}">Blog</a>

        <!-- 7. Contact Us -->
        <a href="contact.html" class="{item_cls(is_contact_active)}">Contact Us</a>

        <!-- 8. Dashboard -->
        <a href="dashboard.html" class="{item_cls(is_dash_active)}">Dashboard</a>
      </nav>
    </div>

    <!-- Drawer Footer: Sign In / Register & Settings Controls (Matching Image 4 & Image 5) -->
    <div class="p-6 border-t border-slate-200 dark:border-darkslate-border space-y-4">
      <a href="login.html" class="w-full flex items-center justify-center py-3.5 rounded-2xl text-base font-extrabold text-white bg-gradient-to-r from-cyan-500 via-purple-600 to-pink-500 hover:from-cyan-400 hover:to-purple-500 shadow-lg shadow-cyan-500/20 transition-all text-center">
        Sign In / Register
      </a>

      <!-- Settings row directly below Sign In button (Image 5) -->
      <div class="pt-2 flex items-center justify-between">
        <span class="text-sm font-bold text-slate-900 dark:text-white">Settings:</span>
        <div class="flex items-center space-x-2.5 rtl:space-x-reverse">
          <!-- Theme toggle button matching Image 5 -->
          <button type="button" class="theme-toggle-btn w-10 h-10 rounded-2xl bg-slate-100 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex items-center justify-center text-slate-800 dark:text-slate-200 hover:border-cyan-500 transition-colors shadow-sm" aria-label="Toggle dark mode">
            <svg class="theme-sun-icon w-5 h-5 text-amber-400 hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/></svg>
            <svg class="theme-moon-icon w-5 h-5 text-slate-800 dark:text-slate-200" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
          </button>
          <!-- RTL toggle button matching Image 5 -->
          <button type="button" class="rtl-toggle-btn px-4 h-10 rounded-2xl bg-slate-100 dark:bg-darkslate-deep border border-slate-200 dark:border-darkslate-border flex items-center space-x-1.5 rtl:space-x-reverse text-sm font-bold text-slate-900 dark:text-white hover:border-cyan-500 transition-colors shadow-sm" title="Switch text direction">
            <span class="rtl-arrow text-sm">\u2190</span>
            <span class="rtl-status-text">RTL</span>
          </button>
        </div>
      </div>
    </div>
  </div>\n\n'''

print("Drawer generator defined.")
