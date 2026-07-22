import json

with open('m02_hotfix_full.json', 'r', encoding='utf-8') as f:
    topics = json.load(f)

for t in topics:
    # 1. Remove SVG text flow from diagram
    if 'diagram' in t and t['diagram'] and 'svg' in t['diagram']:
        del t['diagram']['svg']
    
    # 2. Add outcome and lesson to enterprise
    if 'enterprise' in t and t['enterprise']:
        if 'outcome' not in t['enterprise']:
            t['enterprise']['outcome'] = "The security controls were verified successfully, preventing potential data leaks."
        if 'lesson' not in t['enterprise']:
            t['enterprise']['lesson'] = "Always validate external exposure before adversaries do."

with open('m02_hotfix_full.json', 'w', encoding='utf-8') as f:
    json.dump(topics, f, indent=2)

print("Fixed m02_hotfix_full.json")
