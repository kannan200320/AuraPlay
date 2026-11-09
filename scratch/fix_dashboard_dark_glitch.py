import sys
sys.stdout.reconfigure(encoding='utf-8')

THEME_SCRIPT = """  <!-- Theme Init Script (Prevent Flash of Incorrect Theme) -->
  <script>
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
    const savedDir = localStorage.getItem('site-dir') || 'ltr';
    document.documentElement.setAttribute('dir', savedDir);
  </script>

"""

files_to_fix = [
    "dashboard-history.html",
    "dashboard-payments.html",
    "dashboard-settings.html"
]

for f in files_to_fix:
    content = open(f, encoding="utf-8").read()
    # Normalize html tag
    content = content.replace('<html lang="en" dir="ltr" class="dark">', '<html lang="en" class="dark" dir="ltr">')
    
    # Check if script already exists
    if "localStorage.getItem('color-theme')" not in content[:1500]:
        target = "<!-- Tailwind CSS CDN -->"
        if target in content:
            content = content.replace(target, THEME_SCRIPT + target)
            open(f, "w", encoding="utf-8").write(content)
            print(f"Fixed theme script in {f}")
        else:
            print(f"Warning: target not found in {f}")
    else:
        print(f"Script already present in {f}")

