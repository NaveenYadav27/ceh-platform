content = open('frontend/index.html', encoding='utf8').read()
content = content.replace("city's", "city\\'s")
with open('frontend/index.html', 'w', encoding='utf8') as f:
    f.write(content)
