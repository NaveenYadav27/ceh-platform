import re

def fix_all(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Branding Fixes (Be resilient to exact whitespace)
    # The original logo was: <span style="color:var(--cyber-red);">X</span> SHADOWXLAB
    html = html.replace('>X</span> SHADOWXLAB', '>GFS</span> CYBER DEFENSE')
    html = re.sub(r'CEH v13(\s*)<span class="neon-text-cyan">AI POWERED</span><br/>', r'GLOBAL FINANCIAL\1<span class="neon-text-cyan">SERVICES</span><br/>', html)
    html = re.sub(r'ETHICAL <span class="neon-text-red">HACKING</span>', r'CYBER <span class="neon-text-red">DEFENSE</span>', html)
    
    html = html.replace('Launch Cyber Range', 'Start Shift')
    html = html.replace('Explore Labs', 'View Assignments')
    
    html = html.replace('12.5K+', '1,250+')
    html = html.replace('Operators Trained', 'Active Analysts')
    html = html.replace('246+', '24+')
    html = html.replace('Live Labs', 'Active Incidents')
    html = html.replace('99.9%', '100%')
    html = html.replace('Range Uptime', 'Threat Mitigation')
    
    # Dashboard labels
    html = html.replace('lms-mod-num">MODULE ', 'lms-mod-num">PHASE ')
    html = html.replace(' Topics</span>', ' Tasks</span>')
    html = html.replace(' Topics</th>', ' Tasks</th>')
    html = html.replace('<th>Topics</th>', '<th>Tasks</th>')

    # 2. Module Names (m01 - m06)
    roles = [
        "Phase 01: Security Analyst Trainee",
        "Phase 02: Threat Intelligence Analyst",
        "Phase 03: Vulnerability Assessment Analyst",
        "Phase 04: Vulnerability Assessment Analyst",
        "Phase 05: Vulnerability Management Specialist",
        "Phase 06: Junior Penetration Tester"
    ]
    orig_names = [
        "Introduction to Ethical Hacking",
        "Footprinting & Reconnaissance",
        "Scanning Networks",
        "Enumeration",
        "Vulnerability Analysis",
        "System Hacking"
    ]
    for i in range(6):
        # We need to replace name:'Introduction to Ethical Hacking' or name:"Introduction to Ethical Hacking"
        pattern = r"name:\s*['\"]" + re.escape(orig_names[i]) + r"['\"]"
        replacement = f"name: '{roles[i]} ({orig_names[i]})'"
        html = re.sub(pattern, replacement, html)
        # Also replace in the sidebar rendering string if it exists
        html = html.replace(f'>{orig_names[i]}<', f'>{roles[i]}<')


    # 3. Content Injection for m07 - m20
    # We will use re.sub with a regex that captures id: 'm07' until the matching closing bracket of the topics array.
    # To do this safely, we will match up to `]}` because each module ends with `]}` or `]},`.
    
    m07 = """id: 'm07', name: 'Phase 07: Malware Analyst (Malware Threats)', topics: [
      { id: 't07_01', title: 'Malware Concepts & Analysis', type: 'lab', completed: false, scenario: 'GFS Threat Intel has flagged a suspicious email attachment received by our CFO. Your task is to safely analyze this payload.', commands: [{os:'Windows',cmd:'certutil -hashfile suspicious.exe SHA256'}], summary: ['Static vs Dynamic Analysis', 'Identify malware families'], ctf: {scenario: 'Find the malware family name on VirusTotal', flag: 'TrickBot', points: 50, hint: 'Search hash'} },
      { id: 't07_02', title: 'Fileless Malware', type: 'theory', completed: false, scenario: 'EDR triggered an alert for anomalous PowerShell execution on a GFS workstation. Investigate memory.', commands: [{os:'Windows',cmd:'Get-Process | Where-Object {$_.Name -eq "powershell"}'}], summary: ['Fileless malware uses LotL', 'No disk footprint'], ctf: {scenario: 'Decode the base64 payload', flag: 'GFS_MEM', points: 50, hint: 'Base64 decode'} }
    ]"""

    m08 = """id: 'm08', name: 'Phase 08: Network Security Analyst (Sniffing)', topics: [
      { id: 't08_01', title: 'Network Sniffing Concepts', type: 'lab', completed: false, scenario: 'A rogue device was plugged into the GFS Datacenter switch. Perform a packet capture.', commands: [{os:'Linux',cmd:'tcpdump -i eth0 -w cap.pcap'}], summary: ['Active vs Passive Sniffing', 'Promiscuous Mode'], ctf: {scenario: 'Extract the plaintext password', flag: 'p4ssw0rd', points: 50, hint: 'Filter HTTP'} },
      { id: 't08_02', title: 'Spoofing & MITM', type: 'theory', completed: false, scenario: 'Investigate the network segment for ARP poisoning indicating a Man-in-the-Middle attack.', commands: [{os:'Linux',cmd:'arp -a'}], summary: ['ARP Poisoning', 'DHCP Spoofing'], ctf: {scenario: 'Identify the MAC vendor', flag: 'Cisco', points: 50, hint: 'OUI lookup'} }
    ]"""

    m09 = """id: 'm09', name: 'Phase 09: Security Awareness Officer (Social Engineering)', topics: [
      { id: 't09_01', title: 'Phishing Campaigns', type: 'lab', completed: false, scenario: 'GFS employees received phishing emails. Analyze the email headers to identify the true sender.', commands: [{os:'Linux',cmd:'whois gfs-hr-bonus.com'}], summary: ['Spear-phishing', 'Header Analysis'], ctf: {scenario: 'Extract the hidden domain', flag: 'login.php', points: 50, hint: 'URL decode'} }
    ]"""

    m10 = """id: 'm10', name: 'Phase 10: Network Defense Analyst (Denial of Service)', topics: [
      { id: 't10_01', title: 'DDoS Mitigation', type: 'lab', completed: false, scenario: 'The GFS trading API is experiencing a SYN flood. Implement mitigation.', commands: [{os:'Linux',cmd:'netstat -n | grep SYN_RECV'}], summary: ['SYN Flood', 'Volumetric Attacks'], ctf: {scenario: 'Identify the attack type', flag: 'Slowloris', points: 50, hint: 'Slow HTTP POST'} }
    ]"""
    
    m11 = """id: 'm11', name: 'Phase 11: Application Security Analyst (Session Hijacking)', topics: [
      { id: 't11_01', title: 'Session Hijacking', type: 'lab', completed: false, scenario: 'Investigate an active user session hijacked from a remote location.', commands: [{os:'Linux',cmd:'ettercap -T -q -M arp'}], summary: ['Session theft', 'Prevention via HTTPS'], ctf: {scenario: 'Extract the stolen cookie', flag: 'PHPSESSID', points: 50, hint: 'Check headers'} }
    ]"""
    
    m12 = """id: 'm12', name: 'Phase 12: Advanced Penetration Tester (Evading IDS/Firewalls)', topics: [
      { id: 't12_01', title: 'Firewall Evasion', type: 'lab', completed: false, scenario: 'Verify if the new GFS NGFW detects fragmented packets.', commands: [{os:'Linux',cmd:'nmap -f -D 10.10.1.10 10.10.50.5'}], summary: ['Fragmentation', 'Decoy Scans'], ctf: {scenario: 'Identify the evasion technique', flag: 'Fragmentation', points: 50, hint: 'MTU'} }
    ]"""

    m13 = """id: 'm13', name: 'Phase 13: Web Application Pentester (Web Server Hacking)', topics: [
      { id: 't13_01', title: 'Web Server Attacks', type: 'lab', completed: false, scenario: 'Audit the GFS internal wiki server for misconfigurations.', commands: [{os:'Linux',cmd:'nikto -h http://wiki'}], summary: ['Directory Traversal', 'Banner Grabbing'], ctf: {scenario: 'Grab the Apache banner', flag: 'Apache/2.4', points: 50, hint: 'curl -I'} }
    ]"""
    
    m14 = """id: 'm14', name: 'Phase 14: Web Application Pentester (Hacking Web Applications)', topics: [
      { id: 't14_01', title: 'OWASP Top 10', type: 'lab', completed: false, scenario: 'Perform DAST on the GFS Customer Portal to identify XSS and CSRF.', commands: [{os:'Linux',cmd:'wpscan --url'}], summary: ['XSS, CSRF, IDOR', 'SQLi'], ctf: {scenario: 'Find the XSS payload', flag: 'alert()', points: 50, hint: 'Basic script tag'} }
    ]"""
    
    m15 = """id: 'm15', name: 'Phase 15: Database Security Specialist (SQL Injection)', topics: [
      { id: 't15_01', title: 'SQL Injection', type: 'lab', completed: false, scenario: 'Test the GFS HR database for blind SQL injection vulnerabilities.', commands: [{os:'Linux',cmd:'sqlmap --dbs'}], summary: ['In-band SQLi', 'Blind SQLi'], ctf: {scenario: 'Bypass the login prompt', flag: 'OR 1=1', points: 50, hint: 'Classic boolean'} }
    ]"""

    m16 = """id: 'm16', name: 'Phase 16: Wireless Security Specialist (Wireless Hacking)', topics: [
      { id: 't16_01', title: 'Wireless Security', type: 'lab', completed: false, scenario: 'Audit the new GFS branch WiFi to ensure it is not vulnerable to KRACK.', commands: [{os:'Linux',cmd:'airmon-ng start wlan0'}], summary: ['WPA2/WPA3', 'KRACK Attack'], ctf: {scenario: 'Crack the WPA2 handshake', flag: 'aircrack-ng', points: 50, hint: 'Wordlist'} }
    ]"""

    m17 = """id: 'm17', name: 'Phase 17: Mobile Security Engineer (Hacking Mobile Platforms)', topics: [
      { id: 't17_01', title: 'Mobile OS Vulnerabilities', type: 'lab', completed: false, scenario: 'Decompile the GFS trading APK to find hardcoded AWS credentials.', commands: [{os:'Linux',cmd:'apktool d app.apk'}], summary: ['Rooting/Jailbreaking', 'Reverse Engineering'], ctf: {scenario: 'Find the SMS permission', flag: 'READ_SMS', points: 50, hint: 'AndroidManifest'} }
    ]"""
    
    m18 = """id: 'm18', name: 'Phase 18: OT/IoT Security Researcher (IoT & OT Hacking)', topics: [
      { id: 't18_01', title: 'IoT & OT Security', type: 'lab', completed: false, scenario: 'Test the HVAC MQTT protocol for authentication bypass.', commands: [{os:'Linux',cmd:'mosquitto_sub -t "#"'}], summary: ['MQTT, CoAP', 'SCADA/ICS'], ctf: {scenario: 'Read the temperature topic', flag: '72F', points: 50, hint: 'Subscribe'} }
    ]"""
    
    m19 = """id: 'm19', name: 'Phase 19: Cloud Security Architect (Cloud Computing)', topics: [
      { id: 't19_01', title: 'Cloud Infrastructure Attacks', type: 'lab', completed: false, scenario: 'Identify misconfigured AWS S3 buckets leaking customer data.', commands: [{os:'Linux',cmd:'aws s3 ls'}], summary: ['Shared Responsibility', 'IAM misconfigs'], ctf: {scenario: 'Extract the Access Key', flag: 'AKIA', points: 50, hint: 'Metadata service'} }
    ]"""
    
    m20 = """id: 'm20', name: 'Phase 20: Cryptographic Specialist (Cryptography)', topics: [
      { id: 't20_01', title: 'Applied Cryptography', type: 'lab', completed: false, scenario: 'Analyze the ransomware encryption implementation on the GFS database.', commands: [{os:'Linux',cmd:'hashcat -m 1000'}], summary: ['Symmetric/Asymmetric', 'Hashing'], ctf: {scenario: 'Crack the MD5 hash', flag: 'hello', points: 50, hint: 'Hash cracking'} }
    ]"""

    contents = [m07, m08, m09, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]
    
    for i in range(7, 21):
        mod_id = f"m{i:02d}"
        # We replace the entire `{ id:'mXX', ... topics:[ ... ] }` structure.
        # Find `{ id:'mXX',` or `{ id:"mXX",` and replace up until the matching closing brace of the topics array.
        # A simple way is to match from `id\s*:\s*['"]mXX['"]` up to `]`
        pattern = r"id\s*:\s*['\"]" + mod_id + r"['\"].*?topics\s*:\s*\[.*?\]"
        # We also need to insert the curly brace if we replace it.
        # Actually, let's just replace the id, name, and topics block.
        def repl(match, content=contents[i-7]):
            return content
            
        html = re.sub(pattern, lambda m, c=contents[i-7]: c, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("All modules correctly fixed.")

fix_all('frontend/index.html')
