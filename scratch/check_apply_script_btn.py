with open('scratch/apply_dashboard_ref_header.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Check + Top-Up Hours in apply script
print("+ Top-Up Hours gradient present:", "from-cyan-500 to-purple-600 hover:from-cyan-400 hover:to-purple-500" in c)
