import re

def fix_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find unescaped single quotes between two letters (e.g., don't, domain's)
    # and replace them with escaped single quotes.
    # Note: we need to handle cases where it might already be escaped (e.g. don\'t)
    # The negative lookbehind `(?<!\\)` ensures we only match unescaped quotes.
    
    pattern = r"(?<=[a-zA-Z])(?<!\\)'(?=[a-zA-Z])"
    
    html = re.sub(pattern, r"\'", html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed all contraction quotes.")

fix_quotes('frontend/index.html')
