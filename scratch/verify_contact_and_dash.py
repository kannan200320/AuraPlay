with open('contact.html', 'r', encoding='utf-8') as f:
    c_txt = f.read()

import re
venue = re.search(r'<!-- SECTION 6: LAN PARTY & PRIVATE BOOTCAMP VENUE HIRE -->.*?</section>', c_txt, re.DOTALL)
if venue:
    print("contact.html Section 6 check:")
    print("Has min-h-[64px]:", 'min-h-[64px]' in venue.group(0))
    print("Has flex flex-col justify-between h-full:", 'flex flex-col justify-between h-full' in venue.group(0))

with open('dashboard-settings.html', 'r', encoding='utf-8') as f:
    d_txt = f.read()

print("\ndashboard-settings.html check:")
print("Has 'Remote Station Sign-Out':", 'Remote Station Sign-Out' in d_txt)
print("Has 'Emergency Remote Logout':", 'Emergency Remote Logout' in d_txt)
print("Has 'Emergency Flush':", 'Emergency Flush' in d_txt)
