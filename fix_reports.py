def fix_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace("reports' names", r"reports\' names")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed specific quotes.")

fix_quotes('frontend/index.html')
