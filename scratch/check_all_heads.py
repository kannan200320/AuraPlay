import glob, re

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    head_match = re.search(r'<head>(.*?)(?:<link|<style|<script src)', content, re.DOTALL)
    has_script = "color-theme" in content[:1500]
    html_tag = re.search(r'<html[^>]*>', content).group(0)
    print(f"{f:30} has_theme_script_in_head: {has_script} | html_tag: {html_tag}")
