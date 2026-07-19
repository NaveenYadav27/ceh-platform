import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

topics = [
    'info-security-overview', 'hacker-classes', 'ethical-hacking-concepts',
    'hacking-methodologies', 'security-controls', 'security-laws'
]

meta_template = """,
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Foundation",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
}"""

for t in topics:
    # We find the end of the topic object: 'outcomes: [ ... ] \n}'
    # and replace the final '}' with the meta_template
    
    pattern = r"(CONTENT\['" + t + r"'\] = \{.*?outcomes:\s*\[.*?\])\n\};"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        original = match.group(0)
        # Reconstruct the string with the meta block
        new_block = match.group(1) + meta_template + ";"
        content = content.replace(original, new_block)
        print(f"Injected meta into {t}")
    else:
        print(f"Failed to match {t}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Backfill complete.")
