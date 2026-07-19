with open('frontend/index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'AUTO-STUB GENERATOR' in line:
            print(f"Found at line {i+1}")
