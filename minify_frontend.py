import re
import os

input_file = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
output_file = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.min.html'

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

minified_lines = []
for line in lines:
    stripped = line.strip()
    
    # Remove simple console.logs
    if stripped.startswith('console.log(') and stripped.endswith(');'):
        continue
        
    # Skip empty lines
    if not stripped:
        continue
        
    minified_lines.append(stripped)

# Join without newlines where safe, but to be completely AST-safe, we just use newlines but stripped of leading/trailing spaces.
minified_content = '\n'.join(minified_lines)

# Remove HTML comments (excluding SVG/content if needed, but safer to just remove standard ones)
minified_content = re.sub(r'<!--(?! slide).*?-->', '', minified_content, flags=re.DOTALL)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(minified_content)

print(f"Original size: {os.path.getsize(input_file)} bytes")
print(f"Minified size: {os.path.getsize(output_file)} bytes")
