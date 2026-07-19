
// ═══════════════════════════════════════════════════════════
// DATA
// ═══════════════════════════════════════════════════════════
const MODULES = [
  { id:'m01', name:'Introduction to Ethical Hacking', topics:[
    {id:'info-security-overview',name:'Information Security Overview'},
    {id:'hacker-classes',name:'Hacking Concepts & Hacker Classes'},
    {id:'ethical-hacking-concepts',name:'Ethical Hacking Concepts'},
    {id:'hacking-methodologies',name:'Hacking Methodologies & Frameworks'},
    {id:'security-controls',name:'Information Security Controls'},
    {id:'security-laws',name:'Information Security Laws & Standards'},
  ]},
  { id:'m02', name:'Footprinting & Reconnaissance', topics:[
    {id:'footprinting-concepts',name:'Footprinting Concepts'},
    {id:'osint-techniques',name:'OSINT Techniques'},
    {id:'whois-dns',name:'Whois & DNS Footprinting'},
    {id:'google-hacking',name:'Google Hacking (Dorking)'},
    {id:'shodan-recon',name:'Shodan & Network Recon'},
    {id:'social-media-recon',name:'Social Media Footprinting'},
  ]},
  { id:'m03', name:'Scanning Networks', topics:[
    {id:'network-scanning-overview',name:'Network Scanning Overview'},
    {id:'tcp-ip-scanning',name:'TCP/IP & Port Scanning'},
    {id:'nmap-techniques',name:'Nmap Scanning Techniques'},
    {id:'hping3-scanning',name:'Hping3 & Stealth Scanning'},
    {id:'banner-grabbing',name:'Banner Grabbing & OS Fingerprinting'},
  ]},
  { id:'m04', name:'Enumeration', topics:[
    {id:'enumeration-overview',name:'Enumeration Concepts'},
    {id:'netbios-smb',name:'NetBIOS & SMB Enumeration'},
    {id:'snmp-ldap',name:'SNMP & LDAP Enumeration'},
    {id:'smtp-dns-enum',name:'SMTP & DNS Enumeration'},
  ]},
  { id:'m05', name:'Vulnerability Analysis', topics:[
    {id:'vuln-concepts',name:'Vulnerability Assessment Concepts'},
    {id:'cve-cvss',name:'CVE, CVSS & NVD'},
    {id:'nessus-openvas',name:'Nessus & OpenVAS Scanning'},
  ]},
  { id:'m06', name:'System Hacking', topics:[
    {id:'password-cracking',name:'Password Cracking Techniques'},
    {id:'privilege-escalation',name:'Privilege Escalation'},
    {id:'maintaining-access',name:'Maintaining Access & Rootkits'},
    {id:'steganography',name:'Steganography & Covering Tracks'},
  ]},
  { id:'m07', name:'Malware Threats', topics:[
    {id:'malware-concepts',name:'Malware Concepts & Types'},
    {id:'trojans-rats',name:'Trojans & RATs'},
    {id:'ransomware-apts',name:'Ransomware & APTs'},
    {id:'fileless-malware',name:'Fileless Malware'},
  ]},
  { id:'m08', name:'Sniffing', topics:[
    {id:'sniffing-concepts',name:'Sniffing Concepts'},
    {id:'arp-mac-attacks',name:'ARP & MAC Flooding Attacks'},
    {id:'mitm-attacks',name:'Man-in-the-Middle Attacks'},
    {id:'wireshark-analysis',name:'Wireshark Traffic Analysis'},
  ]},
  { id:'m09', name:'Social Engineering', topics:[
    {id:'social-eng-concepts',name:'Social Engineering Concepts'},
    {id:'phishing-vishing',name:'Phishing & Vishing'},
    {id:'insider-threats',name:'Insider Threats & Impersonation'},
  ]},
  { id:'m10', name:'Denial of Service', topics:[
    {id:'dos-concepts',name:'DoS & DDoS Concepts'},
    {id:'botnet-attacks',name:'Botnets & Amplification Attacks'},
    {id:'syn-flood',name:'SYN Flood & Volumetric Attacks'},
  ]},
  { id:'m11', name:'Session Hijacking', topics:[
    {id:'session-concepts',name:'Session Hijacking Concepts'},
    {id:'tcp-hijacking',name:'TCP Session Hijacking'},
    {id:'cookie-theft-xss',name:'Cookie Theft & XSS Hijacking'},
  ]},
  { id:'m12', name:'Evading IDS/Firewalls', topics:[
    {id:'ids-evasion',name:'IDS/IPS Evasion Techniques'},
    {id:'firewall-bypass',name:'Firewall & WAF Bypass'},
    {id:'tunneling-obfuscation',name:'Tunneling & Obfuscation'},
  ]},
  { id:'m13', name:'Web Server Hacking', topics:[
    {id:'web-server-attacks',name:'Web Server Attack Methodology'},
    {id:'directory-traversal',name:'Directory Traversal & Shellcode'},
  ]},
  { id:'m14', name:'Hacking Web Applications', topics:[
    {id:'owasp-top10',name:'OWASP Top 10 Vulnerabilities'},
    {id:'xss-csrf',name:'XSS, CSRF & IDOR'},
    {id:'web-app-methodology',name:'Web App Hacking Methodology'},
  ]},
  { id:'m15', name:'SQL Injection', topics:[
    {id:'sqli-concepts',name:'SQL Injection Concepts'},
    {id:'sqli-techniques',name:'Blind & Time-Based SQLi'},
    {id:'sqlmap',name:'Automated SQLi with sqlmap'},
  ]},
  { id:'m16', name:'Wireless Hacking', topics:[
    {id:'wireless-concepts',name:'Wireless Network Concepts'},
    {id:'wpa2-cracking',name:'WPA2 Cracking & Evil Twin'},
    {id:'aircrack-suite',name:'Aircrack-ng Suite'},
  ]},
  { id:'m17', name:'Hacking Mobile Platforms', topics:[
    {id:'mobile-threats',name:'Mobile Platform Threats'},
    {id:'android-hacking',name:'Android Hacking Techniques'},
    {id:'ios-hacking',name:'iOS Hacking Techniques'},
  ]},
  { id:'m18', name:'IoT & OT Hacking', topics:[
    {id:'iot-concepts',name:'IoT Attack Surface'},
    {id:'scada-ot',name:'SCADA & OT Security'},
    {id:'mqtt-protocols',name:'MQTT & Industrial Protocols'},
  ]},
  { id:'m19', name:'Cloud Computing Threats', topics:[
    {id:'cloud-concepts',name:'Cloud Security Concepts'},
    {id:'aws-misconfigs',name:'AWS/Azure Misconfigurations'},
    {id:'iam-abuse',name:'IAM Abuse & S3 Bucket Attacks'},
  ]},
  { id:'m20', name:'Cryptography', topics:[
    {id:'crypto-concepts',name:'Cryptography Concepts'},
    {id:'pki-certificates',name:'PKI & Digital Certificates'},
    {id:'crypto-attacks',name:'Cryptographic Attacks'},
  ]},
];

const CONTENT = {
  'info-security-overview':{
    module:'Module 01 · Introduction to Ethical Hacking',
    title:'Information Security Overview',
    sub:'Understanding the CIA Triad, threat landscape, and foundational security concepts.',
    killchain:{phase:'Pre-Attack Phase',mitre:'Foundation',desc:'Core concepts that underpin all CEH domains and attack methodologies.'},
    learn:{
      simple:'Information security is the practice of protecting data from unauthorized access, modification, or destruction. It is the foundation of ethical hacking — you must understand what you are protecting before you can attack or defend it.',
      analogy:'Think of a bank vault. The CIA Triad (Confidentiality, Integrity, Availability) are the three locks. Confidentiality = only authorized people open the vault. Integrity = no one tampers with the contents. Availability = the vault opens when needed.',
      why:'Without understanding security fundamentals, attackers exploit the gaps between policy and implementation. Every penetration test starts with understanding what the target is trying to protect.',
      architecture:'Information security operates across three defense layers: Physical (server rooms, badge access), Network (firewalls, IDS/IPS), and Application (input validation, authentication). The OSI model maps directly to these layers, and CEH attacks target each one.'
    },
    tools:[
      {name:'OpenVAS',cmd:'openvas-start',desc:'Open-source vulnerability scanner'},
      {name:'Nessus',cmd:'service nessusd start',desc:'Enterprise vulnerability scanner'},
      {name:'Nmap',cmd:'nmap -sV target',desc:'Network discovery and port scanning'},
    ],
    commands:{
      win:['systeminfo','net user','net accounts','gpresult /r','wmic os get Caption'],
      lin:['id','uname -a','cat /etc/os-release','cat /etc/passwd','last -n 10']
    },
    ctf:{
      scenario:'You are a new SOC analyst at GlobalFinCorp. Your supervisor hands you a report and says: "Find the baseline." The flag is the CEH acronym for establishing what "normal" looks like on a network.',
      hint:'Think about what you must establish BEFORE you can detect anomalies...',
      flag:'CEH{1nf0_s3cur1ty_b4s3l1n3}',
      points:100
    },
    quiz:[
      {q:'What does the "C" in the CIA Triad stand for?',opts:['Control','Confidentiality','Compliance','Cryptography'],correct:1,fb:'Confidentiality ensures information is accessible only to authorized users.'},
      {q:'Which attack directly violates Availability?',opts:['Phishing','Man-in-the-Middle','DDoS Attack','SQL Injection'],correct:2,fb:'A DDoS attack overwhelms a system making it unavailable to legitimate users, directly violating Availability.'},
      {q:'What is a "zero-day" vulnerability?',opts:['A bug found on January 1st','A vulnerability with no known patch','A vulnerability older than one year','A flaw in encryption algorithms'],correct:1,fb:'A zero-day is a vulnerability unknown to the vendor with no available patch, making it extremely dangerous.'},
      {q:'In CEH methodology, what comes AFTER reconnaissance?',opts:['Gaining Access','Scanning','Maintaining Access','Covering Tracks'],correct:1,fb:'The CEH 5-phase methodology is: Reconnaissance → Scanning → Gaining Access → Maintaining Access → Covering Tracks.'},
      {q:'Which principle states that users should have only the minimum access needed?',opts:['Defense in Depth','Least Privilege','Need to Know','Separation of Duties'],correct:1,fb:'The Principle of Least Privilege (PoLP) limits access rights to the minimum necessary to perform a function.'},
      {q:'What type of hacker has authorization to test systems?',opts:['Black Hat','Grey Hat','White Hat','Script Kiddie'],correct:2,fb:'White hat hackers (ethical hackers) have explicit written permission from the organization to test their systems.'},
      {q:'At GlobalFinCorp, the trading platform went offline for 2 hours due to an attack. Which CIA pillar was violated?',opts:['Confidentiality','Integrity','Availability','Authentication'],correct:2,fb:'System downtime directly violates Availability — the guarantee that systems are accessible when needed.'},
      {q:'A CEH operator finds that database records were altered without authorization. Which pillar is affected?',opts:['Confidentiality','Integrity','Availability','Non-repudiation'],correct:1,fb:'Unauthorized modification of data violates Integrity — the guarantee that data is accurate and unaltered.'},
      {q:'What is the FIRST step before conducting any authorized penetration test?',opts:['Run Nmap scans','Get written authorization (Rules of Engagement)','Deploy Metasploit','Enumerate services'],correct:1,fb:'Without written authorization and a defined scope (Rules of Engagement), any hacking activity is illegal, regardless of intent.'},
      {q:'Which document defines the scope, rules, and limitations of a penetration test?',opts:['NDA','EULA','Rules of Engagement (RoE)','Service Level Agreement'],correct:2,fb:'The Rules of Engagement document legally defines what systems can be tested, when, and what methods are allowed.'},
    ],
    flashcards:[
      {f:'CIA Triad',b:'Confidentiality, Integrity, Availability — the three core principles of information security.'},
      {f:'Threat',b:'Any potential danger that could exploit a vulnerability to cause harm to a system or data.'},
      {f:'Vulnerability',b:'A weakness or flaw in a system that can be exploited by a threat actor.'},
      {f:'Risk',b:'Risk = Threat × Vulnerability × Impact. The probability and impact of a threat exploiting a vulnerability.'},
      {f:'Zero-Day',b:'A vulnerability unknown to the vendor with no available patch or fix.'},
      {f:'White Hat',b:'Ethical hacker with explicit authorization to test systems and improve security.'},
      {f:'Black Hat',b:'Malicious hacker who attacks systems without authorization for personal gain.'},
      {f:'Exploit',b:'A piece of code, tool, or technique that takes advantage of a vulnerability.'},
    ],
    summary:[
      'The CIA Triad (Confidentiality, Integrity, Availability) is the foundation of all security decisions.',
      'Risk = Threat × Vulnerability × Impact — understanding this drives all security investments.',
      'Ethical hacking requires explicit written authorization before any testing begins.',
      'CEH methodology follows 5 phases: Recon → Scan → Gain Access → Maintain Access → Cover Tracks.',
      'Defense in Depth and Least Privilege are essential enterprise security principles.',
    ],
    diagram:{
      title:'Information Security Threat Lifecycle',
      steps:[
        {icon:'👤',label:'Threat Actor Emerges',desc:'An adversary identifies your organization as a target with valuable data or systems.'},
        {icon:'🔍',label:'Reconnaissance',desc:'The attacker researches: open ports, employee names, software versions, IP ranges via OSINT.'},
        {icon:'💥',label:'Exploit Vulnerability',desc:'A weakness is exploited — unpatched software, weak password, phishing, or misconfiguration.'},
        {icon:'🔓',label:'CIA Triad Violated',desc:'Data is stolen (Confidentiality), altered (Integrity), or systems go offline (Availability).'},
        {icon:'🛡️',label:'Detection & Response',desc:'SIEM, IDS, or analysts detect anomaly and trigger the incident response process.'},
        {icon:'📋',label:'Remediation & Lessons',desc:'Root cause fixed, controls updated, post-incident report filed to prevent recurrence.'}
      ]
    },
    enterprise:{
      role:'You are the Security Architect at GlobalFinSec Corp.',
      situation:'An external audit flagged three critical gaps: no asset inventory, no data classification policy, and no formal incident response plan — ahead of a PCI-DSS compliance deadline.',
      challenge:'Map the CIA Triad to the top three assets (trading platform, customer database, internal email) and identify which controls are missing for each.',
      steps:[
        'List the three assets and classify them by CIA priority (customer DB = highest Confidentiality need).',
        'Run: nmap -sV 192.168.1.0/24 to discover what services are exposed on each asset.',
        'Check for missing patches on Windows hosts: systeminfo | findstr "OS Version".',
        'Identify existing controls (firewall? MFA? encryption?) and document gaps.',
        'Write a one-page risk register: Asset, Threat, Vulnerability, CIA Impact, Recommended Control.'
      ],
      outcome:'You identified 12 missing controls. The trading platform lacked MFA (Confidentiality), the database had no encryption at rest (Confidentiality + Integrity), and email had no DLP (Confidentiality).',
      lesson:'Every security investment must map to a CIA pillar. Without this framing, security spending cannot be justified to the board.'
    },
    pitfalls:[
      {icon:'⚠️',title:'Mistaking Compliance for Security',desc:'Passing a PCI-DSS or ISO audit does not mean you are secure. Compliance is a minimum bar, not a security guarantee.',fix:'Treat compliance as the floor. Layer additional threat-model-driven controls beyond regulatory minimums.'},
      {icon:'🔴',title:'Neglecting Availability in Security Planning',desc:'Security teams over-focus on Confidentiality (encryption, access control) and neglect Availability until a DDoS hits.',fix:'Include RTO/RPO metrics in all security plans. Regularly test failover and backup restoration.'},
      {icon:'⛔',title:'Treating Risk as a One-Time Assessment',desc:'A yearly risk assessment misses new vulnerabilities introduced by software updates, new vendors, and infrastructure changes.',fix:'Implement continuous risk monitoring. Reassess whenever major changes occur.'},
      {icon:'🎭',title:'Over-Relying on Perimeter Security',desc:'The castle-and-moat model assumes threats come from outside. Modern threats (insiders, cloud misconfigs) originate inside.',fix:'Adopt Zero Trust: verify every request as untrusted regardless of source location.'}
    ],
    lab:{
      title:'Lab: Map the CIA Triad to Real-World Scenarios',
      steps:[
        'Open a terminal on your Windows or Linux machine.',
        'Run <code>systeminfo</code> (Windows) or <code>uname -a && id</code> (Linux) to identify your current security posture.',
        'List active user accounts: Windows: <code>net user</code> | Linux: <code>cat /etc/passwd | grep -v nologin</code>',
        'Identify running services that affect Availability: Windows: <code>net start</code> | Linux: <code>systemctl list-units --state=running</code>',
        'Check last login times to assess potential unauthorized access (Integrity/Confidentiality): Linux: <code>last -n 20</code>',
        'Document your findings: which CIA pillar does each system control address?',
        'Write a one-paragraph risk statement using the format: "The [asset] is exposed to [threat] via [vulnerability], which violates [CIA pillar], with [impact]."',
      ]
    }
  },

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

// ═══════════════════════════════════════════════════════════
// XP & RANK SYSTEM
// ═══════════════════════════════════════════════════════════
const RANKS = [
  {min:0,label:'Script Kiddie',icon:'🐣'},
  {min:500,label:'Recon Specialist',icon:'🔍'},
  {min:1500,label:'Pen Tester',icon:'💻'},
  {min:3000,label:'Red Team Operator',icon:'🛡️'},
  {min:5000,label:'Exploit Developer',icon:'⚔️'},
  {min:8000,label:'Elite Hacker',icon:'💀'},
  {min:10000,label:'CEH Certified',icon:'🏆'},
];

let xp = parseInt(localStorage.getItem('ceh_xp')||'0');
let completed = JSON.parse(localStorage.getItem('ceh_completed')||'{}');
let currentTopic = null;

function getRank(x){ let r=RANKS[0]; for(const rk of RANKS) if(x>=rk.min) r=rk; return r; }

function addXP(amount, msg){
  xp += amount;
  localStorage.setItem('ceh_xp', xp);
  updateTopbar();
  showToast(`${msg} +${amount} XP ⚡`);
}

function showToast(msg){
  const t = document.getElementById('xp-toast');
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'), 3000);
}

function updateTopbar(){
  document.getElementById('xp-count').textContent = xp.toLocaleString();
  const rank = getRank(xp);
  document.getElementById('rank-badge').textContent = `${rank.icon} ${rank.label}`;
  updateProgress();
}

// ═══════════════════════════════════════════════════════════
// PROGRESS
// ═══════════════════════════════════════════════════════════
function updateProgress(){
  const total = MODULES.reduce((a,m)=>a+m.topics.length,0);
  const done = Object.keys(completed).length;
  const pct = total ? Math.round(done/total*100) : 0;
  document.getElementById('progress-pct').textContent = pct+'%';
  document.getElementById('topics-done').textContent = done;
  document.getElementById('topics-total').textContent = total;
  const circ = 2*Math.PI*20;
  document.getElementById('progress-ring').setAttribute('stroke-dashoffset', circ - (pct/100)*circ);
  document.querySelectorAll('.topic-btn').forEach(b=>{
    b.classList.toggle('done', !!completed[b.dataset.id]);
    const ch = b.querySelector('.topic-check');
    if(ch) ch.textContent = completed[b.dataset.id] ? '✓' : '';
  });
}

// ═══════════════════════════════════════════════════════════
// AUTH
// ═══════════════════════════════════════════════════════════
async function doLogin(){
  const email = document.getElementById('login-email').value.trim();
  const pass = document.getElementById('login-pass').value;
  const errEl = document.getElementById('login-error');
  const btn = document.getElementById('login-btn');
  btn.textContent = 'AUTHENTICATING...';
  btn.disabled = true;
  try {
    const r = await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,password:pass})});
    const data = await r.json();
    if(r.ok && data.token){
      localStorage.setItem('ceh_token',data.token);
      localStorage.setItem('ceh_email',data.email);
      errEl.style.display='none';
      bootApp(data.email);
    } else {
      errEl.textContent = data.error || 'Authentication failed. Access denied.';
      errEl.style.display = 'block';
    }
  } catch(e){
    errEl.textContent = 'Connection refused. Is the backend online?';
    errEl.style.display = 'block';
  }
  btn.textContent = 'AUTHENTICATE →';
  btn.disabled = false;
}

document.getElementById('login-pass').addEventListener('keydown', e=>{ if(e.key==='Enter') doLogin(); });
document.getElementById('login-email').addEventListener('keydown', e=>{ if(e.key==='Enter') document.getElementById('login-pass').focus(); });

async function checkAuth(){
  const token = localStorage.getItem('ceh_token');
  if(!token){ showLogin(); return; }
  try {
    const r = await fetch('/api/me',{headers:{Authorization:'Bearer '+token}});
    if(r.ok){ const u=await r.json(); bootApp(u.email); }
    else { localStorage.removeItem('ceh_token'); showLogin(); }
  } catch(e){ bootApp(localStorage.getItem('ceh_email')||'operator'); }
}

function showLogin(){ document.getElementById('ceh-login-overlay').style.display='flex'; }
function doLogout(){ localStorage.removeItem('ceh_token'); localStorage.removeItem('ceh_email'); location.reload(); }

function bootApp(email){
  document.getElementById('ceh-login-overlay').style.display='none';
  document.getElementById('ceh-app').style.display='flex';
  document.getElementById('user-email-display').textContent = email;
  renderSidebar();
  updateTopbar();
  initParticles();
}

// ═══════════════════════════════════════════════════════════
// SIDEBAR
// ═══════════════════════════════════════════════════════════
function renderSidebar(){
  const nav = document.getElementById('sidebar-nav');
  nav.innerHTML = MODULES.map((m,mi)=>`
    <div class="module-item" data-module="${m.id}">
      <div class="module-header" onclick="toggleModule('${m.id}',this)" ${mi===0?'':''}> 
        <span class="module-num">M${String(mi+1).padStart(2,'0')}</span>
        <span class="module-name">${m.name}</span>
        <span class="module-arrow">▶</span>
      </div>
      <div class="module-topics">
        ${m.topics.map(t=>`
          <button class="topic-btn" data-id="${t.id}" onclick="openTopic('${t.id}',this)">
            <span class="topic-check">${completed[t.id]?'✓':''}</span>
            ${t.name}
          </button>
        `).join('')}
      </div>
    </div>
  `).join('');
  // Open first module by default
  const first = nav.querySelector('.module-header');
  if(first){ first.classList.add('open'); }
}

function toggleModule(id, el){
  el.classList.toggle('open');
}

function filterModules(q){
  q = q.toLowerCase();
  document.querySelectorAll('.module-item').forEach(item=>{
    const name = item.querySelector('.module-name').textContent.toLowerCase();
    const topicBtns = item.querySelectorAll('.topic-btn');
    let anyMatch = name.includes(q);
    topicBtns.forEach(b=>{ const m=b.textContent.toLowerCase().includes(q); b.style.display=q&&!m?'none':''; if(m) anyMatch=true; });
    item.style.display = q && !anyMatch ? 'none' : '';
    if(q && anyMatch) item.querySelector('.module-header').classList.add('open');
  });
}

// ═══════════════════════════════════════════════════════════
// TOPIC VIEW
// ═══════════════════════════════════════════════════════════
function openTopic(id, btnEl){
  document.querySelectorAll('.topic-btn').forEach(b=>b.classList.remove('active'));
  if(btnEl) btnEl.classList.add('active');
  currentTopic = id;
  document.getElementById('welcome-screen').style.display='none';
  const view = document.getElementById('topic-view');
  view.style.display='block';
  const data = CONTENT[id] || TOPIC_STUBS[id] || {title:id,sub:'',module:''};
  view.innerHTML = buildTopicHTML(id, data);
  wireTopicTabs(id, data);
  initTerminal(id);
  wireCTF(id, data);
  wireQuiz(id, data);
  wireDragDrop(id, data);
  wireFlashcards(id, data);
  document.getElementById('content-area').scrollTop = 0;
}

function buildTopicHTML(id, d){
  const hasContent = !!CONTENT[id];
  return `
  <div class="topic-header">
    <div class="topic-eyebrow">${d.module||''}</div>
    <div class="topic-title">${d.title}</div>
    <div class="topic-sub">${d.sub}</div>
    ${d.killchain ? `<div style="margin-top:12px;">
      <span class="kc-badge">⛓ ${d.killchain.phase}</span>
      <span class="mitre-badge">🎯 MITRE: ${d.killchain.mitre}</span>
    </div>` : ''}
  </div>

  <div class="topic-tabs">
    <button class="tab-btn active" data-tab="learn">📚 Learn</button>
    <button class="tab-btn" data-tab="diagram">🔄 Diagram &amp; Workflow</button>
    <button class="tab-btn" data-tab="enterprise">🏢 Enterprise (GFS)</button>
    <button class="tab-btn" data-tab="commands">💻 Commands</button>
    <button class="tab-btn" data-tab="pitfalls">⚠️ Pitfalls &amp; Security</button>
    <button class="tab-btn" data-tab="lab">🔬 Hands-On Lab</button>
    <button class="tab-btn" data-tab="assessment">🎯 Assessment</button>
    <button class="tab-btn" data-tab="summary">📋 Summary</button>
  </div>

  <!-- LEARN -->
  <div class="tab-pane active" data-pane="learn">
    ${buildLearnHTML(d)}
  </div>

  <!-- DIAGRAM -->
  <div class="tab-pane" data-pane="diagram">
    ${buildDiagramHTML(d)}
  </div>

  <!-- ENTERPRISE -->
  <div class="tab-pane" data-pane="enterprise">
    ${buildEnterpriseHTML(d)}
  </div>

  <!-- COMMANDS + TERMINAL -->
  <div class="tab-pane" data-pane="commands">
    ${buildCommandsHTML(d)}
    <div class="terminal-wrap" style="margin-top:20px;">
      <div class="terminal-titlebar">
        <div class="t-dot red"></div><div class="t-dot yellow"></div><div class="t-dot green"></div>
        <span class="terminal-title">root@shadowxlab — ${d.title||''} shell</span>
      </div>
      <div class="terminal-output" id="term-output">
        <div class="t-line"><span class="t-success">ShadowXLab CEH v13 — Operator Shell</span></div>
        <div class="t-line"><span class="t-out">Commands for this topic are listed above. Type 'help' for all commands.</span></div>
        <div class="t-line">&nbsp;</div>
      </div>
      <div class="terminal-input-row">
        <span class="t-prompt-prefix">root@shadowxlab:~# </span>
        <input class="terminal-input" id="term-input" autocomplete="off" spellcheck="false" placeholder=""/>
      </div>
    </div>
  </div>

  <!-- PITFALLS -->
  <div class="tab-pane" data-pane="pitfalls">
    ${buildPitfallsHTML(d)}
  </div>

  <!-- HANDS-ON LAB -->
  <div class="tab-pane" data-pane="lab">
    ${buildLabHTML(d)}
  </div>

  <!-- ASSESSMENT -->
  <div class="tab-pane" data-pane="assessment">
    ${buildAssessmentHTML(d)}
  </div>

  <!-- SUMMARY -->
  <div class="tab-pane" data-pane="summary">
    ${buildSummaryHTML(id,d)}
  </div>
  `;
}

// -- COMING SOON PLACEHOLDER --
function buildComingSoonHTML(icon,message){
  return `<div class="classified-card"><div class="classified-icon">${icon}</div><div class="classified-title">${message}</div><div class="classified-bar"></div><div class="classified-sub">ShadowXLab analysts are preparing this content. Check back soon.</div></div>`;
}

// -- TAB 1: LEARN --
function buildLearnHTML(d){
  if(!d.learn||!d.learn.simple) return buildComingSoonHTML('\u{1F4DA}','Learn content is being prepared');
  return `
  <div class="mission-grid">
    <div class="info-card"><div class="card-label">SIMPLE EXPLANATION</div><div class="card-text">${d.learn.simple}</div></div>
    <div class="info-card"><div class="card-label">ANALOGY</div><div class="card-text">${d.learn.analogy}</div></div>
    <div class="info-card"><div class="card-label">WHY IT EXISTS</div><div class="card-text">${d.learn.why}</div></div>
    <div class="info-card"><div class="card-label">HOW IT WORKS</div><div class="card-text">${d.learn.architecture}</div></div>
  </div>`;
}

// -- TAB 2: DIAGRAM --
function buildDiagramHTML(d){
  if(!d.diagram||!d.diagram.steps||!d.diagram.steps.length) return buildComingSoonHTML('\u{1F504}','Diagram & Workflow is being designed');
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--blue);margin-bottom:24px;font-family:var(--mono);">${d.diagram.title||'Process Flow'}</div>
    <div class="diagram-flow">
      ${d.diagram.steps.map((s,i)=>`
        <div class="diagram-step">
          <div class="diagram-step-icon">${s.icon||'▶'}</div>
          <div class="diagram-step-body">
            <div class="diagram-step-label">Step ${i+1}: ${s.label}</div>
            <div class="diagram-step-desc">${s.desc}</div>
          </div>
        </div>
        ${i<d.diagram.steps.length-1?'<div class="diagram-arrow">↓</div>':''}
      `).join('')}
    </div>
  </div>`;
}

// -- TAB 3: ENTERPRISE --
function buildEnterpriseHTML(d){
  if(!d.enterprise) return buildComingSoonHTML('\u{1F3E2}','Enterprise scenario is being written');
  const e=d.enterprise;
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:24px;">
      <div style="font-size:2.2rem;">\u{1F3E2}</div>
      <div>
        <div style="font-size:0.7rem;font-family:var(--mono);color:var(--green);letter-spacing:0.12em;">ENTERPRISE SCENARIO — GLOBALFINSEC CORP</div>
        <div style="font-size:1rem;font-weight:700;color:var(--text);">${e.role||'Lead Penetration Tester'}</div>
      </div>
    </div>
    <div class="enterprise-grid">
      <div class="ent-card ent-situation"><div class="ent-label">\u{1F4CB} SITUATION</div><div class="ent-text">${e.situation||''}</div></div>
      <div class="ent-card ent-challenge"><div class="ent-label">\u{1F3AF} YOUR CHALLENGE</div><div class="ent-text">${e.challenge||''}</div></div>
    </div>
    ${e.steps&&e.steps.length?`<div style="margin-top:20px;">
      <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:12px;">// YOUR INVESTIGATION STEPS</div>
      ${e.steps.map((s,i)=>`<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:10px;padding:12px;background:rgba(0,0,0,0.3);border-radius:8px;border-left:3px solid var(--green);"><span style="font-family:var(--mono);color:var(--green);font-size:0.75rem;min-width:20px;">${i+1}.</span><span style="font-size:0.88rem;color:var(--text);">${s}</span></div>`).join('')}
    </div>`:''}
    <div class="ent-card" style="margin-top:20px;background:rgba(0,200,83,0.08);border-color:rgba(0,200,83,0.3);">
      <div class="ent-label">\u2705 OUTCOME &amp; LESSON</div>
      <div class="ent-text"><strong>Outcome:</strong> ${e.outcome||''}</div>
      <div class="ent-text" style="margin-top:8px;"><strong>Key Lesson:</strong> ${e.lesson||''}</div>
    </div>
  </div>`;
}

// -- TAB 4: COMMANDS --
function buildCommandsHTML(d){
  const tools=d.tools||[];
  const cmds=d.commands||{win:[],lin:[]};
  return `
  ${tools.length?`<div style="margin-bottom:20px;"><div class="card-label" style="margin-bottom:12px;">KEY TOOLS</div><div style="display:flex;gap:10px;flex-wrap:wrap;">${tools.map(t=>`<div style="background:rgba(0,0,0,0.4);border:1px solid var(--border);border-radius:var(--radius);padding:12px 16px;min-width:180px;"><div style="font-weight:600;color:var(--blue);margin-bottom:4px;">${t.name}</div><div style="font-family:var(--mono);font-size:0.75rem;color:var(--green);margin-bottom:4px;">$ ${t.cmd}</div><div style="font-size:0.78rem;color:var(--text-muted);">${t.desc}</div></div>`).join('')}</div></div>`:''}
  <div class="cmd-grid">
    <div class="cmd-block">
      <div class="cmd-os">\u25B6 WINDOWS</div>
      ${cmds.win&&cmds.win.length?cmds.win.map(c=>`<div class="cmd-line">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Windows commands for this topic.</div>'}
    </div>
    <div class="cmd-block">
      <div class="cmd-os">\u25B6 LINUX / KALI</div>
      ${cmds.lin&&cmds.lin.length?cmds.lin.map(c=>`<div class="cmd-line">${c}</div>`).join(''):'<div style="color:var(--text-dim);font-size:0.8rem;padding:8px;">No Linux commands for this topic.</div>'}
    </div>
  </div>`;
}

// -- TAB 5: PITFALLS --
function buildPitfallsHTML(d){
  if(!d.pitfalls||!d.pitfalls.length) return buildComingSoonHTML('\u26A0','Pitfalls & Security analysis is being prepared');
  return `<div style="display:flex;flex-direction:column;gap:16px;">${d.pitfalls.map((p,i)=>`
    <div style="background:rgba(255,59,92,0.07);border:1px solid rgba(255,59,92,0.25);border-radius:var(--radius);padding:20px;">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
        <span style="font-size:1.3rem;">${p.icon||'\u26A0'}</span>
        <span style="font-weight:700;color:var(--red);font-size:0.95rem;">${p.title}</span>
        <span style="margin-left:auto;font-family:var(--mono);font-size:0.65rem;background:rgba(255,59,92,0.15);color:var(--red);padding:3px 8px;border-radius:20px;">PITFALL #${i+1}</span>
      </div>
      <div style="font-size:0.87rem;color:var(--text);margin-bottom:10px;">${p.desc}</div>
      <div style="background:rgba(0,200,83,0.08);border:1px solid rgba(0,200,83,0.2);border-radius:8px;padding:10px;">
        <span style="font-family:var(--mono);font-size:0.7rem;color:var(--green);">\u2713 FIX: </span>
        <span style="font-size:0.84rem;color:var(--text-muted);">${p.fix}</span>
      </div>
    </div>
  `).join('')}</div>`;
}

// -- TAB 6: LAB --
function buildLabHTML(d){
  if(!d.lab) return buildComingSoonHTML('\u{1F52C}','Hands-On Lab is being designed');
  const dc={'Beginner':'var(--green)','Intermediate':'var(--blue)','Advanced':'var(--red)'};
  const color=dc[d.lab.difficulty]||'var(--text-dim)';
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:24px;">
    <div style="display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px;flex-wrap:wrap;gap:10px;">
      <div>
        <div style="font-size:1.1rem;font-weight:700;color:var(--green);">\u{1F52C} ${d.lab.title}</div>
        ${d.lab.objectives&&d.lab.objectives.length?`<div style="margin-top:8px;">${d.lab.objectives.map(o=>`<div style="font-size:0.82rem;color:var(--text-muted);margin-top:4px;">\u2746 ${o}</div>`).join('')}</div>`:''}
      </div>
      <div style="display:flex;flex-direction:column;gap:6px;align-items:flex-end;">
        <span style="font-family:var(--mono);font-size:0.7rem;background:rgba(0,0,0,0.4);border:1px solid var(--border);padding:4px 10px;border-radius:20px;color:${color};">${d.lab.difficulty||'Beginner'}</span>
        <span style="font-family:var(--mono);font-size:0.7rem;color:var(--text-dim);">\u23F1 ${d.lab.duration||'30 min'}</span>
      </div>
    </div>
    ${d.lab.steps.map((s,i)=>`<div class="lab-step" style="cursor:pointer;" onclick="toggleLabStep(this)"><div class="lab-step-num">${i+1}</div><div class="lab-step-text">${s}</div><span class="lab-check" style="opacity:0;">\u2713</span></div>`).join('')}
    ${d.lab.validation?`<div style="margin-top:20px;padding:14px;background:rgba(0,200,83,0.08);border:1px solid rgba(0,200,83,0.25);border-radius:8px;"><div style="font-family:var(--mono);font-size:0.7rem;color:var(--green);margin-bottom:6px;">\u2713 HOW TO CONFIRM SUCCESS</div><div style="font-size:0.86rem;color:var(--text-muted);">${d.lab.validation}</div></div>`:''}
  </div>`;
}

// -- TAB 7: ASSESSMENT --
function buildAssessmentHTML(d){
  return `
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 1 OF 3 — KNOWLEDGE CHECK</div>
    <div class="quiz-score" id="quiz-score" style="display:none;"></div>
    ${buildQuizHTML(d)}
  </div>
  <div style="margin-bottom:32px;">
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 2 OF 3 — FLASHCARDS (hover to flip)</div>
    ${buildFlashcardsHTML(d)}
  </div>
  <div>
    <div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);letter-spacing:0.1em;margin-bottom:16px;padding:10px;background:rgba(0,0,0,0.3);border-radius:8px;">// SECTION 3 OF 3 — CAPTURE THE FLAG</div>
    ${buildCTFHTML(d)}
  </div>`;
}

// -- TAB 8: SUMMARY --
function buildSummaryHTML(id,d){
  const isDone=!!completed[id];
  return `
  <div style="background:var(--panel);border:1px solid var(--border);border-radius:var(--radius);padding:28px;">
    <div style="font-size:1rem;font-weight:700;color:var(--green);margin-bottom:20px;font-family:var(--mono);">// KEY TAKEAWAYS — EXAM READY</div>
    ${d.summary&&d.summary.length?`<ul class="summary-list">${d.summary.map(s=>`<li>${s}</li>`).join('')}</ul>`:'<div style="color:var(--text-dim);">Summary content coming soon.</div>'}
    <div style="margin-top:32px;padding-top:24px;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
      <div id="complete-status-${id}" style="font-family:var(--mono);font-size:0.8rem;color:var(--text-dim);">
        ${isDone?'<span style="color:var(--green);">\u2713 TOPIC COMPLETED — XP AWARDED</span>':'Complete all sections, then mark done to earn XP.'}
      </div>
      <button class="btn-complete" id="btn-complete-${id}" onclick="markComplete('${id}')"
        ${isDone?'disabled style="opacity:0.5;cursor:default;"':''}>
        ${isDone?'\u2713 COMPLETED':'\u2714 MARK COMPLETE — EARN 200 XP'}
      </button>
    </div>
  </div>`;
}

// -- QUIZ --
function buildQuizHTML(d){
  if(!d.quiz||!d.quiz.length) return buildComingSoonHTML('\u2753','Quiz — 10 questions coming soon');
  return d.quiz.map((q,i)=>`
    <div class="quiz-q" data-qi="${i}" data-correct="${q.correct}">
      <div class="quiz-q-num">QUESTION ${String(i+1).padStart(2,'0')} / ${d.quiz.length}</div>
      <div class="quiz-q-text">${q.q}</div>
      <div class="quiz-opts">${q.opts.map((o,oi)=>`<button class="quiz-opt" data-oi="${oi}" onclick="answerQuiz(this,${i},${oi})">${o}</button>`).join('')}</div>
      <div class="quiz-fb">${q.fb}</div>
    </div>
  `).join('');
}

// -- FLASHCARDS --
function buildFlashcardsHTML(d){
  if(!d.flashcards||!d.flashcards.length) return buildComingSoonHTML('\u{1F0CF}','Flashcards coming soon');
  return `
  <div style="margin-bottom:10px;font-family:var(--mono);font-size:0.75rem;color:var(--text-muted);">// Hover a card to flip and reveal the definition</div>
  <div class="flashcards-grid">${d.flashcards.map(f=>`<div class="flashcard"><div class="fc-front">${f.f}</div><div class="fc-back">${f.b}</div></div>`).join('')}</div>`;
}

// -- CTF --
function buildCTFHTML(d){
  const ctf=d.ctf||{scenario:'Complete all sections to unlock the CTF challenge.',hint:'Study the Learn and Commands tabs first.',flag:'',points:150};
  return `
  <div class="ctf-card">
    <div class="ctf-header"><div class="ctf-flag-icon">\u{1F6A9}</div><div><div class="ctf-title">CAPTURE THE FLAG</div><div class="ctf-subtitle">// CLASSIFIED INTELLIGENCE CHALLENGE</div></div></div>
    <div class="ctf-points">\u{1F48E} ${ctf.points||150} POINTS</div>
    <div class="ctf-scenario">${ctf.scenario}</div>
    <div class="ctf-hint" id="ctf-hint" onclick="revealHint(this)" data-hint="${ctf.hint||''}">\u{1F4A1} HINT: Click to reveal (costs no points)</div>
    <div class="ctf-input-row">
      <input class="ctf-input" id="ctf-flag-input" placeholder="CEH{your_flag_here}" autocomplete="off" spellcheck="false"/>
      <button class="ctf-submit" onclick="submitCTF('${currentTopic}')">SUBMIT FLAG</button>
    </div>
    <div class="ctf-result" id="ctf-result"></div>
  </div>`;
}

// ── TAB WIRING ──
function wireTopicTabs(id, d){
  document.querySelectorAll('.tab-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
      btn.classList.add('active');
      document.querySelector(`.tab-pane[data-pane="${btn.dataset.tab}"]`).classList.add('active');
    });
  });
}

// ── TERMINAL ──
const TERMINAL_CMDS = {
  help: `Available commands:\n  whoami         — Identify current operator\n  nmap -h        — Network scanner help\n  ls -la         — List directory contents\n  uname -a       — System information\n  clear          — Clear terminal\n  ps aux         — List running processes\n  netstat -tulnp — Active network connections\n  id             — User identity and groups`,
  whoami: 'root (authenticated CEH operator — ShadowXLab)',
  'uname -a': 'Linux shadowxlab 6.1.0-kali-amd64 #1 SMP Debian 6.1.15-1kali1 x86_64 GNU/Linux',
  'ls -la': `total 48\ndrwxr-xr-x 8 root root 4096 Jul 17 09:00 .\ndrwxr-xr-x 3 root root 4096 Jul 17 09:00 ..\n-rw------- 1 root root 1234 Jul 17 09:00 .bash_history\n-rw-r--r-- 1 root root  570 Jul 17 09:00 .bashrc\ndrwxr-xr-x 4 root root 4096 Jul 17 09:00 tools\ndrwxr-xr-x 2 root root 4096 Jul 17 09:00 reports`,
  'ps aux': `root      1234  0.0  0.1  4680  3200 pts/0   Ss   09:00   0:00 bash\nroot      5678  2.1  0.5 34012 12800 pts/0   S    09:01   0:02 python3 scan.py\nroot      9012  0.0  0.0  3748  1024 pts/0   R+   09:05   0:00 ps aux`,
  'netstat -tulnp': `Active Internet connections (only servers)\nProto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program\ntcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      890/sshd\ntcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1023/nginx\ntcp6       0      0 :::3000                 :::*                    LISTEN      1456/node`,
  id: 'uid=0(root) gid=0(root) groups=0(root)',
  'nmap -h': `Nmap 7.94SVN ( https://nmap.org )\nUsage: nmap [Scan Type(s)] [Options] {target specification}\n  -sS: TCP SYN Scan (stealth)\n  -sV: Version detection\n  -A:  OS detection, version, scripts, traceroute\n  -p:  Specify ports (e.g., -p 80,443 or -p-)\n  -O:  OS detection\n  --script: Run NSE scripts`,
  pwd: '/root',
  'cat /etc/os-release': `NAME="Kali GNU/Linux"\nVERSION="2024.2"\nID=kali\nID_LIKE=debian\nHOME_URL="https://www.kali.org/"`,
};

function initTerminal(topicId){
  const input = document.getElementById('term-input');
  if(!input) return;
  input.addEventListener('keydown', e=>{
    if(e.key==='Enter'){
      const cmd = input.value.trim();
      input.value = '';
      if(!cmd) return;
      appendTermLine(`root@shadowxlab:~# ${cmd}`, 'prompt');
      const out = TERMINAL_CMDS[cmd.toLowerCase()];
      if(out){ out.split('\n').forEach(l=>appendTermLine(l,'out')); }
      else if(cmd==='clear'){ document.getElementById('term-output').innerHTML=''; }
      else { appendTermLine(`bash: ${cmd}: command not found`, 'err'); appendTermLine(`Try 'help' for available commands`,'out'); }
      const termOut = document.getElementById('term-output');
      if(termOut) termOut.scrollTop = termOut.scrollHeight;
    }
  });
  input.focus();
}

function appendTermLine(text, type='out'){
  const out = document.getElementById('term-output');
  if(!out) return;
  const div = document.createElement('div');
  div.className = 't-line';
  const cls = type==='prompt'?'t-cmd':type==='err'?'t-err':type==='success'?'t-success':'t-out';
  div.innerHTML = `<span class="${cls}">${escapeHtml(text)}</span>`;
  out.appendChild(div);
}

function escapeHtml(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

// ── CTF ──
function wireCTF(id, d){}
function revealHint(el){ el.classList.add('revealed'); el.textContent = '💡 HINT: ' + (el.dataset.hint||'Think carefully about the context.'); }

async function submitCTF(topicId){
  const flag = document.getElementById('ctf-flag-input').value.trim();
  const res = document.getElementById('ctf-result');
  if(!flag){ res.textContent='Enter a flag first.'; res.className='ctf-result fail'; res.style.display='block'; return; }
  try {
    const r = await fetch('/api/ctf/submit',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer '+(localStorage.getItem('ceh_token')||'')},body:JSON.stringify({topic_id:topicId,flag})});
    const data = await r.json();
    if(data.correct){
      res.textContent = '🚩 ' + data.message;
      res.className = 'ctf-result success';
      if(!completed[topicId]) addXP(data.xp||150, '🚩 Flag Captured!');
      completed[topicId] = true;
      localStorage.setItem('ceh_completed', JSON.stringify(completed));
      updateProgress();
    } else {
      res.textContent = data.message;
      res.className = 'ctf-result fail';
    }
    res.style.display = 'block';
  } catch(e){
    res.textContent = '⚠️ Backend unreachable. Flag: '+flag+' noted locally.';
    res.className = 'ctf-result fail';
    res.style.display = 'block';
  }
}

// ── QUIZ ──
function wireQuiz(id, d){
  let score=0, answered=0;
  document.querySelectorAll('.quiz-q').forEach(qEl=>{
    const qi = parseInt(qEl.dataset.qi);
    const correct = parseInt(qEl.dataset.correct);
    qEl.querySelectorAll('.quiz-opt').forEach(opt=>{
      opt.addEventListener('click', ()=>{
        if(qEl.dataset.answered) return;
        qEl.dataset.answered = '1';
        answered++;
        const oi = parseInt(opt.dataset.oi);
        if(oi===correct){ opt.classList.add('correct'); score++; }
        else { opt.classList.add('wrong'); qEl.querySelectorAll('.quiz-opt')[correct].classList.add('correct'); }
        qEl.querySelector('.quiz-fb').style.display = 'block';
        qEl.querySelectorAll('.quiz-opt').forEach(o=>o.setAttribute('disabled',''));
        const total = d.quiz.length;
        const scoreEl = document.getElementById('quiz-score');
        if(scoreEl){ scoreEl.textContent = `Score: ${score} / ${answered} answered`; scoreEl.style.display='block'; }
        if(answered===total && score>=8 && !completed[id]){
          addXP(100, '📝 Quiz Passed!');
          completed[id] = true;
          localStorage.setItem('ceh_completed',JSON.stringify(completed));
          updateProgress();
        }
      });
    });
  });
}

function answerQuiz(el, qi, oi){ el.click(); }

// ── FLASHCARDS & DRAG DROP ──
function wireFlashcards(id, d){}
function wireDragDrop(id, d){}

// -- MARK COMPLETE --
async function markComplete(topicId){
  const btn=document.getElementById('btn-complete-'+topicId);
  if(!btn||btn.disabled) return;
  const token=localStorage.getItem('ceh_token');
  if(!token) return;
  btn.textContent='SAVING...'; btn.disabled=true;
  try{
    const r=await fetch('/api/progress/topic',{method:'POST',
      headers:{'Content-Type':'application/json','Authorization':'Bearer '+token},
      body:JSON.stringify({topic_id:topicId,xp_earned:200,flag_captured:false})});
    const data=await r.json();
    if(r.ok){
      completed[topicId]=true; totalXP=data.total_xp||(totalXP+200);
      localStorage.setItem('ceh_completed',JSON.stringify(completed));
      updateProgressUI(); updateTopicButtons();
      btn.textContent='✓ COMPLETED'; btn.style.opacity='0.5'; btn.style.cursor='default';
      const st=document.getElementById('complete-status-'+topicId);
      if(st) st.innerHTML='<span style="color:var(--green);">✓ TOPIC COMPLETED — XP AWARDED</span>';
    } else { btn.textContent='✔ MARK COMPLETE — EARN 200 XP'; btn.disabled=false; }
  }catch(e){ btn.textContent='✔ MARK COMPLETE — EARN 200 XP'; btn.disabled=false; }
}

// -- LAB STEP TOGGLE --
function toggleLabStep(el){
  const check=el.querySelector('.lab-check');
  if(!check) return;
  const done=check.style.opacity==='1';
  check.style.opacity=done?'0':'1';
  el.style.background=done?'':'rgba(0,200,83,0.06)';
}

// ═══════════════════════════════════════════════════════════
// PARTICLES
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
