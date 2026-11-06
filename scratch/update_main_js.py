with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    c = f.read()

old_open = """    function openSidebar() {
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
    }"""

new_open = """    function openSidebar() {
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
    }"""

c_norm = c.replace('\r\n', '\n')
if old_open in c_norm:
    c_norm = c_norm.replace(old_open, new_open, 1)
    with open('assets/js/main.js', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("Updated main.js successfully.")
else:
    print("Pattern not found in main.js.")
