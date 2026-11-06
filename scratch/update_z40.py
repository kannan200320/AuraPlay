import re

with open('scratch/apply_dashboard_ref_header.py', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('sticky top-0 z-30', 'sticky top-0 z-40')

with open('scratch/apply_dashboard_ref_header.py', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated script to z-40.")
