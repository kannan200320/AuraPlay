import sys
sys.stdout.reconfigure(encoding='utf-8')

main_js = open('assets/js/main.js', encoding='utf-8').read()
idx = main_js.find('initDashboardSidebar')
print(main_js[idx-100:idx+800])
