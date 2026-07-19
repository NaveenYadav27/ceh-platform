import os

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any occurrence of two literal backslashes followed by a single quote
# with a single backslash followed by a single quote
new_content = content.replace("\\\\'", "\\'")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Replaced {content.count("\\\\\'")} occurrences.')
