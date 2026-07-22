import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '// =================================================================\n// MODULE 02'
start_idx = html.find(start_marker)

if start_idx == -1:
    print("Could not find the injected content marker. Maybe it's already removed?")
else:
    # Find the end of the script tag which is right at the end of the file
    end_marker = '</script>'
    end_idx = html.find(end_marker, start_idx)
    
    if end_idx == -1:
        print("Could not find </script>")
        exit(1)
        
    injected_chunk = html[start_idx:end_idx]
    
    # Remove the chunk from html
    new_html = html[:start_idx] + '\n' + html[end_idx:]
    
    with open('frontend/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    with open('frontend/index.min.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    # Append the chunk to content.js
    with open('frontend/content.js', 'a', encoding='utf-8') as f:
        f.write('\n' + injected_chunk)
        
# Now read content.js and clean ALL SVGs out of it.
with open('frontend/content.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Aggressive regex to remove the exact block of SVG or any svg property
# First, remove lines that look like "svg": "<svg...
js_content = re.sub(r'"svg"\s*:\s*".*?</svg>"\s*,?', '', js_content)
# Also remove single-quoted ones
js_content = re.sub(r"'svg'\s*:\s*'.*?</svg>'\s*,?", '', js_content)
# Also remove unquoted key ones
js_content = re.sub(r'svg\s*:\s*["\'].*?</svg>["\']\s*,?', '', js_content)

# Just to be extremely safe, remove the exact string the user reported
exact_svg = '<svg width="100%" height="200" viewBox="0 0 600 200" style="background:#0a0a0f;border:1px solid #1a1a24;border-radius:8px;"><path d="M 100 100 L 250 100" stroke="#00aaff" stroke-width="2" marker-end="url(#arrow)"></path><rect x="20" y="70" width="80" height="60" fill="#1a1a24" stroke="#00aaff"></rect><text x="60" y="105" fill="#fff" font-family="monospace" font-size="12" text-anchor="middle">Analyst</text><rect x="250" y="70" width="120" height="60" fill="#1a1a24" stroke="#00aaff"></rect><text x="310" y="105" fill="#fff" font-family="monospace" font-size="12" text-anchor="middle">OSINT Sources</text></svg>'
js_content = js_content.replace(f'"svg": "{exact_svg}",', '')
js_content = js_content.replace(f'"svg": "{exact_svg}"', '')
js_content = js_content.replace(f"'svg': '{exact_svg}',", '')
js_content = js_content.replace(f"'svg': '{exact_svg}'", '')

with open('frontend/content.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Decoupling of injected content complete! SVGs scrubbed.")
