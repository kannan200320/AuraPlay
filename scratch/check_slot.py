with open('book-slot.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('has auraplay-navbar:', 'auraplay-navbar' in c)
print('has dashboard-sidebar:', 'dashboard-sidebar' in c)
print('sections count:', c.count('id="section-'))
