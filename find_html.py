import re

with open('frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

patterns = {
    'sidebar': r'<div class="sidebar">',
    'topbar': r'<div class="topbar">',
    'notif-panel': r'<div class="notif-panel',
    'loginScreen': r'<div id="loginScreen"',
    'appContainer': r'<div class="app-container"',
    'cyber-particles': r'<div class="cyber-particles">',
    'glitch-overlay': r'<div class="glitch-overlay">',
    'scanline': r'<div class="scanline">',
    'main-content': r'<div class="main-content">'
}

for name, p in patterns.items():
    match = re.search(p, html)
    if match:
        line_num = html[:match.start()].count('\n') + 1
        print(f'{name} found at line {line_num}')
    else:
        print(f'{name} not found')
