with open('frontend/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

targets = ['updateProgressUI', 'updateTopicButtons', 'initFloatingTerminals']
for name in targets:
    print(f'\n=== {name} ===')
    for i, l in enumerate(lines, 1):
        if name in l:
            safe = l.rstrip()[:110].encode('ascii', 'ignore').decode()
            print(f'  L{i}: {safe}')
