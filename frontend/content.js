const MODULES = [
  { id:'m01', name: 'Phase 01: Security Analyst Trainee (Introduction to Ethical Hacking)', topics:[
    {id:'info-security-overview',name:'Information Security Overview'},
    {id:'hacker-classes',name:'Hacking Concepts & Hacker Classes'},
    {id:'ethical-hacking-concepts',name:'Ethical Hacking Concepts'},
    {id:'hacking-methodologies',name:'Hacking Methodologies & Frameworks'},
    {id:'security-controls',name:'Information Security Controls'},
    {id:'security-laws',name:'Information Security Laws & Standards'},
  ]},
  { id:'m02', name: 'Phase 02: Threat Intelligence Analyst (Footprinting & Reconnaissance)', topics:[
    {id:'footprinting-concepts',name:'Footprinting Concepts'},
    {id:'osint-techniques',name:'OSINT Techniques'},
    {id:'whois-dns',name:'Whois & DNS Footprinting'},
    {id:'google-hacking',name:'Google Hacking (Dorking)'},
    {id:'shodan-recon',name:'Shodan & Network Recon'},
    {id:'social-media-recon',name:'Social Media Footprinting'},
  ]},
  { id:'m03', name: 'Phase 03: Vulnerability Assessment Analyst (Scanning Networks)', topics:[
    {id:'network-scanning-overview',name:'Network Scanning Overview'},
    {id:'tcp-ip-scanning',name:'TCP/IP & Port Scanning'},
    {id:'nmap-techniques',name:'Nmap Scanning Techniques'},
    {id:'hping3-scanning',name:'Hping3 & Stealth Scanning'},
    {id:'banner-grabbing',name:'Banner Grabbing & OS Fingerprinting'},
  ]},
  { id:'m04', name: 'Phase 04: Vulnerability Assessment Analyst (Enumeration)', topics:[
    {id:'enumeration-overview',name:'Enumeration Concepts'},
    {id:'netbios-smb',name:'NetBIOS & SMB Enumeration'},
    {id:'snmp-ldap',name:'SNMP & LDAP Enumeration'},
    {id:'smtp-dns-enum',name:'SMTP & DNS Enumeration'},
  ]},
  { id:'m05', name: 'Phase 05: Vulnerability Management Specialist (Vulnerability Analysis)', topics:[
    {id:'vuln-concepts',name:'Vulnerability Assessment Concepts'},
    {id:'cve-cvss',name:'CVE, CVSS & NVD'},
    {id:'nessus-openvas',name:'Nessus & OpenVAS Scanning'},
  ]},
  { id:'m06', name: 'Phase 06: Junior Penetration Tester (System Hacking)', topics:[
    {id:'password-cracking',name:'Password Cracking Techniques'},
    {id:'privilege-escalation',name:'Privilege Escalation'},
    {id:'maintaining-access',name:'Maintaining Access & Rootkits'},
    {id:'steganography',name:'Steganography & Covering Tracks'},
  ]},
  { id: 'm07', name: 'Phase 07: Malware Analyst (Malware Threats)', topics: [
      { id: 'malware-concepts', name: 'Malware Concepts' },
      { id: 'trojans-backdoors', name: 'Trojans & Backdoors' },
      { id: 'viruses-worms', name: 'Viruses & Worms' },
      { id: 'fileless-malware', name: 'Fileless Malware' },
      { id: 'malware-analysis', name: 'Malware Analysis' }
    ]},
    { id: 'm08', name: 'Phase 08: Network Security Analyst (Sniffing)', topics: [
      { id: 'sniffing-concepts', name: 'Sniffing Concepts' },
      { id: 'mac-attacks', name: 'MAC Attacks' },
      { id: 'dhcp-attacks', name: 'DHCP Attacks' },
      { id: 'arp-poisoning', name: 'ARP Poisoning' },
      { id: 'spoofing-mitm', name: 'Spoofing & MITM' }
    ]},
    { id: 'm09', name: 'Phase 09: Security Awareness Officer (Social Engineering)', topics: [
      { id: 'social-engineering-concepts', name: 'Social Engineering Concepts' },
      { id: 'phishing-campaigns', name: 'Phishing Campaigns' },
      { id: 'insider-threats', name: 'Insider Threats' },
      { id: 'impersonation', name: 'Impersonation & Pretexting' }
    ]},
    { id: 'm10', name: 'Phase 10: Network Defense Analyst (Denial of Service)', topics: [
      { id: 'dos-concepts', name: 'DoS/DDoS Concepts' },
      { id: 'botnets', name: 'Botnets' },
      { id: 'dos-attack-techniques', name: 'Attack Techniques' },
      { id: 'ddos-mitigation', name: 'DDoS Mitigation' }
    ]},
    { id: 'm11', name: 'Phase 11: Application Security Analyst (Session Hijacking)', topics: [
      { id: 'session-hijacking-concepts', name: 'Session Hijacking Concepts' },
      { id: 'application-level-hijacking', name: 'Application Level Hijacking' },
      { id: 'network-level-hijacking', name: 'Network Level Hijacking' },
      { id: 'session-hijacking-tools', name: 'Session Hijacking Tools & Countermeasures' }
    ]},
    { id: 'm12', name: 'Phase 12: Advanced Penetration Tester (Evading IDS/Firewalls)', topics: [
      { id: 'ids-firewall-concepts', name: 'IDS & Firewall Concepts' },
      { id: 'evasion-techniques', name: 'Evasion Techniques' },
      { id: 'honeypot-concepts', name: 'Honeypot Architecture' },
      { id: 'evasion-tools', name: 'Evasion Tools & Countermeasures' }
    ]},
    { id: 'm13', name: 'Phase 13: Web Application Pentester (Web Server Hacking)', topics: [
      { id: 'web-server-concepts', name: 'Web Server Concepts' },
      { id: 'web-server-attacks', name: 'Web Server Attacks' },
      { id: 'web-server-attack-methodology', name: 'Attack Methodology' },
      { id: 'web-server-security-tools', name: 'Security Tools & Countermeasures' }
    ]},
    { id: 'm14', name: 'Phase 14: Web Application Pentester (Hacking Web Applications)', topics: [
      { id: 'web-app-concepts', name: 'Web App Architecture & Concepts' },
      { id: 'web-app-threats', name: 'Web App Threats (OWASP Top 10)' },
      { id: 'web-app-hacking-methodology', name: 'Web App Hacking Methodology' },
      { id: 'web-app-security-tools', name: 'Web App Security Tools' }
    ]},
    { id: 'm15', name: 'Phase 15: Database Security Specialist (SQL Injection)', topics: [
      { id: 'sqli-concepts', name: 'SQL Injection Concepts' },
      { id: 'sqli-types', name: 'Types of SQL Injection' },
      { id: 'sqli-methodology', name: 'SQLi Methodology' },
      { id: 'sqli-tools', name: 'SQLi Tools & Countermeasures' }
    ]},
    { id: 'm16', name: 'Phase 16: Network Security Specialist (Wireless Networks)', topics: [
      { id: 'wireless-concepts', name: 'Wireless Concepts' },
      { id: 'wireless-encryption', name: 'Wireless Encryption' },
      { id: 'wireless-threats', name: 'Wireless Threats & Attacks' },
      { id: 'wireless-hacking-tools', name: 'Wireless Hacking Tools' }
    ]},
    { id: 'm17', name: 'Phase 17: Mobile Security Expert (Mobile Platforms)', topics: [
      { id: 'mobile-concepts', name: 'Mobile Platform Architecture' },
      { id: 'android-hacking', name: 'Android Hacking' },
      { id: 'ios-hacking', name: 'iOS Hacking' },
      { id: 'mobile-security-tools', name: 'Mobile Security Tools' }
    ]},
    { id: 'm18', name: 'Phase 18: OT/IoT Security Specialist (IoT & OT Hacking)', topics: [
      { id: 'iot-concepts', name: 'IoT Concepts & Architecture' },
      { id: 'ot-concepts', name: 'OT Concepts & Architecture' },
      { id: 'iot-ot-threats', name: 'IoT & OT Threats' },
      { id: 'iot-ot-hacking-tools', name: 'IoT & OT Hacking Tools' }
    ]},
    { id: 'm19', name: 'Phase 19: Cloud Security Architect (Cloud Computing)', topics: [
      { id: 'cloud-concepts', name: 'Cloud Computing Concepts' },
      { id: 'cloud-threats', name: 'Cloud Threats & Attacks' },
      { id: 'cloud-architecture', name: 'Cloud Security Architecture' },
      { id: 'cloud-security-tools', name: 'Cloud Security Tools' }
    ]},
    { id: 'm20', name: 'Phase 20: Cryptography Expert (Cryptography)', topics: [
      { id: 'crypto-concepts', name: 'Cryptography Concepts' },
      { id: 'encryption-algorithms', name: 'Encryption Algorithms' },
      { id: 'pki-concepts', name: 'Public Key Infrastructure (PKI)' },
      { id: 'crypto-attacks', name: 'Cryptography Attacks' }
    ]}
];

const CONTENT = {
  'info-security-overview':{"module":"Module 01 \u2014 Introduction to Ethical Hacking","title":"Information Security Overview","sub":"Understanding the CIA Triad, threat landscape, and foundational security concepts in an enterprise context.","killchain":{"phase":"Pre-Attack Phase","mitre":"Foundation","desc":"Core concepts that underpin all CEH domains and attack methodologies."},"learn":{"simple":"<strong>DEFINITION & SIMPLE EXPLANATION</strong><br><br>Information security is the practice of protecting data from unauthorized access, modification, or destruction. In an enterprise environment like Global Financial Services (GFS), it means ensuring that customer data, trading algorithms, and internal communications remain secure against an ever-evolving threat landscape.<br><br><strong>ENTERPRISE BRIEFING</strong><br>As a Security Analyst at GFS, your primary mission is to defend the CIA Triad (Confidentiality, Integrity, Availability) across all business units.","analogy":"<strong>ANALOGY</strong><br><br>Think of a bank vault. The CIA Triad are the three locks on the vault door.<br><ul><li><strong>Confidentiality:</strong> Only authorized people have the combination (Encryption, Access Control).</li><li><strong>Integrity:</strong> No one can tamper with the cash inside without it being detected (Hashing, Digital Signatures).</li><li><strong>Availability:</strong> The vault door opens quickly and reliably when the branch manager needs it (DDoS Protection, Redundancy).</li></ul><br><strong>5W1H CONTEXT</strong><br><strong>What:</strong> Protecting information assets.<br><strong>Why:</strong> To prevent financial loss and regulatory fines.<br><strong>Who:</strong> Security Analysts, Architects, and every employee.<br><strong>When:</strong> Continuous monitoring 24/7/365.<br><strong>Where:</strong> On-premise, cloud, and endpoints.<br><strong>How:</strong> People, Process, and Technology.","why":"<strong>THREAT INTELLIGENCE & BUSINESS CONTEXT (GFS)</strong><br><br>Without understanding security fundamentals, attackers exploit the gaps between policy and implementation. At GFS, a breach of confidentiality (e.g., leaked customer PII) violates GDPR and PCI-DSS, resulting in massive fines. A breach of integrity (tampered transaction records) destroys market trust.<br><br>Threat actors continuously probe GFS perimeters using automated reconnaissance, phishing, and zero-day exploits. Every penetration test starts with understanding what the target is trying to protect.","architecture":"<strong>TECHNICAL DEEP DIVE & ENTERPRISE WORKFLOW</strong><br><br>Information security operates across multiple defense layers: Physical (server rooms, badge access), Network (firewalls, IDS/IPS), and Application (input validation, authentication). The OSI model maps directly to these layers, and CEH attacks target each one.<br><br><strong>ENTERPRISE WORKFLOW:</strong><br>1. <strong>Identify:</strong> Asset inventory and data classification.<br>2. <strong>Protect:</strong> Implement firewalls, MFA, and encryption.<br>3. <strong>Detect:</strong> Deploy SIEM and IDS to monitor anomalies.<br>4. <strong>Respond:</strong> Incident Response (IR) team contains the threat.<br>5. <strong>Recover:</strong> Restore from encrypted backups and patch vulnerabilities."},"diagram":{"title":"Information Security Threat Lifecycle","steps":[{"icon":"\ud83d\udc64","label":"Threat Actor Emerges","desc":"An adversary identifies GFS as a target with valuable data or systems."},{"icon":"\ud83d\udd0d","label":"Reconnaissance","desc":"The attacker researches: open ports, employee names, software versions, IP ranges via OSINT."},{"icon":"\ud83d\udca5","label":"Exploit Vulnerability","desc":"A weakness is exploited \u2014 unpatched software, weak password, phishing, or misconfiguration."},{"icon":"\ud83d\udd13","label":"CIA Triad Violated","desc":"Data is stolen (Confidentiality), altered (Integrity), or systems go offline (Availability)."},{"icon":"\ud83d\udee1\ufe0f","label":"Detection & Response","desc":"SIEM, IDS, or SOC analysts detect anomaly and trigger the incident response process."},{"icon":"\ud83d\udccb","label":"Remediation & Lessons","desc":"Root cause fixed, controls updated, post-incident report filed to prevent recurrence."}]},"enterprise":{"gfs":"<strong>ENTERPRISE SCENARIO \u2014 GLOBALFINSEC CORP</strong><br>You are the Security Architect at GlobalFinSec Corp.<br><br><strong>SITUATION</strong><br>An external audit flagged three critical gaps: no asset inventory, no data classification policy, and no formal incident response plan \u2014 ahead of a PCI-DSS compliance deadline.<br><br><strong>YOUR CHALLENGE</strong><br>Map the CIA Triad to the top three assets (trading platform, customer database, internal email) and identify which controls are missing for each.","steps":["List the three assets and classify them by CIA priority (customer DB = highest Confidentiality need).","Run: `nmap -sV 192.168.1.0/24` to discover what services are exposed on each asset.","Check for missing patches on Windows hosts: `systeminfo | findstr \"OS Version\"`.","Identify existing controls (firewall? MFA? encryption?) and document gaps.","Write a one-page risk register: Asset, Threat, Vulnerability, CIA Impact, Recommended Control."],"outcome":"<strong>Outcome:</strong> You identified 12 missing controls. The trading platform lacked MFA (Confidentiality), the database had no encryption at rest (Confidentiality + Integrity), and email had no DLP (Confidentiality).<br><strong>Key Lesson:</strong> Every security investment must map to a CIA pillar. Without this framing, security spending cannot be justified to the board."},"tools":[{"name":"Nmap","desc":"Network discovery and port scanning.","cmd":"nmap -sV target"},{"name":"OpenVAS","desc":"Open-source vulnerability scanner.","cmd":"openvas-start"},{"name":"Nessus","desc":"Enterprise vulnerability scanner.","cmd":"service nessusd start"}],"commands":{"win":[{"cmd":"systeminfo","purpose":"Displays detailed configuration information about a computer and its operating system.","out":"Host Name: GFS-WKSTN-01\\nOS Name: Microsoft Windows 10 Enterprise\\nOS Version: 10.0.19044 N/A Build 19044","note":"Useful for identifying the exact OS build to find missing patches.","mistake":"Running without piping to `findstr` can overwhelm the terminal with output."},{"cmd":"net user","purpose":"Displays a list of all user accounts on the computer.","out":"User accounts for \\\\GFS-WKSTN-01\\n-------------------------------------------------------------------------------\\nAdministrator            Guest                    jdoe\\nThe command completed successfully.","note":"First step in local enumeration to find unauthorized accounts.","mistake":"Does not show domain users unless `/domain` switch is used."}],"lin":[{"cmd":"uname -a","purpose":"Print system information including kernel version.","out":"Linux GFS-DB-01 5.10.0-18-amd64 #1 SMP Debian 5.10.140-1 x86_64 GNU/Linux","note":"Critical for finding kernel exploits (e.g., Dirty COW).","mistake":"Relying only on `uname`; always check `/etc/os-release` as well."},{"cmd":"id","purpose":"Print real and effective user and group IDs.","out":"uid=1000(jdoe) gid=1000(jdoe) groups=1000(jdoe),27(sudo)","note":"Check if the compromised user is in the `sudo` group for privilege escalation.","mistake":"Forgetting to check the groups section which often hides lateral movement paths."},{"cmd":"cat /etc/passwd","purpose":"List all user accounts on the Linux system.","out":"root:x:0:0:root:/root:/bin/bash\\njdoe:x:1000:1000:John Doe,,,:/home/jdoe:/bin/bash","note":"Look for accounts with `/bin/bash` or `/bin/sh` to identify interactive users.","mistake":"Assuming passwords are in this file; they are hashed in `/etc/shadow`."}]},"pitfalls":[{"title":"Mistaking Compliance for Security","desc":"Passing a PCI-DSS or ISO audit does not mean you are secure. Compliance is a minimum bar, not a security guarantee.","fix":"Treat compliance as the floor. Layer additional threat-model-driven controls beyond regulatory minimums."},{"title":"Neglecting Availability in Security Planning","desc":"Security teams over-focus on Confidentiality (encryption, access control) and neglect Availability until a DDoS hits.","fix":"Include RTO/RPO metrics in all security plans. Regularly test failover and backup restoration."},{"title":"Treating Risk as a One-Time Assessment","desc":"A yearly risk assessment misses new vulnerabilities introduced by software updates, new vendors, and infrastructure changes.","fix":"Implement continuous risk monitoring. Reassess whenever major changes occur."},{"title":"Over-Relying on Perimeter Security","desc":"The castle-and-moat model assumes threats come from outside. Modern threats (insiders, cloud misconfigs) originate inside.","fix":"Adopt Zero Trust: verify every request as untrusted regardless of source location."}],"lab":{"title":"Enterprise Scenario: Information Security Core Concepts","scenario":"You are a junior SOC analyst at Global Financial Services. A new Linux server has been deployed in the DMZ without going through the standard security review process. You need to perform initial reconnaissance and identify the CIA triad implications of the current configuration.","objectives":["Perform basic local enumeration to identify the OS and users.","Determine the exposed services.","Correlate findings to CIA Triad risks."],"safety":["Ensure you have written authorization before scanning any GFS assets."],"dependencies":[],"steps":["Step 1: Open your Kali terminal.","Step 2: Identify your current privilege level: `id`.","Step 3: Check the system OS version: `uname -a` and `cat /etc/os-release`.","Step 4: View the active network connections to see what is exposed: `netstat -tulnp`.","Step 5: Review the local user accounts to see if default accounts exist: `cat /etc/passwd`."],"evidence":["Terminal output showing the OS version.","Terminal output showing open ports (e.g., port 22, 80)."],"validation":["You should be able to state exactly which services are running and what the impact would be if they were compromised (e.g., port 80 down = Availability impact)."],"troubleshooting":["If `netstat` is not found, use `ss -tulnp` instead."],"mitre":[{"id":"T1082","name":"System Information Discovery","tactic":"Discovery"}],"cleanup":["Clear your terminal history: `history -c`."]},"quiz":[{"type":"multiple-choice","difficulty":"Easy","q":"Which component of the CIA Triad ensures that information is accessible only to those authorized to have access?","opts":["Confidentiality","Integrity","Availability","Non-repudiation"],"correct":0,"fb":"Confidentiality ensures that data is kept secret from unauthorized entities, typically implemented through encryption and access controls."},{"type":"multiple-choice","difficulty":"Easy","q":"Which component of the CIA Triad ensures that information is not altered by unauthorized persons?","opts":["Confidentiality","Integrity","Availability","Authentication"],"correct":1,"fb":"Integrity guarantees that data has not been changed, destroyed, or lost in an unauthorized or accidental manner. Hashing is a common integrity control."},{"type":"multiple-choice","difficulty":"Easy","q":"A DDoS attack primarily targets which component of the CIA Triad?","opts":["Confidentiality","Integrity","Availability","Non-repudiation"],"correct":2,"fb":"Availability ensures that systems and data are accessible to authorized users when needed. DDoS attacks aim to disrupt this accessibility."},{"type":"multiple-choice","difficulty":"Intermediate","q":"Which of the following best describes 'Non-repudiation'?","opts":["Preventing unauthorized access to data.","Ensuring a sender cannot deny having sent a message.","Guaranteeing system uptime.","Hashing a file to verify its integrity."],"correct":1,"fb":"Non-repudiation ensures that a party to a transaction cannot deny having received a transaction nor can the other party deny having sent a transaction (e.g., using digital signatures)."},{"type":"multiple-choice","difficulty":"Intermediate","q":"What is the primary difference between a Vulnerability and an Exploit?","opts":["A vulnerability is a weakness; an exploit is a tool used to take advantage of it.","A vulnerability is a tool; an exploit is a weakness.","A vulnerability only applies to software; an exploit applies to hardware.","There is no difference; the terms are synonymous."],"correct":0,"fb":"A vulnerability is a flaw or weakness in system security procedures, design, implementation, or internal controls. An exploit is a defined way to breach the security of an IT system through a vulnerability."},{"type":"multiple-choice","difficulty":"Intermediate","q":"Which term describes a potential occurrence that can result in an unwanted outcome for an organization?","opts":["Vulnerability","Threat","Risk","Exploit"],"correct":1,"fb":"A threat is an event or condition that has the potential for causing asset loss and the undesirable consequences or impact from such loss."},{"type":"multiple-choice","difficulty":"Hard","q":"In risk management, how is Risk formally calculated?","opts":["Risk = Threat \u00d7 Vulnerability \u00d7 Asset Value","Risk = Threat + Vulnerability","Risk = Asset Value / Threat","Risk = Vulnerability \u00d7 Exploit"],"correct":0,"fb":"Risk is a function of the likelihood of a given threat-source exercising a particular potential vulnerability, and the resulting impact of that adverse event on the organization (Asset Value)."},{"type":"multiple-choice","difficulty":"Hard","q":"A company implements a biometric scanner to access the server room. This is an example of what type of security control?","opts":["Administrative Control","Technical (Logical) Control","Physical Control","Detective Control"],"correct":2,"fb":"Physical controls are tangible measures taken to protect systems and personnel (e.g., guards, locks, biometric scanners at doors)."},{"type":"true-false","difficulty":"Intermediate","q":"An Acceptable Use Policy (AUP) is an example of an Administrative Control.","opts":["True","False"],"correct":0,"fb":"True. Administrative controls are policies, procedures, and regulations that direct personnel on how to maintain security."},{"type":"multiple-choice","difficulty":"Intermediate","q":"Which of the following is considered a Detective Control?","opts":["Firewall","Intrusion Detection System (IDS)","Data Encryption","Security Guard"],"correct":1,"fb":"An IDS is a detective control designed to identify and alert on malicious activity after or as it occurs. A firewall is a preventative control."}],"flashcards":[{"f":"Confidentiality","b":"Ensuring data is only accessible to authorized individuals (e.g., via encryption)."},{"f":"Integrity","b":"Ensuring data is not altered or tampered with (e.g., via hashing)."},{"f":"Availability","b":"Ensuring systems and data are accessible when needed (e.g., via redundancy)."},{"f":"Non-repudiation","b":"Ensuring a sender cannot deny sending a message, often achieved via digital signatures."},{"f":"Vulnerability","b":"A weakness in a system, application, or process that can be exploited."},{"f":"Threat","b":"A potential danger that could exploit a vulnerability (e.g., a hacker, malware, natural disaster)."},{"f":"Exploit","b":"A piece of software, data, or sequence of commands that takes advantage of a vulnerability."},{"f":"Risk","b":"The potential for loss, damage, or destruction of an asset. (Threat \u00d7 Vulnerability \u00d7 Asset Value)."},{"f":"Physical Control","b":"Tangible security measures like locks, fences, and security guards."},{"f":"Administrative Control","b":"Policies, procedures, and training designed to direct human behavior (e.g., AUP)."}],"summary":["The CIA Triad (Confidentiality, Integrity, Availability) is the foundation of information security.","Security controls are categorized into Physical, Technical (Logical), and Administrative types.","Risk management involves identifying assets, threats, and vulnerabilities to calculate and mitigate risk.","Compliance with laws and standards (PCI-DSS, GDPR) is mandatory but does not equal complete security.","Modern enterprise security requires a defense-in-depth strategy, layering multiple controls."],"outcomes":["Define the core concepts of information security and the CIA Triad.","Differentiate between vulnerabilities, threats, exploits, and risks.","Identify and classify various types of security controls (Physical, Technical, Administrative).","Understand the importance of compliance frameworks in an enterprise context."]},

  'hacker-classes':{
    module:'Module 01 · Introduction to Ethical Hacking',
    title:'Hacking Concepts & Hacker Classes',
    sub:'Threat actor taxonomy, hacker motivations, and attack classification.',
    killchain:{phase:'Pre-Attack Phase',mitre:'TA0043 — Reconnaissance',desc:'Understanding who the adversary is determines the attack methodology to simulate.'},
    learn:{simple:'Hackers are broadly classified by their intent and authorization level. White hats hack with permission to improve security; black hats hack illegally for malicious gain; grey hats fall somewhere in between.',analogy:'Think of locksmiths: a licensed locksmith (white hat) uses the same skills as a burglar (black hat), but with permission. A grey hat is like someone who breaks in but then calls the owner to say the lock is weak.',why:'Understanding attacker motivations and categories helps defenders predict attack methods, model threats accurately, and build the right defenses.',architecture:'Categories include White Hat (ethical), Black Hat (criminal), Grey Hat (ambiguous), Hacktivists (ideology), APT/State-sponsored (espionage), Script Kiddies (low-skill), Insiders (trusted but malicious).'},
    tools:[{name:'Maltego',cmd:'maltego',desc:'OSINT and threat actor visualization'},{name:'theHarvester',cmd:'theharvester -d target.com -b all',desc:'Email and domain intelligence'}],
    commands:{win:['whoami /all','net user /domain','net group "Domain Admins" /domain'],lin:['id','groups','cat /etc/group','last']},
    ctf:{scenario:'A SOC alert fires: an insider with legitimate credentials is exfiltrating data to a personal Dropbox. What class of hacker are they?',hint:'They have authorized access but malicious intent...',flag:'CEH{wh1t3_gr3y_bl4ck_h4t}',points:100},
    quiz:[
      {q:'Which hacker type operates with full authorization?',opts:['Black Hat','Grey Hat','White Hat','Hacktivist'],correct:2,fb:'White hat hackers (ethical hackers/penetration testers) work with written permission from the target organization.'},
      {q:'A hacker who breaks in without permission but reports vulnerabilities to the vendor is called:',opts:['White Hat','Grey Hat','Black Hat','Script Kiddie'],correct:1,fb:'Grey hat hackers operate in a legal grey area — they may hack without permission but typically do not have malicious intent and may disclose findings.'},
      {q:'Anonymous and LulzSec are examples of:',opts:['APT Groups','Hacktivists','Script Kiddies','Insiders'],correct:1,fb:'Hacktivists use hacking to promote political or social agendas — Anonymous and LulzSec are well-known examples.'},
      {q:'What is the primary motivation of a state-sponsored APT group?',opts:['Financial gain','Fame','Espionage and geopolitical objectives','Social justice'],correct:2,fb:'Advanced Persistent Threats (APTs) backed by nation-states primarily aim for long-term espionage, IP theft, and disruption of critical infrastructure.'},
      {q:'A script kiddie is characterized by:',opts:['Advanced programming skills','Using pre-written tools without deep understanding','Nation-state backing','Professional authorization'],correct:1,fb:'Script kiddies use existing tools and exploits without understanding the underlying techniques — they pose a real threat despite limited skill.'},
      {q:'Which threat actor is hardest to detect and defend against?',opts:['Script Kiddie','External Black Hat','Malicious Insider','Hacktivist'],correct:2,fb:'Malicious insiders already have legitimate access, making their activities harder to distinguish from normal behavior.'},
      {q:'At GlobalFinCorp, an admin sells database credentials to a competitor. What actor type is this?',opts:['APT','Hacktivist','Malicious Insider','Script Kiddie'],correct:2,fb:'A malicious insider uses legitimate access for unauthorized or malicious purposes — the most dangerous threat in enterprise environments.'},
      {q:'A CEH is simulating an APT attack on a bank. Which approach should they take?',opts:['Quick hit-and-run scan','Long-term persistent simulation with multiple attack stages','Single vulnerability exploit','Social media scraping only'],correct:1,fb:'APT simulation (Red Team exercises) involves long-term persistent attack chains mimicking real state-sponsored actors, not single-shot scans.'},
      {q:'What legal document must a white hat hacker have before testing?',opts:['NDA only','Verbal agreement','Written authorization and Rules of Engagement','Business card'],correct:2,fb:'Written authorization (often called a Statement of Work or Rules of Engagement) is the legal foundation of all ethical hacking engagements.'},
      {q:'Which hacker class poses the greatest financial threat to organizations globally?',opts:['Hacktivists','Script Kiddies','Cybercriminal groups','Grey Hats'],correct:2,fb:'Organized cybercriminal groups (ransomware operators, financial fraud groups) cause the greatest financial losses globally, totaling trillions annually.'},
    ],
    flashcards:[
      {f:'White Hat',b:'Ethical hacker with written permission. Works to improve security.'},
      {f:'Black Hat',b:'Malicious hacker. No authorization. Criminal intent.'},
      {f:'Grey Hat',b:'Hacks without permission but usually reports findings. Legal grey area.'},
      {f:'Hacktivist',b:'Hacker motivated by political or social ideology (e.g., Anonymous).'},
      {f:'APT',b:'Advanced Persistent Threat — state-sponsored, long-term, stealthy attack campaigns.'},
      {f:'Insider Threat',b:'Malicious or negligent employee with legitimate system access.'},
      {f:'Script Kiddie',b:'Low-skill attacker using pre-made tools without understanding them.'},
    ],
    summary:[
      'Hacker classification is based on authorization and intent, not technical skill.',
      'APTs represent the most sophisticated threat — long-term, stealthy, state-backed.',
      'Insiders are the hardest threat to detect as they have legitimate access.',
      'Every ethical hacker must have written authorization before any testing.',
    ],
    diagram:{
      title:'Hacker Classification Decision Tree',
      steps:[
        {icon:'⚖️',label:'Assess Intent',desc:'Is the actor motivated by financial gain, ideology, espionage, curiosity, or authorized testing?'},
        {icon:'🔑',label:'Check Authorization',desc:'Does the actor have explicit written permission from the target? White hat = yes. Everyone else = no.'},
        {icon:'🎯',label:'Identify Target Type',desc:'Opportunistic (random victims) vs. targeted (specific org, person, or system)?'},
        {icon:'🛠️',label:'Evaluate Skill',desc:'Script kiddie (pre-built tools, zero understanding) vs. sophisticated (custom exploits, zero-days, persistence).'},
        {icon:'🏷️',label:'Apply Classification',desc:'White Hat, Grey Hat, Black Hat, Hacktivist, APT/Nation-State, Malicious Insider, or Script Kiddie.'},
        {icon:'🛡️',label:'Tailor Defenses',desc:'Match your defense investment to the most likely threat actors for your industry and data profile.'}
      ]
    },
    enterprise:{
      role:'You are the Threat Intelligence Analyst at GlobalFinSec Corp.',
      situation:'A SOC alert fires at 2 AM: a privileged database administrator is transferring 50GB of customer records to a personal Dropbox account.',
      challenge:'Classify this threat actor, determine their likely motivation, and recommend immediate containment actions.',
      steps:[
        'Pull the employee access logs for the past 30 days — is this the first anomalous transfer?',
        'Check HR records — any recent performance reviews, disciplinary actions, or resignation notices?',
        'Verify if the destination IP is on threat intelligence blocklists (VirusTotal, AbuseIPDB).',
        'Classify: this is a Malicious Insider — authorized access, clearly malicious intent.',
        'Trigger the Insider Threat IR playbook: disable account, preserve forensic evidence, notify Legal and HR.'
      ],
      outcome:'The employee was a departing staff member harvesting customer PII for a competitor. Early DLP and UEBA detection prevented full exfiltration. The employee was prosecuted under the CFAA.',
      lesson:'Insiders are the hardest threat to detect because their traffic looks legitimate. The solution is behavioral analytics (UEBA), not just perimeter firewalls.'
    },
    pitfalls:[
      {icon:'⚠️',title:'Underestimating Script Kiddies',desc:'Organizations dismiss script kiddies as low-skill noise. But automated tools (Metasploit, SQLmap) require zero expertise and can cause real damage at scale.',fix:'Patch all publicly-known CVEs promptly. Most script kiddie attacks exploit unpatched, well-documented vulnerabilities.'},
      {icon:'🔴',title:'Focusing All Defenses on External Threats',desc:'Most security budgets go to perimeter controls. But Verizon DBIR shows insiders cause 20-30% of all breaches.',fix:'Implement insider threat programs: UEBA, DLP, Privileged Access Management (PAM), and quarterly access reviews.'},
      {icon:'⛔',title:'Treating Grey Hat Reports as Goodwill',desc:'Grey hats who report vulnerabilities after unauthorized testing are still committing a crime under CFAA/Computer Misuse Act.',fix:'Establish a formal Bug Bounty or Responsible Disclosure program. Never encourage unsolicited testing.'}
    ],
    lab:{title:'Lab: Threat Actor Profiling',steps:['Research a real APT group (e.g., APT28, Lazarus Group) on MITRE ATT&CK (attack.mitre.org).','Identify their known TTPs (Tactics, Techniques, Procedures).','Map their attack chain to the CEH 5-phase methodology.','Identify which industries they primarily target.','Write a one-page threat actor profile for a mock board presentation.']}
  },

  'ethical-hacking-concepts':{
    module:'Module 01 · Introduction to Ethical Hacking',
    title:'Ethical Hacking Concepts',
    sub:'Scope, authorization, methodologies, and the legal framework of penetration testing.',
    killchain:{phase:'Pre-Engagement',mitre:'Foundation',desc:'All ethical hacking begins with proper authorization and defined scope — no exceptions.'},
    learn:{simple:'Ethical hacking is the practice of legally and intentionally probing systems for security vulnerabilities, using the same skills and tools as malicious hackers — but with explicit written permission from the target.',analogy:'Ethical hackers are like the security testers hired by a bank to try to break into the vault before real criminals do. The bank gives them the keys and a rulebook; without it, they would be criminals themselves.',why:'Organizations cannot know their true security posture without someone actively trying to break it. Ethical hackers provide a controlled, legal simulation of real attacks to find gaps before real attackers exploit them.',architecture:'Ethical hacking follows a structured process: define scope, get written authorization (Rules of Engagement), conduct testing across 5 phases, report findings, and remediate. Key laws include the CFAA (USA), Computer Misuse Act (UK), and IT Act (India).'},
    tools:[{name:'Dradis',cmd:'dradis',desc:'Reporting and collaboration framework'},{name:'Metasploit',cmd:'msfconsole',desc:'Exploitation framework (authorized use only)'}],
    commands:{win:['ipconfig /all','netstat -an','tasklist /svc'],lin:['ifconfig -a','netstat -tulnp','ps aux']},
    ctf:{scenario:'A security firm is asked to test a bank website. The CEO verbally approves the test. Is this sufficient to begin testing?',hint:'What document is legally required before any pen test?',flag:'CEH{3th1c4l_h4ck3r_m4nd4t3}',points:100},
    quiz:[
      {q:'What is the MOST important document before starting a pen test?',opts:['NDA','Written Authorization / Statement of Work','Verbal Approval Email','LinkedIn Profile'],correct:1,fb:'Written authorization (Rules of Engagement/SOW) is legally mandatory. Verbal approval is insufficient and leaves you legally exposed.'},
      {q:'What defines the boundaries of a penetration test?',opts:['The tester\'s skills','Scope of Engagement','Budget','Time allocated'],correct:1,fb:'The Scope of Engagement defines what systems, networks, and methods are authorized — testing outside scope is illegal.'},
      {q:'Which phase comes LAST in the CEH methodology?',opts:['Scanning','Gaining Access','Covering Tracks','Maintaining Access'],correct:2,fb:'CEH\'s 5 phases: Reconnaissance → Scanning → Gaining Access → Maintaining Access → Covering Tracks.'},
      {q:'A penetration test simulates attacks from which perspective?',opts:['Defender','Attacker','Regulator','Auditor'],correct:1,fb:'Ethical hacking adopts the attacker\'s mindset — thinking like a threat actor to find vulnerabilities before real attackers do.'},
      {q:'What is "vulnerability research" in the context of ethical hacking?',opts:['Writing malware','Finding and analyzing security flaws in systems','Social engineering employees','Installing backdoors'],correct:1,fb:'Vulnerability research involves identifying, analyzing, and documenting security weaknesses — the core skill of an ethical hacker.'},
      {q:'Which law primarily governs unauthorized computer access in the USA?',opts:['GDPR','HIPAA','Computer Fraud and Abuse Act (CFAA)','PCI-DSS'],correct:2,fb:'The Computer Fraud and Abuse Act (CFAA) is the primary US federal law governing unauthorized computer access and cybercrime.'},
      {q:'A pen tester at GlobalFinCorp tests a server not listed in the scope document. This is:',opts:['Acceptable if vulnerabilities are found','Legal since they are hired','Illegal and potentially criminal','Standard practice'],correct:2,fb:'Testing systems outside the defined scope is unauthorized access — a criminal offense under the CFAA regardless of employment status.'},
      {q:'A client requests a "black box" test. What information does the tester receive?',opts:['Full network diagrams and credentials','Source code access','Only the company name and target IP range','Admin credentials'],correct:2,fb:'Black box testing simulates an external attacker with no insider knowledge — testers receive minimal or no information about the target.'},
      {q:'What should a pen tester do upon discovering a critical vulnerability mid-engagement?',opts:['Exploit it further to demonstrate impact','Ignore it until the final report','Immediately notify the client per the escalation plan','Post it to social media'],correct:2,fb:'Critical vulnerabilities (especially those affecting business continuity) must be immediately escalated to the client per the agreed escalation procedure.'},
      {q:'Which ethical hacking type tests employees\' susceptibility to manipulation?',opts:['Network pen test','Web app test','Social engineering assessment','Code review'],correct:2,fb:'Social engineering assessments test human vulnerability — phishing simulations, vishing calls, and physical impersonation tests.'},
    ],
    flashcards:[
      {f:'Rules of Engagement',b:'Document defining scope, methods, timeline, and legal authorization for a pen test.'},
      {f:'Black Box Test',b:'Penetration test where the tester has zero prior knowledge of the target system.'},
      {f:'White Box Test',b:'Penetration test with full access to source code, architecture, and credentials.'},
      {f:'Grey Box Test',b:'Penetration test with partial knowledge — simulates a compromised insider or privileged user.'},
      {f:'CFAA',b:'Computer Fraud and Abuse Act — primary US federal law governing unauthorized computer access.'},
      {f:'CVE',b:'Common Vulnerabilities and Exposures — standardized naming system for publicly known security flaws.'},
    ],
    summary:[
      'All ethical hacking requires written authorization — verbal approval is legally insufficient.',
      'The scope defines the legal boundary — testing outside scope is a crime.',
      'CEH methodology: Reconnaissance → Scanning → Gaining Access → Maintaining Access → Covering Tracks.',
      'Critical vulnerabilities must be escalated immediately to the client, not saved for the final report.',
      'Understanding relevant laws (CFAA, GDPR, HIPAA) is mandatory for every ethical hacker.',
    ],
    diagram:{
      title:'Ethical Hacking Engagement Lifecycle',
      steps:[
        {icon:'📝',label:'Pre-Engagement',desc:'Define scope, sign NDA and SOW, establish Rules of Engagement. Get written authorization — without this you are a criminal.'},
        {icon:'🔍',label:'Reconnaissance',desc:'Gather intelligence: OSINT, WHOIS, DNS enumeration, employee profiling, IP range mapping.'},
        {icon:'📡',label:'Scanning & Enumeration',desc:'Actively probe target: port scanning (Nmap), service versioning, OS fingerprinting, vulnerability scanning.'},
        {icon:'💥',label:'Exploitation',desc:'Attempt to exploit discovered vulnerabilities within the agreed scope to gain unauthorized access.'},
        {icon:'📊',label:'Post-Exploitation & Reporting',desc:'Document findings: proof-of-concept, CVSS scores, business impact assessment, remediation steps.'},
        {icon:'🤝',label:'Remediation & Retest',desc:'Client fixes vulnerabilities. You verify fixes were correctly implemented. Cycle repeats until clean.'}
      ]
    },
    enterprise:{
      role:'You are the Lead Penetration Tester contracted by GlobalFinSec Corp.',
      situation:'The CISO verbally tells you to "test everything" before a PCI-DSS audit next month. No paperwork has been signed.',
      challenge:'Identify every legal and ethical action you must take BEFORE beginning any testing activity.',
      steps:[
        'Decline to start testing. Verbal authorization is legally insufficient under CFAA (USA) and Computer Misuse Act (UK).',
        'Draft a Statement of Work (SOW): scope (IP ranges, domains, apps), excluded systems, testing windows, emergency contacts.',
        'Draft a Rules of Engagement (RoE): allowed techniques, prohibited actions (no production DoS), escalation procedures.',
        'Get both documents signed by an authorized executive (CISO, CTO, or CEO).',
        'Only then begin passive OSINT reconnaissance — no active probing until paperwork is signed.'
      ],
      outcome:'Proper documentation protects both tester (legal immunity) and client (defined liability). Testing began 3 days later after paperwork was signed. 47 vulnerabilities found, including 3 critical RCEs.',
      lesson:'The most important tool in an ethical hacker\'s kit is not Nmap or Metasploit. It is the signed authorization document.'
    },
    pitfalls:[
      {icon:'⚠️',title:'Testing Without Written Authorization',desc:'A verbal "go ahead" from the IT manager is not legal authorization. If anything goes wrong, you face criminal prosecution.',fix:'Always obtain a signed Statement of Work AND Rules of Engagement before generating a single packet.'},
      {icon:'🔴',title:'Testing Systems Outside Defined Scope',desc:'Following an attack chain to an out-of-scope system is unauthorized access — a criminal offense regardless of employment status.',fix:'Define scope boundaries explicitly in the RoE. If you discover a path to out-of-scope systems, stop and notify the client immediately.'},
      {icon:'⛔',title:'Saving Critical Findings for the Final Report',desc:'Discovering a critical RCE on Day 1 and waiting 3 weeks to report it leaves the client exposed throughout the engagement.',fix:'Establish an escalation procedure for critical findings. Call the emergency contact the moment a critical vulnerability is confirmed.'},
      {icon:'🎭',title:'Confusing a Vuln Scan with a Penetration Test',desc:'Running Nessus and handing over a scan report is not a penetration test. It is a vulnerability scan.',fix:'A real penetration test involves manual exploitation, chained attack paths, business impact assessment, and proof-of-concept evidence.'}
    ],
    lab:{title:'Lab: Draft a Rules of Engagement Document',steps:['Create a new document titled "Rules of Engagement — Penetration Test"','Include sections: Executive Summary, Scope (in-scope and out-of-scope systems), Testing Methods Allowed, Testing Schedule, Emergency Contacts, Escalation Procedure, Legal Authorization Statement.','Define a mock scope: "Testing authorized on 192.168.1.0/24 network only, excluding production database server 192.168.1.50."','Add a signature block for both client and tester.','Review against PTES (Penetration Testing Execution Standard) guidelines at pentest-standard.org.']}
  },
  'hacking-methodologies': {
    module: 'Module 01 · Introduction to Ethical Hacking',
    title: 'Hacking Methodologies & Frameworks',
    sub: 'Structured Approaches to Cyber Attacks and Defense',
    killchain: { phase: 'All Phases', mitre: 'TA0001-TA0011', desc: 'Understanding the structured methodologies attackers use helps defenders anticipate and disrupt the attack lifecycle.' },
    diagram:{
      title:'CEH 5-Phase Attack Methodology',
      steps:[
        {icon:'🔍',label:'Phase 1 — Reconnaissance',desc:'Passive and active information gathering: OSINT, WHOIS, DNS, social media, Shodan, Google Dorking. No direct contact with target.'},
        {icon:'📡',label:'Phase 2 — Scanning',desc:'Active probing: port scanning (Nmap), vulnerability scanning (Nessus), OS fingerprinting, service version detection, network mapping.'},
        {icon:'🔓',label:'Phase 3 — Gaining Access',desc:'Exploiting discovered vulnerabilities: password cracking, buffer overflows, social engineering, web app attacks, privilege escalation.'},
        {icon:'🔏',label:'Phase 4 — Maintaining Access',desc:'Establishing persistence: backdoors, rootkits, scheduled tasks, remote access trojans (RATs). Evading AV/EDR detection.'},
        {icon:'🧹',label:'Phase 5 — Covering Tracks',desc:'Erasing evidence: deleting logs, clearing bash_history, timestomping, using covert channels, removing malware artifacts.'}
      ]
    },
    enterprise:{
      role:'You are the Red Team Lead at GlobalFinSec Corp simulating an APT attack.',
      situation:'The CISO has approved a 2-week purple team exercise to test detection capabilities across all 5 phases of the CEH methodology. The Blue Team knows an exercise is happening, but not when or how.',
      challenge:'Execute a realistic kill chain against the test environment (192.168.50.0/24) mapping every action to a CEH phase and a MITRE ATT&CK technique.',
      steps:[
        'Phase 1 — Recon: Run theHarvester and Maltego to map employee names, emails, and LinkedIn profiles. Passive only.',
        'Phase 2 — Scan: Run nmap -sS -sV -O -A 192.168.50.0/24 to map open ports and service versions.',
        'Phase 3 — Gain Access: Use Metasploit to exploit an unpatched EternalBlue (MS17-010) on a test Windows host.',
        'Phase 4 — Maintain Access: Deploy a Meterpreter reverse shell and set up a scheduled task for persistence.',
        'Phase 5 — Cover Tracks: Clear the Windows Event Log (wevtutil cl System), delete prefetch files, timestomp artifacts.'
      ],
      outcome:'The exercise revealed the Blue Team detected Phases 2 and 3 (Nmap scan and exploit) but completely missed Phases 1, 4, and 5. Post-exercise, SIEM rules were added for PowerShell execution and scheduled task creation.',
      lesson:'Defenders must monitor all 5 phases, not just the exploit. Recon and post-exploitation are the most commonly undetected phases in real-world attacks.'
    },
    pitfalls:[
      {icon:'⚠️',title:'Skipping the Methodology and Going Straight to Exploitation',desc:'New penetration testers often skip recon and scanning, jumping directly to running Metasploit. This leads to noisy, incomplete, and incomplete assessments.',fix:'Always follow the methodology in order. Thorough recon reveals attack surface that scanning alone misses.'},
      {icon:'🔴',title:'Confusing MITRE ATT&CK with the CEH Kill Chain',desc:'MITRE ATT&CK has 14 Tactics, CEH has 5 phases. Students mix them up in exams and real assessments.',fix:'CEH 5 phases = strategic overview. MITRE ATT&CK = granular technique library. Use both together: CEH phase identifies "where you are," ATT&CK identifies "how you do it."'},
      {icon:'⛔',title:'Not Clearing Tracks During a Real Engagement',desc:'Leaving Nmap logs, Metasploit sessions, and dropped files on a client system is unprofessional and creates security risks.',fix:'Always clean up artifacts at the end of an engagement. Document what was placed on systems and have a cleanup checklist in your methodology.'},
      {icon:'🎭',title:'Treating the Cyber Kill Chain and CEH Methodology as Identical',desc:'The Lockheed Martin Cyber Kill Chain is 7 steps focused on the attacker; CEH methodology is 5 phases focused on the pen tester. They overlap but differ.',fix:'Know both: CEH methodology for exam and engagement planning; Cyber Kill Chain for understanding and disrupting real attacker behavior.'}
    ],
        learn: { simple: 'A hacking methodology is a step-by-step blueprint for conducting a penetration test or cyber attack, ensuring thoroughness and repeatability.', analogy: 'Like a bank robber casing the joint, planning the route, disabling the alarms, stealing the cash, and erasing the security footage.', why: 'Without a methodology, assessments are chaotic and likely to miss critical vulnerabilities. Frameworks provide a common language for the industry.', architecture: 'Key frameworks include the CEH Methodology (Reconnaissance, Scanning, Gaining Access, Maintaining Access, Clearing Tracks), Lockheed Martin Cyber Kill Chain, MITRE ATT&CK, and PTES (Penetration Testing Execution Standard).' },
    tools: [ { name: 'MITRE ATT&CK Navigator', cmd: 'Online Tool', desc: 'Used to explore and map adversary tactics and techniques.' }, { name: 'OSSTMM', cmd: 'Document', desc: 'Open Source Security Testing Methodology Manual.' } ],
    commands: { win: ['systeminfo', 'netstat -ano'], lin: ['uname -a', 'ps aux'] },
    ctf: { scenario: 'You are analyzing an attacker\'s path through a network. They first gathered OSINT, then ran an Nmap scan, exploited an SMB vulnerability, installed a rootkit, and deleted the bash_history. What is the CEH methodology sequence?', hint: 'Think of the 5 phases of hacking according to EC-Council.', flag: 'CEH{r3c0n_sc4n_g41n_m41nt41n}', points: 100 },
    quiz: [
      { q: 'Which phase of the CEH hacking methodology involves extracting information such as user names, machine names, and network resources?', opts: ['Reconnaissance', 'Scanning and Enumeration', 'Gaining Access', 'Maintaining Access'], correct: 1, fb: 'Scanning and enumeration involves active connection and extraction of specific information.' },
      { q: 'In the Cyber Kill Chain, which step immediately follows Reconnaissance?', opts: ['Delivery', 'Exploitation', 'Weaponization', 'Installation'], correct: 2, fb: 'Weaponization is the preparation of the payload following initial reconnaissance.' },
      { q: 'Which framework focuses heavily on mapping specific adversary behaviors and techniques based on real-world observations?', opts: ['PTES', 'NIST CSF', 'Cyber Kill Chain', 'MITRE ATT&CK'], correct: 3, fb: 'MITRE ATT&CK is a globally accessible knowledge base of adversary tactics and techniques.' },
      { q: 'What is the primary purpose of the "Clearing Tracks" phase?', opts: ['To find more vulnerabilities', 'To maintain long-term access', 'To evade detection and avoid legal consequences', 'To escalate privileges'], correct: 2, fb: 'Clearing tracks (or covering tracks) is done to remove evidence of the intrusion.' },
      { q: 'Which penetration testing standard includes phases such as Threat Modeling, Vulnerability Analysis, and Post-Exploitation?', opts: ['OSSTMM', 'PTES', 'ISO 27001', 'ITIL'], correct: 1, fb: 'The Penetration Testing Execution Standard (PTES) defines these specific phases.' },
      { q: 'What type of reconnaissance involves gathering information without directly interacting with the target system?', opts: ['Active Reconnaissance', 'Passive Reconnaissance', 'Aggressive Scanning', 'Banner Grabbing'], correct: 1, fb: 'Passive reconnaissance relies on publicly available information (OSINT) to avoid detection.' },
      { q: 'In the context of MITRE ATT&CK, what does "TA" stand for?', opts: ['Tactical Assessment', 'Target Acquisition', 'Threat Actor', 'Tactic'], correct: 3, fb: 'TA stands for Tactic, representing the "why" of an ATT&CK technique.' },
      { q: 'Which step of the Cyber Kill Chain involves transmitting the weapon to the targeted environment?', opts: ['Weaponization', 'Delivery', 'Exploitation', 'Action on Objectives'], correct: 1, fb: 'Delivery is the transmission of the payload to the target (e.g., via email attachment or USB).' },
      { q: 'What is the main difference between vulnerability scanning and penetration testing?', opts: ['Vulnerability scanning is manual, pentesting is automated', 'Pentesting actively exploits vulnerabilities, scanning only identifies them', 'Scanning is done by blue teams, pentesting by red teams', 'There is no difference'], correct: 1, fb: 'Penetration testing goes a step further by attempting to exploit the discovered vulnerabilities to determine actual risk.' },
      { q: 'Which EC-Council methodology phase involves installing backdoors or rootkits?', opts: ['Gaining Access', 'Clearing Tracks', 'Scanning', 'Maintaining Access'], correct: 3, fb: 'Maintaining Access involves deploying mechanisms like backdoors to ensure persistent access.' }
    ],
    flashcards: [ { f: 'Five phases of CEH methodology', b: 'Reconnaissance, Scanning, Gaining Access, Maintaining Access, Clearing Tracks' }, { f: 'Cyber Kill Chain: Delivery', b: 'Transmitting the weapon to the targeted environment.' } ],
    summary: [ 'Hacking methodologies provide structured approaches for both attackers and defenders.', 'The CEH methodology consists of 5 phases: Recon, Scanning, Gaining Access, Maintaining Access, Clearing Tracks.', 'MITRE ATT&CK maps real-world adversary tactics and techniques.' ],
    lab: { title: 'Mapping Attacks to Frameworks', steps: [ 'Analyze a given packet capture of an attack.', 'Map the attacker\'s actions to the phases of the Cyber Kill Chain.', 'Identify the corresponding MITRE ATT&CK techniques used.' ] }
  },
  'security-controls': {
    module: 'Module 01 · Introduction to Ethical Hacking',
    title: 'Information Security Controls',
    sub: 'Implementing Defense in Depth',
    killchain: { phase: 'All Phases', mitre: 'Defensive Mitigations', desc: 'Security controls are the countermeasures put in place to mitigate risks and disrupt the kill chain.' },
    diagram:{
      title:'Defense in Depth — Layered Security Control Model',
      steps:[
        {icon:'📜',label:'Administrative Controls (Policies)',desc:'Policies, procedures, security awareness training, background checks, NDAs, acceptable use policies. The human and process layer.'},
        {icon:'🚪',label:'Physical Controls (Barriers)',desc:'Fences, locks, biometric access, security guards, CCTV, mantrap entry systems. Prevent unauthorized physical access.'},
        {icon:'💻',label:'Technical Controls — Perimeter',desc:'Firewalls, IDS/IPS, DMZ, VPN gateways, network segmentation. The first technical line of defense.'},
        {icon:'🔒',label:'Technical Controls — Endpoint',desc:'Antivirus, EDR, host-based firewalls, disk encryption (BitLocker/FileVault), patch management, application whitelisting.'},
        {icon:'📊',label:'Detective Controls — Monitoring',desc:'SIEM, log management, DLP, UEBA, network traffic analysis. Detect anomalies during or after an incident.'},
        {icon:'🔧',label:'Corrective & Recovery Controls',desc:'Incident response playbooks, backup and restore, disaster recovery plans, business continuity. Minimize damage and restore operations.'}
      ]
    },
    enterprise:{
      role:'You are the Information Security Manager at GlobalFinSec Corp.',
      situation:'A ransomware attack encrypted 200 workstations across two branch offices. Post-incident review revealed: no endpoint EDR, backups existed but had never been tested, and there was no formal incident response plan.',
      challenge:'Design a layered Defense in Depth architecture that would have prevented or contained this ransomware attack.',
      steps:[
        'Administrative: Mandate quarterly phishing simulation training (ransomware enters via phishing in 91% of cases).',
        'Technical - Perimeter: Deploy email filtering (ATP) with attachment sandboxing to block malicious Office macros.',
        'Technical - Endpoint: Deploy EDR (CrowdStrike/Defender for Endpoint) with behavioral ransomware detection.',
        'Detective: Configure SIEM alerts for mass file encryption events (high write IOPS + file extension changes).',
        'Recovery: Implement 3-2-1 backup rule: 3 copies, 2 different media, 1 offsite. Test restoration monthly.'
      ],
      outcome:'Post-implementation, a second ransomware attempt 6 months later was detected at the email gateway (ATP blocked the macro), and EDR quarantined the sample on the one endpoint that clicked through within 8 seconds.',
      lesson:'Defense in Depth means no single control failure causes a breach. Every layer buys time for detection and response.'
    },
    pitfalls:[
      {icon:'⚠️',title:'Relying on a Single Control Type',desc:'Organizations often deploy only technical controls (firewall, antivirus) while ignoring administrative controls (training, policies). When the firewall is bypassed, nothing stops the attacker.',fix:'Implement all three control types: Administrative, Technical, and Physical. A policy without a technical enforcement mechanism is just a wish.'},
      {icon:'🔴',title:'Confusing Control Type with Control Function',desc:'Students mix up "what kind" (Admin/Technical/Physical) with "what it does" (Preventive/Detective/Corrective). A firewall is Technical + Preventive. An audit log is Technical + Detective.',fix:'Always classify controls on both axes: Type (Admin/Technical/Physical) AND Function (Preventive/Detective/Corrective/Deterrent/Recovery/Compensating).'},
      {icon:'⛔',title:'Deploying Compensating Controls Permanently',desc:'Compensating controls are meant to be temporary substitutes when primary controls cannot be implemented. Organizations often leave them in place indefinitely.',fix:'Document compensating controls with a sunset date and remediation plan. Review quarterly. Replace with primary controls as soon as feasible.'},
      {icon:'🎭',title:'Never Testing Recovery Controls',desc:'Organizations have backups but never test restoration. Backups that fail during a ransomware recovery are a critical control failure.',fix:'Test backup restoration on a quarterly schedule. Simulate complete system recovery in a staging environment. Backup integrity without restoration testing is false assurance.'}
    ],
        learn: { simple: 'Security controls are safeguards or countermeasures to avoid, detect, counteract, or minimize security risks to physical property, information, computer systems, or other assets.', analogy: 'Like a castle\'s defenses: the moat (physical), the guards checking IDs (administrative), and the heavy iron gates with complex locks (technical).', why: 'No single security measure is foolproof. Layering different types of controls ensures that if one fails, others are there to protect the assets.', architecture: 'Controls are categorized by type (Administrative, Technical/Logical, Physical) and function (Preventive, Detective, Corrective, Deterrent, Recovery, Compensating). Defense in Depth is the strategy of applying multiple layers of controls.' },
    tools: [ { name: 'Firewall', cmd: 'iptables -L', desc: 'A technical preventive control.' }, { name: 'IDS/IPS', cmd: 'snort -c /etc/snort/snort.conf', desc: 'Technical detective and preventive controls.' } ],
    commands: { win: ['secpol.msc', 'gpedit.msc'], lin: ['chmod', 'chown', 'auditd'] },
    ctf: { scenario: 'You need to classify a new policy that requires all employees to attend annual security awareness training. What type of control is this?', hint: 'It\'s not software, and it\'s not a locked door. It\'s a rule for people.', flag: 'CEH{d3f3ns3_1n_d3pth_p0l1cy}', points: 100 },
    quiz: [
      { q: 'Which of the following is an example of a Physical security control?', opts: ['Biometric scanner', 'Firewall rules', 'Acceptable Use Policy', 'Antivirus software'], correct: 0, fb: 'Physical controls restrict physical access to facilities or hardware.' },
      { q: 'Security awareness training is classified as what type of control?', opts: ['Technical', 'Physical', 'Administrative', 'Logical'], correct: 2, fb: 'Administrative controls involve policies, procedures, and training for personnel.' },
      { q: 'What is the primary goal of a "Detective" control?', opts: ['To prevent an incident from occurring', 'To identify and record an incident while it is occurring', 'To restore systems after an incident', 'To discourage an attacker'], correct: 1, fb: 'Detective controls are designed to identify and alert on unauthorized activity.' },
      { q: 'Which concept describes the practice of implementing multiple, overlapping security controls to protect an asset?', opts: ['Least Privilege', 'Separation of Duties', 'Defense in Depth', 'Security through Obscurity'], correct: 2, fb: 'Defense in depth uses multiple layers of security to ensure redundancy.' },
      { q: 'A backup and restore system is an example of which functional control type?', opts: ['Preventive', 'Deterrent', 'Recovery', 'Detective'], correct: 2, fb: 'Recovery controls are used to restore systems and data to normal operations after an incident.' },
      { q: 'Which of the following is a Technical (Logical) control?', opts: ['Security guard', 'Access Control Lists (ACLs)', 'Background checks', 'Fences'], correct: 1, fb: 'Technical controls use technology, such as ACLs, firewalls, and encryption.' },
      { q: 'A "Warning: Guard Dogs on Duty" sign is best described as what type of control?', opts: ['Preventive', 'Detective', 'Deterrent', 'Compensating'], correct: 2, fb: 'Deterrent controls aim to discourage individuals from attempting an attack.' },
      { q: 'If a primary control cannot be implemented due to business constraints, what type of control is used instead?', opts: ['Compensating', 'Corrective', 'Administrative', 'Deterrent'], correct: 0, fb: 'Compensating controls are alternative measures used when primary controls are not feasible.' },
      { q: 'Which control function is designed to fix a system and mitigate the impact after a security incident?', opts: ['Preventive', 'Detective', 'Corrective', 'Deterrent'], correct: 2, fb: 'Corrective controls actively fix or mitigate the damage caused by an incident (e.g., terminating a malicious process).' },
      { q: 'Data encryption at rest is an example of a:', opts: ['Physical Preventive control', 'Technical Preventive control', 'Administrative Detective control', 'Technical Detective control'], correct: 1, fb: 'Encryption uses technology (Technical) to stop unauthorized access to data (Preventive).' }
    ],
    flashcards: [ { f: 'Administrative Controls', b: 'Policies, procedures, training, and regulations.' }, { f: 'Defense in Depth', b: 'Layering multiple security controls to provide redundant protection.' } ],
    summary: [ 'Security controls mitigate risks and are categorized into Administrative, Technical, and Physical types.', 'Controls also have functions: Preventive, Detective, Corrective, Deterrent, Recovery, and Compensating.', 'Defense in Depth is a critical strategy to avoid single points of failure.' ],
    lab: { title: 'Implementing Layered Controls', steps: [ 'Configure a technical control: set up iptables firewall rules.', 'Configure a detective control: review auditd logs for unauthorized access attempts.', 'Draft a brief administrative acceptable use policy.' ] }
  },
  'security-laws': {
    module: 'Module 01 · Introduction to Ethical Hacking',
    title: 'Information Security Laws & Standards',
    sub: 'Compliance, Regulations, and Legal Frameworks',
    killchain: { phase: 'N/A', mitre: 'N/A', desc: 'Understanding laws and standards ensures that ethical hacking is performed legally and that organizations meet their compliance obligations.' },
    diagram:{
      title:'Regulatory Compliance Framework Hierarchy',
      steps:[
        {icon:'🇪🇺',label:'GDPR (EU) — Privacy Law',desc:'General Data Protection Regulation. Applies to any org processing EU citizen data. Max fine: 4% of global annual revenue or €20M. Right to be forgotten, data portability, 72-hour breach notification.'},
        {icon:'🏥',label:'HIPAA (USA) — Healthcare Data',desc:'Health Insurance Portability and Accountability Act. Protects electronic Protected Health Information (ePHI). Applies to covered entities and business associates. Fines up to $1.9M/year.'},
        {icon:'💳',label:'PCI-DSS — Payment Card Data',desc:'Payment Card Industry Data Security Standard. Mandatory for any entity storing, processing, or transmitting cardholder data. 12 core requirements including encryption, access control, and quarterly scans.'},
        {icon:'💼',label:'SOX (USA) — Corporate Finance',desc:'Sarbanes-Oxley Act. Requires accurate financial reporting controls for publicly traded US companies. IT controls for financial systems are audited annually.'},
        {icon:'📋',label:'ISO/IEC 27001 — ISMS Standard',desc:'International standard for Information Security Management Systems. Certification demonstrates systematic approach to managing sensitive information. Risk-based framework with 93 controls in Annex A.'},
        {icon:'🖥️',label:'NIST CSF — Cybersecurity Framework',desc:'US NIST Cybersecurity Framework: Identify, Protect, Detect, Respond, Recover. Voluntary guidance for critical infrastructure. Widely adopted as a baseline globally.'}
      ]
    },
    enterprise:{
      role:'You are the Chief Information Security Officer (CISO) at GlobalFinSec Corp.',
      situation:'GlobalFinSec processes credit card payments for 2 million EU customers and stores electronic health insurance records for their employee benefits program. A breach has just been discovered — 500,000 customer records were accessed by an unauthorized party.',
      challenge:'Identify which regulatory frameworks are triggered, what the notification deadlines are, and what the maximum financial exposure is.',
      steps:[
        'Identify frameworks: GDPR (EU customer data) + HIPAA (employee health insurance ePHI) + PCI-DSS (credit card data) are all triggered.',
        'GDPR: 72-hour breach notification to the supervisory authority (Article 33). Notify affected individuals "without undue delay."',
        'HIPAA: 60-day notification to HHS Office for Civil Rights + affected individuals. If >500 individuals, notify prominent media.',
        'PCI-DSS: Immediately notify your acquiring bank and card brands (Visa/Mastercard). Engage a PCI Forensic Investigator (PFI).',
        'Calculate exposure: GDPR max = 4% of global revenue. PCI-DSS = $5,000-$100,000/month fines + potential card brand termination.'
      ],
      outcome:'GlobalFinSec notified authorities within 68 hours (GDPR compliant), engaged a PFI for PCI-DSS forensics, and avoided the maximum fines by demonstrating existing controls and rapid response. Total regulatory fines: €2.1M (reduced from potential €15M).',
      lesson:'Multi-framework compliance is not a checklist exercise — it requires a unified data classification policy that maps every data type to its regulatory requirements before a breach occurs.'
    },
    pitfalls:[
      {icon:'⚠️',title:'Treating GDPR as Europe-Only',desc:'Organizations outside the EU assume GDPR does not apply to them. If you process data of EU residents — regardless of where you are located — GDPR applies to you.',fix:'Audit your entire data pipeline. If any EU resident data is processed, stored, or transmitted by your systems, GDPR compliance is mandatory.'},
      {icon:'🔴',title:'Confusing ISO 27001 Certification with PCI-DSS Compliance',desc:'ISO 27001 is a framework for information security management. PCI-DSS is a specific standard for cardholder data. They are complementary but neither substitutes for the other.',fix:'Map your compliance requirements by data type. Credit card data = PCI-DSS. Personal data of EU citizens = GDPR. Patient health data = HIPAA. Each may require separate controls.'},
      {icon:'⛔',title:'Missing Breach Notification Deadlines',desc:'GDPR requires 72-hour notification. HIPAA requires 60 days. Many organizations lack incident response plans that include regulatory notification procedures, missing these deadlines and incurring additional fines.',fix:'Build regulatory notification timelines into your Incident Response Plan. Create notification templates in advance. Designate a DPO (Data Protection Officer) for GDPR compliance.'},
      {icon:'🎭',title:'Achieving Compliance Once, Then Neglecting It',desc:'Compliance is treated as a one-time project. Frameworks like PCI-DSS require quarterly vulnerability scans and annual penetration tests. Letting these lapse creates non-compliance.',fix:'Build compliance into operational BAU (business as usual). Use GRC tools (Archer, ServiceNow) to automate compliance tracking and schedule recurring control assessments.'}
    ],
        learn: { simple: 'Information security laws are government-enforced rules regarding data protection, while standards are industry-accepted best practices and frameworks for managing security.', analogy: 'Laws are the speed limits set by the government (you get a ticket if you break them); standards are the safety ratings of your car (best practices to keep you safe).', why: 'Ethical hackers must stay within legal boundaries to avoid prosecution. Furthermore, organizations hire hackers primarily to ensure they comply with these laws and standards to avoid hefty fines.', architecture: 'Key regulations include GDPR (EU privacy), HIPAA (US Healthcare), SOX (US Corporate Financials), and PCI-DSS (Credit Card data). Key standards include ISO/IEC 27001 (ISMS) and the NIST Cybersecurity Framework.' },
    tools: [ { name: 'Compliance Scanners', cmd: 'OpenSCAP', desc: 'Tools that audit systems against standard baselines.' } ],
    commands: { win: ['Get-LocalGroupMember'], lin: ['lynis audit system'] },
    ctf: { scenario: 'A global e-commerce company suffered a breach of European customer data and credit card information. They are facing fines from two major regulatory frameworks. What are they?', hint: 'One is an EU privacy law, the other is a payment card industry standard.', flag: 'CEH{c0mpl14nc3_1s_k3y_2026}', points: 100 },
    quiz: [
      { q: 'Which regulation applies to the protection of healthcare and patient data in the United States?', opts: ['HIPAA', 'GDPR', 'PCI-DSS', 'SOX'], correct: 0, fb: 'The Health Insurance Portability and Accountability Act (HIPAA) secures electronic protected health information (ePHI).' },
      { q: 'If an organization processes credit card transactions, which standard MUST they comply with?', opts: ['ISO 27001', 'PCI-DSS', 'FISMA', 'GLBA'], correct: 1, fb: 'The Payment Card Industry Data Security Standard (PCI-DSS) is mandatory for organizations handling credit card data.' },
      { q: 'Which European Union regulation imposes strict rules on data privacy and gives individuals the "right to be forgotten"?', opts: ['DMCA', 'CFAA', 'GDPR', 'HIPAA'], correct: 2, fb: 'The General Data Protection Regulation (GDPR) enforces strong data privacy rules for EU citizens.' },
      { q: 'Which US law was enacted to protect investors by improving the accuracy and reliability of corporate disclosures and financial reporting?', opts: ['SOX', 'HIPAA', 'GLBA', 'FISMA'], correct: 0, fb: 'The Sarbanes-Oxley Act (SOX) dictates requirements for storing and retaining corporate financial records.' },
      { q: 'ISO/IEC 27001 primarily specifies the requirements for establishing, implementing, maintaining, and continually improving a(n):', opts: ['Firewall architecture', 'Information Security Management System (ISMS)', 'Intrusion Detection System', 'Software Development Life Cycle'], correct: 1, fb: 'ISO 27001 is the international standard for ISMS.' },
      { q: 'Which framework organizes cybersecurity activities into five core functions: Identify, Protect, Detect, Respond, and Recover?', opts: ['NIST CSF', 'ISO 27001', 'PCI-DSS', 'COBIT'], correct: 0, fb: 'The NIST Cybersecurity Framework (CSF) is structured around these five core functions.' },
      { q: 'The Gramm-Leach-Bliley Act (GLBA) requires specific data protection implementations for which type of institutions?', opts: ['Hospitals', 'Financial Institutions', 'E-commerce retailers', 'Government agencies'], correct: 1, fb: 'GLBA requires financial institutions to explain their information-sharing practices and safeguard sensitive data.' },
      { q: 'What is the primary purpose of the Computer Fraud and Abuse Act (CFAA) in the United States?', opts: ['To regulate credit card processing', 'To criminalize unauthorized access to computer systems', 'To enforce healthcare data privacy', 'To mandate corporate financial auditing'], correct: 1, fb: 'The CFAA is the primary federal anti-hacking law in the US.' },
      { q: 'Which standard provides a comprehensive set of controls comprising best practices in information security (often used alongside ISO 27001)?', opts: ['ISO 27002', 'PCI-DSS', 'HIPAA', 'SOX'], correct: 0, fb: 'ISO/IEC 27002 provides a reference set of generic information security controls.' },
      { q: 'Under GDPR, organizations must report certain types of data breaches to the relevant supervisory authority within how many hours of becoming aware of it?', opts: ['24 hours', '48 hours', '72 hours', '1 week'], correct: 2, fb: 'GDPR mandates a 72-hour notification window for personal data breaches.' }
    ],
    flashcards: [ { f: 'HIPAA', b: 'US law protecting healthcare and patient data (ePHI).' }, { f: 'GDPR', b: 'EU regulation for data privacy and personal data protection.' } ],
    summary: [ 'Compliance with laws and standards is non-negotiable and dictates how security is implemented.', 'Key regulations include GDPR (EU Data), HIPAA (US Healthcare), SOX (US Financials), and PCI-DSS (Credit Cards).', 'Frameworks like ISO 27001 and NIST CSF help organizations build structured security programs.' ],
    lab: { title: 'Compliance Auditing', steps: [ 'Run OpenSCAP on a Linux system against a specific compliance profile (e.g., PCI-DSS).', 'Review the generated HTML report.', 'Identify and remediate three non-compliant settings.' ] }
  }
,
};

// Stubs for remaining topics
const TOPIC_STUBS = {
  'footprinting-concepts':{module:'Module 02',title:'Footprinting Concepts',sub:'Active vs passive footprinting, information gathering objectives and methodology.'},
  'osint-techniques':{module:'Module 02',title:'OSINT Techniques',sub:'Open-source intelligence gathering: Shodan, Maltego, theHarvester, and more.'},
  'whois-dns':{module:'Module 02',title:'Whois & DNS Footprinting',sub:'Domain registration data, DNS record enumeration, zone transfer attacks.'},
  'google-hacking':{module:'Module 02',title:'Google Hacking (Dorking)',sub:'Google dorks for finding exposed data, admin panels, and vulnerabilities.'},
  'shodan-recon':{module:'Module 02',title:'Shodan & Network Recon',sub:'Using Shodan to discover internet-exposed devices and vulnerable services.'},
  'social-media-recon':{module:'Module 02',title:'Social Media Footprinting',sub:'Harvesting intelligence from LinkedIn, Twitter, Facebook for target profiling.'},
};
MODULES.forEach(m => m.topics.forEach(t => { if(!CONTENT[t.id] && !TOPIC_STUBS[t.id]) TOPIC_STUBS[t.id] = {module:`Module ${m.id.replace('m','').padStart(2,'0')}`,title:t.name,sub:'Content for this topic is loading in Phase 2.'}; }));

