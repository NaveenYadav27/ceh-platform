import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

topics = [
    'footprinting-concepts', 'osint-techniques', 'whois-dns',
    'google-hacking', 'shodan-recon', 'social-media-recon'
]

# We want to remove the old blocks. The old blocks do NOT have 'meta:' in them.
# The new blocks DO have 'meta:' in them.
# So we can find all blocks for a topic, and if it doesn't have 'meta:', we remove it.

for t in topics:
    # Match any CONTENT['topic'] = { ... }; block non-greedily
    # We have to be careful with nested braces if any, but since the old blocks were simple, this should work:
    # We look for CONTENT['topic'] = { followed by anything up to out: [ ... ] \n};
    # The old baseline blocks usually ended with `outcomes: [ ... ]\n  }` or similar.
    # Let's just use a script that keeps only the LAST occurrence of CONTENT['topic']
    
    pattern = r"CONTENT\['" + t + r"'\] = \{.*?\n\};\n?"
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    if len(matches) > 1:
        # Remove all but the last match
        for m in matches[:-1]:
            content = content.replace(m.group(0), "")
        print(f"Cleaned up {len(matches)-1} old occurrences of {t}")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Cleanup complete.")
