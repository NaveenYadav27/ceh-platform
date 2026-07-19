import re
content = open('frontend/index.html', encoding='utf8').read()
content = re.sub(r"([a-zA-Z])'([a-zA-Z])", r"\1\\'\2", content)
with open('frontend/index.html', 'w', encoding='utf8') as f:
    f.write(content)
