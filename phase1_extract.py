import os

def extract_tag(html, start_tag, tag_name='div'):
    idx = html.find(start_tag)
    if idx == -1:
        return None, html
    
    # Simple nested tag matcher
    count = 0
    in_str = False
    str_char = ''
    i = idx
    
    # fast forward to after the opening tag
    while i < len(html):
        if html[i:i+len(tag_name)+1] == f'<{tag_name}' or html[i:i+len(tag_name)+2] == f'<{tag_name} ':
            count += 1
        elif html[i:i+len(tag_name)+3] == f'</{tag_name}>':
            count -= 1
            if count == 0:
                end_idx = i + len(tag_name) + 3
                component = html[idx:end_idx]
                return component, html[:idx] + f"<!-- COMPONENT_PLACEHOLDER -->" + html[end_idx:]
        i += 1
    return None, html


with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

os.makedirs('frontend/components', exist_ok=True)

components_to_extract = [
    ('header.html', '<div class="nav-bar">', 'div'),
    ('topbar.html', '<header id="topbar">', 'header'),
    ('sidebar.html', '<nav id="sidebar">', 'nav'),
    ('notification-panel.html', '<div id="notif-panel"', 'div'),
]

for filename, start_tag, tag_name in components_to_extract:
    comp, new_html = extract_tag(html, start_tag, tag_name)
    if comp:
        with open(f'frontend/components/{filename}', 'w', encoding='utf-8') as f:
            f.write(comp)
        
        include_stmt = f"<%- include('components/{filename}') %>"
        html = new_html.replace('<!-- COMPONENT_PLACEHOLDER -->', include_stmt)
        print(f"Extracted {filename}")
    else:
        print(f"Could not extract {filename} using start_tag: {start_tag}")

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished extraction.")
