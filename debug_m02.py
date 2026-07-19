import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

t = 'footprinting-concepts'
pattern = r"CONTENT\['" + t + r"'\] = \{(.*?)\n\};\n?"
matches = list(re.finditer(pattern, content, re.DOTALL))
print("Total matches:", len(matches))
if matches:
    block = matches[-1].group(1)
    print("Block length:", len(block))
    print("Snippet:", block[:200])
    has_why = 'why:' in block
    has_what = 'simple:' in block
    has_how = 'workflow:' in block and 'lab:' in block
    print(f"Educational Flow: WHY={has_why}, WHAT={has_what}, HOW={has_how}")
    print("Is workflow: in block?", 'workflow:' in block)
    print("Is lab: in block?", 'lab:' in block)
    
    lin_cmds = re.findall(r"cmd:\s*'(.*?)'", block)
    print(f"Linux Cmds: {len(lin_cmds)}")
