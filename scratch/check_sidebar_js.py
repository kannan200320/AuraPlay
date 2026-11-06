with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Let's inspect initDashboardSidebar in main.js
start_idx = c.find('function initDashboardSidebar()')
end_idx = c.find('// --- Initialize when DOM is ready ---')
print("Current initDashboardSidebar:")
print(c[start_idx:end_idx])
