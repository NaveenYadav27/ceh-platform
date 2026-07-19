import os
import json

html_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')

m16_data = """
CONTENT['wireless-concepts'] = {
  eyebrow: 'Module 16 · Topic 1',
  title: 'Wireless Concepts',
  module: 'Phase 16: Network Security Specialist',
  sub: 'Fundamental principles of wireless networking architecture and communication protocols.',
  objectives: ['Understand 802.11 standards', 'Analyze wireless network architectures', 'Identify radio frequency principles'],
  learn: {
    simple: 'Wireless networking relies on radio frequency (RF) to transmit data between devices without physical cables. Devices connect through Access Points (APs) that act as bridges between the wireless medium and the wired network infrastructure. The IEEE 802.11 family of standards governs how these devices communicate, dictating frequencies, modulation techniques, and data rates.',
    analogy: 'Think of a wireless network like a crowded room where people are talking. The Access Point is the person at the front with a megaphone. Everyone must take turns speaking (CSMA/CA) and use the right language (802.11 standard) to be understood. If everyone speaks at once, interference occurs.',
    architecture: 'At a technical level, 802.11 architectures consist of Basic Service Sets (BSS), where devices communicate through a single AP. Multiple BSSs can be connected via a Distribution System (DS) to form an Extended Service Set (ESS), allowing seamless roaming. Communication occurs on specific channels within the 2.4 GHz, 5 GHz, or 6 GHz frequency bands. Devices use Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) to manage access to the shared RF medium, transmitting Request to Send (RTS) and Clear to Send (CTS) frames to reserve the channel before data transmission.',
    why: 'In enterprise environments, wireless networks expand the attack surface beyond physical walls. Understanding these concepts is critical because an attacker does not need physical access to the building to compromise the network, intercept data, or inject malicious packets.'
  },
  enterprise: {
    gfs: 'At Global Financial Services, employees rely on seamless Wi-Fi roaming across multiple floors. Understanding BSS and ESS is crucial for ensuring uninterrupted connectivity and preventing rogue APs from mimicking the corporate network.',
    windows: 'Windows manages wireless connections using the WLAN AutoConfig service, storing profiles and preferred network lists.',
    linux: 'Linux relies on tools like NetworkManager and wpa_supplicant to manage wireless interfaces, SSIDs, and authentication protocols.'
  },
  workflow: ['Step 1: Identify the frequency band and channels in use.', 'Step 2: Determine the 802.11 standard (e.g., 802.11ac/ax).', 'Step 3: Analyze the Basic Service Set (BSS) configuration.', 'Step 4: Understand the authentication and association process.', 'Step 5: Monitor for interference and signal strength.', 'Step 6: Assess the physical boundaries of the RF coverage.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a1a" /><text x="300" y="200" fill="white" text-anchor="middle" font-size="20">Wireless Network Architecture</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'iwconfig', purpose: 'View wireless interfaces', out: 'Wireless extensions info', note: 'Basic tool', mistake: 'Using on non-wireless interface' }
    ],
    win: [
      { cmd: 'netsh wlan show interfaces', purpose: 'View Wi-Fi details', out: 'Signal strength, BSSID', note: 'Useful for troubleshooting', mistake: 'Running without admin rights' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Aircrack-ng', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires an audit of the wireless spectrum in the main lobby to ensure no unauthorized APs are broadcasting.',
    objectives: ['Identify broadcasting SSIDs and channels.'],
    steps: ['Step 1: Put interface into monitor mode with `airmon-ng start wlan0`.', 'Step 2: Scan the airwaves using `airodump-ng wlan0mon`.'],
    evidence: ['Terminal output showing discovered networks.'],
    validation: ['You should see: A list of nearby Access Points and their channels.'],
    troubleshooting: ['If no networks appear, check if the interface is actually in monitor mode.'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['Stop monitor mode with `airmon-ng stop wlan0mon`.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which 802.11 standard operates only in the 5 GHz band?', opts: ['802.11b', '802.11g', '802.11ac', '802.11n'], correct: 2, fb: '802.11ac is exclusively 5 GHz.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What mechanism does Wi-Fi use for media access?', opts: ['CSMA/CD', 'CSMA/CA', 'Token Passing', 'TDMA'], correct: 1, fb: 'Wi-Fi uses Collision Avoidance (CA).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which component bridges wireless and wired networks?', opts: ['Switch', 'Router', 'Access Point', 'Hub'], correct: 2, fb: 'The AP bridges the wireless medium to the wired network.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does BSSID typically represent?', opts: ['Network name', 'AP MAC address', 'Client IP', 'Encryption type'], correct: 1, fb: 'BSSID is the MAC address of the Access Point.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which frequency band generally has better wall penetration?', opts: ['2.4 GHz', '5 GHz', '6 GHz', '60 GHz'], correct: 0, fb: 'Lower frequencies penetrate obstacles better.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a beacon frame used for?', opts: ['Data transfer', 'Network advertisement', 'Authentication', 'Encryption'], correct: 1, fb: 'Beacon frames announce the presence of a wireless network.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'How many non-overlapping channels are in the US 2.4 GHz band?', opts: ['1', '3', '6', '11'], correct: 1, fb: 'Channels 1, 6, and 11 are non-overlapping.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does SSID stand for?', opts: ['Secure System ID', 'Service Set Identifier', 'System Security ID', 'Station Set Identifier'], correct: 1, fb: 'SSID is the name of the network.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which management frame is sent by a client to discover networks?', opts: ['Beacon', 'Probe Request', 'Association Request', 'Auth Request'], correct: 1, fb: 'Clients send Probe Requests to find networks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What defines an Extended Service Set (ESS)?', opts: ['One AP', 'Multiple BSSs connected via DS', 'Ad-hoc network', 'Bluetooth mesh'], correct: 1, fb: 'An ESS is multiple BSSs connected by a Distribution System.' }
  ],
  flashcards: [
    { f: 'BSSID', b: 'The MAC address of the Access Point radio.' },
    { f: 'SSID', b: 'The human-readable name of the wireless network.' }
  ],
  summary: ['Wireless uses RF.', 'Access Points bridge wired and wireless.', '802.11 is the governing standard.', 'CSMA/CA is used for media access.', 'Bands are 2.4GHz, 5GHz, 6GHz.'],
  outcomes: ['Understand wireless architecture.', 'Identify key 802.11 concepts.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['wireless-encryption'] = {
  eyebrow: 'Module 16 · Topic 2',
  title: 'Wireless Encryption',
  module: 'Phase 16: Network Security Specialist',
  sub: 'Mechanisms for securing wireless traffic against interception.',
  objectives: ['Understand WEP, WPA, WPA2, and WPA3', 'Analyze the 4-way handshake', 'Identify vulnerabilities in older protocols'],
  learn: {
    simple: 'Because wireless data is broadcast through the air, anyone with a capable receiver can capture it. Encryption protocols scramble this data so that only authorized parties with the correct key can read it. Over the years, these protocols have evolved from the weak WEP to the highly secure WPA3, each addressing the cryptographic flaws of its predecessor.',
    analogy: 'Encryption is like sending a locked box through a public mail system. Everyone can see the box, but only the person with the right key can open it. WEP was a flimsy padlock that could be picked in seconds; WPA3 is a biometric vault.',
    architecture: 'WEP used the RC4 stream cipher with a 24-bit Initialization Vector (IV), which was easily crackable due to IV reuse. WPA introduced TKIP to change keys dynamically. WPA2 standardized AES-CCMP for robust encryption, though it remains vulnerable to offline dictionary attacks if the pre-shared key (PSK) is weak. WPA3 introduces Simultaneous Authentication of Equals (SAE), replacing the PSK handshake and providing forward secrecy, making offline dictionary attacks virtually impossible even if the password is weak.',
    why: 'Strong encryption is the primary defense against eavesdropping and unauthorized network access in enterprise environments. Weak encryption can lead to complete network compromise.'
  },
  enterprise: {
    gfs: 'Global Financial Services uses WPA2/WPA3-Enterprise (802.1X) with RADIUS to authenticate users individually, rather than using a single shared password.',
    windows: 'Windows Group Policy can enforce wireless profiles, ensuring clients only connect using WPA3-Enterprise.',
    linux: 'Linux wpa_supplicant handles complex 802.1X EAP authentication for enterprise networks.'
  },
  workflow: ['Step 1: Identify encryption type (WEP/WPA/WPA2/WPA3).', 'Step 2: Determine if Personal (PSK) or Enterprise (802.1X) is used.', 'Step 3: Capture the authentication handshake.', 'Step 4: Attempt offline dictionary attack (if applicable).', 'Step 5: Analyze the key exchange mechanism.', 'Step 6: Implement stronger protocols.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a1a" /><text x="300" y="200" fill="white" text-anchor="middle" font-size="20">WPA2 4-Way Handshake</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aircrack-ng -w wordlist.txt capture.cap', purpose: 'Crack WPA2 PSK', out: 'KEY FOUND!', note: 'Requires captured handshake', mistake: 'Using wrong wordlist' }
    ],
    win: [
      { cmd: 'netsh wlan show profile name="SSID" key=clear', purpose: 'View saved Wi-Fi password', out: 'Key Content: Password', note: 'Requires admin rights', mistake: 'Looking for non-existent profile' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Aircrack-ng', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS wants to test the strength of the guest network password by simulating an offline dictionary attack.',
    objectives: ['Capture a WPA2 handshake and crack it.'],
    steps: ['Step 1: Capture handshake with `airodump-ng`.', 'Step 2: Crack with `aircrack-ng -w words.txt capture.cap`.'],
    evidence: ['Screenshot of cracked password.'],
    validation: ['You should see: KEY FOUND! [ password123 ]'],
    troubleshooting: ['If aircrack fails immediately, check if the handshake is fully captured.'],
    mitre: [{ id: 'T1110', name: 'Brute Force', tactic: 'Credential Access' }],
    cleanup: ['Delete capture files.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which encryption standard uses SAE?', opts: ['WEP', 'WPA', 'WPA2', 'WPA3'], correct: 3, fb: 'WPA3 introduces Simultaneous Authentication of Equals.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What cipher does WPA2 mandate?', opts: ['RC4', 'TKIP', 'AES-CCMP', 'DES'], correct: 2, fb: 'WPA2 uses AES-CCMP.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which protocol is highly vulnerable due to IV reuse?', opts: ['WEP', 'WPA', 'WPA2', 'WPA3'], correct: 0, fb: 'WEP\'s 24-bit IV leads to key reuse and rapid cracking.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is captured to crack WPA2-PSK?', opts: ['Beacon frame', '4-way handshake', 'CTS frame', 'RTS frame'], correct: 1, fb: 'The 4-way handshake contains the hashed password material.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which enterprise authentication method uses a RADIUS server?', opts: ['WPA2-Personal', '802.1X', 'WEP', 'Open'], correct: 1, fb: '802.1X is the standard for port-based network access control, often using RADIUS.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What did TKIP address in WPA?', opts: ['Speed', 'Key reuse in WEP', 'Range', '5GHz support'], correct: 1, fb: 'TKIP generated dynamic keys to fix WEPs static key flaws.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What attack is WPA3 designed to prevent?', opts: ['Deauth', 'Offline dictionary', 'Evil Twin', 'Jamming'], correct: 1, fb: 'SAE prevents offline dictionary attacks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What length is the WEP IV?', opts: ['24-bit', '48-bit', '128-bit', '256-bit'], correct: 0, fb: 'WEP uses a short 24-bit IV.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a PMK in WPA2?', opts: ['Pairwise Master Key', 'Primary Master Key', 'Personal Master Key', 'Public Master Key'], correct: 0, fb: 'The PMK is derived from the PSK.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which of the following offers Forward Secrecy?', opts: ['WEP', 'WPA', 'WPA2', 'WPA3'], correct: 3, fb: 'WPA3 offers forward secrecy.' }
  ],
  flashcards: [
    { f: 'WPA3', b: 'The latest Wi-Fi security standard using SAE.' },
    { f: '4-Way Handshake', b: 'Process used in WPA/WPA2 to derive session keys.' }
  ],
  summary: ['WEP is broken.', 'WPA2 uses AES.', 'WPA3 uses SAE.', 'Enterprise uses 802.1X.', '4-way handshake is targeted in WPA2 attacks.'],
  outcomes: ['Identify wireless encryption protocols.', 'Understand WPA2 vulnerabilities.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['wireless-threats'] = {
  eyebrow: 'Module 16 · Topic 3',
  title: 'Wireless Threats',
  module: 'Phase 16: Network Security Specialist',
  sub: 'Common attacks against wireless infrastructure and clients.',
  objectives: ['Understand Rogue APs and Evil Twins', 'Analyze Deauthentication attacks', 'Identify wireless sniffing techniques'],
  learn: {
    simple: 'Because wireless signals cannot be contained within physical walls, attackers can interact with the network from the parking lot. Threats include Rogue APs (unauthorized APs plugged into the corporate network), Evil Twins (APs mimicking the corporate network to steal credentials), and Denial of Service (DoS) attacks like Deauthentication spoofing.',
    analogy: 'An Evil Twin is like someone setting up a fake ATM next to a real one. It looks identical, but when you put your card in, they steal your PIN.',
    architecture: 'Deauthentication attacks leverage the fact that management frames in 802.11 (prior to 802.11w) are unencrypted and unauthenticated. An attacker can spoof the MAC address of an AP and send a broadcast deauth frame, causing all clients to disconnect. This is often used as a precursor to an Evil Twin attack or to force a WPA2 handshake capture. Rogue APs bypass network access controls because the AP itself is connected to a trusted switch port.',
    why: 'Wireless threats bypass perimeter physical security. Defending against them requires continuous spectrum monitoring and strong endpoint authentication.'
  },
  enterprise: {
    gfs: 'GFS employs Wireless Intrusion Prevention Systems (WIPS) to detect and contain Rogue APs and Evil Twins near their corporate offices.',
    windows: 'Windows devices can be tricked by Evil Twins if certificate validation is not strictly enforced for 802.1X connections.',
    linux: 'Linux clients can be configured to require Management Frame Protection (802.11w) to resist deauth attacks.'
  },
  workflow: ['Step 1: Monitor the RF spectrum.', 'Step 2: Identify anomalous SSIDs or MAC addresses.', 'Step 3: Detect deauthentication floods.', 'Step 4: Locate unauthorized APs using triangulation.', 'Step 5: Isolate Rogue AP switch ports.', 'Step 6: Implement 802.11w PMF.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a1a" /><text x="300" y="200" fill="white" text-anchor="middle" font-size="20">Evil Twin Attack Flow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'aireplay-ng -0 0 -a [BSSID] wlan0mon', purpose: 'Deauth attack', out: 'Sending DeAuth', note: 'Continuous attack', mistake: 'Targeting wrong AP' }
    ],
    win: [
      { cmd: 'Get-NetAdapter | Where-Object Status -eq "Up"', purpose: 'Check adapters', out: 'Adapter list', note: 'Basic troubleshooting', mistake: 'None' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Aireplay-ng', 'Wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS needs to demonstrate how easily clients can be disconnected to justify the upgrade to equipment supporting PMF.',
    objectives: ['Execute a deauthentication attack.'],
    steps: ['Step 1: Identify target AP MAC.', 'Step 2: Run `aireplay-ng -0 10 -a <MAC> wlan0mon`.'],
    evidence: ['Wireshark capture showing deauth frames.'],
    validation: ['You should see: Clients disconnecting from the target AP.'],
    troubleshooting: ['If clients do not disconnect, they may be using 802.11w.'],
    mitre: [{ id: 'T1498', name: 'Network Denial of Service', tactic: 'Impact' }],
    cleanup: ['Stop the aireplay-ng script.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Rogue AP?', opts: ['An AP mimicking the corporate network', 'An unauthorized AP connected to the corporate LAN', 'A honeypot AP', 'A misconfigured router'], correct: 1, fb: 'A Rogue AP is physically connected to the corporate network without authorization.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is an Evil Twin?', opts: ['A malicious AP with the same SSID as a legitimate one', 'A clone of the domain controller', 'Two APs on the same channel', 'A backup AP'], correct: 0, fb: 'An Evil Twin mimics a legitimate SSID to steal credentials.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Why are deauth attacks successful against older networks?', opts: ['Encryption is weak', 'Management frames are unauthenticated', 'Passwords are short', 'IPs are static'], correct: 1, fb: 'Prior to 802.11w, management frames could be spoofed.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What standard introduces Protected Management Frames (PMF)?', opts: ['802.11a', '802.11b', '802.11g', '802.11w'], correct: 3, fb: '802.11w secures management frames.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is commonly used for Deauth attacks?', opts: ['Airodump-ng', 'Aireplay-ng', 'Airbase-ng', 'Airmon-ng'], correct: 1, fb: 'Aireplay-ng is used for packet injection, including deauth.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is the primary goal of an Evil Twin attack on an open network?', opts: ['Denial of Service', 'Intercept traffic/credentials', 'Crack WEP', 'Find hidden SSIDs'], correct: 1, fb: 'Evil Twins are used for Man-in-the-Middle attacks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What prevents Evil Twin attacks in 802.1X environments?', opts: ['Strong passwords', 'Certificate validation', 'MAC filtering', 'Hidden SSIDs'], correct: 1, fb: 'Clients validating the server certificate prevents Evil Twins.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Is MAC filtering a strong security measure?', opts: ['Yes, it prevents unauthorized access', 'No, MAC addresses are easily spoofed', 'Yes, if combined with hidden SSIDs', 'No, it slows down the network'], correct: 1, fb: 'MAC addresses are broadcast in plaintext and easily spoofed.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is a Karma attack?', opts: ['Brute forcing WPS', 'Responding to all Probe Requests', 'Jamming the RF signal', 'Cracking WPA2'], correct: 1, fb: 'Karma attacks respond to probe requests, telling the client "Yes, I am the network you are looking for."' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is Wi-Fi jamming?', opts: ['Sending Deauth frames', 'Overpowering the RF frequency with noise', 'Cracking the PSK', 'ARP poisoning'], correct: 1, fb: 'Jamming is a physical layer DoS attack using RF noise.' }
  ],
  flashcards: [
    { f: 'Evil Twin', b: 'A malicious AP designed to look like a legitimate one.' },
    { f: 'Deauth Attack', b: 'Spoofed management frames causing clients to disconnect.' }
  ],
  summary: ['Rogue APs are plugged into the LAN.', 'Evil Twins impersonate legitimate APs.', 'Deauth attacks spoof management frames.', '802.11w protects management frames.', 'WIPS is needed for enterprise defense.'],
  outcomes: ['Understand wireless attacks.', 'Differentiate Rogue APs and Evil Twins.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};

CONTENT['wireless-hacking-tools'] = {
  eyebrow: 'Module 16 · Topic 4',
  title: 'Wireless Hacking Tools',
  module: 'Phase 16: Network Security Specialist',
  sub: 'Software and hardware utilized for auditing wireless networks.',
  objectives: ['Utilize the Aircrack-ng suite', 'Understand hardware requirements (Monitor mode)', 'Identify automated exploitation frameworks'],
  learn: {
    simple: 'Auditing wireless networks requires specialized tools and hardware. The most famous software suite is Aircrack-ng, which contains tools for monitoring, packet injection, and cracking. However, software is useless without a compatible wireless adapter that supports "Monitor Mode" and "Packet Injection".',
    analogy: 'Standard Wi-Fi adapters are like people focused on their own conversation. Monitor mode adapters are like spies in a cafe, listening to every conversation in the room, and packet injection is the ability to interject into those conversations.',
    architecture: 'The Aircrack-ng suite consists of airodump-ng (for 802.11 frame capture), aireplay-ng (for frame injection), airmon-ng (for enabling monitor mode), and aircrack-ng (for cryptographic cracking). Other tools like Kismet operate as passive WIDS (Wireless Intrusion Detection Systems). Hardware tools, like the Hak5 WiFi Pineapple, automate Evil Twin and Karma attacks, making complex wireless exploitation trivial.',
    why: 'Security professionals must master these tools to identify vulnerabilities before attackers do. Understanding the capabilities of tools like the WiFi Pineapple is essential for designing defenses that thwart automated attacks.'
  },
  enterprise: {
    gfs: 'GFS security engineers use Kismet on Raspberry Pi drones to perform periodic wireless site surveys of their campus.',
    windows: 'Windows has limited native support for monitor mode; professionals typically use Linux VMs with USB passthrough.',
    linux: 'Kali Linux includes all necessary drivers and tools, making it the standard for wireless auditing.'
  },
  workflow: ['Step 1: Connect a compatible USB Wi-Fi adapter.', 'Step 2: Enable monitor mode (airmon-ng).', 'Step 3: Survey the area (airodump-ng / Kismet).', 'Step 4: Execute targeted attacks (aireplay-ng / Wifite).', 'Step 5: Capture handshakes or perform MitM.', 'Step 6: Analyze captures (Wireshark / Aircrack-ng).'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1a1a1a" /><text x="300" y="200" fill="white" text-anchor="middle" font-size="20">Aircrack-ng Workflow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'wifite', purpose: 'Automated auditing', out: 'Scanning...', note: 'Automates aircrack-ng suite', mistake: 'Running without compatible adapter' }
    ],
    win: [
      { cmd: 'inSSIDer', purpose: 'GUI spectrum analysis', out: 'Graphs', note: 'Not a native command, requires install', mistake: 'N/A' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['Wifite'],
    dependencies: [],
    safety: ['Perform this lab only in an isolated environment.'],
    scenario: 'GFS requires a rapid assessment of wireless security posture using automated tools.',
    objectives: ['Use Wifite to automate WPA2 cracking.'],
    steps: ['Step 1: Run `sudo wifite`.', 'Step 2: Select the target network.', 'Step 3: Wait for handshake capture and automated cracking.'],
    evidence: ['Terminal output showing successful crack.'],
    validation: ['You should see: Wifite successfully retrieving the PSK.'],
    troubleshooting: ['Ensure the adapter supports packet injection.'],
    mitre: [{ id: 'T1110', name: 'Brute Force', tactic: 'Credential Access' }],
    cleanup: ['Exit Wifite.']
  },
  quiz: [
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What feature must a Wi-Fi adapter have for wireless hacking?', opts: ['Dual-band support', 'Monitor mode and Packet Injection', 'USB 3.0', 'High gain antenna'], correct: 1, fb: 'Monitor mode is required to capture all traffic, and injection is needed for active attacks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is used to enable monitor mode in the Aircrack suite?', opts: ['Airodump-ng', 'Aireplay-ng', 'Airmon-ng', 'Airbase-ng'], correct: 2, fb: 'Airmon-ng starts monitor mode on interfaces.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What is Kismet primarily used for?', opts: ['Cracking WPA2', 'Passive sniffing and WIDS', 'Deauth attacks', 'Creating Rogue APs'], correct: 1, fb: 'Kismet is a passive sniffer and intrusion detection system.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does Aireplay-ng do?', opts: ['Packet injection', 'Packet capture', 'Password cracking', 'Spectrum analysis'], correct: 0, fb: 'Aireplay-ng is used for injecting frames (like deauths).' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which hardware device is famous for automating Evil Twin attacks?', opts: ['Rubber Ducky', 'WiFi Pineapple', 'LAN Turtle', 'Bash Bunny'], correct: 1, fb: 'Hak5 WiFi Pineapple specializes in rogue AP attacks.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does Wifite do?', opts: ['It is a GUI for Wireshark', 'It automates the Aircrack-ng suite', 'It is a hardware antenna', 'It cracks WPA3 offline'], correct: 1, fb: 'Wifite is a script that automates aircrack, reaver, etc.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which tool is used to crack WPA2 handshakes?', opts: ['Airodump-ng', 'Aircrack-ng', 'Airmon-ng', 'Aireplay-ng'], correct: 1, fb: 'Aircrack-ng performs the cryptographic cracking.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What does Reaver target?', opts: ['WPA2 Handshakes', 'WPS PINs', 'WEP IVs', 'Captive Portals'], correct: 1, fb: 'Reaver is designed to brute-force WPS PINs.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'Which OS is best suited for wireless auditing?', opts: ['Windows 10', 'macOS', 'Kali Linux', 'ChromeOS'], correct: 2, fb: 'Kali Linux has built-in drivers and tools for wireless auditing.' },
    { type: 'multiple-choice', difficulty: 'Intermediate', q: 'What command kills interfering processes before using airmon-ng?', opts: ['airmon-ng kill', 'airmon-ng check kill', 'killall network', 'service network-manager stop'], correct: 1, fb: 'airmon-ng check kill stops processes like wpa_supplicant that interfere with monitor mode.' }
  ],
  flashcards: [
    { f: 'Monitor Mode', b: 'Allows an adapter to capture all wireless traffic in the air, regardless of destination.' },
    { f: 'WiFi Pineapple', b: 'A hardware tool designed to automate wireless attacks like Evil Twins.' }
  ],
  summary: ['Hardware must support monitor mode.', 'Aircrack-ng is the standard suite.', 'Kismet is for passive sniffing.', 'Wifite automates attacks.', 'Hardware like the Pineapple simplifies Evil Twins.'],
  outcomes: ['Identify wireless hacking tools.', 'Understand monitor mode and packet injection.'],
  meta: { contentVersion: "1.0.0", estimatedTime: 45, difficulty: "Intermediate", prerequisites: [], lastReviewed: "2026-07-18" }
};
"""

try:
    with open(html_path, 'r', encoding='utf-8') as f:
        html_data = f.read()

    target_str = "// ── TAB WIRING ──"
    if target_str in html_data:
        new_html = html_data.replace(target_str, m16_data + "\\n" + target_str)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Injected successfully.")
    else:
        print("Target string not found in index.html")
except Exception as e:
    print(f"Error: {e}")
