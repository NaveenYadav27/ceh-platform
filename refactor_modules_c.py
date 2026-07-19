import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

m11_replacement = """{ id: 'm11', name: 'Phase 11: Application Security Analyst (Session Hijacking)', topics: [
      { id: 'session-hijacking-concepts', name: 'Session Hijacking Concepts' },
      { id: 'application-level-hijacking', name: 'Application Level Hijacking' },
      { id: 'network-level-hijacking', name: 'Network Level Hijacking' },
      { id: 'session-hijacking-tools', name: 'Session Hijacking Tools & Countermeasures' }
    ]}"""

m12_replacement = """{ id: 'm12', name: 'Phase 12: Advanced Penetration Tester (Evading IDS/Firewalls)', topics: [
      { id: 'ids-firewall-concepts', name: 'IDS & Firewall Concepts' },
      { id: 'evasion-techniques', name: 'Evasion Techniques' },
      { id: 'honeypot-concepts', name: 'Honeypot Architecture' },
      { id: 'evasion-tools', name: 'Evasion Tools & Countermeasures' }
    ]}"""

m13_replacement = """{ id: 'm13', name: 'Phase 13: Web Application Pentester (Web Server Hacking)', topics: [
      { id: 'web-server-concepts', name: 'Web Server Concepts' },
      { id: 'web-server-attacks', name: 'Web Server Attacks' },
      { id: 'web-server-attack-methodology', name: 'Attack Methodology' },
      { id: 'web-server-security-tools', name: 'Security Tools & Countermeasures' }
    ]}"""

m14_replacement = """{ id: 'm14', name: 'Phase 14: Web Application Pentester (Hacking Web Applications)', topics: [
      { id: 'web-app-concepts', name: 'Web App Architecture & Concepts' },
      { id: 'web-app-threats', name: 'Web App Threats (OWASP Top 10)' },
      { id: 'web-app-hacking-methodology', name: 'Web App Hacking Methodology' },
      { id: 'web-app-security-tools', name: 'Web App Security Tools' }
    ]}"""

m15_replacement = """{ id: 'm15', name: 'Phase 15: Database Security Specialist (SQL Injection)', topics: [
      { id: 'sqli-concepts', name: 'SQL Injection Concepts' },
      { id: 'sqli-types', name: 'Types of SQL Injection' },
      { id: 'sqli-methodology', name: 'SQLi Methodology' },
      { id: 'sqli-tools', name: 'SQLi Tools & Countermeasures' }
    ]}"""

# Replace M11
content = re.sub(
    r"\{\s*id:\s*'m11'.*?\]\}",
    m11_replacement,
    content,
    flags=re.DOTALL
)

# Replace M12
content = re.sub(
    r"\{\s*id:\s*'m12'.*?\]\}",
    m12_replacement,
    content,
    flags=re.DOTALL
)

# Replace M13
content = re.sub(
    r"\{\s*id:\s*'m13'.*?\]\}",
    m13_replacement,
    content,
    flags=re.DOTALL
)

# Replace M14
content = re.sub(
    r"\{\s*id:\s*'m14'.*?\]\}",
    m14_replacement,
    content,
    flags=re.DOTALL
)

# Replace M15
content = re.sub(
    r"\{\s*id:\s*'m15'.*?\]\}",
    m15_replacement,
    content,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated MODULES array for M11-M15")
