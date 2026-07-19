with open('frontend/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

targets = ['totalXP', 'let xp', 'var xp']
for name in targets:
    print(f'\n=== {name} ===')
    for i, l in enumerate(lines, 1):
        if name in l:
            safe = l.rstrip()[:120].encode('ascii', 'ignore').decode()
            print(f'  L{i}: {safe}')
