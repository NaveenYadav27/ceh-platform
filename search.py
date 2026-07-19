with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'tab-commands' in line or 'updateCommands' in line or 'renderCommands' in line or 'const render' in line:
        print(f"{i}: {line.strip()[:100]}")
