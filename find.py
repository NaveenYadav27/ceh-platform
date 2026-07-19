import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lines = html.split('\n')
for i, line in enumerate(lines):
    l = line.lower()
    if 'sidebar' in l or 'topbar' in l or 'nav' in l or 'footer' in l or 'header' in l:
        if '<div' in l or '<nav' in l or '<footer' in l or '<header' in l or '<aside' in l:
            # ignore CSS classes that don't match exactly the component names we want
            print(f"Line {i+1}: {line.strip().encode('ascii', 'ignore').decode()}")
