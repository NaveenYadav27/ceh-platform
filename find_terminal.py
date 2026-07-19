with open('frontend/index.html', encoding='utf8') as f:
    html = f.read()

import re
matches = re.finditer(r'<div id=\"term-pane\".*?</div>\s*</div>\s*</div>', html, re.DOTALL)
for m in matches:
    print(m.group(0))
