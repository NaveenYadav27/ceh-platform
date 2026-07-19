import re

def fix_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find unescaped single quotes between alphanumeric characters
    pattern = r"(?<=[a-zA-Z0-9])(?<!\\)'(?=[a-zA-Z0-9])"
    html = re.sub(pattern, r"\'", html)
    
    # Let's also fix specific known ones just in case
    html = html.replace("Rapid7's", r"Rapid7\'s")
    html = html.replace("reports' names", r"reports\' names")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed alphanumeric contraction quotes.")

fix_quotes('frontend/index.html')
