import sys
sys.stdout.reconfigure(encoding='utf-8')

book = open('book-slot.html', encoding='utf-8').read()

# Replace legend
old_legend = """          <!-- Legend -->
          <div class="flex items-center space-x-4 rtl:space-x-reverse text-xs font-semibold mt-3 md:mt-0">
            <div class="flex items-center space-x-1.5"><span class="w-3.5 h-3.5 rounded bg-cyan-500"></span><span>Selected</span></div>
            <div class="flex items-center space-x-1.5"><span class="w-3.5 h-3.5 rounded bg-slate-200 dark:bg-darkslate-card border border-slate-300 dark:border-darkslate-border"></span><span>Available</span></div>
            <div class="flex items-center space-x-1.5"><span class="w-3.5 h-3.5 rounded bg-slate-400/40 opacity-40"></span><span>Occupied</span></div>
          </div>"""

new_legend = """          <!-- Legend -->
          <div class="flex items-center space-x-4 rtl:space-x-reverse text-xs font-semibold mt-3 md:mt-0">
            <div class="flex items-center space-x-1.5"><span class="w-3.5 h-3.5 rounded bg-cyan-500 shadow-sm shadow-cyan-500/50 ring-1 ring-cyan-400/50"></span><span>Selected</span></div>
            <div class="flex items-center space-x-1.5"><span class="w-3.5 h-3.5 rounded bg-emerald-500 shadow-sm shadow-emerald-500/50 ring-1 ring-emerald-400/50"></span><span>Available</span></div>
            <div class="flex items-center space-x-1.5"><span class="w-3.5 h-3.5 rounded bg-rose-500/80 border border-rose-500 shadow-sm shadow-rose-500/30 flex items-center justify-center text-[8px] text-white font-black leading-none">✕</span><span>Occupied</span></div>
          </div>"""

# Replace buttons
old_buttons = """          <div class="grid grid-cols-5 sm:grid-cols-10 gap-2 sm:gap-3 text-center">
            <!-- Row 1: Arena Alpha -->
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A01">A01</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A02">A02</button>
            <button class="seat-btn py-3 rounded-xl border-2 border-cyan-500 bg-cyan-500 text-black font-mono text-xs font-black shadow-md" data-seat="A03">A03</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A04">A04</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border opacity-40 cursor-not-allowed bg-slate-200 dark:bg-slate-800 font-mono text-xs font-bold" disabled>A05</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border opacity-40 cursor-not-allowed bg-slate-200 dark:bg-slate-800 font-mono text-xs font-bold" disabled>A06</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A07">A07</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A08">A08</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A09">A09</button>
            <button class="seat-btn py-3 rounded-xl border border-slate-300 dark:border-darkslate-border hover:border-cyan-500 bg-slate-50 dark:bg-darkslate-deep font-mono text-xs font-bold transition-all" data-seat="A10">A10</button>
          </div>"""

new_buttons = """          <div class="grid grid-cols-5 sm:grid-cols-10 gap-2 sm:gap-3 text-center">
            <!-- Row 1: Arena Alpha -->
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A01">A01</button>
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A02">A02</button>
            <button class="seat-btn py-3 rounded-xl border-2 border-cyan-400 bg-cyan-500 text-slate-950 font-mono text-xs font-black shadow-lg shadow-cyan-500/30 ring-2 ring-cyan-400/50" data-seat="A03">A03</button>
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A04">A04</button>
            <button class="seat-btn py-3 rounded-xl border border-rose-500/40 bg-rose-500/10 dark:bg-rose-950/20 text-rose-500/60 line-through opacity-60 cursor-not-allowed font-mono text-xs font-bold" disabled title="Station Occupied">A05</button>
            <button class="seat-btn py-3 rounded-xl border border-rose-500/40 bg-rose-500/10 dark:bg-rose-950/20 text-rose-500/60 line-through opacity-60 cursor-not-allowed font-mono text-xs font-bold" disabled title="Station Occupied">A06</button>
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A07">A07</button>
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A08">A08</button>
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A09">A09</button>
            <button class="seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm" data-seat="A10">A10</button>
          </div>"""

# Replace script
old_script = """      // 1. Interactive Seat Selection
      const seatBtns = document.querySelectorAll('.seat-btn:not([disabled])');
      const seatLabel = document.getElementById('selected-seat-label');

      seatBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          seatBtns.forEach(b => {
            b.classList.remove('border-2', 'border-cyan-500', 'bg-cyan-500', 'text-black', 'shadow-md');
            b.classList.add('border-slate-300', 'dark:border-darkslate-border', 'bg-slate-50', 'dark:bg-darkslate-deep', 'text-slate-900', 'dark:text-white');
          });
          btn.classList.add('border-2', 'border-cyan-500', 'bg-cyan-500', 'text-black', 'shadow-md');
          btn.classList.remove('border-slate-300', 'dark:border-darkslate-border', 'bg-slate-50', 'dark:bg-darkslate-deep', 'text-slate-900', 'dark:text-white');
          const seatNum = btn.getAttribute('data-seat');
          if (seatLabel) {
            seatLabel.textContent = `Station ${seatNum} (Zone Alpha - 360Hz QD-OLED)`;
          }
          const summaryStation = document.querySelector('.order-station-text');
          if (summaryStation) {
            summaryStation.textContent = `Station ${seatNum} (Zone Alpha)`;
          }
        });
      });"""

new_script = """      // 1. Interactive Seat Selection
      const seatBtns = document.querySelectorAll('.seat-btn:not([disabled])');
      const seatLabel = document.getElementById('selected-seat-label');

      seatBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          seatBtns.forEach(b => {
            b.className = 'seat-btn py-3 rounded-xl border border-emerald-500/40 hover:border-emerald-400 bg-emerald-500/10 dark:bg-emerald-950/30 text-emerald-700 dark:text-emerald-400 font-mono text-xs font-bold transition-all hover:scale-105 shadow-sm';
          });
          btn.className = 'seat-btn py-3 rounded-xl border-2 border-cyan-400 bg-cyan-500 text-slate-950 font-mono text-xs font-black shadow-lg shadow-cyan-500/30 ring-2 ring-cyan-400/50';
          const seatNum = btn.getAttribute('data-seat');
          if (seatLabel) {
            seatLabel.textContent = `Station ${seatNum} (Zone Alpha - 360Hz QD-OLED)`;
          }
          const summaryStation = document.querySelector('.order-station-text');
          if (summaryStation) {
            summaryStation.textContent = `Station ${seatNum} (Zone Alpha)`;
          }
        });
      });"""

# Normalize CRLF / LF
book_norm = book.replace('\r\n', '\n')
old_legend_norm = old_legend.replace('\r\n', '\n')
new_legend_norm = new_legend.replace('\r\n', '\n')
old_buttons_norm = old_buttons.replace('\r\n', '\n')
new_buttons_norm = new_buttons.replace('\r\n', '\n')
old_script_norm = old_script.replace('\r\n', '\n')
new_script_norm = new_script.replace('\r\n', '\n')

assert old_legend_norm in book_norm, "old_legend not found!"
assert old_buttons_norm in book_norm, "old_buttons not found!"
assert old_script_norm in book_norm, "old_script not found!"

book_norm = book_norm.replace(old_legend_norm, new_legend_norm)
book_norm = book_norm.replace(old_buttons_norm, new_buttons_norm)
book_norm = book_norm.replace(old_script_norm, new_script_norm)

open('book-slot.html', 'w', encoding='utf-8').write(book_norm)
print("Successfully updated book-slot.html seat picker differentiation!")
