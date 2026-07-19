import re
content = open('frontend/index.min.html', encoding='utf8').read()
match = re.search(r'CONTENT\[.malware-concepts.\] = (\{.*?\});', content, re.DOTALL)
if match:
    payload = match.group(1)
    print('Has objectives:', '"objectives"' in payload)
    print('Has pitfalls:', '"pitfalls"' in payload)
