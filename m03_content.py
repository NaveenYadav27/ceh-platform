import os
import re

CONTENT_PAYLOAD = """
CONTENT['network-scanning-overview'] = {
  eyebrow: 'Module 03 · Topic 1',
  title: 'Network Scanning Overview',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Understanding the fundamentals of network scanning in the CEH methodology.',
  objectives: ['Understand the purpose of network scanning', 'Identify scanning methodologies', 'Understand CEH methodology phase 2'],
  learn: {
    simple: 'Network scanning is the process of identifying active hosts, open ports, and services running on a target network. It is the second phase of the CEH methodology, following footprinting and reconnaissance.',
    analogy: 'Imagine a security guard walking through a building, checking which doors are unlocked and noting what type of locks are on them.',
    architecture: 'Scanning involves sending specially crafted packets to a target and analyzing the responses. This can reveal the network topology, live hosts, open ports, and underlying operating systems. It forms the basis for vulnerability assessment.',
    why: 'In enterprise environments, scanning helps security teams maintain visibility over their assets, identify unauthorized devices, and detect potential vulnerabilities before attackers do.'
  },
  enterprise: {
    gfs: 'Global Financial Services regularly scans its internal network to ensure no unauthorized devices have connected to the trading floor VLAN.',
    windows: 'Using native tools or third-party scanners to identify Active Directory domain controllers and file servers.',
    linux: 'Using Nmap or similar tools to map out internal segments and identify SSH or web servers.'
  },
  workflow: ['Step 1: Define the scope of the scan.', 'Step 2: Perform host discovery.', 'Step 3: Perform port scanning.', 'Step 4: Perform service version detection.', 'Step 5: Perform OS fingerprinting.', 'Step 6: Document findings.'],
  diagram: {
    caption: 'Click to interact with the diagram',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="20">Network Scanning Overview</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'ping -c 4 target', purpose: 'Check host availability', out: 'ICMP echo replies', note: 'Basic host discovery', mistake: 'Ping can be blocked by firewalls' }
    ],
    win: [
      { cmd: 'ping target', purpose: 'Check host availability', out: 'ICMP echo replies', note: 'Basic host discovery', mistake: 'Ping can be blocked by firewalls' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['ping', 'arp-scan'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS needs to map the active IP addresses in a newly acquired subsidiary subnet.',
    objectives: ['Identify live hosts on the network'],
    steps: ['Step 1: Use ping to check a specific host.', 'Step 2: Use arp-scan to discover local hosts.'],
    evidence: ['Terminal output showing discovered IP addresses.'],
    validation: ['You should see: list of active IP and MAC addresses'],
    troubleshooting: ['If no hosts are found, ensure you are on the correct subnet.'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['Remove any temporary files.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which phase of the CEH methodology does network scanning fall under?',
      opts: ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'],
      correct: 1,
      fb: 'Network scanning is the second phase, following footprinting and reconnaissance.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary goal of network scanning?',
      opts: ['Gaining access', 'Covering tracks', 'Identifying active hosts and services', 'Deploying malware'],
      correct: 2,
      fb: 'The primary goal is to map the network and find active hosts and open ports.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is NOT a typical step in network scanning?',
      opts: ['Host discovery', 'Port scanning', 'Privilege escalation', 'OS fingerprinting'],
      correct: 2,
      fb: 'Privilege escalation is part of the gaining access phase, not scanning.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'True or False: ICMP ping requests are always reliable for host discovery.',
      opts: ['True', 'False', 'Sometimes', 'Only on local networks'],
      correct: 1,
      fb: 'False. Firewalls often block ICMP, making ping unreliable.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What type of scanning is used to identify the operating system of a target?',
      opts: ['Port scanning', 'OS fingerprinting', 'Vulnerability scanning', 'Service detection'],
      correct: 1,
      fb: 'OS fingerprinting uses TCP/IP stack behavior to guess the OS.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which protocol is most commonly used for basic host discovery?',
      opts: ['HTTP', 'FTP', 'ICMP', 'SMTP'],
      correct: 2,
      fb: 'ICMP (specifically Echo Request/Reply) is commonly used for pinging hosts.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why do attackers scan networks?',
      opts: ['To improve performance', 'To identify entry points', 'To configure routers', 'To update software'],
      correct: 1,
      fb: 'Attackers scan to find vulnerabilities and entry points into the network.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does a port state of "filtered" mean in Nmap?',
      opts: ['The port is open', 'The port is closed', 'A firewall is blocking the probe', 'The service is down'],
      correct: 2,
      fb: '"Filtered" means Nmap cannot determine if the port is open or closed because packet filtering prevents its probes from reaching the port.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following is a network scanning tool?',
      opts: ['Wireshark', 'Nmap', 'Burp Suite', 'Metasploit'],
      correct: 1,
      fb: 'Nmap is a premier network scanning and discovery tool.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the purpose of service version detection?',
      opts: ['To find the OS', 'To determine the application and version running on an open port', 'To discover hidden hosts', 'To bypass firewalls'],
      correct: 1,
      fb: 'Service version detection identifies the exact software and version running on a port, which is crucial for finding specific vulnerabilities.'
    }
  ],
  flashcards: [
    { f: 'Host Discovery', b: 'The process of identifying live systems on a network.' },
    { f: 'Port Scanning', b: 'Probing a server or host for open ports.' }
  ],
  summary: ['Scanning is Phase 2 of CEH.', 'It identifies live hosts.', 'It finds open ports.', 'It detects service versions.', 'It fingerprints operating systems.'],
  outcomes: ['Explain network scanning concepts.', 'Identify scanning phases.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['tcp-ip-scanning'] = {
  eyebrow: 'Module 03 · Topic 2',
  title: 'TCP/IP Scanning Fundamentals',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Deep dive into TCP 3-way handshake, TCP flags, Connect vs SYN scans.',
  objectives: ['Understand the TCP 3-way handshake', 'Differentiate between TCP flags', 'Compare Connect and SYN scans'],
  learn: {
    simple: 'TCP/IP scanning relies on the underlying mechanics of the TCP protocol. By manipulating TCP flags (SYN, ACK, RST, FIN, etc.), scanners can determine port states without necessarily completing a full connection.',
    analogy: 'It is like calling someone on the phone. A Connect scan is letting it ring and saying "hello". A SYN scan is letting it ring, hearing them pick up, and then immediately hanging up.',
    architecture: 'The TCP 3-way handshake (SYN, SYN-ACK, ACK) is foundational. A Connect scan uses the OS system call to complete this handshake. A SYN scan (half-open) sends a SYN, waits for a SYN-ACK, and sends an RST to tear down the connection before it is fully established, often bypassing basic logging.',
    why: 'Understanding these mechanics is critical for security professionals to interpret scan results, troubleshoot network issues, and detect stealthy scanning attempts.'
  },
  enterprise: {
    gfs: 'GFS SOC analysts monitor for SYN scan patterns to detect potential internal reconnaissance by compromised endpoints.',
    windows: 'Windows firewalls can be configured to block or log incomplete TCP handshakes.',
    linux: 'Linux iptables/nftables can rate-limit SYN packets to mitigate SYN floods and aggressive scanning.'
  },
  workflow: ['Step 1: Understand TCP flags.', 'Step 2: Initiate a Connect scan.', 'Step 3: Analyze Connect scan traffic.', 'Step 4: Initiate a SYN scan.', 'Step 5: Analyze SYN scan traffic.', 'Step 6: Compare stealth capabilities.'],
  diagram: {
    caption: 'TCP 3-Way Handshake',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="20">TCP Handshake Diagram</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -sT target', purpose: 'TCP Connect scan', out: 'Open ports', note: 'Completes full handshake', mistake: 'Highly visible in logs' },
      { cmd: 'nmap -sS target', purpose: 'TCP SYN scan', out: 'Open ports', note: 'Requires root privileges', mistake: 'Running as non-root defaults to Connect scan' }
    ],
    win: [
      { cmd: 'Test-NetConnection -Port 80 target', purpose: 'TCP Connect check', out: 'TcpTestSucceeded', note: 'Native PowerShell', mistake: 'Cannot perform SYN scans natively' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['nmap', 'wireshark'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS wants to demonstrate why full connect scans are easily detected by their IDS compared to SYN scans.',
    objectives: ['Perform and analyze Connect and SYN scans'],
    steps: ['Step 1: Start Wireshark.', 'Step 2: Run nmap -sT.', 'Step 3: Run nmap -sS.', 'Step 4: Compare packet captures.'],
    evidence: ['Wireshark captures showing full handshake vs RST teardown.'],
    validation: ['You should see: RST packets sent by the scanner in the SYN scan.'],
    troubleshooting: ['If SYN scan fails, ensure you are running nmap with sudo.'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['Stop packet captures and close Wireshark.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which flags are involved in the TCP 3-way handshake?',
      opts: ['SYN, ACK, FIN', 'SYN, SYN-ACK, ACK', 'SYN, PSH, ACK', 'ACK, RST, FIN'],
      correct: 1,
      fb: 'The standard handshake is SYN, SYN-ACK, ACK.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is another name for a TCP SYN scan?',
      opts: ['Full Connect Scan', 'Half-open Scan', 'Xmas Scan', 'Null Scan'],
      correct: 1,
      fb: 'It is called half-open because it never completes the final ACK of the handshake.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why does a SYN scan require root/administrator privileges?',
      opts: ['To run faster', 'To bypass the OS network stack and craft raw packets', 'To write to log files', 'To access the firewall'],
      correct: 1,
      fb: 'Creating raw packets (sending a SYN and then a RST instead of an ACK) requires raw socket access, which needs root.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'If a port is closed, what response is sent to a SYN packet?',
      opts: ['SYN-ACK', 'ACK', 'RST', 'No response'],
      correct: 2,
      fb: 'A closed port responds with an RST (Reset) packet.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which scan type is more likely to be logged by the target application?',
      opts: ['SYN Scan', 'Connect Scan', 'FIN Scan', 'Null Scan'],
      correct: 1,
      fb: 'Connect scans complete the handshake, so the OS passes the connection to the application, which likely logs it.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does the RST flag indicate?',
      opts: ['Acknowledge data', 'Synchronize sequence numbers', 'Reset the connection', 'Finish connection'],
      correct: 2,
      fb: 'RST stands for Reset, used to abruptly close a connection or indicate a closed port.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'In a SYN scan against an open port, what does the scanner send after receiving a SYN-ACK?',
      opts: ['ACK', 'FIN', 'RST', 'PSH'],
      correct: 2,
      fb: 'The scanner sends an RST to tear down the half-open connection.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which nmap flag initiates a Connect scan?',
      opts: ['-sS', '-sT', '-sU', '-sN'],
      correct: 1,
      fb: '-sT is the flag for a TCP Connect scan.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What happens if a SYN scan is sent to a filtered port?',
      opts: ['Receives SYN-ACK', 'Receives RST', 'Receives no response or ICMP error', 'Receives FIN'],
      correct: 2,
      fb: 'Firewalls usually drop the packet silently (no response) or send an ICMP unreachable error.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'True or False: SYN scans are completely undetectable by modern IDS/IPS systems.',
      opts: ['True', 'False', 'Only on Linux', 'Only on Windows'],
      correct: 1,
      fb: 'False. Modern IDS/IPS can easily detect the pattern of SYN packets sent to multiple ports.'
    }
  ],
  flashcards: [
    { f: 'SYN Scan', b: 'Half-open scan that does not complete the 3-way handshake.' },
    { f: 'Connect Scan', b: 'Full scan that completes the TCP handshake.' }
  ],
  summary: ['TCP handshake is SYN, SYN-ACK, ACK.', 'Connect scan completes handshake.', 'SYN scan is half-open (sends RST).', 'SYN scans need root.', 'Connect scans are highly visible.'],
  outcomes: ['Explain TCP handshake.', 'Differentiate scan types.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['nmap-techniques'] = {
  eyebrow: 'Module 03 · Topic 3',
  title: 'Advanced Nmap Techniques',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Mastering Nmap usage, timing templates, and the Nmap Scripting Engine (NSE).',
  objectives: ['Master Nmap timing and performance options', 'Utilize NSE scripts for advanced enumeration', 'Optimize Nmap scans for different environments'],
  learn: {
    simple: 'Nmap is a powerful network scanner. Beyond basic port scanning, it offers timing templates to control scan speed (stealth vs. speed) and the Nmap Scripting Engine (NSE) to automate vulnerability detection and advanced enumeration.',
    analogy: 'Timing templates are like driving a car: T0 is creeping along to avoid radar, T5 is a high-speed chase. NSE scripts are like giving the driver specific tasks, like "check if this door has a specific known vulnerability."',
    architecture: 'Nmap timing templates (-T0 to -T5) adjust timeouts, packet rates, and retry counts. NSE uses Lua scripts categorized into domains (e.g., default, vuln, safe, intrusive) to interact with discovered services, pulling banners, testing for default credentials, or checking for CVEs.',
    why: 'Security engineers need to balance scan speed with network impact and stealth. NSE transforms Nmap from a simple port scanner into a versatile vulnerability assessment tool.'
  },
  enterprise: {
    gfs: 'GFS vulnerability management team uses customized Nmap NSE scripts to rapidly audit the entire infrastructure for newly announced critical CVEs.',
    windows: 'Using NSE scripts like smb-os-discovery to enumerate Windows domains without full credentials.',
    linux: 'Using T4 timing for fast internal subnet sweeps during incident response.'
  },
  workflow: ['Step 1: Select timing template (-T).', 'Step 2: Specify target and port range.', 'Step 3: Enable OS and service detection (-A).', 'Step 4: Select NSE categories (--script).', 'Step 5: Run the scan.', 'Step 6: Analyze the NSE output.'],
  diagram: {
    caption: 'Nmap Scan Flow',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="20">Nmap Timing & NSE</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nmap -T4 -A target', purpose: 'Aggressive, fast scan', out: 'OS, services, traceroute', note: 'Noisy on the network', mistake: 'Can cause network congestion' },
      { cmd: 'nmap --script vuln target', purpose: 'Run vulnerability scripts', out: 'List of CVEs/vulns', note: 'Can be intrusive', mistake: 'Running intrusive scripts in production without approval' }
    ],
    win: [
      { cmd: 'nmap -T4 -A target', purpose: 'Aggressive, fast scan', out: 'OS, services', note: 'Requires Nmap installed on Windows', mistake: 'Windows firewall might block raw sockets' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '60',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['nmap'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment. NSE vuln scripts can crash services.'],
    scenario: 'GFS suspects an internal file server is vulnerable to MS17-010 (EternalBlue) and needs confirmation.',
    objectives: ['Use NSE to detect specific vulnerabilities'],
    steps: ['Step 1: Run nmap with --script smb-vuln-ms17-010.', 'Step 2: Analyze the script output.', 'Step 3: Compare T2 vs T4 scan durations.'],
    evidence: ['Nmap output showing the vulnerability status.'],
    validation: ['You should see: State: VULNERABLE or NOT VULNERABLE'],
    troubleshooting: ['If script fails, ensure Nmap scripts are updated (nmap --script-updatedb).'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['None.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which Nmap timing template is known as "Insane"?',
      opts: ['T3', 'T4', 'T5', 'T6'],
      correct: 2,
      fb: 'T5 is the Insane template, prioritizing speed over accuracy and stealth.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What programming language is used for Nmap Scripting Engine (NSE) scripts?',
      opts: ['Python', 'Ruby', 'Lua', 'Bash'],
      correct: 2,
      fb: 'NSE scripts are written in Lua.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which Nmap flag is a shortcut for enabling OS detection, version detection, script scanning, and traceroute?',
      opts: ['-sV', '-O', '-A', '-sC'],
      correct: 2,
      fb: '-A enables aggressive scanning options.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What does the Nmap flag -sC do?',
      opts: ['SYN scan', 'Script scanning using default scripts', 'Service version detection', 'UDP scan'],
      correct: 1,
      fb: '-sC is equivalent to --script=default.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which timing template is recommended for normal, everyday scanning?',
      opts: ['T2', 'T3', 'T4', 'T5'],
      correct: 1,
      fb: 'T3 is the normal default timing template.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'If you want to evade an IDS by scanning very slowly, which timing template is best?',
      opts: ['T0', 'T2', 'T4', 'T5'],
      correct: 0,
      fb: 'T0 (Paranoid) serializes the scan and waits a long time between packets.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'How do you run all scripts in the "vuln" category against a target?',
      opts: ['nmap -sV vuln target', 'nmap --script vuln target', 'nmap -script-vuln target', 'nmap -A vuln target'],
      correct: 1,
      fb: '--script vuln runs all scripts categorized as vulnerabilities.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'True or False: All NSE scripts are safe to run against production systems.',
      opts: ['True', 'False', 'Only default scripts', 'Only safe scripts'],
      correct: 1,
      fb: 'False. Many scripts (like DoS or intrusive exploit scripts) can crash systems.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the purpose of Nmap version detection (-sV)?',
      opts: ['Find open ports', 'Identify the specific software version running on a port', 'Identify the OS', 'Bypass firewalls'],
      correct: 1,
      fb: 'Version detection queries the service to determine the exact software and version.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which NSE category should be avoided during a stealthy reconnaissance phase?',
      opts: ['safe', 'discovery', 'intrusive', 'version'],
      correct: 2,
      fb: 'Intrusive scripts are noisy and can potentially alter or crash target systems.'
    }
  ],
  flashcards: [
    { f: 'NSE', b: 'Nmap Scripting Engine, uses Lua to automate networking tasks.' },
    { f: 'Timing T5', b: 'Insane timing, very fast but inaccurate and noisy.' }
  ],
  summary: ['Timing templates range from T0 to T5.', 'NSE uses Lua scripts.', '-A enables OS, version, script, and traceroute.', 'Categories include safe, vuln, intrusive.', 'Scripts automate advanced enumeration.'],
  outcomes: ['Use Nmap timing templates.', 'Execute NSE scripts.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['hping3-scanning'] = {
  eyebrow: 'Module 03 · Topic 4',
  title: 'Hping3 and Packet Crafting',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Custom packet crafting, firewall evasion, and ACK scans using Hping3.',
  objectives: ['Craft custom TCP/IP packets', 'Perform ACK scans for firewall testing', 'Understand firewall evasion techniques'],
  learn: {
    simple: 'Hping3 is a command-line packet assembler and analyzer. Unlike Nmap, which relies on predefined scan types, Hping3 allows you to manually craft every aspect of a packet (flags, window size, fragmentation) to bypass firewalls and test network defenses.',
    analogy: 'If Nmap is an automated Swiss Army knife, Hping3 is a raw set of lockpicks, allowing you to manipulate the pins manually to bypass complex locks.',
    architecture: 'Hping3 can send custom ICMP, UDP, and TCP packets. By setting specific flags (like only the ACK flag), it can test stateless firewalls to see if they allow traffic through based on the assumption that it belongs to an established connection. Packet fragmentation can also be used to evade IDS signatures.',
    why: 'Advanced penetration testing and firewall auditing require the ability to craft arbitrary packets to test edge cases and evasion capabilities that standard scanners might miss.'
  },
  enterprise: {
    gfs: 'GFS security engineers use Hping3 to validate the rule sets on their new perimeter firewalls, ensuring they correctly drop out-of-state ACK packets.',
    windows: 'While Hping3 is primarily Linux-based, similar crafting can be done with PowerShell or third-party tools, though less natively.',
    linux: 'Hping3 is a staple on Linux for low-level network troubleshooting and firewall testing.'
  },
  workflow: ['Step 1: Identify target firewall/host.', 'Step 2: Craft an ACK packet.', 'Step 3: Analyze the response (RST vs No Response).', 'Step 4: Craft a fragmented packet.', 'Step 5: Send traffic to target.', 'Step 6: Evaluate evasion success.'],
  diagram: {
    caption: 'Packet Crafting with Hping3',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="20">Hping3 Packet Flow</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'hping3 -A target -p 80', purpose: 'ACK scan', out: 'RST or Drop', note: 'Tests firewall statefulness', mistake: 'Requires root' },
      { cmd: 'hping3 -S -f target -p 80', purpose: 'Fragmented SYN scan', out: 'Responses', note: 'Evades simple IDS', mistake: 'Modern firewalls reassemble packets' }
    ],
    win: [
      { cmd: 'N/A', purpose: 'Packet crafting', out: 'N/A', note: 'Use Kali WSL or VMs', mistake: 'Native Windows lacks raw socket crafting tools out of the box' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Advanced',
    duration: '45',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['hping3', 'tcpdump'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment. Sending malformed packets can disrupt networks.'],
    scenario: 'GFS needs to verify if their legacy router is performing stateful inspection or just stateless packet filtering.',
    objectives: ['Perform an ACK scan using Hping3'],
    steps: ['Step 1: Run an ACK scan against the target.', 'Step 2: Observe if an RST is returned.', 'Step 3: Conclude firewall type.'],
    evidence: ['Hping3 output showing RST replies.'],
    validation: ['You should see: RST packets indicating the port is unfiltered (stateless firewall).'],
    troubleshooting: ['Ensure target IP is correct and responsive to ping.'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['None.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'What is the primary use case for an ACK scan?',
      opts: ['To find open ports', 'To map firewall rules and determine if it is stateful', 'To discover OS version', 'To launch a DoS attack'],
      correct: 1,
      fb: 'ACK scans do not find open ports; they determine if ports are filtered by a stateful firewall.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'If you send an ACK packet to a port and receive an RST back, what does this indicate?',
      opts: ['The port is open', 'The port is closed', 'The port is unfiltered (no stateful firewall blocking it)', 'The port is filtered'],
      correct: 2,
      fb: 'An RST response to an ACK means the packet reached the target, so no firewall blocked it (unfiltered).'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which hping3 flag sets the TCP SYN flag?',
      opts: ['-A', '-S', '-F', '-R'],
      correct: 1,
      fb: '-S sets the SYN flag.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'How does packet fragmentation (-f in hping3) help evade IDS?',
      opts: ['It makes the packets move faster', 'It splits the packet header and payload, making signature matching harder', 'It changes the IP address', 'It encrypts the payload'],
      correct: 1,
      fb: 'Fragmentation splits the packet into smaller pieces, which older IDS might not reassemble before inspecting for signatures.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which tool is better suited for scanning an entire subnet for open ports?',
      opts: ['Hping3', 'Nmap', 'Ping', 'Traceroute'],
      correct: 1,
      fb: 'While Hping3 can scan, Nmap is highly optimized for subnet scanning and service detection.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'What type of packet does Hping3 send by default if no protocol is specified?',
      opts: ['ICMP', 'UDP', 'TCP', 'IGMP'],
      correct: 2,
      fb: 'Hping3 defaults to sending TCP packets to port 0.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Why does Hping3 require root privileges?',
      opts: ['To read files', 'To use raw sockets for crafting custom packets', 'To bypass the local firewall', 'To run scripts'],
      correct: 1,
      fb: 'Creating packets from scratch (raw sockets) requires root access.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'If an ACK scan receives no response, what is the port state?',
      opts: ['Open', 'Closed', 'Filtered', 'Unfiltered'],
      correct: 2,
      fb: 'No response indicates a firewall dropped the packet, meaning the port is filtered.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Which hping3 command spoofs the source IP address?',
      opts: ['-a [IP]', '-S [IP]', '-spoof [IP]', '--source [IP]'],
      correct: 0,
      fb: '-a is used to spoof the source IP address in Hping3.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Advanced',
      q: 'Can Hping3 be used for ICMP flooding?',
      opts: ['Yes', 'No', 'Only on local network', 'Only against Windows'],
      correct: 0,
      fb: 'Yes, using the -1 (ICMP) and --flood options, it can perform an ICMP flood.'
    }
  ],
  flashcards: [
    { f: 'ACK Scan', b: 'Used to determine firewall rulesets, not open ports.' },
    { f: 'Fragmentation', b: 'Splitting packets to evade IDS signature matching.' }
  ],
  summary: ['Hping3 crafts custom packets.', 'ACK scans test firewall statefulness.', 'RST response to ACK = unfiltered.', 'Fragmentation evades older IDS.', 'Spoofing source IP is possible with Hping3.'],
  outcomes: ['Craft packets with Hping3.', 'Understand firewall evasion.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Advanced",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};

CONTENT['banner-grabbing'] = {
  eyebrow: 'Module 03 · Topic 5',
  title: 'Banner Grabbing & OS Fingerprinting',
  module: 'Phase 02: Threat Intelligence Analyst',
  sub: 'Techniques for OS fingerprinting, active vs passive grabbing, telnet/nc usage.',
  objectives: ['Perform active banner grabbing', 'Understand passive OS fingerprinting', 'Utilize telnet and netcat for interaction'],
  learn: {
    simple: 'Banner grabbing is the process of collecting information about a networked system, specifically the software type and version running on open ports. OS fingerprinting goes a step further to determine the target operating system.',
    analogy: 'Banner grabbing is like knocking on a door and asking "Who are you?", and they reply "I am Apache web server version 2.4." OS fingerprinting is analyzing their accent and behavior to realize they are from Linux.',
    architecture: 'Active banner grabbing involves sending requests (like an HTTP GET or connecting via Telnet/Netcat) and reading the response banner. Active OS fingerprinting sends malformed packets and analyzes TCP/IP stack anomalies to guess the OS. Passive fingerprinting analyzes normal traffic (e.g., using Wireshark) without sending probes, relying on default TTLs or Window sizes.',
    why: 'Identifying specific software versions and OS types is crucial for vulnerability mapping. If an attacker knows you run IIS 6.0, they know exactly which exploits to use.'
  },
  enterprise: {
    gfs: 'GFS implements strict egress filtering and modifies default server banners to prevent automated scanners from easily identifying their internal tech stack.',
    windows: 'Windows Server admins often disable or spoof IIS banners to mitigate reconnaissance.',
    linux: 'Linux admins configure Apache/Nginx to return generic headers (Server: Apache) instead of full version numbers.'
  },
  workflow: ['Step 1: Identify open ports.', 'Step 2: Connect using Netcat/Telnet.', 'Step 3: Send an interaction trigger (e.g., HEAD / HTTP/1.0).', 'Step 4: Record the returned banner.', 'Step 5: Perform passive capture (Wireshark).', 'Step 6: Analyze TTLs for OS guessing.'],
  diagram: {
    caption: 'Banner Grabbing Process',
    svg: '<svg viewBox="0 0 600 400" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#eee"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="20">Banner Grabbing</text></svg>'
  },
  commands: {
    lin: [
      { cmd: 'nc -nv target 80', purpose: 'Netcat banner grab', out: 'HTTP Banner', note: 'Press Enter or type GET / HTTP/1.0', mistake: 'Connection times out if no input is sent to some services' }
    ],
    win: [
      { cmd: 'telnet target 80', purpose: 'Telnet banner grab', out: 'HTTP Banner', note: 'Telnet client must be installed on Windows', mistake: 'Telnet sends data in plaintext' }
    ]
  },
  lab: {
    type: 'guided',
    difficulty: 'Intermediate',
    duration: '30',
    platform: 'Kali Linux',
    environment: 'Local Lab',
    tools: ['netcat', 'telnet', 'nmap'],
    dependencies: [],
    safety: ['Perform this lab only in an authorized environment.'],
    scenario: 'GFS needs to audit internal web servers to ensure they are not leaking precise version information in their HTTP headers.',
    objectives: ['Perform active banner grabbing on an HTTP server'],
    steps: ['Step 1: Use nc to connect to port 80.', 'Step 2: Type HEAD / HTTP/1.0 and press Enter twice.', 'Step 3: Analyze the Server header.'],
    evidence: ['Terminal output showing the Server banner.'],
    validation: ['You should see: Server: Apache/2.4.41 (Ubuntu)'],
    troubleshooting: ['If connection closes immediately, try sending the HTTP request faster.'],
    mitre: [{ id: 'T1046', name: 'Network Service Discovery', tactic: 'Discovery' }],
    cleanup: ['None.']
  },
  quiz: [
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is the primary goal of banner grabbing?',
      opts: ['To crash the service', 'To identify the software and version running on a port', 'To open a backdoor', 'To encrypt traffic'],
      correct: 1,
      fb: 'Banner grabbing captures the welcome message or header that reveals software details.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which tool is commonly used for manual banner grabbing?',
      opts: ['Ping', 'Traceroute', 'Netcat', 'Arp'],
      correct: 2,
      fb: 'Netcat (nc) is the "Swiss army knife" of networking and easily connects to ports for banner grabbing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is passive OS fingerprinting?',
      opts: ['Sending malformed packets to see the response', 'Analyzing network traffic without sending any probes', 'Using Nmap with the -O flag', 'Calling the system admin to ask'],
      correct: 1,
      fb: 'Passive fingerprinting relies on analyzing captured traffic (like TTL and Window sizes) without interacting directly.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which of the following default TTL values strongly suggests a Windows OS?',
      opts: ['64', '128', '255', '32'],
      correct: 1,
      fb: 'Windows typically uses a default TTL of 128.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What HTTP method is commonly used in banner grabbing to get headers without downloading the full page?',
      opts: ['GET', 'POST', 'HEAD', 'PUT'],
      correct: 2,
      fb: 'HEAD requests only the headers, not the body, making it ideal and stealthy for banner grabbing.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Why do organizations suppress or alter server banners?',
      opts: ['To speed up the network', 'To hide version information from potential attackers', 'To save disk space', 'To comply with DNS protocols'],
      correct: 1,
      fb: 'Security through obscurity; hiding the version makes it harder for attackers to find specific exploits.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'Which Nmap flag is used for active OS fingerprinting?',
      opts: ['-sV', '-O', '-sS', '-p'],
      correct: 1,
      fb: '-O directs Nmap to perform active OS fingerprinting.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'True or False: Banner grabbing always reveals the true software and version.',
      opts: ['True', 'False', 'Only on Linux', 'Only on Windows'],
      correct: 1,
      fb: 'False. Administrators can easily spoof or modify banners to deceive attackers.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What is a common limitation of passive OS fingerprinting?',
      opts: ['It crashes the target', 'It is very noisy and easily detected', 'It requires capturing existing traffic, which may not be present', 'It requires root access'],
      correct: 2,
      fb: 'Passive fingerprinting relies on observing traffic; if the host is quiet, you get no information.'
    },
    {
      type: 'multiple-choice',
      difficulty: 'Intermediate',
      q: 'What default TTL value is most commonly associated with Linux systems?',
      opts: ['64', '128', '255', '256'],
      correct: 0,
      fb: 'Linux systems generally use a default TTL of 64.'
    }
  ],
  flashcards: [
    { f: 'Active Fingerprinting', b: 'Sending probes to analyze target responses.' },
    { f: 'TTL 128', b: 'Default Time To Live typical of Windows operating systems.' }
  ],
  summary: ['Banner grabbing identifies software versions.', 'Active fingerprinting sends probes.', 'Passive fingerprinting analyzes existing traffic.', 'TTL values (128 for Win, 64 for Linux) help identify OS.', 'Admins should mask banners.'],
  outcomes: ['Perform banner grabbing.', 'Differentiate active vs passive fingerprinting.'],
  meta: {
    contentVersion: "1.0.0",
    estimatedTime: 45,
    difficulty: "Intermediate",
    prerequisites: [],
    lastReviewed: "2026-07-18"
  }
};
"""

target_file = r"C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html"

with open(target_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Insert the payload before // ── TAB WIRING ──
if '// ── TAB WIRING ──' in html_content:
    new_html = html_content.replace('// ── TAB WIRING ──', CONTENT_PAYLOAD + '\n// ── TAB WIRING ──')
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated frontend/index.html")
else:
    print("Could not find '// ── TAB WIRING ──' in frontend/index.html")
