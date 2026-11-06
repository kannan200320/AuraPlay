with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    c = f.read()

target = """/* ========================================================
   DARK CONTAINER TEXT SHIELD (BOTH LIGHT & DARK MODES)
   Ensures sections with dark backgrounds, photo overlays,
   or dark gradients ALWAYS have bright white/light text.
   ======================================================== */
.cyber-grid,
.bg-slate-900,
.bg-slate-950,
[class*="from-cyan-950"],
[class*="from-purple-950"],
[class*="from-slate-950"],
[class*="via-slate-900"],
[class*="bg-gradient-to-t from-slate-950"],
[class*="bg-gradient-to-r from-cyan-950"],
[class*="bg-gradient-to-r from-purple-950"],
[class*="bg-gradient-to-br from-cyan-950"] {
  color: #ffffff;
}

/* Headings inside dark sections */
.cyber-grid h1, .cyber-grid h2, .cyber-grid h3, .cyber-grid h4,
.bg-slate-900 h1, .bg-slate-900 h2, .bg-slate-900 h3, .bg-slate-900 h4,
.bg-slate-950 h1, .bg-slate-950 h2, .bg-slate-950 h3, .bg-slate-950 h4,
[class*="from-cyan-950"] h1:not([class*="text-transparent"]), 
[class*="from-cyan-950"] h2:not([class*="text-transparent"]), 
[class*="from-cyan-950"] h3:not([class*="text-transparent"]),
[class*="from-purple-950"] h1:not([class*="text-transparent"]), 
[class*="from-purple-950"] h2:not([class*="text-transparent"]), 
[class*="from-purple-950"] h3:not([class*="text-transparent"]),
[class*="from-slate-950"] h1:not([class*="text-transparent"]), 
[class*="from-slate-950"] h2:not([class*="text-transparent"]), 
[class*="from-slate-950"] h3:not([class*="text-transparent"]),
[class*="bg-gradient-to-t from-slate-950"] h1, 
[class*="bg-gradient-to-t from-slate-950"] h2, 
[class*="bg-gradient-to-t from-slate-950"] h3 {
  color: #ffffff !important;
}

/* Body copy & descriptions inside dark sections */
.cyber-grid p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
.bg-slate-900 p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
.bg-slate-950 p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="from-cyan-950"] p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="from-purple-950"] p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="from-slate-950"] p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="bg-gradient-to-t from-slate-950"] p {
  color: #cbd5e1 !important;
}"""

replacement = """/* ========================================================
   DARK CONTAINER TEXT SHIELD (BOTH LIGHT & DARK MODES)
   Ensures sections with dark backgrounds, photo overlays,
   or dark gradients ALWAYS have bright white/light text.
   ======================================================== */
.bg-slate-900,
.bg-slate-950,
[class*="from-cyan-950"],
[class*="from-purple-950"],
[class*="from-slate-950"],
[class*="via-slate-900"],
[class*="bg-gradient-to-t from-slate-950"],
[class*="bg-gradient-to-r from-cyan-950"],
[class*="bg-gradient-to-r from-purple-950"],
[class*="bg-gradient-to-br from-cyan-950"] {
  color: #ffffff;
}

/* Headings inside permanent dark sections */
.bg-slate-900 h1, .bg-slate-900 h2, .bg-slate-900 h3, .bg-slate-900 h4,
.bg-slate-950 h1, .bg-slate-950 h2, .bg-slate-950 h3, .bg-slate-950 h4,
[class*="from-cyan-950"] h1:not([class*="text-transparent"]), 
[class*="from-cyan-950"] h2:not([class*="text-transparent"]), 
[class*="from-cyan-950"] h3:not([class*="text-transparent"]),
[class*="from-purple-950"] h1:not([class*="text-transparent"]), 
[class*="from-purple-950"] h2:not([class*="text-transparent"]), 
[class*="from-purple-950"] h3:not([class*="text-transparent"]),
[class*="from-slate-950"] h1:not([class*="text-transparent"]), 
[class*="from-slate-950"] h2:not([class*="text-transparent"]), 
[class*="from-slate-950"] h3:not([class*="text-transparent"]),
[class*="bg-gradient-to-t from-slate-950"] h1, 
[class*="bg-gradient-to-t from-slate-950"] h2, 
[class*="bg-gradient-to-t from-slate-950"] h3 {
  color: #ffffff !important;
}

/* Body copy & descriptions inside permanent dark sections */
.bg-slate-900 p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
.bg-slate-950 p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="from-cyan-950"] p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="from-purple-950"] p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="from-slate-950"] p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]),
[class*="bg-gradient-to-t from-slate-950"] p {
  color: #cbd5e1 !important;
}

/* Cyber-grid dynamic light / dark contrast rules */
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) {
  color: #0f172a !important;
}
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) h1:not([class*="text-transparent"]),
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) h2:not([class*="text-transparent"]),
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) h3:not([class*="text-transparent"]),
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) h4:not([class*="text-transparent"]) {
  color: #000000 !important;
}
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]) {
  color: #1e293b !important;
}
html:not(.dark) .cyber-grid:not(.bg-slate-900):not(.bg-slate-950) .text-black {
  color: #000000 !important;
}

.dark .cyber-grid h1:not([class*="text-transparent"]),
.dark .cyber-grid h2:not([class*="text-transparent"]),
.dark .cyber-grid h3:not([class*="text-transparent"]),
.dark .cyber-grid h4:not([class*="text-transparent"]) {
  color: #ffffff !important;
}
.dark .cyber-grid p:not([class*="text-emerald-"]):not([class*="text-cyan-"]):not([class*="text-purple-"]):not([class*="text-pink-"]) {
  color: #cbd5e1 !important;
}

html:not(.dark) .text-black {
  color: #000000 !important;
}"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')

if target_norm in c_norm:
    c_norm = c_norm.replace(target_norm, replacement)
    with open('assets/css/style.css', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("Updated style.css successfully.")
else:
    print("Target not found in style.css.")
