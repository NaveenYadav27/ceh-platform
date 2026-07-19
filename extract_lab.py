with open('frontend/index.html', encoding='utf8') as f:
    html = f.read()
import re
import sys

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
        if 'buildLabHTML' in html[start:end]:
            sys.stdout.buffer.write(html[start:end].encode('utf8'))
