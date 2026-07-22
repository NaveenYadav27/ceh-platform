import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('const MODULES = [')
end_marker = '// ═══════════════════════════════════════════════════════════\n// XP & RANK SYSTEM'
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Markers not found.")
    exit(1)

content_block = html[start_idx:end_idx]

# Clean out any SVG diagram strings
# Matches exactly the SVG payload that the user showed
cleaned_block = re.sub(r'"svg"\s*:\s*".*?(</svg>)",?', '', content_block)
cleaned_block = re.sub(r'^\s*"?svg"?\s*:\s*.*?</svg>.*?\n', '', cleaned_block, flags=re.MULTILINE)

with open('frontend/content.js', 'w', encoding='utf-8') as f:
    f.write(cleaned_block)

new_html = html[:start_idx] + '<script src="content.js"></script>\n\n' + html[end_idx:]

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('frontend/index.min.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Decoupling complete!")
