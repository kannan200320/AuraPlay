import sys
sys.stdout.reconfigure(encoding='utf-8')

packs = open('dashboard-packs.html', encoding='utf-8').read()

target = "window.handlePackBuy = function(packName, price) {"

replacement = """window.openCheckoutModal = function(packName, price) {
      const modal = document.getElementById('checkout-modal');
      const nameEl = document.getElementById('modal-pack-name');
      const priceEl = document.getElementById('modal-pack-price');
      if (nameEl) nameEl.textContent = packName;
      if (priceEl) priceEl.textContent = '$' + Number(price).toFixed(2);
      if (modal) modal.classList.remove('hidden');
    };

    window.closeCheckoutModal = function() {
      const modal = document.getElementById('checkout-modal');
      if (modal) modal.classList.add('hidden');
    };

    window.executePurchase = function() {
      const nameEl = document.getElementById('modal-pack-name');
      const packName = nameEl ? nameEl.textContent : 'Hour Package';
      window.closeCheckoutModal();
      if (window.showAuraPopup) {
        window.showAuraPopup('Hour Pack Added!', 'Successfully purchased ' + packName + '. Hours banked to your NFC profile.', true);
      }
    };

    window.handlePackBuy = function(packName, price) {"""

if target in packs:
    packs = packs.replace(target, replacement, 1)
    open('dashboard-packs.html', 'w', encoding='utf-8').write(packs)
    print("Added modal functions to dashboard-packs.html")
else:
    print("Target not found!")
