import re
import json

with open('frontend/index.min.html', encoding='utf8') as f:
    html = f.read()

# Let's see the keys of CONTENT
matches = re.findall(r'CONTENT\[[\'\"]([^\'\"]+)[\'\"]\] = \{', html)
print(matches[:10])
