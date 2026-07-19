with open('frontend/index.html', encoding='utf8') as f:
    lines = f.readlines()
with open('find_out.txt', 'w', encoding='utf8') as f_out:
    for i, line in enumerate(lines):
        if 'Close Terminals' in line or 'floating-close' in line:
            f_out.write(f'{i+1}: {line.strip()}\n')
        if '<div id="' in line and ('term' in line or 'panel' in line):
            f_out.write(f'{i+1}: {line.strip()}\n')
