import sys
sys.stdout.reconfigure(encoding='utf-8')

# Clean dashboard-payments.html
pay_content = open('dashboard-payments.html', encoding='utf-8').read()
# Let's inspect everything from </body> backwards
script_start = pay_content.find('  <script>\n    let selectedReload = 50;')
if script_start != -1:
    second_script_start = pay_content.find('  <script>\n    let selectedReload = 50;', script_start + 20)
    if second_script_start != -1:
        # cut out everything from second_script_start up to </body>
        body_end = pay_content.find('</body>', second_script_start)
        cleaned_pay = pay_content[:second_script_start] + pay_content[body_end:]
        open('dashboard-payments.html', 'w', encoding='utf-8').write(cleaned_pay)
        print("Cleaned duplicate script in dashboard-payments.html")

# Clean dashboard-packs.html
packs_content = open('dashboard-packs.html', encoding='utf-8').read()
script_start_packs = packs_content.find('  <script>\n    window.handlePackBuy')
if script_start_packs != -1:
    second_packs_start = packs_content.find('  <script>\n    window.handlePackBuy', script_start_packs + 20)
    if second_packs_start != -1:
        body_end = packs_content.find('</body>', second_packs_start)
        cleaned_packs = packs_content[:second_packs_start] + packs_content[body_end:]
        open('dashboard-packs.html', 'w', encoding='utf-8').write(cleaned_packs)
        print("Cleaned duplicate script in dashboard-packs.html")
