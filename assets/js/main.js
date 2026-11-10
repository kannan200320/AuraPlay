/**
 * AuraPlay - Gaming & PC Lounge
 * Core JavaScript: Theme Toggle, RTL/LTR Toggle, Mobile Navigation, Interactive UI
 */

(function () {
  'use strict';

  // --- Theme Management ---
  function initTheme() {
    const savedTheme = localStorage.getItem('color-theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
      document.documentElement.classList.add('dark');
      updateThemeIcons(true);
    } else {
      document.documentElement.classList.remove('dark');
      updateThemeIcons(false);
    }

    const themeToggleBtns = document.querySelectorAll('.theme-toggle-btn');
    themeToggleBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const isDark = document.documentElement.classList.toggle('dark');
        localStorage.setItem('color-theme', isDark ? 'dark' : 'light');
        updateThemeIcons(isDark);
      });
    });
  }

  function updateThemeIcons(isDark) {
    const sunIcons = document.querySelectorAll('.theme-sun-icon');
    const moonIcons = document.querySelectorAll('.theme-moon-icon');
    
    sunIcons.forEach(icon => {
      icon.style.display = isDark ? 'block' : 'none';
    });
    moonIcons.forEach(icon => {
      icon.style.display = isDark ? 'none' : 'block';
    });
  }

  // --- RTL / LTR Direction Management ---
  function initDirection() {
    const savedDir = localStorage.getItem('site-dir') || 'ltr';
    setDirection(savedDir);

    const rtlToggleBtns = document.querySelectorAll('.rtl-toggle-btn');
    rtlToggleBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const currentDir = document.documentElement.getAttribute('dir') || 'ltr';
        const newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
        setDirection(newDir);
        localStorage.setItem('site-dir', newDir);
      });
    });
  }

  function setDirection(dir) {
    document.documentElement.setAttribute('dir', dir);
    const rtlTexts = document.querySelectorAll('.rtl-status-text');
    rtlTexts.forEach(el => {
      el.textContent = dir === 'rtl' ? 'LTR' : 'RTL';
    });
    const rtlArrows = document.querySelectorAll('.rtl-arrow');
    rtlArrows.forEach(el => {
      el.textContent = dir === 'rtl' ? '→' : '←';
    });
  }

  // --- Mobile Navigation Drawer ---
    // --- Desktop Navigation Dropdown Freeze-on-Click ---
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

function initMobileMenu() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenuCloseBtn = document.getElementById('mobile-menu-close');
    const mobileMenuDrawer = document.getElementById('mobile-menu-drawer');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');

    if (!mobileMenuBtn || !mobileMenuDrawer) return;

    function openMobileMenu() {
      mobileMenuDrawer.classList.remove('translate-x-full', '-translate-x-full');
      if (mobileMenuOverlay) {
        mobileMenuOverlay.classList.remove('opacity-0', 'pointer-events-none');
        mobileMenuOverlay.classList.add('opacity-100', 'pointer-events-auto');
      }
      document.body.style.overflow = 'hidden';
      mobileMenuBtn.setAttribute('aria-expanded', 'true');
    }

    function closeMobileMenu() {
      const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
      if (isRtl) {
        mobileMenuDrawer.classList.add('-translate-x-full');
      } else {
        mobileMenuDrawer.classList.add('translate-x-full');
      }
      if (mobileMenuOverlay) {
        mobileMenuOverlay.classList.add('opacity-0', 'pointer-events-none');
        mobileMenuOverlay.classList.remove('opacity-100', 'pointer-events-auto');
      }
      document.body.style.overflow = '';
      mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }

    mobileMenuBtn.addEventListener('click', openMobileMenu);
    if (mobileMenuCloseBtn) {
      mobileMenuCloseBtn.addEventListener('click', closeMobileMenu);
    }
    if (mobileMenuOverlay) {
      mobileMenuOverlay.addEventListener('click', closeMobileMenu);
    }

    // Close on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !mobileMenuDrawer.classList.contains('translate-x-full') && !mobileMenuDrawer.classList.contains('-translate-x-full')) {
        closeMobileMenu();
      }
    });

    // Mobile Submenu accordions
    const accordionTriggers = document.querySelectorAll('.mobile-dropdown-btn');
    accordionTriggers.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-target');
        const targetMenu = document.getElementById(targetId);
        const arrow = btn.querySelector('.mobile-arrow');
        
        if (targetMenu) {
          const isOpen = !targetMenu.classList.contains('hidden');
          targetMenu.classList.toggle('hidden');
          if (arrow) {
            arrow.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
          }
        }
      });
    });
  }

  // --- Universal Toast System (Disabled per user requirement: No popups) ---
    // --- Custom Game Request Handler with Top-Right Popup Toast ---
  window.submitGameRequest = function () {
    const input = document.getElementById('custom-game-input');
    const toast = document.getElementById('game-request-toast');
    const inner = document.getElementById('game-toast-inner');
    const icon = document.getElementById('game-toast-icon');
    const title = document.getElementById('game-toast-title');
    const msg = document.getElementById('game-toast-msg');
    if (!input || !toast || !inner) return;

    const val = input.value.trim();

    // Check if game title is greater than 2 letters
    if (val.length <= 2) {
      inner.className = 'p-4 rounded-2xl shadow-2xl border-2 border-amber-500/80 bg-slate-900 text-white flex items-start space-x-3 rtl:space-x-reverse';
      icon.className = 'w-6 h-6 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center shrink-0 mt-0.5 text-xs font-bold';
      icon.innerHTML = '&#9888;';
      title.className = 'font-bold text-xs uppercase tracking-wider text-amber-400 mb-0.5';
      title.textContent = 'Invalid Game Title';
      msg.className = 'text-xs text-slate-200 leading-relaxed';
      msg.textContent = 'Please enter the correct game title (more than 2 characters).';

      toast.classList.remove('translate-x-[150%]');
      toast.classList.add('translate-x-0');

      if (window._gameToastTimeout) clearTimeout(window._gameToastTimeout);
      window._gameToastTimeout = setTimeout(window.dismissGameToast, 4000);
      input.focus();
    } else {
      inner.className = 'p-4 rounded-2xl shadow-2xl border-2 border-emerald-500/80 bg-slate-900 text-white flex items-start space-x-3 rtl:space-x-reverse';
      icon.className = 'w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 mt-0.5 text-xs font-bold';
      icon.innerHTML = '&#10003;';
      title.className = 'font-bold text-xs uppercase tracking-wider text-emerald-400 mb-0.5';
      title.textContent = 'Request Submitted!';
      msg.className = 'text-xs text-slate-200 leading-relaxed';
      msg.textContent = '"' + val + '" request received! Our NOC team will cache and preload the title within 4 hours.';

      toast.classList.remove('translate-x-[150%]');
      toast.classList.add('translate-x-0');

      if (window._gameToastTimeout) clearTimeout(window._gameToastTimeout);
      window._gameToastTimeout = setTimeout(window.dismissGameToast, 4000);
      input.value = '';
    }
  };

  window.dismissGameToast = function () {
    const toast = document.getElementById('game-request-toast');
    if (toast) {
      toast.classList.remove('translate-x-0');
      toast.classList.add('translate-x-[150%]');
    }
  };

  window.showAuraToast = function (message, type = 'success') {
    const isSuccess = (type === 'success' || type === 'info');
    const title = (type === 'info') ? 'AuraPlay Telemetry' : (isSuccess ? 'AuraPlay Confirmed' : 'System Notice');
    if (window.showAuraPopup) {
      window.showAuraPopup(title, message, isSuccess);
    }
  };

  // --- Universal Form Feedback Mock ---
  function initForms() {
    const forms = document.querySelectorAll('form[data-aura-form]');
    forms.forEach(form => {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const successMsg = form.getAttribute('data-success-msg') || 'Action completed successfully!';
        showAuraToast(successMsg, 'success');
        form.reset();
      });
    });
  }

  // --- Interactive Modals ---
  window.openAuraModal = function (modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  };

  window.closeAuraModal = function (modalId) {
    const modal = document.getElementById(modalId);
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
  };


  // --- Dashboard Sidebar Drawer & Background Scroll Lock ---
  function initDashboardSidebar() {
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
  }

  // --- Initialize when DOM is ready ---
  

  document.addEventListener('DOMContentLoaded', () => {
        initTheme();
    initDirection();
    initMobileMenu();
    initDesktopDropdowns();
    initForms();
    initDashboardSidebar();
  });
})();

// ========================================================
// FAQ ACCORDION DROPDOWN SYSTEM ACROSS ALL PAGES
// ========================================================
document.addEventListener('DOMContentLoaded', () => {
  const faqDetails = document.querySelectorAll('details.faq-item, section details');
  faqDetails.forEach(detail => {
    detail.classList.add('faq-item');
    const summary = detail.querySelector('summary');
    if (summary) {
      summary.addEventListener('click', (e) => {
        const isOpening = !detail.hasAttribute('open');
        if (isOpening) {
          // Close other open FAQ items in the same container for clean accordion dropdown
          const container = detail.closest('.space-y-4') || detail.parentElement;
          if (container) {
            container.querySelectorAll('details[open]').forEach(other => {
              if (other !== detail) {
                other.removeAttribute('open');
              }
            });
          }
        }
      });
    }
  });
});

// ========================================================
// UNIVERSAL TOP-RIGHT POPUP NOTIFICATION SYSTEM
// ========================================================
(function() {
  let auraToastTimeout = null;

  window.dismissAuraPopup = function() {
    const toast = document.getElementById('aura-universal-toast');
    if (toast) {
      toast.classList.remove('translate-x-0');
      toast.classList.add('translate-x-[150%]');
    }
    if (auraToastTimeout) {
      clearTimeout(auraToastTimeout);
      auraToastTimeout = null;
    }
  };

  window.showAuraPopup = function(title, message, isSuccess = false) {
    let toast = document.getElementById('aura-universal-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'aura-universal-toast';
      toast.className = 'fixed top-5 right-5 z-[99999] transform translate-x-[150%] transition-transform duration-300 ease-out max-w-sm pointer-events-auto';
      toast.innerHTML = `
        <div id="aura-toast-inner" class="p-4 rounded-2xl shadow-2xl border flex items-start space-x-3 rtl:space-x-reverse">
          <div id="aura-toast-icon" class="w-6 h-6 rounded-full flex items-center justify-center shrink-0 mt-0.5 text-xs font-black"></div>
          <div class="flex-1 text-left rtl:text-right">
            <div id="aura-toast-title" class="font-bold text-xs uppercase tracking-wider mb-0.5"></div>
            <div id="aura-toast-msg" class="text-xs leading-relaxed"></div>
          </div>
          <button type="button" onclick="window.dismissAuraPopup()" class="text-slate-400 hover:text-white p-1 focus:outline-none shrink-0" aria-label="Close notification">&#x2715;</button>
        </div>
      `;
      document.body.appendChild(toast);
    }

    const inner = document.getElementById('aura-toast-inner');
    const icon = document.getElementById('aura-toast-icon');
    const titleEl = document.getElementById('aura-toast-title');
    const msgEl = document.getElementById('aura-toast-msg');

    if (inner && icon && titleEl && msgEl) {
      if (isSuccess) {
        inner.className = 'p-4 rounded-2xl shadow-2xl border flex items-start space-x-3 rtl:space-x-reverse bg-slate-900/95 border-emerald-500/80 text-white backdrop-blur-md shadow-emerald-500/20';
        icon.className = 'w-6 h-6 rounded-full flex items-center justify-center shrink-0 mt-0.5 text-xs font-black bg-emerald-500 text-slate-950';
        icon.innerHTML = '&#x2713;';
        titleEl.className = 'font-bold text-xs uppercase tracking-wider mb-0.5 text-emerald-400';
      } else {
        inner.className = 'p-4 rounded-2xl shadow-2xl border flex items-start space-x-3 rtl:space-x-reverse bg-slate-900/95 border-red-500/80 text-white backdrop-blur-md shadow-red-500/20';
        icon.className = 'w-6 h-6 rounded-full flex items-center justify-center shrink-0 mt-0.5 text-xs font-black bg-red-500 text-white';
        icon.innerHTML = '&#x2715;';
        titleEl.className = 'font-bold text-xs uppercase tracking-wider mb-0.5 text-red-400';
      }

      titleEl.textContent = title;
      msgEl.className = 'text-xs text-slate-200 leading-relaxed';
      msgEl.textContent = message;

      toast.classList.remove('translate-x-[150%]');
      toast.classList.add('translate-x-0');

      if (auraToastTimeout) clearTimeout(auraToastTimeout);
      auraToastTimeout = setTimeout(() => {
        window.dismissAuraPopup();
      }, 4500);
    }
  };
})();


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
          const btnText = btn.innerText.trim().replace(/\s+/g, ' ');
          if (btnText && btnText.length > 0 && !btnText.includes('✕') && !btnText.includes('RTL')) {
            window.showAuraPopup('Action Confirmed', btnText + ' completed successfully.', true);
          }
        }
      }, 150);
    });
  });
});
