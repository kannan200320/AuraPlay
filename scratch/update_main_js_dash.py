with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js_txt = f.read()

dashboard_sidebar_js = '''
  // --- Dashboard Sidebar Drawer & Background Scroll Lock ---
  function initDashboardSidebar() {
    const toggleBtn = document.getElementById('sidebar-toggle-btn');
    const closeBtn = document.getElementById('dashboard-sidebar-close');
    const sidebar = document.getElementById('dashboard-sidebar');
    const overlay = document.getElementById('dashboard-sidebar-overlay');

    if (!toggleBtn || !sidebar) return;

    function openSidebar() {
      const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
      sidebar.classList.remove('-translate-x-full', 'translate-x-full');
      if (overlay) {
        overlay.classList.remove('opacity-0', 'pointer-events-none');
        overlay.classList.add('opacity-100', 'pointer-events-auto');
      }
      document.body.style.overflow = 'hidden';
      toggleBtn.setAttribute('aria-expanded', 'true');
    }

    function closeSidebar() {
      const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
      if (isRtl) {
        sidebar.classList.add('translate-x-full');
      } else {
        sidebar.classList.add('-translate-x-full');
      }
      if (overlay) {
        overlay.classList.add('opacity-0', 'pointer-events-none');
        overlay.classList.remove('opacity-100', 'pointer-events-auto');
      }
      document.body.style.overflow = '';
      toggleBtn.setAttribute('aria-expanded', 'false');
    }

    toggleBtn.addEventListener('click', openSidebar);
    if (closeBtn) closeBtn.addEventListener('click', closeSidebar);
    if (overlay) overlay.addEventListener('click', closeSidebar);

    // Close on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !sidebar.classList.contains('-translate-x-full') && !sidebar.classList.contains('translate-x-full')) {
        closeSidebar();
      }
    });
  }
'''

# Add dashboard_sidebar_js before "  // --- Initialize when DOM is ready ---"
marker = "  // --- Initialize when DOM is ready ---"
assert marker in js_txt, "marker not found in main.js"

js_txt = js_txt.replace(marker, dashboard_sidebar_js + "\n" + marker)

# Add initDashboardSidebar(); to DOMContentLoaded
old_init = '''    initTheme();
    initDirection();
    initMobileMenu();
    initForms();'''

new_init = '''    initTheme();
    initDirection();
    initMobileMenu();
    initForms();
    initDashboardSidebar();'''

assert old_init in js_txt, "old_init not found in main.js"
js_txt = js_txt.replace(old_init, new_init)

with open('assets/js/main.js', 'w', encoding='utf-8') as f:
    f.write(js_txt)

print("main.js updated with initDashboardSidebar()!")
