import os, re

search_dir = '.'
pattern = re.compile(r'TOPIC_STUBS', re.IGNORECASE)
skip_dirs = {'node_modules', '.git'}
results = []

for root, dirs, files in os.walk(search_dir):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for fname in files:
        if fname.endswith(('.html', '.js', '.ts', '.py', '.css', '.json')):
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        if pattern.search(line):
                            results.append(f"{fpath}:{i}: {line.rstrip()[:120]}")
            except Exception as e:
                results.append(f"ERROR reading {fpath}: {e}")

if results:
    print(f"TOPIC_STUBS references found ({len(results)}):")
    for r in results:
        print(r)
else:
    print("CONFIRMED: TOPIC_STUBS has ZERO references in the project.")
