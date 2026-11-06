with open('book-slot.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<div class="text-[10px] text-black dark:text-slate-400 mt-2">Valid for 3 Hours</div>',
              '<div class="text-[10px] text-slate-300 mt-2">Valid for 3 Hours</div>')
with open('book-slot.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c2 = f.read()
c2 = c2.replace('<span class="text-black dark:text-slate-400">|</span>\n                  <span>Zero Cable Tether</span>',
                '<span class="text-slate-400">|</span>\n                  <span>Zero Cable Tether</span>')
with open('player-lounge.html', 'w', encoding='utf-8') as f:
    f.write(c2)

print("Fixed book-slot.html and player-lounge.html minor dark container classes!")
