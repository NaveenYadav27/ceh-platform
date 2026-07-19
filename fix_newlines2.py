def fix_ui(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace("output.split('\n", "output.split('\\n")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed JS newlines.")

fix_ui('frontend/index.html')
