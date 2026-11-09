import glob

files = [
    "about.html",
    "blog.html",
    "book-slot.html",
    "contact.html",
    "games.html",
    "index.html",
    "membership.html",
    "player-lounge.html",
    "pricing.html",
    "blog-detail.html",
    "blog-detail-cs2-subtick.html",
    "blog-detail-direct-drive-sim.html",
    "blog-detail-wooting-rapid-trigger.html",
    "blog-detail-zero-bufferbloat.html"
]

target = '<a href="login.html" class="hidden sm:inline-flex items-center px-5 py-2.5 rounded-xl text-sm font-extrabold text-white bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 shadow-lg shadow-cyan-500/20 transition-all shrink-0">'
replacement = '<a href="login.html" class="hidden xl:inline-flex items-center px-5 py-2.5 rounded-xl text-sm font-extrabold text-white bg-gradient-to-r from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500 shadow-lg shadow-cyan-500/20 transition-all shrink-0">'

for f in files:
    content = open(f, encoding="utf-8").read()
    if target in content:
        content = content.replace(target, replacement)
        open(f, "w", encoding="utf-8").write(content)
        print(f"Updated header signin in {f}")
    else:
        print(f"Target not found in {f}")
