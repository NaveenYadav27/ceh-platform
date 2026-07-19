import re

def fix_file(filename):
    with open(filename, encoding='utf8') as f:
        html = f.read()
        
    html = html.replace("\\u{1F504','Diagram", "\\u{1F504}','Diagram")
    
    with open(filename, "w", encoding="utf8") as f:
        f.write(html)

fix_file('frontend/index.html')
fix_file('frontend/index.min.html')
