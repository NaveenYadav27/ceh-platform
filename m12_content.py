import os

html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

payload = """
CONTENT['ids-firewall-concepts'] = {
  eyebrow: 'Module 12 · Topic 1',
  title: 'IDS and Firewall Concepts',
  module: 'Phase 12: Advanced Penetration Tester',
  sub: 'Understanding the foundational concepts of Intrusion Detection Systems and Firewalls.',
  objectives: ['Understand IDS architectures', 'Identify firewall types', 'Differentiate between stateful and stateless firewalls'],
  learn: {
    simple: 'Intrusion Detection Systems (IDS) and Firewalls are fundamental components of network security. An IDS monitors network traffic for suspicious activities and issues alerts when such activities are discovered. Firewalls, on the other hand, act as a barrier between a trusted network and an untrusted network, controlling incoming and outgoing network traffic based on predetermined security rules.\\n\\nWhile a firewall actively blocks traffic, an IDS is primarily a passive system that analyzes traffic patterns. Modern networks often combine these capabilities into Intrusion Prevention Systems (IPS) and Next-Generation Firewalls (NGFW).',
    analogy: 'A firewall is like the bouncer at the club door checking IDs and deciding who gets in. An IDS is like the security cameras inside watching for bad behavior.',
    architecture: 'IDS architectures typically consist of sensors, an analysis engine, and a reporting mechanism. Network-based IDS (NIDS) sensors monitor traffic on network segments, while Host-based IDS (HIDS) monitor activity on individual endpoints. Firewalls can be implemented in hardware or software and operate at different layers of the OSI model, such as packet-filtering (Layer 3/4), stateful inspection (Layer 4/5), or application-level gateways (Layer 7).',
    why: 'Understanding these systems is critical because they form the first line of defense in enterprise networks. Bypassing them is often a necessary first step for penetration testers.'
  },
  enterprise: {
    gfs: 'Global Financial Services relies on stateful firewalls to protect its core banking systems, alongside NIDS deployed at key network chokepoints to monitor for anomalies in transaction traffic.',
    windows: 'Windows Defender Firewall with Advanced Security provides host-based firewall capabilities, while Windows Event Forwarding can feed logs into an enterprise HIDS/SIEM.',
    linux: 'Linux environments frequently use iptables or nftables for host-based firewalls, and Suricata or Snort for NIDS deployments.'
  },
  workflow: ['Step 1: Identify firewall presence using port scanning.', 'Step 2: Determine firewall rules via protocol testing.', 'Step 3: Analyze IDS responses to malformed packets.', 'Step 4: Map network architecture based on firewall responses.', 'Step 5: Identify potential bypass vectors.', 'Step 6: Document discovered security controls.'],
  diagram: {
    caption: 'Click to interact with the IDS/Firewall Architecture diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="500" height="300" fill="#f0f0f0"/><text x="300" y="200" text-anchor="middle">IDS/Firewall Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -sS -p 80,443 192.168.1.1', purpose: 'SYN Stealth Scan', out: 'Open/Closed/Filtered ports', note: 'Basic scan to identify firewall filtering', mistake: 'Scanning without rate limiting triggers IDS' }
    ],
    win: [
      { cmd: 'Get-NetFirewallRule', purpose: 'Check Firewall Rules', out: 'List of rules', note: 'Useful for auditing local firewall configuration', mistake: 'Ignoring profile scopes (Domain, Private, Public)' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'Snort'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to audit its edge firewall configuration to ensure it effectively blocks unauthorized access while allowing legitimate traffic.',
    objectives: ['Identify filtered ports using Nmap.', 'Analyze firewall responses to different scan types.'],
    steps: ['Step 1: Run an ACK scan to map firewall rules (`nmap -sA 10.10.10.1`).', 'Step 2: Observe the results to determine stateful inspection.', 'Step 3: Attempt a FIN scan to bypass stateless filters (`nmap -sF 10.10.10.1`).'],
    evidence: ['Terminal output showing filtered and unfiltered ports.'],
    validation: ['You should see: Ports marked as unfiltered by the ACK scan but closed or open in SYN scan.'],
    troubleshooting: ['If all ports appear filtered, ensure the target IP is correct and reachable.'],
    mitre: [{ id: 'T1562', name: 'Impair Defenses', tactic: 'Defense Evasion' }],
    cleanup: ['Stop the Nmap scans.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which type of firewall keeps track of the state of network connections?', opts: ['Packet-filtering firewall', 'Stateful firewall', 'Application-level gateway', 'Circuit-level gateway'], correct: 1, fb: 'Stateful firewalls maintain a state table to track active connections.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary function of an IDS?', opts: ['Block malicious traffic', 'Route network packets', 'Monitor traffic for suspicious activity', 'Encrypt sensitive data'], correct: 2, fb: 'An IDS primarily monitors and alerts on suspicious activity, unlike an IPS which blocks it.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which OSI layer does a packet-filtering firewall primarily operate on?', opts: ['Layer 2', 'Layer 3', 'Layer 7', 'Layer 1'], correct: 1, fb: 'Packet-filtering firewalls operate at the Network layer (Layer 3).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a false positive in the context of an IDS?', opts: ['Malicious traffic not detected', 'Benign traffic flagged as malicious', 'Malicious traffic successfully blocked', 'A crashed sensor'], correct: 1, fb: 'A false positive occurs when legitimate traffic is incorrectly identified as an attack.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a host-based firewall?', opts: ['Cisco ASA', 'Palo Alto NGFW', 'Windows Defender Firewall', 'Snort'], correct: 2, fb: 'Windows Defender Firewall is a host-based firewall software.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: An IPS is typically deployed in-line with network traffic.', opts: ['True', 'False', 'Depends on the OS', 'None of the above'], correct: 0, fb: 'True. An IPS must be in-line to actively block traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which evasion technique involves splitting packets?', opts: ['IP Spoofing', 'Source Routing', 'Fragmentation', 'Decoys'], correct: 2, fb: 'Fragmentation involves splitting the payload into smaller packets to evade detection.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Next-Generation Firewall (NGFW)?', opts: ['A firewall that only filters by IP', 'A firewall combining traditional filtering with application awareness and IPS', 'A hardware-only firewall', 'A firewall that cannot inspect SSL traffic'], correct: 1, fb: 'NGFWs integrate multiple security features including deep packet inspection and IPS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used as an open-source NIDS?', opts: ['Wireshark', 'Metasploit', 'Snort', 'Nmap'], correct: 2, fb: 'Snort is a widely used open-source network intrusion detection system.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of an application-level gateway?', opts: ['Filter traffic based on MAC addresses', 'Filter traffic at the application layer of the OSI model', 'Provide wireless security', 'Encrypt network storage'], correct: 1, fb: 'Application-level gateways operate at Layer 7 to filter specific application data.' }
  ],
  flashcards: [
    { f: 'IDS', b: 'Intrusion Detection System; monitors for suspicious activity.' },
    { f: 'Stateful Firewall', b: 'A firewall that tracks the state of active network connections.' }
  ],
  summary: ['IDS monitors for threats passively.', 'Firewalls enforce network access policies.', 'Stateful inspection tracks connection state.', 'Understanding these systems helps in designing evasive attacks.', 'Enterprise networks use a layered security approach.'],
  outcomes: ['Differentiate between IDS and firewalls.', 'Explain stateful vs stateless inspection.', 'Identify common enterprise security architectures.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['evasion-techniques'] = {
  eyebrow: 'Module 12 · Topic 2',
  title: 'Evasion Techniques',
  module: 'Phase 12: Advanced Penetration Tester',
  sub: 'Advanced methods for bypassing network defenses.',
  objectives: ['Master packet fragmentation', 'Understand decoy scanning', 'Learn timing and obfuscation techniques'],
  learn: {
    simple: 'Evasion techniques are strategies used by attackers and penetration testers to bypass security controls like Firewalls and IDS. These techniques aim to disguise malicious traffic or exploit weaknesses in how security devices process packets.\\n\\nCommon methods include fragmentation, where the attack payload is split across multiple packets to avoid signature matching, and using decoys to mask the true source of an attack.',
    analogy: 'Evasion is like wearing a disguise and sending fake delivery trucks to a building so the guards do not notice the real thief sneaking in.',
    architecture: 'IDS and firewalls must reassemble fragmented packets to inspect them properly. If an IDS uses a different reassembly method than the target host, it might fail to detect an attack (insertion or evasion attacks). Attackers exploit these discrepancies at the network (Layer 3) and transport (Layer 4) levels. Techniques like IP Address Decoys (sending spoofed packets alongside real ones) and Timing/Rate Limiting (sending packets very slowly) help bypass detection thresholds.',
    why: 'Security controls are imperfect. Penetration testers must use evasion techniques to simulate sophisticated adversaries who will attempt to bypass standard defenses rather than attacking them head-on.'
  },
  enterprise: {
    gfs: 'GFS regularly tests its NIDS by simulating fragmented attacks to ensure its security appliances correctly reassemble and inspect complex packet flows.',
    windows: 'Attackers might use PowerShell obfuscation to evade Windows Defender before making network connections that could trigger a host-based firewall alert.',
    linux: 'Evasion on Linux targets often involves manipulating TTL values to ensure packets reach the target but expire before reaching the IDS.'
  },
  workflow: ['Step 1: Identify the target IDS/Firewall characteristics.', 'Step 2: Test basic fragmentation against the target.', 'Step 3: Introduce decoy traffic to dilute logs.', 'Step 4: Adjust packet timing (e.g., sneaky or paranoid modes).', 'Step 5: Utilize source routing or spoofed MAC addresses if on local segment.', 'Step 6: Validate successful bypass by confirming payload execution.'],
  diagram: {
    caption: 'Click to interact with the Evasion Techniques diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="500" height="300" fill="#e0e0e0"/><text x="300" y="200" text-anchor="middle">Packet Fragmentation Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -f -D 10.1.1.1,10.1.1.2 192.168.1.5', purpose: 'Fragmentation & Decoy', out: 'Scan results', note: 'Use cautiously', mistake: 'Too many decoys can cause network congestion' }
    ],
    win: [
      { cmd: 'Invoke-Obfuscation -ScriptBlock {Write-Host "Test"}', purpose: 'PowerShell Obfuscation', out: 'Obfuscated command', note: 'Bypasses basic HIDS signatures', mistake: 'Over-obfuscating making the payload invalid' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'Hping3'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'You are tasked with testing the evasion capabilities of the newly deployed GFS intrusion detection system.',
    objectives: ['Perform a fragmented scan.', 'Use decoy IP addresses to obscure the origin.'],
    steps: ['Step 1: Start Snort on the target.', 'Step 2: Run a standard Nmap scan and observe Snort alerts.', 'Step 3: Run `nmap -f -sS 192.168.1.5` and observe alerts.', 'Step 4: Add decoys `nmap -D RND:10 192.168.1.5`.'],
    evidence: ['Terminal output showing successful scans with fewer/no Snort alerts.'],
    validation: ['You should see: The target ports are discovered but Snort fails to trigger on the fragmented payloads.'],
    troubleshooting: ['If Snort still detects it, try adjusting the MTU size (`--mtu 8`).'],
    mitre: [{ id: 'T1562.001', name: 'Disable or Modify Tools', tactic: 'Defense Evasion' }],
    cleanup: ['Stop the scans and the Snort service.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does the Nmap `-f` flag do?', opts: ['Fast scan', 'Fragment packets', 'Force connection', 'Find MAC address'], correct: 1, fb: 'The -f flag fragments IP packets to evade firewalls and IDS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does a decoy scan work?', opts: ['It sends fake payloads', 'It hides the attacker IP among spoofed IPs', 'It uses encryption', 'It attacks a honeypot'], correct: 1, fb: 'Decoy scans send packets from spoofed IPs alongside the attacker\'s IP to confuse defenders.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which evasion technique relies on sending traffic very slowly?', opts: ['Fragmentation', 'Timing / Rate Limiting', 'Source Routing', 'MAC Spoofing'], correct: 1, fb: 'Sending traffic slowly can evade threshold-based detection rules in an IDS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is an insertion attack against an IDS?', opts: ['Inserting malicious code into the database', 'Sending packets the IDS accepts but the target rejects', 'Sending packets the target accepts but the IDS rejects', 'SQL injection'], correct: 1, fb: 'In an insertion attack, the IDS accepts dummy packets that the target host drops, causing the IDS to assemble a different stream than the target.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is an evasion attack against an IDS?', opts: ['Sending packets the IDS accepts but target rejects', 'Sending packets the IDS drops but the target accepts', 'Bypassing physical security', 'Using a VPN'], correct: 1, fb: 'In an evasion attack, the IDS drops a packet that the target host accepts, causing the IDS to miss part of the payload.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: Using random source ports can help evade simple firewall rules.', opts: ['True', 'False', 'Depends on the OS', 'None of the above'], correct: 0, fb: 'True. Some firewalls might trust traffic originating from specific ports like 53 or 80.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which Nmap option is used to specify a custom MTU?', opts: ['-m', '--mtu', '--max-transmission', '-M'], correct: 1, fb: 'The --mtu option allows specifying a custom maximum transmission unit for fragmentation.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does changing the TTL (Time to Live) help evade?', opts: ['Intrusion Prevention Systems (IPS)', 'Certain IDS deployments', 'Antivirus', 'Web Application Firewalls'], correct: 1, fb: 'Manipulating TTL can cause packets to reach the IDS but expire before reaching the target host.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is frequently used for crafting custom packets for evasion?', opts: ['Hping3', 'Nessus', 'John the Ripper', 'Dirb'], correct: 0, fb: 'Hping3 is a powerful tool for crafting custom TCP/IP packets.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of obfuscation?', opts: ['Increase execution speed', 'Hide the true intent or signature of the payload', 'Reduce file size', 'Ensure compatibility'], correct: 1, fb: 'Obfuscation changes the appearance of a payload without changing its function to avoid signature detection.' }
  ],
  flashcards: [
    { f: 'Fragmentation', b: 'Splitting IP packets to evade signature detection.' },
    { f: 'Decoy Scan', b: 'Masking the real attacker IP among spoofed IP addresses.' }
  ],
  summary: ['Fragmentation splits packets to evade signatures.', 'Decoys mask the attacker IP.', 'Timing attacks bypass threshold alerts.', 'Insertion and evasion attacks exploit protocol reassembly differences.', 'Obfuscation hides the payload intent.'],
  outcomes: ['Implement packet fragmentation.', 'Execute decoy scans.', 'Understand advanced evasion concepts like insertion.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['honeypot-concepts'] = {
  eyebrow: 'Module 12 · Topic 3',
  title: 'Honeypot Concepts',
  module: 'Phase 12: Advanced Penetration Tester',
  sub: 'Understanding deception technology in network defense.',
  objectives: ['Define honeypots and honeynets', 'Differentiate interaction levels', 'Understand how honeypots gather intelligence'],
  learn: {
    simple: 'A honeypot is a security mechanism set up to detect, deflect, or study attempts at unauthorized use of information systems. It consists of a computer, data, or a network site that appears to be part of a network but is actually isolated and closely monitored.\\n\\nHoneypots have no legitimate production value; therefore, any interaction with a honeypot is inherently suspicious and likely malicious.',
    analogy: 'A honeypot is like a decoy safe placed in a bank lobby with fake money inside. It distracts bank robbers and alerts the police while keeping the real vault safe.',
    architecture: 'Honeypots are classified by their level of interaction. Low-interaction honeypots simulate basic services and operating systems, typically just opening ports to listen for connections (e.g., Honeyd). High-interaction honeypots are fully functional operating systems that attackers can fully compromise (e.g., a real Windows Server VM instrumented for monitoring). Multiple honeypots connected together form a honeynet. Data gathered includes malware samples, keystrokes, and attack techniques.',
    why: 'For defenders, honeypots provide high-fidelity alerts and intelligence on emerging threats. For attackers, identifying and avoiding honeypots is crucial to remain undetected and not waste time on fake targets.'
  },
  enterprise: {
    gfs: 'GFS uses internal low-interaction honeypots (honeytokens) disguised as database servers to immediately detect lateral movement by an internal threat actor.',
    windows: 'Windows honeypots might use fake Active Directory credentials (honeycreds) left in memory to track attackers who attempt Pass-the-Hash.',
    linux: 'Cowrie is a popular medium-interaction SSH/Telnet honeypot deployed on Linux to log brute-force attacks and capture uploaded malware payloads.'
  },
  workflow: ['Step 1: Identify potential targets.', 'Step 2: Analyze port responses for unnatural behavior (e.g., all ports open).', 'Step 3: Look for default honeypot configurations or banners.', 'Step 4: Check for MAC address artifacts associated with common virtualization.', 'Step 5: Avoid interacting deeply if a honeypot is suspected.', 'Step 6: Document the presence of deception technology.'],
  diagram: {
    caption: 'Click to interact with the Honeypot Architecture diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="500" height="300" fill="#d0e0f0"/><text x="300" y="200" text-anchor="middle">Honeynet Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -sV -O 192.168.1.100', purpose: 'OS Fingerprinting', out: 'OS guess', note: 'Conflicting OS and service banners may indicate a honeypot', mistake: 'Trusting banners blindly' }
    ],
    win: [
      { cmd: 'Get-WmiObject Win32_ComputerSystem', purpose: 'Check VM Status', out: 'Manufacturer info', note: 'Detects if running in a VM, common for honeypots', mistake: 'Assuming all VMs are honeypots' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Nmap', 'Cowrie'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS has deployed a new SSH server. You need to determine if it is a legitimate production server or a Cowrie honeypot.',
    objectives: ['Interact with a honeypot.', 'Identify artifacts that reveal its true nature.'],
    steps: ['Step 1: Connect to the target using SSH (`ssh root@192.168.1.100`).', 'Step 2: Attempt standard commands like `ls`, `uname -a`.', 'Step 3: Look for unimplemented commands or generic responses typical of Cowrie.', 'Step 4: Review Nmap version scan results for SSH banner anomalies.'],
    evidence: ['Terminal output showing restricted command execution environments.'],
    validation: ['You should see: Commands like `wget` or `curl` might work but download to an isolated environment, and obscure commands return generic errors.'],
    troubleshooting: ['If SSH connection drops, the honeypot might have a timeout configured.'],
    mitre: [{ id: 'T1082', name: 'System Information Discovery', tactic: 'Discovery' }],
    cleanup: ['Exit the SSH session.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a low-interaction honeypot?', opts: ['A fully functional vulnerable server', 'A system that simulates basic services and ports', 'A firewall rule', 'A physical security device'], correct: 1, fb: 'Low-interaction honeypots simulate services to gather basic threat intelligence.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a key characteristic of a honeypot?', opts: ['It processes legitimate user traffic', 'It has no production value', 'It is always physically isolated', 'It must run on Windows'], correct: 1, fb: 'Because a honeypot has no legitimate purpose, any interaction is considered suspicious.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a honeynet?', opts: ['A network of bots', 'A network composed of multiple honeypots', 'A social engineering technique', 'A wireless hacking tool'], correct: 1, fb: 'A honeynet is a network designed to look like a real production network but consists entirely of honeypots.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why might an attacker look for VMware or VirtualBox MAC addresses?', opts: ['To exploit the hypervisor', 'To detect if they are in a honeypot or sandbox', 'To bypass firewalls', 'To increase network speed'], correct: 1, fb: 'Many honeypots run as VMs; detecting virtualization artifacts can tip off an attacker.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a honeytoken?', opts: ['A physical security key', 'A fake digital entity (like a database record or credential) used for tracking', 'A cryptocurrency', 'A type of malware'], correct: 1, fb: 'Honeytokens are fake data designed to trigger an alert if accessed or used.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is a famous SSH/Telnet honeypot?', opts: ['Snort', 'Cowrie', 'Nmap', 'Burp Suite'], correct: 1, fb: 'Cowrie is a widely deployed medium-interaction SSH and Telnet honeypot.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: High-interaction honeypots are safer to deploy than low-interaction ones.', opts: ['True', 'False', 'Depends on the OS', 'None of the above'], correct: 1, fb: 'False. High-interaction honeypots are real, vulnerable systems and carry a higher risk of being fully compromised and used against other targets.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is tarpitting?', opts: ['Infecting a system with malware', 'Purposely slowing down responses to frustrate attackers and scanners', 'Deleting logs', 'Bypassing an IDS'], correct: 1, fb: 'Tarpits delay incoming connections to slow down scanning and exploit attempts.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can conflicting service banners indicate a honeypot?', opts: ['It means the server is outdated', 'Low-interaction honeypots might return a Linux OS banner but Windows service responses', 'It indicates a load balancer', 'It shows the firewall is blocking traffic'], correct: 1, fb: 'Simulated services might not accurately reflect the complexities of real OS stacks, leading to fingerprinting conflicts.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary risk of a high-interaction honeypot?', opts: ['False positives', 'Attacker using it to pivot into the real network', 'High cost', 'Slow performance'], correct: 1, fb: 'If an attacker completely compromises a high-interaction honeypot, they might use it as a pivot point if it is not properly isolated.' }
  ],
  flashcards: [
    { f: 'Honeypot', b: 'A decoy system designed to detect and study attacks.' },
    { f: 'Honeytoken', b: 'Fake data or credentials used to detect unauthorized access.' }
  ],
  summary: ['Honeypots are decoy systems with no production value.', 'Low-interaction simulates services; high-interaction provides real OS.', 'Honeynets are networks of honeypots.', 'Attackers look for virtualization artifacts to detect honeypots.', 'Tarpitting slows down automated attacks.'],
  outcomes: ['Understand the purpose of deception technology.', 'Identify signs of a honeypot.', 'Differentiate interaction levels.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['evasion-tools'] = {
  eyebrow: 'Module 12 · Topic 4',
  title: 'Evasion Tools',
  module: 'Phase 12: Advanced Penetration Tester',
  sub: 'Practical tools used for evading network defenses.',
  objectives: ['Utilize Nmap for evasion', 'Understand Hping3 capabilities', 'Explore tunneling and proxy tools'],
  learn: {
    simple: 'While understanding the theory of evasion is important, practical application requires specialized tools. Many standard penetration testing tools have built-in evasion capabilities, while other standalone tools are designed specifically to bypass security controls.\\n\\nTools range from packet crafters like Hping3, which can manipulate TCP/IP headers, to tunneling tools like Stunnel or SSH, which encapsulate malicious traffic within encrypted channels.',
    analogy: 'Using evasion tools is like choosing the right vehicle for a heist: sometimes you need a fast, stealthy sports car, and other times you need a delivery van to blend in with normal traffic.',
    architecture: 'Evasion tools operate at various layers. Layer 3/4 tools (Nmap, Hping3, Scapy) manipulate IP fragmentation, TTL, and TCP flags. Layer 7 tools (Proxychains, Stunnel, Metasploit encoders) focus on hiding the payload or routing it through intermediate systems to mask the origin. Network tunneling involves wrapping the payload in a trusted protocol (e.g., DNS or HTTPS tunneling) so the firewall allows it through based on port/protocol rules.',
    why: 'Mastering these tools allows penetration testers to simulate advanced persistent threats (APTs) that utilize sophisticated techniques to maintain stealth and persistence within an enterprise network.'
  },
  enterprise: {
    gfs: 'GFS penetration testers use customized Metasploit payloads and DNS tunneling tools to test if the Data Loss Prevention (DLP) and NGFW can detect exfiltration.',
    windows: 'Tools like Invoke-CradleCrafter or specialized C2 frameworks are used to evade Windows Defender and endpoint detection and response (EDR) agents.',
    linux: 'Linux environments might see the use of Proxychains to route attacker traffic through multiple compromised intermediate hosts (SOCKS proxies).'
  },
  workflow: ['Step 1: Select the appropriate tool based on the target defense mechanism.', 'Step 2: Configure the tool for stealth (e.g., enable encryption or fragmentation).', 'Step 3: Test the tool against a local replica of the defense if possible.', 'Step 4: Execute the tool against the target.', 'Step 5: Monitor for blocking or connection drops.', 'Step 6: Adjust parameters (e.g., change proxy, alter timing) and retry.'],
  diagram: {
    caption: 'Click to interact with the Evasion Tools diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="50" y="50" width="500" height="300" fill="#f0d0d0"/><text x="300" y="200" text-anchor="middle">Network Tunneling Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'proxychains nmap -sT -Pn 192.168.1.5', purpose: 'Proxy Routing', out: 'Scan results routed through proxy', note: 'Hides source IP', mistake: 'Using UDP scans (Proxychains typically supports TCP only)' }
    ],
    win: [
      { cmd: 'plink.exe -D 8080 user@remote-host', purpose: 'Dynamic SSH Tunnel', out: 'SOCKS proxy port opened', note: 'Creates an encrypted tunnel to evade inspection', mistake: 'Leaving the port open after the assessment' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Proxychains', 'Nmap', 'Stunnel'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS has a strict firewall blocking all outgoing traffic except HTTPS. You must use Stunnel to encapsulate your C2 traffic.',
    objectives: ['Configure Proxychains.', 'Tunnel traffic using Stunnel.'],
    steps: ['Step 1: Edit `/etc/proxychains4.conf` to add a SOCKS proxy.', 'Step 2: Run an Nmap scan through proxychains: `proxychains nmap -sT 10.10.10.1`.', 'Step 3: Observe that the target sees the proxy IP, not your Kali IP.'],
    evidence: ['Terminal output showing Proxychains routing connections.'],
    validation: ['You should see: Proxychains intercepting the Nmap TCP connections and routing them through the specified chain.'],
    troubleshooting: ['If the connection fails, ensure the proxy server in the config is active and reachable.'],
    mitre: [{ id: 'T1090', name: 'Proxy', tactic: 'Command and Control' }],
    cleanup: ['Remove the proxy entry from the configuration file.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary function of Proxychains?', opts: ['Encrypt hard drives', 'Route TCP connections through a series of proxies', 'Fragment IP packets', 'Generate custom TCP flags'], correct: 1, fb: 'Proxychains forces TCP connections made by a given application to go through proxies like SOCKS4, SOCKS5, or HTTP.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is best known for creating custom TCP/IP packets?', opts: ['Wireshark', 'Hping3', 'Nessus', 'John the Ripper'], correct: 1, fb: 'Hping3 is a network tool able to send custom ICMP/UDP/TCP packets and to display target replies.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is network tunneling?', opts: ['Digging physical cables', 'Encapsulating one protocol within another', 'Bypassing passwords', 'Deleting logs'], correct: 1, fb: 'Tunneling encapsulates a protocol (like SSH) inside another (like HTTPS) to bypass filtering.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why might an attacker use DNS tunneling?', opts: ['DNS is usually allowed through firewalls', 'DNS is faster than HTTP', 'DNS is naturally encrypted', 'DNS does not use IP addresses'], correct: 0, fb: 'DNS traffic is required for normal network operation and is rarely blocked completely, making it a prime candidate for tunneling data.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does the tool Stunnel do?', opts: ['Creates VPNs', 'Adds SSL/TLS encryption to any TCP connection', 'Cracks passwords', 'Scans for vulnerabilities'], correct: 1, fb: 'Stunnel is designed to add TLS encryption to programs that do not have native TLS support.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: Proxychains can seamlessly route ICMP traffic (like standard ping).', opts: ['True', 'False', 'Depends on the OS', 'None of the above'], correct: 1, fb: 'False. Proxychains primarily supports TCP. ICMP does not have the concept of ports used in SOCKS/HTTP proxies.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following can be used to evade Deep Packet Inspection (DPI)?', opts: ['Changing the source IP', 'Changing the MAC address', 'Encryption (TLS/SSL)', 'Fragmentation'], correct: 2, fb: 'Encryption hides the payload content, making it impossible for DPI to inspect the application data.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is Scapy?', opts: ['A web application scanner', 'A Python-based interactive packet manipulation program', 'A firewall hardware device', 'A proxy server'], correct: 1, fb: 'Scapy is a powerful Python library used for packet crafting, sniffing, and manipulation.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which Nmap scan type is generally considered the most "stealthy" (though modern IDS still catch it)?', opts: ['TCP Connect Scan (-sT)', 'SYN Scan (-sS)', 'UDP Scan (-sU)', 'Ping Scan (-sn)'], correct: 1, fb: 'The SYN scan (half-open scan) does not complete the TCP handshake, which historically bypassed older logging mechanisms.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is domain fronting?', opts: ['Registering a similar domain name', 'Using different domain names in the SNI and HTTP Host header to bypass filters', 'Hosting a website on multiple servers', 'Attacking a DNS server'], correct: 1, fb: 'Domain fronting routes traffic through a CDN by masking the true destination in the HTTP Host header while using a permitted domain in the TLS SNI.' }
  ],
  flashcards: [
    { f: 'Proxychains', b: 'Tool that forces TCP connections through a chain of proxy servers.' },
    { f: 'Tunneling', b: 'Encapsulating one network protocol within another to bypass filters.' }
  ],
  summary: ['Proxychains hides the source IP.', 'Hping3 crafts custom packets for evasion testing.', 'Tunneling encapsulates traffic (e.g., DNS, HTTPS) to bypass rules.', 'Encryption prevents deep packet inspection.', 'Domain fronting leverages CDNs for stealth.'],
  outcomes: ['Configure tools for network evasion.', 'Understand the principles of network tunneling.', 'Use proxies to mask attack origins.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert the payload before // ── TAB WIRING ──
marker = "// ── TAB WIRING ──"
if marker in html_content:
    new_html_content = html_content.replace(marker, payload + "\\n" + marker)
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html_content)
    print("Successfully injected payload into index.html")
else:
    print("Marker not found in index.html")
