with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace in Section 4:
# 1. Section subtitle:
old_sub = '<span class="text-xs sm:text-sm font-extrabold uppercase tracking-widest text-purple-600 dark:text-purple-400">No Compromises</span>'
new_sub = '<span class="text-xs sm:text-sm font-extrabold uppercase tracking-widest text-cyan-600 dark:text-cyan-400">No Compromises</span>'
assert old_sub in content, "old_sub not found"
content = content.replace(old_sub, new_sub)

# 2. Tier 2:
content = content.replace(
    'hover:border-purple-500 transition-colors">\n            <div class="flex-1 flex flex-col">\n              <div class="text-xs font-bold uppercase tracking-wider text-purple-600 dark:text-purple-400">Tier 2: Esports Pro</div>',
    'hover:border-cyan-500 transition-colors">\n            <div class="flex-1 flex flex-col">\n              <div class="text-xs font-bold uppercase tracking-wider text-cyan-600 dark:text-cyan-400">Tier 2: Esports Pro</div>'
)
content = content.replace(
    '<a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-purple-600 hover:bg-purple-500">Book Pro</a>',
    '<a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-cyan-600 hover:bg-cyan-500">Book Pro</a>'
)

# 3. Tier 3:
content = content.replace(
    'hover:border-pink-500 transition-colors">\n            <div class="flex-1 flex flex-col">\n              <div class="text-xs font-bold uppercase tracking-wider text-pink-600 dark:text-pink-400">Tier 3: Sim Racing</div>',
    'hover:border-cyan-500 transition-colors">\n            <div class="flex-1 flex flex-col">\n              <div class="text-xs font-bold uppercase tracking-wider text-cyan-600 dark:text-cyan-400">Tier 3: Sim Racing</div>'
)
content = content.replace(
    '<a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-pink-600 hover:bg-pink-500">Book Sim</a>',
    '<a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-cyan-600 hover:bg-cyan-500">Book Sim</a>'
)

# 4. Tier 4:
content = content.replace(
    'hover:border-emerald-500 transition-colors">\n            <div class="flex-1 flex flex-col">\n              <div class="text-xs font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Tier 4: Console Pod</div>',
    'hover:border-cyan-500 transition-colors">\n            <div class="flex-1 flex flex-col">\n              <div class="text-xs font-bold uppercase tracking-wider text-cyan-600 dark:text-cyan-400">Tier 4: Console Pod</div>'
)
content = content.replace(
    '<a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-emerald-600 hover:bg-emerald-500">Book Console</a>',
    '<a href="book-slot.html" class="px-4 py-2 rounded-xl text-xs font-extrabold text-white bg-cyan-600 hover:bg-cyan-500">Book Console</a>'
)

# Replace all purple, pink, emerald checkmarks in section 4 with cyan checkmarks:
# We isolate Section 4 bounds:
sec4_start = content.find('<!-- ================= SECTION 4: HARDWARE RIG SPECIFICATIONS ================= -->')
sec5_start = content.find('<!-- ================= SECTION 5: FOUR GAMING CATEGORIES ================= -->')

sec4_content = content[sec4_start:sec5_start]
sec4_content = sec4_content.replace('text-purple-500 font-bold', 'text-cyan-500 font-bold')
sec4_content = sec4_content.replace('text-pink-500 font-bold', 'text-cyan-500 font-bold')
sec4_content = sec4_content.replace('text-emerald-500 font-bold', 'text-cyan-500 font-bold')

content = content[:sec4_start] + sec4_content + content[sec5_start:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated index.html Section 4!")
