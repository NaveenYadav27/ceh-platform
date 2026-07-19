"""
Trace exact execution order and find all DOM element IDs referenced in JS,
then verify they exist in the HTML.
"""
import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Split into HTML and JS sections
script_start = html.find('<script>')
html_part = html[:script_start]
js_part = html[script_start:]

# Find all getElementById calls in JS
getelements = re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js_part)
ids_in_js = sorted(set(getelements))

# Find all id= definitions in HTML
ids_in_html = set(re.findall(r'\bid=["\']([^"\']+)["\']', html_part))

print("=== IDs referenced in JS but NOT in HTML (potential null refs) ===")
missing = []
for id_ in ids_in_js:
    if id_ not in ids_in_html:
        missing.append(id_)
        print(f"  MISSING: #{id_}")

if not missing:
    print("  All IDs exist in HTML.")

print(f"\n=== Total JS getElementById refs: {len(ids_in_js)} ===")
print(f"=== Missing from HTML: {len(missing)} ===")

# Check execution order at bottom of script
print("\n=== Script entry points (last 20 lines of script) ===")
js_lines = js_part.split('\n')
for i, line in enumerate(js_lines[-25:], len(js_lines)-25):
    print(f"  L{i+1}: {line.rstrip()[:100]}")
