import re
content=open('frontend/index.html', encoding='utf8').read()
matches = re.findall(r"CONTENT\['(.*?)'\]", content)
print('\n'.join(sorted(set(matches))))
