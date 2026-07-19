import re
with open('frontend/index.html', encoding='utf8') as f:
    html = f.read()

keys = re.findall(r'[\'\"]([^\'\"]+)[\'\"]\s*:\s*\{[^}]*eyebrow', html)
print(keys)
