import glob
import re

html_files = sorted(glob.glob('*.html'))
issues = []

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    
    # Check for text-white on elements that do not have dark: prefix and are NOT inside an explicit dark container
    # Let's look for headings and paragraphs that have "text-white" without "dark:text-white"
    # and without "bg-slate-900", "bg-slate-950", "bg-gradient-to-r from-cyan-500", etc.
    sections = re.findall(r'<section\b([^>]*)>(.*?)</section>', c, re.DOTALL)
    for s_attrs, s_content in sections:
        s_cls = re.search(r'class=["\']([^"\']+)["\']', s_attrs)
        s_cls_str = s_cls.group(1) if s_cls else ""
        
        # Is section dark in light mode?
        is_dark_section = any(d in s_cls_str for d in ['bg-slate-900', 'bg-slate-950', 'bg-darkslate-deep', 'bg-slate-900/90'])
        
        if not is_dark_section:
            # Look for headings with bare text-white or text-slate-300 or text-slate-400
            bare_whites = re.findall(r'<(?:h1|h2|h3|h4|p)\b[^>]*class=["\']([^"\']+)["\'][^>]*>(.*?)</(?:h1|h2|h3|h4|p)>', s_content, re.DOTALL)
            for cls, inner in bare_whites:
                # If it has text-white without dark:text-white or dark:text-slate
                tokens = cls.split()
                has_bare_white = 'text-white' in tokens and not any('dark:' in t for t in tokens)
                if has_bare_white and not any(p in cls for p in ['bg-gradient-to-r', 'from-']):
                    txt = re.sub(r'<[^>]+>', '', inner).strip()
                    issues.append((f, "bare text-white", txt[:40], cls))

print(f"Total potential bare text-white issues: {len(issues)}")
for f, itype, txt, cls in issues[:15]:
    line = f"[{f}] {itype}: {txt} (cls: {cls})"
    print(line.encode('ascii', 'backslashreplace').decode('ascii'))
