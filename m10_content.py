import os

CONTENT_JS = """
CONTENT['dos-concepts'] = {
  eyebrow: 'Module 10 · Topic 1',
  title: 'DoS and DDoS Concepts',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Understanding the fundamentals of Denial of Service and Distributed Denial of Service attacks.',
  objectives: ['Understand Volumetric attacks', 'Identify Protocol attacks', 'Recognize Application-layer attacks'],
  learn: {
    simple: 'A Denial of Service (DoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic. A Distributed Denial of Service (DDoS) attack involves multiple compromised computer systems as sources of attack traffic. These sources can include computers and other networked resources such as IoT devices.',
    analogy: 'Imagine a store with a single entrance. If a large crowd of people gathers at the entrance and refuses to move, legitimate customers cannot enter the store. A DoS attack works similarly by clogging the entry points to a digital service.',
    architecture: 'At a technical level, DoS/DDoS attacks are categorized into three main types: Volumetric (e.g., UDP floods, ICMP floods) which consume bandwidth; Protocol (e.g., SYN floods, Ping of Death) which consume server resources like firewalls or load balancers; and Application-layer (e.g., HTTP GET/POST floods) which crash web servers by making seemingly legitimate but resource-intensive requests.',
    why: 'In enterprise cybersecurity, DDoS attacks can lead to significant downtime, loss of revenue, and reputational damage. Understanding these concepts is critical for designing resilient architectures capable of absorbing or mitigating such attacks.'
  },
  enterprise: {
    gfs: 'Global Financial Services (GFS) experienced a multi-vector DDoS attack during a major trading period, highlighting the need for robust volumetric and application-layer defense mechanisms.',
    windows: 'Windows servers can be targeted with protocol attacks; monitoring performance counters and event logs helps in early detection of resource exhaustion.',
    linux: 'Linux environments often serve as edge firewalls or reverse proxies and can be configured with iptables rate limiting to thwart basic DoS attempts.'
  },
  workflow: ['Step 1: Monitor network baseline traffic.', 'Step 2: Identify traffic anomalies or sudden spikes.', 'Step 3: Analyze traffic sources to distinguish legitimate users from attackers.', 'Step 4: Determine the attack vector (volumetric, protocol, or application).', 'Step 5: Activate mitigation protocols.', 'Step 6: Conduct post-incident analysis.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="400" height="200" fill="#e2e8f0"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="24">DoS/DDoS Attack Vectors</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'tcpdump -i eth0 -n "tcp[tcpflags] & (tcp-syn) != 0"', purpose: 'Capture SYN packets', out: 'List of SYN packets', note: 'Useful for detecting SYN floods', mistake: 'Running without filters capturing too much data' }
    ],
    win: [
      { cmd: 'Get-NetTCPConnection -State SynReceived', purpose: 'Check half-open connections', out: 'List of connections', note: 'High count indicates SYN flood', mistake: 'Running on non-server systems unnecessarily' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['hping3', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS network operations wants to simulate a SYN flood attack to test detection mechanisms.',
    objectives: ['Simulate a SYN flood', 'Detect the flood using network monitoring tools'],
    steps: ['Step 1: Open terminal in Kali Linux.', 'Step 2: Run hping3 to start the flood.', 'Step 3: Open Wireshark on the target machine.', 'Step 4: Filter for SYN packets without ACKs.'],
    evidence: ['Terminal output from hping3', 'Wireshark packet capture showing SYN flood'],
    validation: ['You should see a massive amount of SYN packets arriving at the target in Wireshark.'],
    troubleshooting: ['If hping3 fails, ensure you are running it as root (sudo hping3).'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop hping3 by pressing Ctrl+C.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the primary goal of a DoS attack?', opts: ['To steal data', 'To disrupt service', 'To install malware', 'To gain unauthorized access'], correct: 1, fb: 'The goal is to disrupt service by overwhelming resources.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'A DDoS attack uses multiple systems to attack a single target.', opts: ['True', 'False'], correct: 0, fb: 'DDoS stands for Distributed DoS, utilizing multiple compromised hosts.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which attack type focuses on consuming network bandwidth?', opts: ['Application-layer', 'Protocol', 'Volumetric', 'Physical'], correct: 2, fb: 'Volumetric attacks aim to saturate the bandwidth of the targeted site.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is a Protocol attack?', opts: ['HTTP GET Flood', 'SYN Flood', 'DNS Amplification', 'Slowloris'], correct: 1, fb: 'SYN Flood attacks the TCP protocol handshake mechanism.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Application-layer attacks are easier to detect than volumetric attacks.', opts: ['True', 'False'], correct: 1, fb: 'False. Application-layer attacks mimic legitimate traffic and require fewer resources, making them harder to detect.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'How does an amplification attack work?', opts: ['By spoofing the target IP', 'By exploiting vulnerabilities in web apps', 'By sending large requests that trigger even larger responses', 'By cracking passwords'], correct: 2, fb: 'Amplification relies on protocols that send large responses to small queries.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which OSI layer does a volumetric attack primarily target?', opts: ['Layer 7', 'Layer 3 and 4', 'Layer 2', 'Layer 1'], correct: 1, fb: 'Volumetric attacks often operate at the network and transport layers.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'DoS attacks can be launched accidentally by legitimate users.', opts: ['True', 'False'], correct: 0, fb: 'True. A sudden massive surge in legitimate traffic (the "Slashdot effect") can cause an unintentional DoS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What resource does a Ping of Death attack target?', opts: ['Memory buffers', 'Bandwidth', 'CPU cycles', 'Disk space'], correct: 0, fb: 'Ping of Death sends oversized ICMP packets that can overflow memory buffers.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which attack vector targets the state tables of firewalls?', opts: ['ICMP Flood', 'SYN Flood', 'UDP Flood', 'HTTP POST Flood'], correct: 1, fb: 'SYN Floods consume state table entries in stateful firewalls.' }
  ],
  flashcards: [
    { f: 'DoS', b: 'Denial of Service; an attack meant to shut down a machine or network.' },
    { f: 'DDoS', b: 'Distributed Denial of Service; a DoS attack originating from multiple sources.' }
  ],
  summary: ['DoS disrupts services by overwhelming resources.', 'DDoS uses multiple compromised systems.', 'Volumetric attacks consume bandwidth.', 'Protocol attacks consume server resources.', 'Application-layer attacks target web applications.'],
  outcomes: ['Differentiate between DoS and DDoS.', 'Identify the three main categories of DoS attacks.', 'Understand the business impact of service disruption.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: ["Network Basics"], lastReviewed: "2026-07-18" }
};

CONTENT['botnets'] = {
  eyebrow: 'Module 10 · Topic 2',
  title: 'Botnets & IoT Exploitation',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Understanding Command and Control (C2) architecture and the role of botnets in modern DDoS attacks.',
  objectives: ['Analyze C2 architecture', 'Examine the Mirai botnet', 'Understand IoT exploitation techniques'],
  learn: {
    simple: 'A botnet is a network of compromised computers or devices (bots) controlled by a central attacker, known as a botmaster. These networks are often used to launch massive DDoS attacks. With the proliferation of Internet of Things (IoT) devices, attackers have found a vast pool of vulnerable devices to recruit into botnets.',
    analogy: 'Think of a botnet like a zombie army. The attacker is the necromancer controlling the zombies. Individually, a zombie might not be very strong, but a massive horde coordinated by the necromancer can overrun any defense.',
    architecture: 'Botnets rely on a Command and Control (C2) infrastructure. Earlier botnets used centralized IRC servers, but modern botnets often use decentralized Peer-to-Peer (P2P) architectures or Domain Generation Algorithms (DGA) to evade takedowns. The Mirai botnet, infamous for massive DDoS attacks, specifically targeted vulnerable IoT devices using default credentials, turning IP cameras and home routers into attack nodes.',
    why: 'IoT botnets represent a significant threat to enterprises because the attack volume they can generate is unprecedented. Organizations must understand botnet mechanisms to filter traffic and cooperate with ISPs for upstream mitigation.'
  },
  enterprise: {
    gfs: 'GFS threat intelligence identified a large portion of inbound attack traffic originating from consumer IoT devices, prompting a shift in edge defense strategies.',
    windows: 'Windows machines can be infected by malware to become part of a botnet; Endpoint Detection and Response (EDR) solutions monitor for C2 beacons.',
    linux: 'Linux-based IoT devices are prime targets for botnets like Mirai; securing SSH/Telnet and updating firmware is crucial.'
  },
  workflow: ['Step 1: Monitor outbound traffic for C2 communication patterns.', 'Step 2: Identify compromised endpoints within the network.', 'Step 3: Isolate infected devices.', 'Step 4: Analyze malware payload to understand the botnet family.', 'Step 5: Clean the infected devices.', 'Step 6: Update network perimeter defenses.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><circle cx="300" cy="200" r="100" fill="#fca5a5"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="20">Botnet C2 Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'netstat -tulnp | grep -i listen', purpose: 'Check listening ports', out: 'List of listening services', note: 'Helps identify backdoors left by botnet malware', mistake: 'Ignoring non-standard ports' }
    ],
    win: [
      { cmd: 'Get-Process | Where-Object {$_.Path -match "Temp"}', purpose: 'Find suspicious processes running from Temp', out: 'List of processes', note: 'Malware often executes from temporary directories', mistake: 'Terminating critical system processes by mistake' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Wireshark', 'Snort'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS SOC analysts need to identify C2 beaconing activity from a suspected compromised host.',
    objectives: ['Analyze network traffic for C2 beacons', 'Write an IDS rule to detect the activity'],
    steps: ['Step 1: Open the provided PCAP file in Wireshark.', 'Step 2: Look for regular, small DNS requests to unusual domains.', 'Step 3: Note the domain and frequency.', 'Step 4: Write a Snort rule to alert on this specific DNS query.'],
    evidence: ['Wireshark screenshots of beaconing', 'Custom Snort rule text'],
    validation: ['You should find a DNS query occurring exactly every 60 seconds to a randomly generated domain name.'],
    troubleshooting: ['If you cannot spot the beacon, filter by "dns" and sort by time.'],
    mitre: [{ id: 'T1071', name: 'Application Layer Protocol', tactic: 'Command and Control' }],
    cleanup: ['Close Wireshark and delete the PCAP.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is a botnet?', opts: ['A network of compromised devices', 'A type of firewall', 'A legitimate internet scanning tool', 'An antivirus software'], correct: 0, fb: 'A botnet is a network of compromised devices controlled by an attacker.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'IoT devices are frequently targeted by botnets because they often have weak or default passwords.', opts: ['True', 'False'], correct: 0, fb: 'True. Default credentials are a primary infection vector for IoT botnets like Mirai.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does C2 stand for in the context of botnets?', opts: ['Command and Control', 'Central Communication', 'Computer Coordination', 'Cyber Connection'], correct: 0, fb: 'C2 refers to Command and Control infrastructure.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which botnet is famous for turning IoT devices into DDoS attack nodes?', opts: ['Zeus', 'Conficker', 'Mirai', 'Stuxnet'], correct: 2, fb: 'Mirai exploited default telnet credentials on IoT devices.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Botnets can only be used for DDoS attacks.', opts: ['True', 'False'], correct: 1, fb: 'False. Botnets are also used for spamming, credential stuffing, and cryptomining.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is a Domain Generation Algorithm (DGA) used for in botnets?', opts: ['To speed up network scanning', 'To generate passwords for brute forcing', 'To create multiple dynamic domains for C2 communication', 'To encrypt malware payloads'], correct: 2, fb: 'DGAs help botnets evade takedowns by constantly changing the C2 domain.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a common protocol used by early botnets for C2 communication?', opts: ['HTTP', 'IRC', 'DNS', 'SSH'], correct: 1, fb: 'Internet Relay Chat (IRC) was widely used for early centralized botnet C2.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'Peer-to-Peer (P2P) botnets are easier to take down than centralized IRC botnets.', opts: ['True', 'False'], correct: 1, fb: 'False. P2P botnets lack a single point of failure, making them much harder to dismantle.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does malware typically recruit an IoT device into a botnet?', opts: ['By sending a phishing email', 'By exploiting unpatched vulnerabilities or weak credentials over the network', 'By physical access', 'Through social engineering of the device owner'], correct: 1, fb: 'IoT malware scans the internet for exposed services with vulnerabilities or default credentials.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which of the following is NOT a common use of a botnet?', opts: ['DDoS attacks', 'Spam distribution', 'Hardware upgrading', 'Cryptomining'], correct: 2, fb: 'Botnets perform malicious actions; hardware upgrading is not one of them.' }
  ],
  flashcards: [
    { f: 'C2', b: 'Command and Control infrastructure used by botmasters.' },
    { f: 'Mirai', b: 'A notorious malware that turns networked devices running Linux into remotely controlled bots.' }
  ],
  summary: ['Botnets are networks of compromised devices.', 'IoT devices are prime targets due to poor security.', 'C2 infrastructure is essential for botnet coordination.', 'Mirai popularized large-scale IoT botnets.', 'DGAs and P2P architectures make botnets resilient.'],
  outcomes: ['Explain how a botnet operates.', 'Identify the risks associated with IoT devices.', 'Describe C2 mechanisms.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 50, difficulty: "Intermediate", prerequisites: ["DoS Concepts"], lastReviewed: "2026-07-18" }
};

CONTENT['dos-attack-techniques'] = {
  eyebrow: 'Module 10 · Topic 3',
  title: 'DoS/DDoS Attack Techniques',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Deep dive into specific attack vectors including SYN floods, UDP floods, Slowloris, and HTTP POST attacks.',
  objectives: ['Understand SYN and UDP floods', 'Analyze the Slowloris attack', 'Identify HTTP POST attacks'],
  learn: {
    simple: 'Attackers use various techniques to disrupt services. Some aim to overwhelm network pipes with massive amounts of data (UDP floods), while others target specific protocols to tie up server resources (SYN floods). More sophisticated attacks target the application layer (Slowloris, HTTP POST), achieving a DoS condition with surprisingly little bandwidth.',
    analogy: 'A UDP flood is like sending thousands of junk mail letters to a post office, overwhelming the sorters. Slowloris is like a customer at a checkout counter who takes five minutes to find each penny to pay their bill, holding up the entire line indefinitely.',
    architecture: 'A SYN flood exploits the TCP 3-way handshake by sending SYN requests but never sending the final ACK, leaving the server waiting with half-open connections. Slowloris is a Layer 7 attack that opens multiple connections to a web server and keeps them open as long as possible by sending partial HTTP requests. This exhausts the web server’s concurrent connection pool.',
    why: 'Defenders must understand these specific techniques because the mitigation strategies vary wildly. You cannot mitigate a Slowloris attack with the same volumetric defenses used against a UDP flood.'
  },
  enterprise: {
    gfs: 'GFS web applications were targeted by a Slowloris attack, which bypassed volumetric DDoS protections and exhausted the web server connection pools.',
    windows: 'IIS servers can be protected from Slowloris-style attacks by adjusting connection timeout limits and using reverse proxies.',
    linux: 'Apache web servers on Linux are notoriously vulnerable to Slowloris, whereas event-driven servers like Nginx handle such slow connections more efficiently.'
  },
  workflow: ['Step 1: Analyze server connection states (e.g., too many SYN_RECV or ESTABLISHED).', 'Step 2: Inspect packet payloads for malformed or unusually slow requests.', 'Step 3: Identify the specific technique being used.', 'Step 4: Apply protocol-specific mitigations (e.g., SYN cookies).', 'Step 5: Adjust server timeout settings.', 'Step 6: Monitor for technique shifting by the attacker.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="400" height="200" fill="#fde047"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="24">Attack Techniques</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'netstat -ntu | awk \\'{print $5}\\' | cut -d: -f1 | sort | uniq -c | sort -n', purpose: 'Count connections per IP', out: 'List of IPs and connection counts', note: 'Useful for spotting IP addresses opening too many connections', mistake: 'Not running as root' }
    ],
    win: [
      { cmd: 'Get-NetTCPConnection | Group-Object RemoteAddress | Sort-Object Count -Descending', purpose: 'Identify IPs with most connections', out: 'Grouped connection counts', note: 'Identifies potential sources of connection-exhaustion attacks', mistake: 'Ignoring IPv6 connections' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Slowloris', 'Apache'],
    dependencies: ['python3-slowloris'],
    safety: ['Perform this lab only in an isolated environment against your own VMs.'],
    scenario: 'GFS security team wants to demonstrate how a low-bandwidth attack can take down a legacy Apache server.',
    objectives: ['Execute a Slowloris attack', 'Observe the effect on the target web server', 'Implement a mitigation'],
    steps: ['Step 1: Start Apache on the target VM.', 'Step 2: Run Slowloris against the target VM IP.', 'Step 3: Attempt to browse to the target VM website from a third machine.', 'Step 4: Install and configure mod_reqtimeout on Apache to mitigate.'],
    evidence: ['Terminal output showing Slowloris sending partial headers', 'Browser timeout error'],
    validation: ['The Apache server should stop responding to legitimate requests while Slowloris is running.'],
    troubleshooting: ['If Apache doesn\\'t crash, try increasing the number of sockets Slowloris opens (-s parameter).'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop Slowloris and restart Apache.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'Which attack exploits the TCP 3-way handshake?', opts: ['UDP Flood', 'SYN Flood', 'Ping of Death', 'HTTP GET Flood'], correct: 1, fb: 'SYN floods leave connections half-open.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Slowloris requires a massive amount of bandwidth to be effective.', opts: ['True', 'False'], correct: 1, fb: 'False. Slowloris is a low-bandwidth attack that exhausts server connection limits.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary target of an HTTP POST attack?', opts: ['Network bandwidth', 'DNS servers', 'Server processing resources (e.g., database, parsing)', 'Router interfaces'], correct: 2, fb: 'POST attacks force the server to process data, consuming CPU and memory.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is connectionless and easily spoofed in flood attacks?', opts: ['TCP', 'HTTP', 'UDP', 'FTP'], correct: 2, fb: 'UDP does not require a handshake, making source IP spoofing trivial.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'SYN Cookies can help mitigate SYN flood attacks.', opts: ['True', 'False'], correct: 0, fb: 'True. SYN cookies allow the server to avoid allocating resources until the final ACK is received.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does Slowloris maintain open connections?', opts: ['By sending huge files', 'By sending partial HTTP headers very slowly', 'By exploiting a buffer overflow', 'By sending TCP keep-alives'], correct: 1, fb: 'It sends incomplete headers periodically to keep the socket open.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What type of server architecture is most vulnerable to Slowloris?', opts: ['Thread-based (like traditional Apache)', 'Event-driven (like Nginx)', 'Serverless', 'Microservices'], correct: 0, fb: 'Servers that spawn a thread per connection quickly run out of available threads.' },
    { type: 'true-false', difficulty: 'Beginner', q: 'A UDP flood is an example of a volumetric attack.', opts: ['True', 'False'], correct: 0, fb: 'True. UDP floods aim to consume all available bandwidth.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the "Smurf attack"?', opts: ['An HTTP application attack', 'An ICMP echo request amplification attack directed at a broadcast address', 'A type of SQL injection', 'A botnet propagation method'], correct: 1, fb: 'The Smurf attack uses ICMP echo requests with a spoofed source IP sent to a broadcast network.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'Which of the following is an effective mitigation specifically against HTTP POST floods?', opts: ['Increasing network bandwidth', 'Implementing SYN cookies', 'Web Application Firewall (WAF) rate limiting and inspection', 'Blocking UDP traffic'], correct: 2, fb: 'WAFs can inspect Layer 7 traffic and limit request rates based on behavior.' }
  ],
  flashcards: [
    { f: 'SYN Flood', b: 'An attack that exploits the TCP handshake by leaving connections half-open.' },
    { f: 'Slowloris', b: 'A Layer 7 attack that keeps connections open by sending partial HTTP requests.' }
  ],
  summary: ['SYN floods exhaust connection state tables.', 'UDP floods consume network bandwidth.', 'Slowloris targets web server concurrent connection limits.', 'HTTP POST attacks consume processing power.', 'Different attack vectors require distinct mitigation strategies.'],
  outcomes: ['Describe how a SYN flood works.', 'Explain the mechanics of a Slowloris attack.', 'Identify the differences between UDP and TCP-based attacks.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 60, difficulty: "Advanced", prerequisites: ["Botnets"], lastReviewed: "2026-07-18" }
};

CONTENT['ddos-mitigation'] = {
  eyebrow: 'Module 10 · Topic 4',
  title: 'DDoS Mitigation & Defense',
  module: 'Phase 10: Network Defense Analyst',
  sub: 'Strategies for defending against DDoS attacks, including Anycast, WAFs, rate limiting, and BGP blackholing.',
  objectives: ['Understand Anycast routing', 'Configure WAF rules', 'Implement BGP blackholing'],
  learn: {
    simple: 'Defending against massive DDoS attacks requires a multi-layered approach. Modern mitigation relies heavily on distributing traffic and filtering out malicious requests before they reach the target server. Techniques range from simple rate limiting to complex BGP routing alterations.',
    analogy: 'Mitigating a DDoS attack is like managing a flooded river. You can build higher levees (more bandwidth), divert the water into flood plains (Anycast), or use filters to pull debris out of the water (WAFs).',
    architecture: 'Anycast network architecture distributes incoming traffic across multiple geographically dispersed data centers, absorbing volumetric attacks naturally. Web Application Firewalls (WAFs) inspect Layer 7 traffic to block application-specific attacks like HTTP floods. BGP Remotely Triggered Black Hole (RTBH) routing is an ISP-level mitigation where traffic destined for the targeted IP is dropped entirely, protecting the rest of the network but effectively completing the DoS for that specific IP.',
    why: 'No single enterprise has enough bandwidth to absorb a massive terabit-scale DDoS attack alone. Mitigation requires leveraging cloud-based scrubbing centers and advanced routing techniques to ensure business continuity.'
  },
  enterprise: {
    gfs: 'GFS utilizes a cloud-based DDoS scrubbing service with an Anycast network to protect its primary customer portals from volumetric attacks.',
    windows: 'Windows Server environments utilize dynamic IP restrictions in IIS to automatically block IPs exhibiting abusive request rates.',
    linux: 'Linux firewalls use advanced iptables modules like "hashlimit" or utilize Fail2ban to dynamically rate-limit and ban malicious IP addresses.'
  },
  workflow: ['Step 1: Detect anomaly via monitoring systems.', 'Step 2: Trigger automated mitigation (e.g., local rate limiting).', 'Step 3: If volumetric attack exceeds capacity, initiate failover to a scrubbing center.', 'Step 4: Apply WAF rules for any Layer 7 attack components.', 'Step 5: As a last resort for extreme attacks, initiate BGP blackholing with the ISP.', 'Step 6: Monitor mitigation effectiveness and adjust rules.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect x="100" y="100" width="400" height="200" fill="#86efac"/><text x="300" y="200" dominant-baseline="middle" text-anchor="middle" font-size="24">DDoS Mitigation Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT', purpose: 'Rate limit HTTP traffic', out: 'No output (rule added)', note: 'Basic local mitigation for HTTP floods', mistake: 'Setting limits too low and blocking legitimate users' }
    ],
    win: [
      { cmd: 'New-WebConfigurationProperty -pspath "IIS:\\\\" -filter "system.webServer/security/dynamicIpSecurity/denyByRequestRate" -name "enabled" -value "True"', purpose: 'Enable IIS Dynamic IP Security', out: 'Configuration updated', note: 'Helps protect against Layer 7 DoS on Windows Server', mistake: 'Not testing in a staging environment first' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '45',
    platform: 'Linux / AWS',
    environment: 'Cloud Lab',
    tools: ['iptables', 'AWS WAF'],
    dependencies: [],
    safety: ['Do not apply aggressive blocking rules to production systems without testing.'],
    scenario: 'GFS requires a demonstration of Layer 7 mitigation using rate limiting and WAF rules.',
    objectives: ['Configure iptables for basic rate limiting', 'Simulate traffic to trigger the limit', 'Review dropped packet logs'],
    steps: ['Step 1: Access the Linux target server.', 'Step 2: Apply an iptables rule to limit incoming ICMP (ping) traffic.', 'Step 3: Ping the server rapidly from an attacker VM.', 'Step 4: Verify that excess pings are dropped.'],
    evidence: ['iptables rules list', 'Attacker terminal showing dropped pings'],
    validation: ['Pings exceeding the defined rate limit should result in packet loss.'],
    troubleshooting: ['If all pings succeed, ensure the default policy or subsequent rules are not overriding your limit rule.'],
    mitre: [{ id: 'M1041', name: 'Filter Network Traffic', tactic: 'Mitigation' }],
    cleanup: ['Flush the iptables rules (iptables -F).']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is the purpose of a Web Application Firewall (WAF) in DDoS mitigation?', opts: ['To increase network bandwidth', 'To inspect and filter Layer 7 malicious traffic', 'To route traffic via BGP', 'To provide antivirus scanning'], correct: 1, fb: 'WAFs analyze HTTP/HTTPS traffic to block application-layer attacks.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Anycast routing allows multiple servers in different geographic locations to share the same IP address.', opts: ['True', 'False'], correct: 0, fb: 'True. Anycast routes requests to the nearest geographic server, dispersing attack traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does BGP Blackholing do?', opts: ['Encrypts all traffic', 'Routes all traffic destined for a targeted IP into a "null0" interface (drops it)', 'Redirects traffic to a honeypot', 'Cleans the traffic and sends it back'], correct: 1, fb: 'Blackholing drops all traffic (good and bad) intended for the target to save the broader network.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'What is a "Scrubbing Center"?', opts: ['A facility that physically cleans server hardware', 'A centralized data center where traffic is analyzed and malicious packets are removed', 'An on-premise firewall', 'A software tool for deleting malware'], correct: 1, fb: 'Scrubbing centers ingest raw traffic, filter out the attack, and forward clean traffic to the enterprise.' },
    { type: 'true-false', difficulty: 'Intermediate', q: 'Rate limiting is an effective defense against massive volumetric attacks (e.g., 500 Gbps).', opts: ['True', 'False'], correct: 1, fb: 'False. Local rate limiting cannot save a network connection if the incoming pipe is physically saturated.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which mitigation technique is best suited for a Slowloris attack?', opts: ['BGP Blackholing', 'Anycast', 'Reverse proxy with aggressive connection timeout settings', 'Adding more hard drives'], correct: 2, fb: 'Configuring servers or reverse proxies to drop slow connections mitigates Slowloris.' },
    { type: 'multiple-choice', difficulty: 'Beginner', q: 'What is an SLA in the context of DDoS protection services?', opts: ['Service Level Agreement', 'System Log Analysis', 'Secure Layer Access', 'Standard Logic Architecture'], correct: 0, fb: 'SLAs define the guaranteed response and mitigation times provided by a vendor.' },
    { type: 'true-false', difficulty: 'Advanced', q: 'BGP Flowspec allows for more granular filtering than traditional BGP Blackholing.', opts: ['True', 'False'], correct: 0, fb: 'True. Flowspec can distribute fine-grained filtering rules (like blocking specific ports) rather than just dropping all traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Content Delivery Network (CDN) primarily used for, which also helps in DDoS mitigation?', opts: ['Creating botnets', 'Caching content closer to users, thus distributing load', 'Encrypting databases', 'Managing local network switches'], correct: 1, fb: 'CDNs naturally absorb DDoS attacks by serving cached content from distributed edge nodes.' },
    { type: 'multiple-choice', difficulty: 'Advanced', q: 'When configuring iptables for rate limiting, what does the "limit-burst" parameter define?', opts: ['The maximum size of a packet', 'The number of packets allowed before the rate limit kicks in', 'The total duration of the rule', 'The specific port to block'], correct: 1, fb: 'Limit-burst allows an initial burst of packets before enforcing the strict rate limit.' }
  ],
  flashcards: [
    { f: 'Anycast', b: 'A network routing method where multiple machines share the same IP address to distribute traffic load.' },
    { f: 'BGP Blackholing', b: 'A technique to drop all traffic directed at a specific IP address to save the wider network from an attack.' }
  ],
  summary: ['DDoS mitigation requires defense in depth.', 'Anycast disperses traffic globally.', 'WAFs protect against Layer 7 attacks.', 'Scrubbing centers filter malicious volumetric traffic.', 'BGP blackholing is a last resort to protect ISP infrastructure.'],
  outcomes: ['Identify different DDoS mitigation techniques.', 'Understand the role of a WAF.', 'Explain how Anycast helps absorb attacks.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: ["Attack Techniques"], lastReviewed: "2026-07-18" }
};
"""

def inject_content():
    html_path = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        marker = '// ── TAB WIRING ──'
        if marker not in html_content:
            print("Marker not found in index.html")
            return

        # Inject the content right before the marker
        new_html = html_content.replace(marker, CONTENT_JS + '\n' + marker)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print("Successfully injected Module 10 content into index.html")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inject_content()
