import re
content=open('frontend/index.html', encoding='utf8').read()
matches = re.findall(r"CONTENT\['(.*?)'\] = \{(.*?)\n  \};", content, re.DOTALL)
for k, v in matches:
    if 'Module 07' in v: print(f'M07: {k}')
    elif 'Module 08' in v: print(f'M08: {k}')
    elif 'Module 09' in v: print(f'M09: {k}')
    elif 'Module 10' in v: print(f'M10: {k}')
