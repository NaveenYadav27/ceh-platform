import re

def fix_modules(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the exact string where m07 starts (it could be broken, but it should be the first instance of m07)
    # The safest way is to find `{ id: 'm07'` and the `];` that ends the MODULES array.
    
    start_match = re.search(r"\{\s*id:\s*['\"]m07['\"].*?name:.*?", html)
    if not start_match:
        print("Could not find start of m07")
        return
        
    start_idx = start_match.start()
    
    # Find the `];` that closes MODULES
    # We look for `];` after the start_idx
    end_idx = html.find('];\n\nconst STATE = {', start_idx)
    if end_idx == -1:
        # fallback if exact string isn't found
        end_idx = html.find('];', start_idx)
        
    if end_idx == -1:
        print("Could not find end of MODULES array")
        return
        
    # The new content for m07 through m20
    new_content = """{ id: 'm07', name: 'Phase 07: Malware Analyst (Malware Threats)', topics: [
      { id: 't07_01', title: 'Malware Concepts & Analysis', type: 'lab', completed: false, scenario: 'GFS Threat Intel has flagged a suspicious email attachment received by our CFO. Your task is to safely analyze this payload.', commands: [{name:'certutil', cmd:'certutil -hashfile suspicious.exe SHA256', desc:'Generates file hashes to verify payload integrity against known IOCs.'}], summary: ['Static vs Dynamic Analysis', 'Identify malware families'], ctf: {scenario: 'Find the malware family name on VirusTotal', flag: 'TrickBot', points: 50, hint: 'Search hash'} },
      { id: 't07_02', title: 'Fileless Malware', type: 'theory', completed: false, scenario: 'EDR triggered an alert for anomalous PowerShell execution on a GFS workstation. Investigate memory.', commands: [{name:'PowerShell', cmd:'Get-Process | Where-Object {$_.Name -eq "powershell"}', desc:'Queries active processes to hunt for fileless malware executing in memory.'}], summary: ['Fileless malware uses LotL', 'No disk footprint'], ctf: {scenario: 'Decode the base64 payload', flag: 'GFS_MEM', points: 50, hint: 'Base64 decode'} }
    ]},
    { id: 'm08', name: 'Phase 08: Network Security Analyst (Sniffing)', topics: [
      { id: 't08_01', title: 'Network Sniffing Concepts', type: 'lab', completed: false, scenario: 'A rogue device was plugged into the GFS Datacenter switch. Perform a packet capture.', commands: [{name:'tcpdump', cmd:'tcpdump -i eth0 -w cap.pcap', desc:'Command-line packet analyzer for network troubleshooting and monitoring.'}], summary: ['Active vs Passive Sniffing', 'Promiscuous Mode'], ctf: {scenario: 'Extract the plaintext password', flag: 'p4ssw0rd', points: 50, hint: 'Filter HTTP'} },
      { id: 't08_02', title: 'Spoofing & MITM', type: 'theory', completed: false, scenario: 'Investigate the network segment for ARP poisoning indicating a Man-in-the-Middle attack.', commands: [{name:'ARP Utility', cmd:'arp -a', desc:'Displays the current ARP cache tables for all interfaces to detect spoofing.'}], summary: ['ARP Poisoning', 'DHCP Spoofing'], ctf: {scenario: 'Identify the MAC vendor', flag: 'Cisco', points: 50, hint: 'OUI lookup'} }
    ]},
    { id: 'm09', name: 'Phase 09: Security Awareness Officer (Social Engineering)', topics: [
      { id: 't09_01', title: 'Phishing Campaigns', type: 'lab', completed: false, scenario: 'GFS employees received phishing emails. Analyze the email headers to identify the true sender.', commands: [{name:'WHOIS', cmd:'whois gfs-hr-bonus.com', desc:'Queries the WHOIS database to identify the registered owner of the phishing domain.'}], summary: ['Spear-phishing', 'Header Analysis'], ctf: {scenario: 'Extract the hidden domain', flag: 'login.php', points: 50, hint: 'URL decode'} }
    ]},
    { id: 'm10', name: 'Phase 10: Network Defense Analyst (Denial of Service)', topics: [
      { id: 't10_01', title: 'DDoS Mitigation', type: 'lab', completed: false, scenario: 'The GFS trading API is experiencing a SYN flood. Implement mitigation.', commands: [{name:'netstat', cmd:'netstat -n | grep SYN_RECV', desc:'Displays active TCP connections, filtering for incomplete handshakes indicative of a SYN flood.'}], summary: ['SYN Flood', 'Volumetric Attacks'], ctf: {scenario: 'Identify the attack type', flag: 'Slowloris', points: 50, hint: 'Slow HTTP POST'} }
    ]},
    { id: 'm11', name: 'Phase 11: Application Security Analyst (Session Hijacking)', topics: [
      { id: 't11_01', title: 'Session Hijacking', type: 'lab', completed: false, scenario: 'Investigate an active user session hijacked from a remote location.', commands: [{name:'Ettercap', cmd:'ettercap -T -q -M arp', desc:'Comprehensive suite for man-in-the-middle attacks, used here defensively to monitor ARP caches.'}], summary: ['Session theft', 'Prevention via HTTPS'], ctf: {scenario: 'Extract the stolen cookie', flag: 'PHPSESSID', points: 50, hint: 'Check headers'} }
    ]},
    { id: 'm12', name: 'Phase 12: Advanced Penetration Tester (Evading IDS/Firewalls)', topics: [
      { id: 't12_01', title: 'Firewall Evasion', type: 'lab', completed: false, scenario: 'Verify if the new GFS NGFW detects fragmented packets.', commands: [{name:'Nmap', cmd:'nmap -f -D 10.10.1.10 10.10.50.5', desc:'Uses fragmented IP packets and decoys to test IDS/IPS evasion capabilities.'}], summary: ['Fragmentation', 'Decoy Scans'], ctf: {scenario: 'Identify the evasion technique', flag: 'Fragmentation', points: 50, hint: 'MTU'} }
    ]},
    { id: 'm13', name: 'Phase 13: Web Application Pentester (Web Server Hacking)', topics: [
      { id: 't13_01', title: 'Web Server Attacks', type: 'lab', completed: false, scenario: 'Audit the GFS internal wiki server for misconfigurations.', commands: [{name:'Nikto', cmd:'nikto -h http://wiki', desc:'Open-source web server scanner that tests for dangerous files, outdated server software, and vulnerabilities.'}], summary: ['Directory Traversal', 'Banner Grabbing'], ctf: {scenario: 'Grab the Apache banner', flag: 'Apache/2.4', points: 50, hint: 'curl -I'} }
    ]},
    { id: 'm14', name: 'Phase 14: Web Application Pentester (Hacking Web Applications)', topics: [
      { id: 't14_01', title: 'OWASP Top 10', type: 'lab', completed: false, scenario: 'Perform DAST on the GFS Customer Portal to identify XSS and CSRF.', commands: [{name:'WPScan', cmd:'wpscan --url', desc:'Black box vulnerability scanner used to audit the security of web platforms.'}], summary: ['XSS, CSRF, IDOR', 'SQLi'], ctf: {scenario: 'Find the XSS payload', flag: 'alert()', points: 50, hint: 'Basic script tag'} }
    ]},
    { id: 'm15', name: 'Phase 15: Database Security Specialist (SQL Injection)', topics: [
      { id: 't15_01', title: 'SQL Injection', type: 'lab', completed: false, scenario: 'Test the GFS HR database for blind SQL injection vulnerabilities.', commands: [{name:'SQLMap', cmd:'sqlmap --dbs', desc:'Automatic SQL injection and database takeover tool to map out database structures.'}], summary: ['In-band SQLi', 'Blind SQLi'], ctf: {scenario: 'Bypass the login prompt', flag: 'OR 1=1', points: 50, hint: 'Classic boolean'} }
    ]},
    { id: 'm16', name: 'Phase 16: Wireless Security Specialist (Wireless Hacking)', topics: [
      { id: 't16_01', title: 'Wireless Security', type: 'lab', completed: false, scenario: 'Audit the new GFS branch WiFi to ensure it is not vulnerable to KRACK.', commands: [{name:'Airmon-ng', cmd:'airmon-ng start wlan0', desc:'Enables monitor mode on wireless interfaces for auditing and packet capture.'}], summary: ['WPA2/WPA3', 'KRACK Attack'], ctf: {scenario: 'Crack the WPA2 handshake', flag: 'aircrack-ng', points: 50, hint: 'Wordlist'} }
    ]},
    { id: 'm17', name: 'Phase 17: Mobile Security Engineer (Hacking Mobile Platforms)', topics: [
      { id: 't17_01', title: 'Mobile OS Vulnerabilities', type: 'lab', completed: false, scenario: 'Decompile the GFS trading APK to find hardcoded AWS credentials.', commands: [{name:'Apktool', cmd:'apktool d app.apk', desc:'Tool for reverse engineering third party, closed, binary Android apps.'}], summary: ['Rooting/Jailbreaking', 'Reverse Engineering'], ctf: {scenario: 'Find the SMS permission', flag: 'READ_SMS', points: 50, hint: 'AndroidManifest'} }
    ]},
    { id: 'm18', name: 'Phase 18: OT/IoT Security Researcher (IoT & OT Hacking)', topics: [
      { id: 't18_01', title: 'IoT & OT Security', type: 'lab', completed: false, scenario: 'Test the HVAC MQTT protocol for authentication bypass.', commands: [{name:'Mosquitto', cmd:'mosquitto_sub -t "#"', desc:'MQTT client used to subscribe to message topics and intercept IoT telemetry data.'}], summary: ['MQTT, CoAP', 'SCADA/ICS'], ctf: {scenario: 'Read the temperature topic', flag: '72F', points: 50, hint: 'Subscribe'} }
    ]},
    { id: 'm19', name: 'Phase 19: Cloud Security Architect (Cloud Computing)', topics: [
      { id: 't19_01', title: 'Cloud Infrastructure Attacks', type: 'lab', completed: false, scenario: 'Identify misconfigured AWS S3 buckets leaking customer data.', commands: [{name:'AWS CLI', cmd:'aws s3 ls', desc:'Command line interface for Amazon Web Services used here to list bucket contents.'}], summary: ['Shared Responsibility', 'IAM misconfigs'], ctf: {scenario: 'Extract the Access Key', flag: 'AKIA', points: 50, hint: 'Metadata service'} }
    ]},
    { id: 'm20', name: 'Phase 20: Cryptographic Specialist (Cryptography)', topics: [
      { id: 't20_01', title: 'Applied Cryptography', type: 'lab', completed: false, scenario: 'Analyze the ransomware encryption implementation on the GFS database.', commands: [{name:'Hashcat', cmd:'hashcat -m 1000', desc:'Advanced password recovery utility, used here to crack intercepted NTLM hashes.'}], summary: ['Symmetric/Asymmetric', 'Hashing'], ctf: {scenario: 'Crack the MD5 hash', flag: 'hello', points: 50, hint: 'Hash cracking'} }
    ]}
"""
    
    reconstructed = html[:start_idx] + new_content + html[end_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(reconstructed)
        print("MODULES array perfectly reconstructed.")

fix_modules('frontend/index.html')
