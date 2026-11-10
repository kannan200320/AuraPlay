import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Update style.css
css = open('assets/css/style.css', encoding='utf-8').read()

css_addition = """

/* ========================================================
   DESKTOP DROPDOWN FREEZE-ON-CLICK & HOVER BRIDGE
   ======================================================== */
.relative.group.is-frozen > div[class*="absolute"],
.relative.group.is-open > div[class*="absolute"] {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
}

.relative.group.is-frozen .dropdown-toggle svg,
.relative.group.is-open .dropdown-toggle svg {
  transform: rotate(180deg) !important;
}

/* Invisible bridge across the mt-2 gap */
.relative.group > div[class*="absolute"]::before {
  content: "";
  position: absolute;
  top: -14px;
  left: 0;
  right: 0;
  height: 16px;
}
"""

if "DESKTOP DROPDOWN FREEZE-ON-CLICK" not in css:
    css += css_addition
    open('assets/css/style.css', 'w', encoding='utf-8').write(css)
    print("Added dropdown CSS to style.css")
else:
    print("Dropdown CSS already in style.css")

# 2. Update main.js
main_js = open('assets/js/main.js', encoding='utf-8').read()

js_func = """  // --- Desktop Navigation Dropdown Freeze-on-Click ---
  function initDesktopDropdowns() {
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(toggle => {
      const container = toggle.closest('.relative.group') || toggle.parentElement;
      if (!container) return;

      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const isCurrentlyOpen = container.classList.contains('is-frozen');

        // Close all other dropdowns
        document.querySelectorAll('.relative.group.is-frozen').forEach(other => {
          if (other !== container) {
            other.classList.remove('is-frozen', 'is-open');
          }
        });

        // Toggle freeze state on this dropdown
        if (isCurrentlyOpen) {
          container.classList.remove('is-frozen', 'is-open');
        } else {
          container.classList.add('is-frozen', 'is-open');
        }
      });
    });

    // Close frozen dropdown on click outside
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.relative.group')) {
        document.querySelectorAll('.relative.group.is-frozen').forEach(el => {
          el.classList.remove('is-frozen', 'is-open');
        });
      }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        document.querySelectorAll('.relative.group.is-frozen').forEach(el => {
          el.classList.remove('is-frozen', 'is-open');
        });
      }
    });
  }

"""

target_dom = "initMobileMenu();"
replacement_dom = "initMobileMenu();\n    initDesktopDropdowns();"

if "initDesktopDropdowns" not in main_js:
    # insert before initMobileMenu definition
    idx = main_js.find('function initMobileMenu()')
    assert idx != -1, "initMobileMenu not found in main.js"
    main_js = main_js[:idx] + js_func + main_js[idx:]
    
    # insert call inside DOMContentLoaded
    main_js = main_js.replace(target_dom, replacement_dom, 1)
    
    open('assets/js/main.js', 'w', encoding='utf-8').write(main_js)
    print("Added initDesktopDropdowns to main.js")
else:
    print("initDesktopDropdowns already in main.js")
