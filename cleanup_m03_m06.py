import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

topics = [
    # M03
    'network-scanning-overview', 'tcp-ip-scanning', 'nmap-techniques', 'hping3-scanning', 'banner-grabbing',
    # M04
    'enumeration-overview', 'netbios-smb', 'snmp-ldap', 'smtp-dns-enum',
    # M05
    'vuln-concepts', 'cve-cvss', 'nessus-openvas',
    # M06
    'password-cracking', 'privilege-escalation', 'maintaining-access', 'steganography'
]

for t in topics:
    # Match any CONTENT['topic'] = { ... }; block non-greedily
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
