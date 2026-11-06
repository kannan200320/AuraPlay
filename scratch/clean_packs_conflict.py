with open('dashboard-packs.html', 'r', encoding='utf-8') as f:
    c = f.read()

bad_block = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const toggle = document.getElementById('sidebar-toggle-btn');
      const sidebar = document.getElementById('dashboard-sidebar');
      if (toggle && sidebar) {
        toggle.addEventListener('click', () => {
          sidebar.classList.toggle('hidden');
          sidebar.classList.toggle('flex');
        });
      }
    });
  </script>"""

if bad_block in c:
    c = c.replace(bad_block, '')
    with open('dashboard-packs.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Successfully removed conflicting script from dashboard-packs.html")
else:
    # Try normalizing line breaks
    c_norm = c.replace('\r\n', '\n')
    bad_norm = bad_block.replace('\r\n', '\n')
    if bad_norm in c_norm:
        c_norm = c_norm.replace(bad_norm, '')
        with open('dashboard-packs.html', 'w', encoding='utf-8') as f:
            f.write(c_norm)
        print("Successfully removed (normalized) from dashboard-packs.html")
    else:
        print("Pattern not found in dashboard-packs.html")
