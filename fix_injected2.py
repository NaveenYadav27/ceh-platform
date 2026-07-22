import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find("CONTENT['malware-concepts'] = {")
end_idx = html.find("\nfunction wireTopicTabs(id, d)")

if start_idx == -1 or end_idx == -1:
    print("Markers not found!")
    print("Start:", start_idx, "End:", end_idx)
    exit(1)

# Extract the massive injected block
injected_block = html[start_idx:end_idx]

# Remove it from index.html
new_html = html[:start_idx] + html[end_idx:]

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

with open('frontend/index.min.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# Append it to content.js
with open('frontend/content.js', 'a', encoding='utf-8') as f:
    f.write('\n// MORE INJECTED CONTENT\n')
    f.write(injected_block)

# Clean content.js of SVGs
with open('frontend/content.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Aggressive scrub of any SVG properties inside the JSON objects
js = re.sub(r'"svg"\s*:\s*".*?</svg>"\s*,?', '', js)
js = re.sub(r"'svg'\s*:\s*'.*?</svg>'\s*,?", '', js)
js = re.sub(r'svg\s*:\s*["\'].*?</svg>["\']\s*,?', '', js)

# And specifically the exact string
exact_svg = '<svg width="100%" height="200" viewBox="0 0 600 200" style="background:#0a0a0f;border:1px solid #1a1a24;border-radius:8px;"><path d="M 100 100 L 250 100" stroke="#00aaff" stroke-width="2" marker-end="url(#arrow)"></path><rect x="20" y="70" width="80" height="60" fill="#1a1a24" stroke="#00aaff"></rect><text x="60" y="105" fill="#fff" font-family="monospace" font-size="12" text-anchor="middle">Analyst</text><rect x="250" y="70" width="120" height="60" fill="#1a1a24" stroke="#00aaff"></rect><text x="310" y="105" fill="#fff" font-family="monospace" font-size="12" text-anchor="middle">OSINT Sources</text></svg>'
js = js.replace(f'"svg": "{exact_svg}",', '')
js = js.replace(f'"svg": "{exact_svg}"', '')
js = js.replace(f"'svg': '{exact_svg}',", '')
js = js.replace(f"'svg': '{exact_svg}'", '')

with open('frontend/content.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Decoupled the rest of the injected content!")
