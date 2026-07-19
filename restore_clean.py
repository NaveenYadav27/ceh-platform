"""
Restore the platform to a clean working state:
1. Inline the extracted component files back into main.html
2. Strip all EJS <%- include(...) %> tags
3. Save as index.html (the static file Express will serve directly)
"""
import re
import os

components_dir = 'frontend/components'
main_file = 'frontend/main.html'
out_file = 'frontend/index.html'

# Read components
def read_comp(name):
    p = os.path.join(components_dir, name)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

with open(main_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace EJS include tags with their actual file content
def replace_include(match):
    filename = match.group(1).strip()
    # filename is like "components/topbar.html"
    basename = os.path.basename(filename)
    content = read_comp(basename)
    return content

html = re.sub(r"<%[-=]\s*include\s*\(['\"]([^'\"]+)['\"]\s*\)\s*%>", replace_include, html)

# Also strip any remaining EJS tags just in case
html = re.sub(r"<%[-=]?[^%]*%>", '', html)

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done! Wrote clean index.html ({len(html)} bytes)")
