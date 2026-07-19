def fix_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix the PHP web shell snippet
    html = html.replace(r"$_GET['cmd']", r"$_GET[\'cmd\']")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed specific quotes again.")

fix_quotes('frontend/index.html')
