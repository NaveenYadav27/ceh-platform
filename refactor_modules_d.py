import re

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

m16_replacement = """{ id: 'm16', name: 'Phase 16: Network Security Specialist (Wireless Networks)', topics: [
      { id: 'wireless-concepts', name: 'Wireless Concepts' },
      { id: 'wireless-encryption', name: 'Wireless Encryption' },
      { id: 'wireless-threats', name: 'Wireless Threats & Attacks' },
      { id: 'wireless-hacking-tools', name: 'Wireless Hacking Tools' }
    ]}"""

m17_replacement = """{ id: 'm17', name: 'Phase 17: Mobile Security Expert (Mobile Platforms)', topics: [
      { id: 'mobile-concepts', name: 'Mobile Platform Architecture' },
      { id: 'android-hacking', name: 'Android Hacking' },
      { id: 'ios-hacking', name: 'iOS Hacking' },
      { id: 'mobile-security-tools', name: 'Mobile Security Tools' }
    ]}"""

m18_replacement = """{ id: 'm18', name: 'Phase 18: OT/IoT Security Specialist (IoT & OT Hacking)', topics: [
      { id: 'iot-concepts', name: 'IoT Concepts & Architecture' },
      { id: 'ot-concepts', name: 'OT Concepts & Architecture' },
      { id: 'iot-ot-threats', name: 'IoT & OT Threats' },
      { id: 'iot-ot-hacking-tools', name: 'IoT & OT Hacking Tools' }
    ]}"""

m19_replacement = """{ id: 'm19', name: 'Phase 19: Cloud Security Architect (Cloud Computing)', topics: [
      { id: 'cloud-concepts', name: 'Cloud Computing Concepts' },
      { id: 'cloud-threats', name: 'Cloud Threats & Attacks' },
      { id: 'cloud-architecture', name: 'Cloud Security Architecture' },
      { id: 'cloud-security-tools', name: 'Cloud Security Tools' }
    ]}"""

m20_replacement = """{ id: 'm20', name: 'Phase 20: Cryptography Expert (Cryptography)', topics: [
      { id: 'crypto-concepts', name: 'Cryptography Concepts' },
      { id: 'encryption-algorithms', name: 'Encryption Algorithms' },
      { id: 'pki-concepts', name: 'Public Key Infrastructure (PKI)' },
      { id: 'crypto-attacks', name: 'Cryptography Attacks' }
    ]}"""

content = re.sub(r"\{\s*id:\s*'m16'.*?\]\}", m16_replacement, content, flags=re.DOTALL)
content = re.sub(r"\{\s*id:\s*'m17'.*?\]\}", m17_replacement, content, flags=re.DOTALL)
content = re.sub(r"\{\s*id:\s*'m18'.*?\]\}", m18_replacement, content, flags=re.DOTALL)
content = re.sub(r"\{\s*id:\s*'m19'.*?\]\}", m19_replacement, content, flags=re.DOTALL)
content = re.sub(r"\{\s*id:\s*'m20'.*?\]\}", m20_replacement, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated MODULES array for M16-M20")
