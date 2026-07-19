import os
import json

HTML_PATH = os.path.join("frontend", "index.html")

CONTENT = """
CONTENT['sniffing-concepts'] = {
  eyebrow: 'Module 08 · Topic 1',
  title: 'Sniffing Concepts',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Understanding the fundamentals of network sniffing, active vs passive methods, and collision domains.',
  objectives: ['Differentiate between active and passive sniffing', 'Understand promiscuous mode and collision domains', 'Identify common sniffing tools and their use cases'],
  learn: {
    simple: 'Network sniffing is the process of monitoring and capturing all data packets passing through a given network. It is analogous to tapping a phone line, allowing an attacker to intercept communications. Sniffing can be passive (listening without transmitting) or active (injecting traffic to manipulate the network switch).',
    analogy: 'Imagine a postal worker reading everyone\\'s mail before delivering it. Passive sniffing is like reading postcards that are openly visible, while active sniffing is like convincing the post office to route all mail through your personal mailbox.',
    architecture: 'In a non-switched network (hub), all traffic is broadcasted, making passive sniffing easy. In a switched network, each port is its own collision domain. Active sniffing techniques, like MAC flooding or ARP spoofing, are required to force the switch to send traffic to the attacker\\'s port. Promiscuous mode allows a network interface card (NIC) to process all traffic it receives, regardless of the destination MAC address.',
    why: 'In enterprise environments, unencrypted traffic (like HTTP, FTP, Telnet) can be intercepted, leading to the compromise of sensitive data, credentials, and session tokens. Understanding sniffing is critical for implementing secure, encrypted protocols.'
  },
  enterprise: {
    gfs: 'At Global Financial Services, an unauthorized device connected to a branch office network could silently capture unencrypted SNMP traffic, exposing network device configurations.',
    windows: 'Windows environments can be vulnerable to LLMNR/NBT-NS spoofing (using tools like Responder), which relies on sniffing broadcast requests and spoofing responses to capture NTLM hashes.',
    linux: 'Linux systems are often used as sniffing platforms using tcpdump or Wireshark. Linux administrators must ensure management traffic (like SSH) is used instead of Telnet to prevent credential sniffing.'
  },
  workflow: ['Step 1: Identify the target network and topology.', 'Step 2: Connect to the network or compromise a host.', 'Step 3: Enable promiscuous mode on the network interface.', 'Step 4: Use a sniffing tool (e.g., Wireshark) to capture packets.', 'Step 5: Filter the captured data for sensitive information.', 'Step 6: Analyze the captured credentials or data.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">Sniffing Architecture Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'tcpdump -i eth0 -w capture.pcap', purpose: 'Capture network traffic to a file', out: 'Packets saved to capture.pcap', note: 'Requires root privileges', mistake: 'Not specifying an interface can lead to capturing wrong traffic' }
    ],
    win: [
      { cmd: 'pktmon start --etw -p 0', purpose: 'Start packet monitor in Windows', out: 'Packet capture started', note: 'Built-in Windows tool', mistake: 'Forgetting to stop the capture can fill up disk space' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Wireshark', 'tcpdump'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires a baseline analysis of cleartext protocols on their internal network.',
    objectives: ['Capture and analyze FTP credentials using Wireshark'],
    steps: ['Step 1: Start Wireshark and select the active interface.', 'Step 2: Initiate an FTP connection from a client to a server.', 'Step 3: Stop the capture and filter for \\'ftp\\'.', 'Step 4: Identify the USER and PASS commands in the packet details.'],
    evidence: ['Screenshot of captured FTP credentials in Wireshark.'],
    validation: ['You should see: Cleartext username and password in the FTP traffic'],
    troubleshooting: ['If no FTP traffic is seen, ensure the client and server are on the same subnet.'],
    mitre: [{ id: 'T1040', name: 'Network Sniffing', tactic: 'Credential Access' }],
    cleanup: ['Close Wireshark and delete the capture file.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following is an example of active sniffing?', opts: ['Monitoring traffic on a hub', 'Using span ports', 'MAC flooding', 'Mirroring traffic'], correct: 2, fb: 'MAC flooding is an active sniffing technique used to overwhelm a switch\\'s CAM table, forcing it to act like a hub.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does promiscuous mode do?', opts: ['Blocks all incoming traffic', 'Encrypts all outgoing traffic', 'Allows a NIC to process all traffic it receives', 'Hides the MAC address of the NIC'], correct: 2, fb: 'Promiscuous mode allows a NIC to process all frames it sees, not just those addressed to it.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which layer of the OSI model does network sniffing primarily operate on?', opts: ['Layer 1', 'Layer 2', 'Layer 3', 'Layer 7'], correct: 1, fb: 'Sniffing primarily operates at the Data Link layer (Layer 2) by capturing frames.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used for passive network sniffing?', opts: ['arpspoof', 'macof', 'Wireshark', 'ettercap'], correct: 2, fb: 'Wireshark is a widely used protocol analyzer for passive sniffing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a collision domain?', opts: ['A network segment where data packets can collide', 'A firewall rule blocking traffic', 'A type of encrypted tunnel', 'A routing protocol'], correct: 0, fb: 'A collision domain is a network segment where simultaneous data transmissions can collide with each other.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does a switch mitigate passive sniffing?', opts: ['By encrypting all traffic', 'By sending traffic only to the intended destination port', 'By blocking unknown MAC addresses', 'By disabling promiscuous mode'], correct: 1, fb: 'Switches maintain a CAM table to send traffic only to the specific port where the destination MAC address is located, mitigating passive sniffing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is vulnerable to cleartext credential sniffing?', opts: ['HTTPS', 'SSH', 'Telnet', 'SFTP'], correct: 2, fb: 'Telnet transmits data, including credentials, in cleartext.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: Passive sniffing requires injecting packets into the network.', opts: ['True', 'False'], correct: 1, fb: 'False. Passive sniffing simply involves listening to existing traffic without injecting anything.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of sniffing in a penetration test?', opts: ['To crash the network', 'To capture sensitive information like credentials', 'To map the network topology', 'To exploit a web vulnerability'], correct: 1, fb: 'The primary goal is often to capture sensitive data, such as credentials, session IDs, or confidential documents.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which hardware device makes passive sniffing easiest?', opts: ['Switch', 'Router', 'Firewall', 'Hub'], correct: 3, fb: 'A hub broadcasts all traffic to all ports, making passive sniffing trivial.' }
  ],
  flashcards: [
    { f: 'Passive Sniffing', b: 'Listening to network traffic without transmitting any data, typically on a hub.' },
    { f: 'Promiscuous Mode', b: 'A configuration that allows a network interface to pass all traffic it receives to the CPU, rather than just frames addressed to it.' },
    { f: 'Collision Domain', b: 'A logical network area where data packets can collide with one another when sent on a shared medium.' }
  ],
  summary: ['Sniffing captures network traffic for analysis.', 'Passive sniffing works on hubs; active sniffing is required for switches.', 'Promiscuous mode enables full packet capture.', 'Unencrypted protocols are highly vulnerable to sniffing.', 'Switches use CAM tables to route traffic, which attackers try to manipulate.'],
  outcomes: ['Differentiate between active and passive sniffing.', 'Explain the concept of promiscuous mode.', 'Identify tools used for network sniffing.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['mac-attacks'] = {
  eyebrow: 'Module 08 · Topic 2',
  title: 'MAC Attacks',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Understanding MAC flooding, CAM table overflow, and switch spoofing techniques.',
  objectives: ['Explain the function of a CAM table', 'Execute and mitigate MAC flooding attacks', 'Understand switch spoofing vulnerabilities'],
  learn: {
    simple: 'MAC attacks target the Layer 2 infrastructure, primarily switches. A switch uses a Content Addressable Memory (CAM) table to map MAC addresses to physical ports. Attackers manipulate this table to intercept traffic or bypass network segmentation.',
    analogy: 'Imagine a hotel receptionist (the switch) who keeps a list of which guest is in which room (CAM table). If someone creates thousands of fake reservations, the receptionist runs out of paper and just starts shouting messages to the whole lobby (hub behavior).',
    architecture: 'A MAC flooding attack bombards the switch with thousands of fake source MAC addresses. The CAM table, having limited memory, overflows. When the CAM table is full, the switch cannot learn new addresses and falls back to fail-open mode, broadcasting all incoming traffic to all ports (like a hub). This allows the attacker to passively sniff traffic meant for other users. Switch spoofing involves an attacker configuring their device to emulate a switch and negotiate a trunk link using Dynamic Trunking Protocol (DTP), gaining access to all VLANs.',
    why: 'Enterprise networks rely on switches for segmentation and security. If a switch is compromised via a MAC attack, attackers can bypass VLAN restrictions, capture sensitive data across the network, and launch further man-in-the-middle attacks.'
  },
  enterprise: {
    gfs: 'A malicious actor in a GFS visitor lounge could use MAC flooding to force the local switch into hub mode, capturing VoIP traffic and internal communications.',
    windows: 'Windows hosts are typically the victims of MAC attacks, as their traffic is broadcasted to the attacker. Network administrators must configure port security on switches to prevent Windows hosts from being spoofed.',
    linux: 'Linux tools like macof (part of the dsniff suite) are frequently used to generate the thousands of random MAC addresses required for a CAM table overflow attack.'
  },
  workflow: ['Step 1: Connect to the target switch network.', 'Step 2: Identify the switch behavior (e.g., VLANs, port security).', 'Step 3: Launch a MAC flooding tool (e.g., macof).', 'Step 4: Monitor the network traffic to see if the switch fails open.', 'Step 5: Capture the broadcasted traffic using a sniffer.', 'Step 6: Stop the attack to avoid prolonged network disruption.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">MAC Attack Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'macof -i eth0', purpose: 'Flood the network with random MAC addresses', out: 'Thousands of packets sent rapidly', note: 'Can cause severe network degradation', mistake: 'Running without authorization can take down production networks' }
    ],
    win: [
      { cmd: 'Get-NetAdapterAdvancedProperty', purpose: 'View advanced NIC properties in Windows', out: 'List of NIC properties', note: 'Useful for checking if NIC is configured for specific VLANs', mistake: 'Modifying properties without understanding can break connectivity' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['macof', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS wants to test the resilience of their edge switches against CAM overflow attacks.',
    objectives: ['Demonstrate a CAM table overflow and capture resulting traffic'],
    steps: ['Step 1: Start Wireshark on the attacker machine.', 'Step 2: Run `macof -i eth0` for 10 seconds.', 'Step 3: Observe the flood of random MAC addresses in Wireshark.', 'Step 4: Stop macof.', 'Step 5: Check if traffic from other hosts is now visible in Wireshark.'],
    evidence: ['Screenshot of macof running and Wireshark capturing broadcasted unicast traffic.'],
    validation: ['You should see: Unicast traffic intended for other devices being captured by the attacker.'],
    troubleshooting: ['If the switch does not fail open, it may have port security enabled or a very large CAM table.'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop macof and clear the switch CAM table (requires switch admin access).']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary target of a MAC flooding attack?', opts: ['The router\\'s routing table', 'The switch\\'s CAM table', 'The DHCP server\\'s lease table', 'The victim\\'s ARP cache'], correct: 1, fb: 'MAC flooding targets the switch\\'s Content Addressable Memory (CAM) table.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What happens when a switch\\'s CAM table is full?', opts: ['It shuts down all ports', 'It routes traffic to the default gateway', 'It broadcasts all incoming frames to all ports', 'It drops all incoming frames'], correct: 2, fb: 'When full, a switch typically "fails open," behaving like a hub and broadcasting traffic.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used to perform a MAC flooding attack?', opts: ['Nmap', 'macof', 'Metasploit', 'Burp Suite'], correct: 1, fb: 'macof, part of the dsniff suite, is designed specifically for MAC flooding.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can a network administrator mitigate MAC flooding?', opts: ['Disable ARP', 'Enable Port Security', 'Use WEP encryption', 'Disable DHCP'], correct: 1, fb: 'Port Security limits the number of MAC addresses allowed on a single switch port.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What protocol is exploited in a Switch Spoofing attack?', opts: ['STP', 'VTP', 'DTP', 'ARP'], correct: 2, fb: 'Dynamic Trunking Protocol (DTP) is exploited to negotiate a trunk link.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the result of a successful switch spoofing attack?', opts: ['Denial of service', 'Access to all VLANs configured on the switch', 'Bypassing the firewall', 'Cracking Wi-Fi passwords'], correct: 1, fb: 'By negotiating a trunk link, the attacker gains access to traffic from all VLANs.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: A MAC address is a logical address that can be easily changed.', opts: ['True', 'False'], correct: 0, fb: 'True. While burned into hardware, MAC addresses can be easily spoofed in software.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which mitigation prevents an attacker from negotiating a trunk link?', opts: ['switchport mode access', 'spanning-tree portfast', 'ip dhcp snooping', 'arp inspection'], correct: 0, fb: 'Setting a port to "switchport mode access" disables DTP negotiation.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In a MAC flooding attack, what type of frames are sent?', opts: ['Frames with identical source MAC addresses', 'Frames with random source MAC addresses', 'Frames with broadcast destination MAC addresses', 'Frames with multicast destination MAC addresses'], correct: 1, fb: 'Random source MAC addresses are used to quickly fill up the CAM table.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does CAM stand for in networking?', opts: ['Centralized Access Management', 'Content Addressable Memory', 'Computer Aided Monitoring', 'Control and Monitoring'], correct: 1, fb: 'CAM stands for Content Addressable Memory.' }
  ],
  flashcards: [
    { f: 'CAM Table', b: 'Content Addressable Memory table; stores the MAC address-to-port mappings on a switch.' },
    { f: 'MAC Flooding', b: 'An attack that overloads the CAM table with fake MAC addresses, forcing the switch to broadcast traffic.' },
    { f: 'Switch Spoofing', b: 'An attacker mimics a switch using DTP to form a trunk link and gain access to multiple VLANs.' }
  ],
  summary: ['MAC attacks exploit Layer 2 switch functionalities.', 'MAC flooding fills the CAM table, causing hub-like behavior.', 'macof is a common tool for MAC flooding.', 'Switch spoofing uses DTP to gain VLAN access.', 'Port security is the primary mitigation for MAC attacks.'],
  outcomes: ['Understand the mechanics of a CAM table.', 'Perform a simulated MAC flooding attack.', 'Implement mitigation strategies for MAC attacks.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['dhcp-attacks'] = {
  eyebrow: 'Module 08 · Topic 3',
  title: 'DHCP Attacks',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Exploring DHCP starvation and rogue DHCP server deployments.',
  objectives: ['Understand the DHCP DORA process', 'Execute DHCP starvation attacks', 'Identify the risks of rogue DHCP servers'],
  learn: {
    simple: 'Dynamic Host Configuration Protocol (DHCP) assigns IP addresses to devices on a network. Attackers can exploit DHCP through Starvation attacks (exhausting all available IP addresses) or by setting up a Rogue DHCP server (assigning malicious IP settings to clients).',
    analogy: 'Think of DHCP as a coat check. DHCP starvation is like an attacker bringing 1,000 fake coats to take up all the hangers, so legitimate guests cannot check their coats. A rogue DHCP server is like a fake coat check attendant who steals coats instead of storing them.',
    architecture: 'The DHCP process involves four steps: Discover, Offer, Request, Acknowledge (DORA). In a DHCP Starvation attack, the attacker broadcasts thousands of DHCP Discover messages with spoofed MAC addresses. The legitimate DHCP server responds with Offers, depleting its IP pool. Once the legitimate server is exhausted, the attacker can introduce a Rogue DHCP server. This rogue server responds to new Discover requests, providing an IP address along with a malicious Default Gateway and DNS server, enabling Man-in-the-Middle (MitM) attacks.',
    why: 'In an enterprise, a rogue DHCP server can redirect all traffic from newly connected clients to an attacker-controlled machine, allowing for silent interception of credentials and data injection.'
  },
  enterprise: {
    gfs: 'If an attacker plugs a rogue access point with a DHCP server into a GFS conference room, they could intercept all web traffic from employees connecting to that AP.',
    windows: 'Windows Server provides DHCP services. Administrators must monitor event logs for IP pool exhaustion (Event ID 1020) to detect starvation attacks.',
    linux: 'Attackers frequently use tools like Yersinia on Linux to launch DHCP starvation attacks and execute rogue DHCP server scripts using dnsmasq.'
  },
  workflow: ['Step 1: Connect to the target network.', 'Step 2: Launch a DHCP starvation tool (e.g., Yersinia).', 'Step 3: Monitor the DHCP server to confirm IP pool exhaustion.', 'Step 4: Start a rogue DHCP server on the attacker machine.', 'Step 5: Wait for new clients to request IP addresses.', 'Step 6: Intercept and analyze traffic routed through the rogue gateway.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">DHCP Attack Process (DORA)</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'yersinia dhcp -attack 1 -interface eth0', purpose: 'Launch DHCP starvation attack', out: 'Thousands of DHCP Discover packets sent', note: 'Use with caution on live networks', mistake: 'Attacking the wrong interface' }
    ],
    win: [
      { cmd: 'ipconfig /release && ipconfig /renew', purpose: 'Request a new DHCP lease', out: 'New IP address assigned', note: 'Useful for testing DHCP functionality', mistake: 'Doing this on a remote server will disconnect your session' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Yersinia', 'dnsmasq'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to validate if DHCP Snooping is properly configured on their access switches.',
    objectives: ['Perform DHCP starvation and deploy a rogue DHCP server'],
    steps: ['Step 1: Open Yersinia in graphical mode (`yersinia -G`).', 'Step 2: Select the DHCP tab and launch a "sending DISCOVER packet" attack.', 'Step 3: Verify the legitimate DHCP pool is exhausted.', 'Step 4: Configure and start `dnsmasq` to act as a rogue DHCP server.', 'Step 5: Connect a new client to the network and verify it receives the rogue IP settings.'],
    evidence: ['Screenshot of the client receiving IP settings from the rogue DHCP server.'],
    validation: ['You should see: The client\\'s default gateway points to the attacker\\'s IP address.'],
    troubleshooting: ['If starvation fails, the switch may have DHCP rate limiting or port security enabled.'],
    mitre: [{ id: 'T1557', name: 'Adversary-in-the-Middle', tactic: 'Credential Access' }],
    cleanup: ['Stop Yersinia, stop dnsmasq, and restart the legitimate DHCP service.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does the acronym DORA stand for in DHCP?', opts: ['Discover, Offer, Route, Acknowledge', 'Discover, Offer, Request, Acknowledge', 'Data, Output, Request, Allocate', 'Domain, Origin, Route, Access'], correct: 1, fb: 'DORA stands for Discover, Offer, Request, Acknowledge.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of a DHCP starvation attack?', opts: ['To crash the DHCP server', 'To exhaust the DHCP server\\'s IP address pool', 'To spoof the DNS server', 'To bypass the firewall'], correct: 1, fb: 'DHCP starvation aims to deplete the available IP addresses so legitimate clients cannot get one.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is famous for exploiting DHCP, STP, and CDP vulnerabilities?', opts: ['Nmap', 'Metasploit', 'Yersinia', 'Hydra'], correct: 2, fb: 'Yersinia is a network vulnerability tool designed for Layer 2 protocols like DHCP, STP, and CDP.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does an attacker typically do immediately after a successful DHCP starvation attack?', opts: ['Launch a DoS attack', 'Set up a Rogue DHCP server', 'Format the victim\\'s hard drive', 'Exfiltrate database records'], correct: 1, fb: 'Once the legitimate server is exhausted, the attacker introduces a Rogue DHCP server to assign malicious settings.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which DHCP setting is manipulated by a rogue server to perform a Man-in-the-Middle attack?', opts: ['Subnet Mask', 'Default Gateway', 'Lease Time', 'MAC Address'], correct: 1, fb: 'By setting the Default Gateway to the attacker\\'s IP, all off-subnet traffic is routed through the attacker.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can a switch prevent rogue DHCP servers?', opts: ['Port Security', 'MAC Filtering', 'DHCP Snooping', 'ARP Inspection'], correct: 2, fb: 'DHCP Snooping configures switch ports as trusted (for legitimate DHCP servers) or untrusted, blocking rogue offers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: A DHCP Discover message is sent as a unicast packet.', opts: ['True', 'False'], correct: 1, fb: 'False. A DHCP Discover message is broadcasted to find available DHCP servers.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In the DORA process, who sends the DHCP Offer?', opts: ['The Client', 'The Router', 'The DHCP Server', 'The Switch'], correct: 2, fb: 'The DHCP Server sends the Offer in response to a Client\\'s Discover message.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What type of packet does a DHCP Starvation attack flood the network with?', opts: ['DHCP Release', 'DHCP Request', 'DHCP Offer', 'DHCP Discover'], correct: 3, fb: 'The attack floods the network with DHCP Discover packets using spoofed MAC addresses.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which defense mechanism relies on DHCP Snooping to prevent ARP spoofing?', opts: ['Dynamic ARP Inspection (DAI)', 'IP Source Guard', 'Port Security', 'VLAN Access Control Lists (VACLs)'], correct: 0, fb: 'DAI uses the DHCP Snooping binding database to validate ARP packets.' }
  ],
  flashcards: [
    { f: 'DORA', b: 'The four-step DHCP process: Discover, Offer, Request, Acknowledge.' },
    { f: 'DHCP Starvation', b: 'An attack that exhausts the IP address pool of a DHCP server by flooding it with spoofed Discover requests.' },
    { f: 'Rogue DHCP Server', b: 'An unauthorized DHCP server placed on a network to assign malicious IP configurations to clients.' }
  ],
  summary: ['DHCP assigns IP configurations using the DORA process.', 'DHCP starvation depletes the IP pool using fake MAC addresses.', 'Rogue DHCP servers assign malicious default gateways for MitM.', 'Yersinia is a primary tool for DHCP attacks.', 'DHCP Snooping is the best defense against DHCP attacks.'],
  outcomes: ['Explain the DORA process.', 'Execute a DHCP starvation attack.', 'Configure mitigations against rogue DHCP servers.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['arp-poisoning'] = {
  eyebrow: 'Module 08 · Topic 4',
  title: 'ARP Poisoning',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Executing ARP spoofing, Man-in-the-Middle (MitM) attacks, and Gratuitous ARP manipulation.',
  objectives: ['Understand Address Resolution Protocol (ARP) operations', 'Execute ARP poisoning attacks', 'Analyze MitM traffic'],
  learn: {
    simple: 'Address Resolution Protocol (ARP) maps IP addresses to MAC addresses on a local network. ARP Poisoning (or Spoofing) involves sending forged ARP responses to a victim, tricking them into believing the attacker\\'s MAC address is associated with the IP address of the default gateway or another victim.',
    analogy: 'Imagine a physical address book in an office. If an attacker crosses out the CEO\\'s real room number and writes in their own room number, all mail meant for the CEO goes to the attacker. This is ARP poisoning.',
    architecture: 'ARP is a stateless protocol; devices will accept ARP replies even if they did not send an ARP request (this is called a Gratuitous ARP). In a typical ARP spoofing MitM attack, the attacker sends an ARP reply to the victim (claiming to be the router) and an ARP reply to the router (claiming to be the victim). Both devices update their ARP caches, routing traffic through the attacker. IP Forwarding must be enabled on the attacker\\'s machine so traffic is passed along, otherwise, it results in a Denial of Service (DoS).',
    why: 'ARP spoofing is the most common method for achieving a Man-in-the-Middle position on a local enterprise network, allowing attackers to intercept credentials, modify data in transit, or downgrade encrypted connections.'
  },
  enterprise: {
    gfs: 'If an attacker compromises a workstation in the GFS accounting department, they could use ARP poisoning to intercept traffic between other accountants and the internal financial database server.',
    windows: 'Windows clients cache ARP entries dynamically. Administrators can use Group Policy to configure static ARP entries for critical servers, though this is difficult to maintain at scale.',
    linux: 'Linux attackers use tools like `arpspoof` or `ettercap`. It is crucial that the attacker enables IP forwarding (`sysctl -w net.ipv4.ip_forward=1`) to act as a router and avoid dropping the intercepted packets.'
  },
  workflow: ['Step 1: Identify the IP of the victim and the default gateway.', 'Step 2: Enable IP forwarding on the attacker machine.', 'Step 3: Launch the ARP poisoning tool targeting the victim and gateway.', 'Step 4: Use a sniffer (e.g., Wireshark) to capture the intercepted traffic.', 'Step 5: Optionally, use tools to modify the traffic in real-time.', 'Step 6: Stop the attack and restore the original ARP tables (re-arping).'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">ARP Poisoning & MitM Flow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'arpspoof -i eth0 -t 192.168.1.10 192.168.1.1', purpose: 'ARP Poisoning', out: 'Redirected traffic', note: 'Requires IP forwarding enabled', mistake: 'Not enabling IP forwarding causes a DoS instead of MITM' },
      { cmd: 'echo 1 > /proc/sys/net/ipv4/ip_forward', purpose: 'Enable IP forwarding in Linux', out: 'Silent success', note: 'Essential for MitM', mistake: 'Forgetting this step breaks the victim\\'s internet connection' }
    ],
    win: [
      { cmd: 'arp -a', purpose: 'Check ARP cache', out: 'List of IPs and MACs', note: 'Useful for detecting ARP poisoning', mistake: 'Ignoring static ARP entries' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['arpspoof', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS SOC analysts need to understand how to detect ARP poisoning attacks on the network.',
    objectives: ['Execute an ARP spoofing attack and capture traffic'],
    steps: ['Step 1: Enable IP forwarding on the attacker Kali machine.', 'Step 2: Run `arpspoof -i eth0 -t <VICTIM_IP> <GATEWAY_IP>`.', 'Step 3: Run `arpspoof -i eth0 -t <GATEWAY_IP> <VICTIM_IP>` in a new terminal.', 'Step 4: Open Wireshark and capture traffic from the victim.', 'Step 5: Stop the arpspoof processes to restore the network.'],
    evidence: ['Screenshot of the victim\\'s ARP table showing the attacker\\'s MAC address for the Gateway IP.'],
    validation: ['You should see: The victim\\'s traffic passing through the attacker\\'s Wireshark interface.'],
    troubleshooting: ['If the victim loses internet access, verify IP forwarding is enabled on the attacker machine.'],
    mitre: [{ id: 'T1557', name: 'Adversary-in-the-Middle', tactic: 'Credential Access' }],
    cleanup: ['Stop arpspoof tools and clear the ARP cache on the victim machine.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the purpose of the ARP protocol?', opts: ['To resolve domain names to IP addresses', 'To route packets between different networks', 'To resolve IP addresses to MAC addresses', 'To assign IP addresses to clients'], correct: 2, fb: 'ARP (Address Resolution Protocol) maps Layer 3 IP addresses to Layer 2 MAC addresses.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why is ARP inherently vulnerable to spoofing?', opts: ['It does not use encryption', 'It is a stateless protocol that accepts unsolicited replies', 'It operates at Layer 3', 'It uses UDP for communication'], correct: 1, fb: 'ARP is stateless; devices will update their cache with unsolicited ARP replies (Gratuitous ARP) without authentication.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In a Man-in-the-Middle attack via ARP spoofing, what must the attacker do to ensure the victim does not lose network connectivity?', opts: ['Disable the firewall', 'Enable IP Forwarding', 'Run a DHCP server', 'Change their MAC address'], correct: 1, fb: 'IP forwarding allows the attacker\\'s machine to route the intercepted packets to their true destination.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which command displays the ARP cache on a Windows machine?', opts: ['ipconfig /all', 'route print', 'arp -a', 'netstat -nr'], correct: 2, fb: 'The `arp -a` command displays the current ARP cache in Windows.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Gratuitous ARP?', opts: ['An ARP request sent to a different subnet', 'An unsolicited ARP reply used to update ARP caches', 'An encrypted ARP message', 'An ARP message sent to the default gateway'], correct: 1, fb: 'A Gratuitous ARP is an ARP response that was not prompted by an ARP request, often used for failover or spoofing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used to perform ARP poisoning?', opts: ['Nmap', 'arpspoof', 'John the Ripper', 'Hydra'], correct: 1, fb: 'arpspoof (part of dsniff) is a classic tool for ARP poisoning.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How can a network mitigate ARP poisoning?', opts: ['Implementing Dynamic ARP Inspection (DAI)', 'Disabling the switch CAM table', 'Using WEP encryption', 'Disabling DHCP'], correct: 0, fb: 'DAI validates ARP packets against the DHCP Snooping binding database, dropping invalid ones.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'If an attacker performs ARP spoofing but forgets to enable IP forwarding, what is the result?', opts: ['Man-in-the-Middle', 'Denial of Service (DoS)', 'DNS Spoofing', 'MAC Flooding'], correct: 1, fb: 'Without IP forwarding, the packets are dropped by the attacker, resulting in a DoS for the victim.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: ARP poisoning can be performed across different VLANs by default.', opts: ['True', 'False'], correct: 1, fb: 'False. ARP is a Layer 2 protocol and is confined to the local broadcast domain (VLAN).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which file must be modified in Linux to enable IP forwarding?', opts: ['/etc/hosts', '/etc/resolv.conf', '/proc/sys/net/ipv4/ip_forward', '/etc/network/interfaces'], correct: 2, fb: 'Writing a \\'1\\' to `/proc/sys/net/ipv4/ip_forward` enables IP forwarding in Linux.' }
  ],
  flashcards: [
    { f: 'ARP', b: 'Address Resolution Protocol; maps IP addresses to MAC addresses.' },
    { f: 'Gratuitous ARP', b: 'An unsolicited ARP reply used to update the ARP caches of devices on the network.' },
    { f: 'Dynamic ARP Inspection (DAI)', b: 'A security feature that validates ARP packets and drops invalid IP-to-MAC bindings to prevent spoofing.' }
  ],
  summary: ['ARP maps IPs to MAC addresses.', 'ARP is stateless and vulnerable to forged replies.', 'ARP poisoning redirects traffic to the attacker (MitM).', 'IP forwarding is crucial to avoid causing a DoS during MitM.', 'DAI is the primary enterprise defense against ARP spoofing.'],
  outcomes: ['Understand ARP vulnerabilities.', 'Execute an ARP poisoning attack.', 'Implement DAI to secure the network.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['spoofing-mitm'] = {
  eyebrow: 'Module 08 · Topic 5',
  title: 'Spoofing & MitM Attacks',
  module: 'Phase 08: Network Security Analyst',
  sub: 'Advanced Man-in-the-Middle techniques: DNS spoofing, cache poisoning, and SSL stripping.',
  objectives: ['Execute DNS spoofing to redirect traffic', 'Understand DNS cache poisoning mechanics', 'Perform SSL stripping to downgrade secure connections'],
  learn: {
    simple: 'Once a Man-in-the-Middle (MitM) position is established (e.g., via ARP poisoning), attackers can manipulate higher-layer protocols. DNS Spoofing provides fake IP addresses for domain names, redirecting users to malicious sites. SSL Stripping downgrades secure HTTPS connections to unencrypted HTTP.',
    analogy: 'DNS spoofing is like changing the phonebook so the bank\\'s name points to the attacker\\'s phone number. SSL stripping is like the attacker answering the phone, telling the user "we don\\'t need a secure line," and then relaying the messages to the real bank over a secure line, acting as a translator.',
    architecture: 'In DNS Spoofing, the attacker intercepts a DNS request and sends a forged response before the legitimate DNS server can reply. Cache poisoning involves tricking a DNS server itself into caching the forged record, affecting all its clients. SSL Stripping (e.g., using sslstrip) works by intercepting HTTP traffic and replacing all `https://` links with `http://`. The attacker maintains an HTTPS connection with the legitimate server but provides a plaintext HTTP connection to the victim, capturing credentials in the process. HSTS (HTTP Strict Transport Security) was developed to prevent SSL stripping.',
    why: 'These attacks allow threat actors to bypass encryption and steal credentials for critical enterprise applications (O365, internal portals) even if the user attempts to visit the legitimate domain.'
  },
  enterprise: {
    gfs: 'An attacker targeting GFS could use DNS spoofing to redirect employees trying to access the internal HR portal (hr.gfs.local) to a fake phishing page hosted on the attacker\\'s machine.',
    windows: 'Windows DNS servers can be targets for cache poisoning. Enabling DNSSEC is crucial for enterprises to ensure the cryptographic integrity of DNS responses.',
    linux: 'Linux-based tools like Ettercap and Bettercap are widely used for performing combined ARP poisoning, DNS spoofing, and SSL stripping attacks in a single framework.'
  },
  workflow: ['Step 1: Achieve MitM (e.g., via ARP poisoning).', 'Step 2: Configure the DNS spoofing tool with the target domain and malicious IP.', 'Step 3: Launch the DNS spoofing tool.', 'Step 4: (For SSL Stripping) Configure iptables to route HTTP traffic to the SSL stripping tool.', 'Step 5: Run the SSL stripping tool (e.g., sslstrip).', 'Step 6: Monitor the captured traffic for credentials.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="600" height="400" fill="#f8f9fa"/><text x="300" y="200" font-family="Arial" font-size="20" text-anchor="middle" fill="#333">SSL Stripping & DNS Spoofing</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'ettercap -T -q -i eth0 -M arp:remote -P dns_spoof /192.168.1.10// /192.168.1.1//', purpose: 'ARP Poisoning and DNS Spoofing', out: 'Intercepted and redirected traffic', note: 'Requires editing etter.dns file first', mistake: 'Not configuring the etter.dns file results in no spoofing' },
      { cmd: 'sslstrip -l 8080', purpose: 'Run SSL strip on port 8080', out: 'Listens for traffic', note: 'Requires iptables port redirection', mistake: 'Forgetting iptables rule means traffic won\\'t hit sslstrip' }
    ],
    win: [
      { cmd: 'ipconfig /displaydns', purpose: 'View the DNS resolver cache', out: 'List of cached DNS records', note: 'Useful to verify if DNS has been spoofed/poisoned', mistake: 'Misinterpreting legitimate records as spoofed' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Ettercap', 'Bettercap', 'sslstrip'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires testing against advanced MitM attacks to validate their HSTS and DNSSEC configurations.',
    objectives: ['Perform DNS spoofing and SSL stripping using Ettercap/Bettercap'],
    steps: ['Step 1: Edit `/etc/ettercap/etter.dns` to map a target domain to the attacker\\'s IP.', 'Step 2: Start Apache on Kali to host a fake login page.', 'Step 3: Run Ettercap with the `dns_spoof` plugin.', 'Step 4: On the victim machine, ping the target domain and verify the IP resolves to the attacker.', 'Step 5: Access the domain in a browser and verify the fake page loads.'],
    evidence: ['Screenshot of the victim pinging the spoofed domain, showing the attacker IP.'],
    validation: ['You should see: DNS queries for the target domain resolving to the attacker\\'s machine.'],
    troubleshooting: ['If the victim browser shows a certificate error, HSTS is likely blocking the SSL strip attempt.'],
    mitre: [{ id: 'T1557', name: 'Adversary-in-the-Middle', tactic: 'Credential Access' }],
    cleanup: ['Stop Ettercap, flush the victim\\'s DNS cache (`ipconfig /flushdns`), and stop Apache.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary objective of DNS Spoofing?', opts: ['To crash the DNS server', 'To redirect a user to a malicious website by providing a fake IP address', 'To encrypt DNS traffic', 'To bypass firewall rules'], correct: 1, fb: 'DNS spoofing provides a fraudulent IP address for a legitimate domain name.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How does SSL Stripping work?', opts: ['It cracks the SSL certificate', 'It steals the private key of the server', 'It downgrades HTTPS links to HTTP, acting as a proxy between the victim and server', 'It exploits vulnerabilities in TLS 1.3'], correct: 2, fb: 'SSL stripping intercepts traffic and changes `https://` references to `http://`, forcing the victim to communicate in plaintext.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which security mechanism is designed specifically to prevent SSL Stripping?', opts: ['DNSSEC', 'HSTS (HTTP Strict Transport Security)', 'IPsec', 'MAC Filtering'], correct: 1, fb: 'HSTS instructs browsers to only connect to the site using HTTPS, ignoring any HTTP links.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'In an Ettercap DNS spoofing attack, which file must be modified to map domains to IPs?', opts: ['/etc/hosts', '/etc/resolv.conf', 'etter.dns', 'etter.conf'], correct: 2, fb: 'The `etter.dns` file contains the records used by Ettercap\\'s dns_spoof plugin.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is DNS Cache Poisoning?', opts: ['Infecting the victim\\'s browser cache', 'Corrupting the DNS server\\'s cache with forged records so it serves them to multiple clients', 'Deleting the DNS cache', 'Encrypting the DNS cache'], correct: 1, fb: 'Cache poisoning targets the DNS resolver itself, affecting all users who query that resolver.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is famous for automating SSL Stripping?', opts: ['Nmap', 'sslstrip (by Moxie Marlinspike)', 'Hydra', 'John the Ripper'], correct: 1, fb: 'sslstrip was created by Moxie Marlinspike to automate this MitM attack.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What prerequisite is required before performing DNS Spoofing or SSL Stripping on a local network?', opts: ['Cracking the Wi-Fi password', 'Achieving a Man-in-the-Middle position (e.g., via ARP spoofing)', 'Installing malware on the victim', 'Compromising the ISP'], correct: 1, fb: 'The attacker must first be in a position to intercept the traffic, typically via ARP spoofing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What protocol secures DNS to prevent cache poisoning and spoofing?', opts: ['DNS-over-HTTP', 'DNSSEC', 'HTTPS', 'TLS'], correct: 1, fb: 'DNSSEC (Domain Name System Security Extensions) provides cryptographic authentication of DNS data.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'True or False: SSL Stripping requires the attacker to generate a fake SSL certificate.', opts: ['True', 'False'], correct: 1, fb: 'False. SSL Stripping relies on preventing the secure connection from happening at all, avoiding certificate errors.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'When preparing for SSL stripping on Linux, what iptables rule is typically needed?', opts: ['Block port 443', 'Redirect traffic from port 80 to the port where sslstrip is listening', 'Redirect port 443 to port 80', 'Block all ICMP traffic'], correct: 1, fb: 'iptables is used to redirect outbound HTTP traffic (port 80) to the local port where sslstrip is listening.' }
  ],
  flashcards: [
    { f: 'DNS Spoofing', b: 'Providing fake IP addresses in response to DNS queries to redirect traffic.' },
    { f: 'SSL Stripping', b: 'A MitM attack that downgrades secure HTTPS connections to plaintext HTTP.' },
    { f: 'HSTS', b: 'HTTP Strict Transport Security; a web security policy mechanism that helps to protect websites against MitM attacks such as protocol downgrade attacks and cookie hijacking.' }
  ],
  summary: ['DNS spoofing redirects users to malicious IPs.', 'Cache poisoning affects the DNS server directly.', 'SSL stripping downgrades HTTPS to HTTP.', 'HSTS protects against SSL stripping.', 'DNSSEC protects against DNS spoofing.'],
  outcomes: ['Execute a DNS spoofing attack.', 'Explain the mechanics of SSL stripping.', 'Implement HSTS and DNSSEC as mitigations.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Advanced", prerequisites: [], lastReviewed: "2026-07-18" }
};
"""

def upgrade_index_html():
    if not os.path.exists(HTML_PATH):
        print(f"Error: {HTML_PATH} not found.")
        return

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    # The user asked to inject the content before "// ── TAB WIRING ──"
    target_string = "// ── TAB WIRING ──"
    
    if target_string not in html_content:
        print(f"Error: Could not find '{target_string}' in {HTML_PATH}")
        return
    
    new_html_content = html_content.replace(target_string, CONTENT + "\n\n" + target_string)
    
    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(new_html_content)
        
    print(f"Successfully injected new content into {HTML_PATH}")

if __name__ == "__main__":
    upgrade_index_html()
