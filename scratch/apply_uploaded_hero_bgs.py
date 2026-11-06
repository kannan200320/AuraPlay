import re

def update_membership():
    with open('membership.html', 'r', encoding='utf-8') as f:
        c = f.read()
    
    old_img = 'assets/images/tour-vip-console-lounge.jpg'
    new_img = 'assets/images/hero-bg-membership.png'
    
    if old_img in c:
        c = c.replace(old_img, new_img)
        # Update alt and opacity
        c = c.replace(
            'alt="AuraPlay VIP Member Lounge" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105"',
            'alt="AuraPlay VIP Memberships & Lounge Setup" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105"'
        )
        with open('membership.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated membership.html with hero-bg-membership.png!")
    else:
        print("Warning: old_img not found in membership.html")

def update_blog():
    with open('blog.html', 'r', encoding='utf-8') as f:
        c = f.read()

    old_img = 'assets/images/stage-main-broadcast-arena.jpg'
    new_img = 'assets/images/hero-bg-blog.png'

    if old_img in c:
        c = c.replace(old_img, new_img)
        # Update alt and opacity
        c = c.replace(
            'alt="AuraPlay Esports Engineering Hub" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105"',
            'alt="AuraPlay Esports Engineering & Hardware Lab" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105"'
        )
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated blog.html with hero-bg-blog.png!")
    else:
        print("Warning: old_img not found in blog.html")

def update_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # In contact.html, contact-noc-telemetry.png was in hero section
    old_target = '''        <img src="assets/images/contact-noc-telemetry.png" alt="AuraPlay Operations Center" class="w-full h-full object-cover object-center opacity-35 dark:opacity-45 filter dark:brightness-85 transform scale-105">'''
    new_target = '''        <img src="assets/images/hero-bg-contact.png" alt="AuraPlay 24/7 Welcome Desk & Support Center" class="w-full h-full object-cover object-center opacity-45 dark:opacity-55 filter dark:brightness-90 transform scale-105">'''

    if old_target in c:
        c = c.replace(old_target, new_target, 1)
        with open('contact.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated contact.html with hero-bg-contact.png!")
    else:
        print("Warning: old_target not found in contact.html")

update_membership()
update_blog()
update_contact()
