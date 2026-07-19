import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

m07_replacement = """{ id: 'm07', name: 'Phase 07: Malware Analyst (Malware Threats)', topics: [
      { id: 'malware-concepts', name: 'Malware Concepts' },
      { id: 'trojans-backdoors', name: 'Trojans & Backdoors' },
      { id: 'viruses-worms', name: 'Viruses & Worms' },
      { id: 'fileless-malware', name: 'Fileless Malware' },
      { id: 'malware-analysis', name: 'Malware Analysis' }
    ]}"""

m08_replacement = """{ id: 'm08', name: 'Phase 08: Network Security Analyst (Sniffing)', topics: [
      { id: 'sniffing-concepts', name: 'Sniffing Concepts' },
      { id: 'mac-attacks', name: 'MAC Attacks' },
      { id: 'dhcp-attacks', name: 'DHCP Attacks' },
      { id: 'arp-poisoning', name: 'ARP Poisoning' },
      { id: 'spoofing-mitm', name: 'Spoofing & MITM' }
    ]}"""

m09_replacement = """{ id: 'm09', name: 'Phase 09: Security Awareness Officer (Social Engineering)', topics: [
      { id: 'social-engineering-concepts', name: 'Social Engineering Concepts' },
      { id: 'phishing-campaigns', name: 'Phishing Campaigns' },
      { id: 'insider-threats', name: 'Insider Threats' },
      { id: 'impersonation', name: 'Impersonation & Pretexting' }
    ]}"""

m10_replacement = """{ id: 'm10', name: 'Phase 10: Network Defense Analyst (Denial of Service)', topics: [
      { id: 'dos-concepts', name: 'DoS/DDoS Concepts' },
      { id: 'botnets', name: 'Botnets' },
      { id: 'dos-attack-techniques', name: 'Attack Techniques' },
      { id: 'ddos-mitigation', name: 'DDoS Mitigation' }
    ]}"""

# Replace M07
content = re.sub(
    r"\{\s*id:\s*'m07'.*?\]\}",
    m07_replacement,
    content,
    flags=re.DOTALL
)

# Replace M08
content = re.sub(
    r"\{\s*id:\s*'m08'.*?\]\}",
    m08_replacement,
    content,
    flags=re.DOTALL
)

# Replace M09
content = re.sub(
    r"\{\s*id:\s*'m09'.*?\]\}",
    m09_replacement,
    content,
    flags=re.DOTALL
)

# Replace M10
content = re.sub(
    r"\{\s*id:\s*'m10'.*?\]\}",
    m10_replacement,
    content,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated MODULES array for M07-M10")
