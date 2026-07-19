content = open('frontend/index.html', encoding='utf8').read()
content = content.replace("WEP's", "WEP\\'s")
with open('frontend/index.html', 'w', encoding='utf8') as f:
    f.write(content)
