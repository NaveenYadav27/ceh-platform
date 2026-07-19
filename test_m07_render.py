import re

with open('frontend/index.html', encoding='utf8') as f:
    html = f.read()

# Extract all build functions
build_funcs = []
for match in re.finditer(r'function (build[A-Za-z]+)\(.*?\)\s*\{', html):
    start = match.start()
    brace_count = 0
    in_string = False
    string_char = ''
    end = -1
    for i in range(start, len(html)):
        c = html[i]
        if not in_string:
            if c in ('"', "'", "`"):
                in_string = True
                string_char = c
            elif c == '{':
                brace_count += 1
            elif c == '}':
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break
        else:
            if c == string_char and html[i-1] != '\\':
                in_string = False
    
    if end != -1:
        build_funcs.append(html[start:end])

funcs_js = '\n'.join(build_funcs)

with open('frontend/index.min.html', encoding='utf8') as f:
    minhtml = f.read()
    
m07_match = re.search(r'CONTENT\[.malware-concepts.\] = (\{.*?\});', minhtml, re.DOTALL)
m07_data = m07_match.group(1)

js_script = f"""
const CONTENT = {{}};

{funcs_js}

const d = {m07_data};
CONTENT['malware-concepts'] = d;
function buildComingSoonHTML() {{ return ''; }} // mock
try {{
    const html = buildTopicHTML('malware-concepts', d);
    console.log('SUCCESS!');
    console.log('HTML Length:', html.length);
}} catch(e) {{
    console.error('ERROR:', e.stack);
}}
"""

with open('test_build.js', 'w', encoding='utf8') as f:
    f.write(js_script)
