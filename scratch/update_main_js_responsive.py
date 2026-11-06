with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    c = f.read()

target = """  function initDashboardSidebar() {
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
      document.documentElement.style.overflow = 'hidden';
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
      document.documentElement.style.overflow = '';
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
  }"""

replacement = """  function initDashboardSidebar() {
    const toggleBtn = document.getElementById('sidebar-toggle-btn');
    const closeBtn = document.getElementById('dashboard-sidebar-close');
    const sidebar = document.getElementById('dashboard-sidebar');
    const overlay = document.getElementById('dashboard-sidebar-overlay');

    if (!toggleBtn || !sidebar) return;

    function openSidebar() {
      // Mobile only drawer action (< 1024px)
      if (window.innerWidth >= 1024) return;
      const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
      sidebar.classList.remove('-translate-x-full', 'translate-x-full');
      if (overlay) {
        overlay.classList.remove('opacity-0', 'pointer-events-none');
        overlay.classList.add('opacity-100', 'pointer-events-auto');
      }
      document.body.style.overflow = 'hidden';
      document.documentElement.style.overflow = 'hidden';
      toggleBtn.setAttribute('aria-expanded', 'true');
    }

    function closeSidebar() {
      if (window.innerWidth < 1024) {
        const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
        if (isRtl) {
          sidebar.classList.add('translate-x-full');
        } else {
          sidebar.classList.add('-translate-x-full');
        }
      }
      if (overlay) {
        overlay.classList.add('opacity-0', 'pointer-events-none');
        overlay.classList.remove('opacity-100', 'pointer-events-auto');
      }
      document.body.style.overflow = '';
      document.documentElement.style.overflow = '';
      toggleBtn.setAttribute('aria-expanded', 'false');
    }

    toggleBtn.addEventListener('click', openSidebar);
    if (closeBtn) closeBtn.addEventListener('click', closeSidebar);
    if (overlay) overlay.addEventListener('click', closeSidebar);

    // Close on escape key on mobile
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && window.innerWidth < 1024 && !sidebar.classList.contains('-translate-x-full') && !sidebar.classList.contains('translate-x-full')) {
        closeSidebar();
      }
    });

    // Close on mobile nav link click
    const mobileLinks = sidebar.querySelectorAll('.dash-nav-link');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth < 1024) {
          closeSidebar();
        }
      });
    });

    // Reset when resizing between mobile and desktop/laptop
    window.addEventListener('resize', () => {
      if (window.innerWidth >= 1024) {
        document.body.style.overflow = '';
        document.documentElement.style.overflow = '';
        if (overlay) {
          overlay.classList.add('opacity-0', 'pointer-events-none');
          overlay.classList.remove('opacity-100', 'pointer-events-auto');
        }
        sidebar.classList.remove('-translate-x-full', 'translate-x-full');
      } else {
        if (!overlay || overlay.classList.contains('pointer-events-none')) {
          const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
          if (isRtl) {
            sidebar.classList.add('translate-x-full');
          } else {
            sidebar.classList.add('-translate-x-full');
          }
        }
      }
    });
  }"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')

if target_norm in c_norm:
    c_norm = c_norm.replace(target_norm, replacement)
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("Updated main.js with responsive dashboard sidebar behavior.")
else:
    print("Could not match target in main.js")
