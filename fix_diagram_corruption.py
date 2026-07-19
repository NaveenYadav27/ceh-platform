import re

def fix_file(filename):
    with open(filename, encoding='utf8') as f:
        html = f.read()
        
    # The leftover garbage starts with: }','Diagram & Workflow is being designed');
    # And ends before: // -- TAB 3: ENTERPRISE -- or just the next function
    
    # Let's find exactly the leftover block using regex
    pattern = r"\}','Diagram & Workflow is being designed'\);\s*return `\s*<div style=\"background:var\(--panel\);border:1px solid var\(--border\);border-radius:var\(--radius\);padding:28px;\">\s*<div style=\"font-size:1rem;font-weight:700;color:var\(--blue\);margin-bottom:24px;font-family:var\(--mono\);\">(.*?)\}\s*"
    
    # Actually, simpler: replace the exact duplicated leftover string!
    # Or just use a lazy regex from }','Diagram... up to the next }
    
    # We can match literally what we saw in the output
    bad_part_regex = r"\}','Diagram & Workflow is being designed'\);\s*return `[\s\S]*?</div>`;\s*\}"
    
    html = re.sub(bad_part_regex, "", html, flags=re.DOTALL)
    
    with open(filename, "w", encoding="utf8") as f:
        f.write(html)

fix_file('frontend/index.html')
fix_file('frontend/index.min.html')
