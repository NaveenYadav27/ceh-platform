import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

topics = [
    'info-security-overview', 'hacker-classes', 'ethical-hacking-concepts',
    'hacking-methodologies', 'security-controls', 'security-laws'
]

print("=== SPRINT 3.2 TECHNICAL REVIEW: GATE 2 VALIDATION ===")

for t in topics:
    # Find the block for the topic
    pattern = r"CONTENT\['" + t + r"'\] = \{(.*?)\n\};\n"
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print(f"\n[FAIL] Topic '{t}' not found in CONTENT.")
        continue
        
    block = match.group(1)
    
    print(f"\n--- Topic: {t} ---")
    
    # 1. Educational Flow (Why/What/How)
    has_why = 'why:' in block
    has_what = 'simple:' in block
    has_how = 'workflow:' in block and 'lab:' in block
    print(f"Educational Flow: WHY={has_why}, WHAT={has_what}, HOW={has_how}")
    
    # 2. Command Validation
    lin_cmds = re.findall(r"\{ cmd: '(.*?)', purpose: '(.*?)', out: '(.*?)', note: '(.*?)', mistake: '(.*?)' \}", block)
    win_cmds = re.findall(r"\{ cmd: '(.*?)', purpose: '(.*?)', out: '(.*?)', note: '(.*?)', mistake: '(.*?)' \}", block)
    print(f"Commands: {len(lin_cmds)} Linux, {len(win_cmds)} Windows commands found with full documentation.")
    
    # 3. MITRE Validation
    mitre = re.findall(r"id: '(.*?)', name: '(.*?)', tactic: '(.*?)'", block)
    print(f"MITRE Mappings: {len(mitre)} found -> {mitre}")
    
    # 4. Assessment Quality
    quizzes = re.findall(r"q: '.*?',\s*opts: \[.*?\],\s*correct: .*?,\s*fb: '.*?'", block)
    tf_quizzes = re.findall(r"q: '.*?',\s*correct: '.*?',\s*fb: '.*?'", block)
    total_q = len(quizzes) + len(tf_quizzes)
    print(f"Quizzes: {total_q} total (MCQ={len(quizzes)}, T/F={len(tf_quizzes)})")
    
    # 5. Flashcards
    fc = re.findall(r"f: '.*?',\s*b: '.*?'", block)
    print(f"Flashcards: {len(fc)} found")
