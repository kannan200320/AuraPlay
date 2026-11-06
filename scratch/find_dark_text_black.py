import os
import re
from html.parser import HTMLParser

DARK_BG_INDICATORS = [
    'bg-slate-900', 'bg-slate-950', 'bg-[#1a1528]', 'bg-[#0f1016]', 'bg-[#0B0E14]',
    'bg-black', 'from-slate-950', 'from-cyan-950', 'from-purple-950', 'to-slate-950',
    'bg-slate-900/90', 'bg-slate-900/80', 'bg-black/70', 'bg-black/80', 'bg-black/60',
    'via-darkslate-card'
]

class DarkChecker(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.stack = [] # (tag, is_dark, dark_class)
        self.issues = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        classes_str = attr_dict.get('class', '')
        classes = classes_str.split()

        # Check if this element is dark
        is_dark = False
        dark_class = None
        for c in classes:
            if not c.startswith('dark:') and not c.startswith('hover:'):
                for ind in DARK_BG_INDICATORS:
                    if ind in c:
                        is_dark = True
                        dark_class = c
                        break
            if is_dark:
                break

        # Also inherits dark if any parent is dark, EXCEPT if this element explicitly sets a light bg:
        has_light_override = False
        for c in classes:
            if not c.startswith('dark:'):
                if c in ['bg-white', 'bg-slate-50', 'bg-slate-100', 'bg-emerald-50', 'bg-purple-50']:
                    has_light_override = True
                    break

        parent_is_dark = False
        if self.stack and not has_light_override:
            for parent_tag, p_dark, p_cls in reversed(self.stack):
                if p_dark:
                    parent_is_dark = True
                    dark_class = p_cls
                    break

        effective_dark = is_dark or parent_is_dark

        if 'text-black' in classes and effective_dark:
            line_no, _ = self.getpos()
            self.issues.append((line_no, tag, classes_str, dark_class))

        self.stack.append((tag, effective_dark, dark_class))

    def handle_endtag(self, tag):
        # Pop matching tag if available
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

total_issues = 0
for f in sorted(os.listdir('.')):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        parser = DarkChecker(f)
        parser.feed(content)
        if parser.issues:
            print(f"\n=== {f} ({len(parser.issues)} issues) ===")
            for line_no, tag, classes, dark_cls in parser.issues:
                print(f"  Line {line_no}: <{tag} class='{classes}'> inside '{dark_cls}'")
            total_issues += len(parser.issues)

print(f"\n>>> Total issues across all files: {total_issues}")
