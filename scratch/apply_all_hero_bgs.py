import os

def update_membership():
    with open('membership.html', 'r', encoding='utf-8') as f:
        c = f.read()
    
    target = '''    <!-- SECTION 1: HERO & MEMBERSHIP BENEFITS -->
    <section class="py-16 lg:py-24 bg-slate-100/90 dark:bg-darkslate-deep/90 border-b border-slate-200 dark:border-darkslate-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-4xl mx-auto space-y-6">'''

    replacement = '''    <!-- SECTION 1: HERO & MEMBERSHIP BENEFITS -->
    <section class="py-16 lg:py-24 bg-slate-100 dark:bg-darkslate-deep border-b border-slate-200 dark:border-darkslate-border relative overflow-hidden">
      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/tour-vip-console-lounge.jpg" alt="AuraPlay VIP Member Lounge" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center max-w-4xl mx-auto space-y-6">'''

    if target in c:
        c = c.replace(target, replacement, 1)
        with open('membership.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated membership.html hero background!")
    else:
        print("Warning: target not found in membership.html")

def update_book_slot():
    with open('book-slot.html', 'r', encoding='utf-8') as f:
        c = f.read()

    target = '''    <!-- SECTION 1: HERO & REAL-TIME BOOKING ENGINE -->
    <section class="py-16 lg:py-20 bg-slate-100/90 dark:bg-darkslate-deep/90 border-b border-slate-200 dark:border-darkslate-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-4xl mx-auto space-y-6">'''

    replacement = '''    <!-- SECTION 1: HERO & REAL-TIME BOOKING ENGINE -->
    <section class="py-16 lg:py-20 bg-slate-100 dark:bg-darkslate-deep border-b border-slate-200 dark:border-darkslate-border relative overflow-hidden">
      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/tour-pc-arena-wide.jpg" alt="AuraPlay PC Arena Station Floor" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center max-w-4xl mx-auto space-y-6">'''

    if target in c:
        c = c.replace(target, replacement, 1)
        with open('book-slot.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated book-slot.html hero background!")
    else:
        print("Warning: target not found in book-slot.html")

def update_blog():
    with open('blog.html', 'r', encoding='utf-8') as f:
        c = f.read()

    target = '''    <!-- SECTION 1: HERO & EDITORIAL HUB -->
    <section class="py-16 lg:py-24 bg-slate-100/90 dark:bg-darkslate-deep/90 border-b border-slate-200 dark:border-darkslate-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-4xl mx-auto space-y-6">'''

    replacement = '''    <!-- SECTION 1: HERO & EDITORIAL HUB -->
    <section class="py-16 lg:py-24 bg-slate-100 dark:bg-darkslate-deep border-b border-slate-200 dark:border-darkslate-border relative overflow-hidden">
      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/stage-main-broadcast-arena.jpg" alt="AuraPlay Esports Engineering Hub" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center max-w-4xl mx-auto space-y-6">'''

    if target in c:
        c = c.replace(target, replacement, 1)
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated blog.html hero background!")
    else:
        print("Warning: target not found in blog.html")

def update_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        c = f.read()

    target = '''    <!-- SECTION 1: HERO & 24/7 HELPDESK OVERVIEW -->
    <section class="py-16 lg:py-24 bg-slate-100/90 dark:bg-darkslate-deep/90 border-b border-slate-200 dark:border-darkslate-border">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center max-w-4xl mx-auto space-y-6">'''

    replacement = '''    <!-- SECTION 1: HERO & 24/7 HELPDESK OVERVIEW -->
    <section class="py-16 lg:py-24 bg-slate-100 dark:bg-darkslate-deep border-b border-slate-200 dark:border-darkslate-border relative overflow-hidden">
      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/contact-noc-telemetry.png" alt="AuraPlay Operations Center" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-50/85 via-slate-50/75 to-slate-50/90 dark:from-darkslate-deep/88 dark:via-darkslate-deep/75 dark:to-darkslate-deep/90 backdrop-blur-[1px]"></div>
      </div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center max-w-4xl mx-auto space-y-6">'''

    if target in c:
        c = c.replace(target, replacement, 1)
        with open('contact.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated contact.html hero background!")
    else:
        print("Warning: target not found in contact.html")

def update_about_comment():
    with open('about.html', 'r', encoding='utf-8') as f:
        c = f.read()

    target = '<!-- ================= SECTION 1: ABOUT HERO (MODERN DIGITAL - NO HERO IMAGE) ================= -->'
    replacement = '<!-- ================= SECTION 1: ABOUT HERO (HARDWARE LAB) ================= -->'
    if target in c:
        c = c.replace(target, replacement, 1)
        with open('about.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated about.html Section 1 comment!")
    else:
        print("Warning: target comment not found in about.html")

update_membership()
update_book_slot()
update_blog()
update_contact()
update_about_comment()
