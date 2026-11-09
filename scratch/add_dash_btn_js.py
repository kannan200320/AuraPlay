import sys
sys.stdout.reconfigure(encoding='utf-8')

main_js = open('assets/js/main.js', encoding='utf-8').read()

addon = """

// ========================================================
// DASHBOARD BUTTON NOTIFICATION ENHANCEMENT
// Ensures all buttons across dashboard pages trigger
// proper top-right popup toast notifications.
// ========================================================
document.addEventListener('DOMContentLoaded', () => {
  const isDashboardPage = window.location.pathname.includes('dashboard') || !!document.querySelector('.dash-nav-link');
  if (!isDashboardPage) return;

  const buttons = document.querySelectorAll('button:not(#theme-toggle):not(#rtl-toggle):not(#theme-toggle-drawer):not(#rtl-toggle-drawer):not(#sidebar-toggle-btn):not(#dashboard-sidebar-close):not([aria-label="Close notification"]):not([data-target])');
  
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      setTimeout(() => {
        const toast = document.getElementById('aura-universal-toast');
        const isShown = toast && toast.classList.contains('translate-x-0');
        if (!isShown && window.showAuraPopup) {
          const btnText = btn.innerText.trim().replace(/\\s+/g, ' ');
          if (btnText && btnText.length > 0 && !btnText.includes('✕') && !btnText.includes('RTL')) {
            window.showAuraPopup('Action Confirmed', btnText + ' completed successfully.', true);
          }
        }
      }, 150);
    });
  });
});
"""

if "DASHBOARD BUTTON NOTIFICATION ENHANCEMENT" not in main_js:
    open('assets/js/main.js', 'w', encoding='utf-8').write(main_js + addon)
    print("Added dashboard button enhancement to main.js")
else:
    print("Already added to main.js")
