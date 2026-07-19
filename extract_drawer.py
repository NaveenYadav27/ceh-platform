with open('frontend/index.html', encoding='utf8') as f:
    html = f.read()

import re
match = re.search(r'<div id="term-drawer".*?<!-- FLOATING TERMINALS END -->', html, re.DOTALL)
if match:
    with open('term_drawer.txt', 'w', encoding='utf8') as f2:
        f2.write(match.group(0))
