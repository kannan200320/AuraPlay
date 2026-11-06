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
  window.showAuraToast = function (message, type = 'success') {
    // Popups suppressed as requested
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
    initForms();
    initDashboardSidebar();
  });
})();
