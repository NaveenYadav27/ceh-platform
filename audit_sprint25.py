import re

content = open('frontend/index.html', encoding='utf-8').read()
lines = content.split('\n')
print(f"Total lines: {len(lines)}")
print(f"Total bytes: {len(content)}")

# ── 1. Hard-coded colors in CSS section ──────────────────────────────────────
script_start = content.find('<script>')
css_part = content[:script_start]
# Match hex colors not immediately preceded by -- (variable definitions) or 'cyber-'
hardcoded_css = re.findall(r'(?<!\-\-)(?<!cyber-)(?<!rgb\()#[0-9A-Fa-f]{6}(?!\w)', css_part)
unique_hcss = list(set(hardcoded_css))
print(f"\nHard-coded hex colors in CSS ({len(unique_hcss)} unique):")
for h in sorted(unique_hcss):
    print(f"  {h}")

# ── 2. Legacy var() tokens ────────────────────────────────────────────────────
old_vars = re.findall(r'var\(--(?:bg2?|panel|border(?:-bright)?|green(?:-dim|-glow)?|red(?:-dim)?|blue(?:-dim)?|purple(?:-dim)?|yellow|text(?:-muted|-dim)?|sidebar-w|topbar-h|radius|font|mono)\)', content)
unique_old = list(set(old_vars))
print(f"\nLegacy --var tokens still in use ({len(unique_old)} unique):")
for v in sorted(unique_old):
    cnt = content.count(v)
    print(f"  {v}  x{cnt}")

# ── 3. Engine function presence ───────────────────────────────────────────────
engines = [
    'buildTopicHTML', 'buildLabHTML', 'buildAssessmentHTML',
    'buildQuizHTML', 'buildStandardizedCommands',
    'wireQuiz', 'toggleLabStep',
    'renderLMSDashboard', 'completeTopic',
    'syncProgressFromServer', 'checkAuth', 'doLogout',
]
print(f"\nEngine functions:")
for fn in engines:
    present = fn in content
    count = content.count(fn)
    print(f"  {'OK' if present else 'MISSING':<7}  {fn}  (refs: {count})")

# ── 4. CSS class consistency: gfs- token usage ───────────────────────────────
gfs_tokens = re.findall(r'var\(--gfs-[a-z\-]+\)', content)
print(f"\nTotal --gfs-* token references: {len(gfs_tokens)}")

# ── 5. MODULES count ─────────────────────────────────────────────────────────
module_count = content.count("{ id:'m")
topic_count  = content.count("{id:'") - module_count
print(f"\nModules defined: {module_count}")
print(f"Topics defined (approx): {topic_count}")

# ── 6. CONTENT vs TOPIC_STUBS coverage ───────────────────────────────────────
content_keys = re.findall(r"CONTENT\['([^']+)'\]", content)
stub_keys    = re.findall(r"TOPIC_STUBS\['([^']+)'\]", content)
print(f"\nCONTENT entries defined: {len(set(content_keys))}")
print(f"TOPIC_STUBS entries defined: {len(set(stub_keys))}")
