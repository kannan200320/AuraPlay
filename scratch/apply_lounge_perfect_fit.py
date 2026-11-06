import re

with open('player-lounge.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Fix <main class="pt-20"> -> <main>
c = c.replace('<main class="pt-20">', '<main>', 1)

# 2. Replace Section 1 with the optimized perfect-fit version matching index.html
s1_comment = "<!-- ================= SECTION 1: HERO - PLAYER'S LOUNGE ================= -->"
s2_comment = "<!-- ================= SECTION 2: LOUNGE QUICK STATUS TICKER ================= -->"

start = c.find(s1_comment)
end = c.find(s2_comment)

new_sec1 = """<!-- ================= SECTION 1: HERO - PLAYER'S LOUNGE ================= -->
    <section class="relative min-h-[calc(100vh-5rem)] flex items-center overflow-hidden py-6 sm:py-8 lg:py-10 bg-mesh-light dark:bg-mesh-dark">
      <!-- Background Image with Theme-Adaptive Scrim Overlay -->
      <div class="absolute inset-0 z-0 pointer-events-none overflow-hidden">
        <img src="assets/images/hero-bg-lounge.png" alt="AuraPlay Lounge Suite" class="w-full h-full object-cover object-center opacity-80 sm:opacity-90 dark:opacity-90 filter dark:brightness-100 transform scale-105">
        <div class="absolute inset-0 bg-gradient-to-r from-slate-50/75 via-slate-50/45 to-transparent dark:from-darkslate-deep/85 dark:via-darkslate-deep/50 dark:to-transparent"></div>
        <div class="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-slate-50 dark:to-darkslate-deep"></div>
      </div>
      <div class="absolute top-1/4 right-1/4 w-[500px] h-[500px] bg-purple-500/10 dark:bg-purple-500/15 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute bottom-10 left-10 w-[450px] h-[450px] bg-pink-500/10 dark:bg-pink-500/15 rounded-full blur-3xl pointer-events-none"></div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-8 items-center">
          
          <div class="lg:col-span-7 space-y-3.5 lg:space-y-4 text-center lg:text-left rtl:lg:text-right">
            <div class="inline-flex items-center space-x-2.5 rtl:space-x-reverse px-3.5 py-1 rounded-full bg-white/95 dark:bg-slate-900/90 backdrop-blur-md border border-purple-400 dark:border-purple-500/50 text-purple-950 dark:text-purple-200 text-xs sm:text-sm font-extrabold shadow-sm">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 live-indicator"></span>
              <span>THE SOCIAL GAMING SANCTUARY • COUCH CO-OP & COCKPITS</span>
            </div>

            <h1 class="text-3xl sm:text-5xl lg:text-5xl xl:text-6xl font-black font-display tracking-tight text-black dark:text-white uppercase leading-none hero-headline">
              Your Living Room, <br>
              <span>Radically Upgraded.</span>
            </h1>

            <p class="text-sm sm:text-base lg:text-base xl:text-lg text-black dark:text-white max-w-2xl mx-auto lg:mx-0 font-bold leading-normal sm:leading-relaxed hero-subtitle-boosted">
              Forget cramped sofas and small televisions. Immerse yourself in 65" LG OLED couch suites, tactile Fanatec direct drive cockpits, room-scale wireless VR pods, and craft mocktails with your squad.
            </p>

            <!-- Experience Chips -->
            <div class="flex flex-wrap gap-2 justify-center lg:justify-start rtl:lg:justify-end pt-1">
              <span class="px-2.5 py-1 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-black dark:text-white shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-purple-500">🎮</span>
                <span>PlayStation 5 Pro & OLEDs</span>
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-black dark:text-white shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-pink-500">🏎️</span>
                <span>Fanatec Motion Simulators</span>
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-black dark:text-white shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-amber-500">🥽</span>
                <span>Wireless VR Arenas</span>
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-300 dark:border-slate-700 text-xs font-bold text-black dark:text-white shadow-sm flex items-center space-x-1.5 rtl:space-x-reverse">
                <span class="text-cyan-500">🍸</span>
                <span>Artisan Gamer Refreshments</span>
              </span>
            </div>

            <!-- CTA Buttons -->
            <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start rtl:lg:justify-end gap-3 pt-1.5">
              <a href="book-slot.html" class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl text-sm sm:text-base font-extrabold text-white bg-gradient-to-r from-purple-600 via-pink-600 to-amber-500 hover:from-purple-500 hover:to-pink-500 shadow-xl shadow-purple-500/25 transition-all transform hover:-translate-y-0.5 text-center">
                Book a Lounge Couch Bay
              </a>
              <a href="#lounge-bays" class="w-full sm:w-auto px-6 sm:px-8 py-3 rounded-xl text-sm sm:text-base font-bold text-black dark:text-slate-200 dark:text-white bg-white dark:bg-darkslate-card border border-slate-200 dark:border-darkslate-border hover:bg-slate-100 dark:hover:bg-darkslate-lighter transition-all text-center">
                Tour Lounge Experiences ↓
              </a>
            </div>
          </div>

          <!-- Hero Visual: Lounge Suite Composite -->
          <div class="lg:col-span-5 relative">
            <div class="relative mx-auto max-w-md lg:max-w-none">
              <div class="absolute -inset-1 rounded-3xl bg-gradient-to-r from-purple-600 via-pink-500 to-amber-500 opacity-30 dark:opacity-40 blur-xl"></div>
              <div class="relative rounded-3xl overflow-hidden border border-slate-200 dark:border-darkslate-border bg-white dark:bg-darkslate-card shadow-2xl">
                <img src="assets/images/hero-player-lounge-pods.jpg" alt="AuraPlay Player Lounge Pods" class="w-full h-64 sm:h-80 lg:h-[350px] xl:h-[390px] object-cover transform hover:scale-105 transition-transform duration-700">
                <div class="absolute bottom-3 left-3 right-3 p-3 rounded-2xl bg-white/95 dark:bg-darkslate-card/95 backdrop-blur-md border border-slate-200 dark:border-darkslate-border shadow-lg">
                  <div class="flex items-center justify-between mb-0.5">
                    <span class="text-xs font-bold uppercase text-purple-600 dark:text-purple-400">VIP Couch Suite #04</span>
                    <span class="px-2 py-0.5 rounded-full text-[10px] font-black bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-300">4-PLAYER LOCAL</span>
                  </div>
                  <div class="text-xs sm:text-sm font-extrabold text-black dark:text-white">65" LG OLED • DualSense Edge • Dolby Atmos 7.1</div>
                  <div class="text-[11px] text-black dark:text-slate-400 mt-0.5">Available for Squad Bookings</div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    """

if start != -1 and end != -1:
    c = c[:start] + new_sec1 + c[end:]
    with open('player-lounge.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated player-lounge.html Section 1 successfully!")
else:
    print(f"Error finding section markers: start={start}, end={end}")
