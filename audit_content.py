import re

content = open('frontend/index.html', encoding='utf-8').read()

# CONTENT coverage
content_matches = re.findall(r"CONTENT\['([^']+)'\]\s*=", content)
print(f"CONTENT topics with full data: {len(content_matches)}")
for k in content_matches:
    print(f"  {k}")

# M01 topic presence
m01_topics = [
    'info-security-overview','hacker-classes','ethical-hacking-concepts',
    'hacking-methodologies','security-controls','security-laws'
]
print("\nM01 topic CONTENT check:")
for tid in m01_topics:
    has = f"CONTENT['{tid}']" in content or f'CONTENT["{tid}"]' in content
    in_stubs = f"TOPIC_STUBS['{tid}']" in content
    print(f"  {tid}: {'CONTENT' if has else ('STUB' if in_stubs else 'MISSING')}")

# Module topic counts
module_blocks = re.findall(r"{ id:'(m\d+)'.*?topics:\[(.*?)\]\s*}", content, re.DOTALL)
print(f"\nModule topic counts:")
for mid, tblock in module_blocks:
    tc = tblock.count('{id:') + tblock.count("{ id:")
    print(f"  {mid}: {tc} topics")
