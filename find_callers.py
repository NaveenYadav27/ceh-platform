"""Find all callers of renderSidebar and updateTopbar and updateProgress"""
with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = ['renderSidebar', 'updateTopbar', 'updateProgress', 'renderLMSDashboard', 'bootApp', 'checkAuth']

for name in targets:
    print(f"\n=== {name} callers ===")
    for i, line in enumerate(lines, 1):
        if name in line and i > 673:  # only in JS section
            print(f"  L{i}: {line.rstrip()[:120].encode('ascii','ignore').decode()}")
