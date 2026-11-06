with open('dashboard-history.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('bg-amber-500 text-slate-950 font-bold hover:bg-amber-400', 'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white font-bold')
with open('dashboard-history.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('dashboard.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

c2 = c2.replace('bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-300', 'bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 text-white')
with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(c2)

print("Updated dashboard-history and dashboard.")
