import re
content=open('frontend/index.html', encoding='utf8').read()
matches = re.findall(r"CONTENT\['(.*?)'\] = \{(.*?)\n  \};", content, re.DOTALL)
for k, v in matches:
    if 'Module 03' in v or 'Module 04' in v or 'Module 05' in v or 'Module 06' in v:
        if 'Module 03' in v: mod = 'M03'
        elif 'Module 04' in v: mod = 'M04'
        elif 'Module 05' in v: mod = 'M05'
        else: mod = 'M06'
        print(f'{mod}: {k}')
