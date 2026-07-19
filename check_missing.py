import re

content = open('frontend/index.min.html', encoding='utf8').read()

modules_match = re.search(r'const MODULES = \[(.*?)\];', content, re.DOTALL)
modules_str = modules_match.group(1) if modules_match else ''
topic_ids = re.findall(r'\{\s*id:\s*\'([^\']+)\'', modules_str)
topic_ids = [t for t in topic_ids if not re.match(r'^m\d+$', t)]

missing = []
for tid in topic_ids:
    if f'"{tid}":' not in content and f"'{tid}':" not in content:
        missing.append(tid)

print('Missing topics from CONTENT:', missing)
