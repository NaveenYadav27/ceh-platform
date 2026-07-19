import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lines = html.split('\n')
# Find all function definitions
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('function ') or 'async function ' in stripped or ') {' in stripped and 'function' in stripped:
        print(f"Line {i+1}: {stripped[:120].encode('ascii', 'ignore').decode()}")
