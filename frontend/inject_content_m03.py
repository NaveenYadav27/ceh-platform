"""
CEH Platform — Content Injection Script
Fills in all tab content for:
- Module 03 Full (5 topics, all 8 tabs)
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

html_path = r'C:\Users\navee\OneDrive\Desktop\Greatcoder\CEHv13\ceh-platform\frontend\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

INJECT_BEFORE = '// ==========================================================\n// AUTO-STUB GENERATOR'

ok = []
fail = []

MODULE03_CONTENT = """
// =================================================================
// MODULE 03 — Scanning Networks
// =================================================================

CONTENT['network-scanning-overview'] = {
  module:'Module 03 \u00b7 Scanning Networks',
  title:'Network Scanning Concepts',
  sub:'Moving from passive reconnaissance to active probing.',
  killchain:{phase:'Scanning',mitre:'TA0046 \u2014 Discovery',desc:'Scanning is the first time the attacker directly touches the target network, generating traffic that can be detected by defensive systems.'},
  learn:{
    simple:'Network scanning is the process of actively sending packets to a target network to discover live hosts, open ports, and running services. It transitions from the "detective work" of footprinting to "testing the door handles".',
    analogy:'If footprinting is reading the blueprints of a building, scanning is walking through the hallways, knocking on every door to see which ones are unlocked, and asking the people inside who they are.',
    why:'Footprinting only tells you what the target owns. Scanning tells you what is actually turned on, exposed to the internet, and potentially vulnerable. Without scanning, you cannot identify specific services to exploit.',
    architecture:'Scanning involves three distinct steps: 1. Host Discovery (is the IP alive? e.g., Ping Sweep), 2. Port Scanning (what ports are open on the live host? e.g., TCP SYN Scan), 3. Service Versioning/OS Fingerprinting (what software is running on the open port?).'
  },
  diagram:{
    title:'The Scanning Methodology Lifecycle',
    steps:[
      {icon:'\U0001f4e1',label:'1. Check for Live Systems',desc:'Host discovery using ICMP ping sweeps, ARP pings (local), or TCP ACK probes to see which IP addresses are active.'},
      {icon:'\U0001f6aa',label:'2. Check for Open Ports',desc:'Port scanning (Nmap) on live hosts to identify open TCP/UDP ports.'},
      {icon:'\U0001f4c4',label:'3. Identify Services',desc:'Banner grabbing and service version detection to determine what application (e.g., Apache 2.4, OpenSSH 7.2) is running on the open ports.'},
      {icon:'\U0001f5fa\ufe0f',label:'4. Identify OS',desc:'OS Fingerprinting by analyzing the TCP/IP stack response to determine if the host is Windows, Linux, network gear, etc.'},
      {icon:'\U0001f50d',label:'5. Vulnerability Scan',desc:'Using tools like Nessus or OpenVAS to check identified services against known vulnerabilities (CVEs).'},
      {icon:'\U0001f9e9',label:'6. Map Network',desc:'Drawing a network topology map based on traceroute and discovered hosts/routers.'}
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
    {icon:'\u26a0\ufe0f',title:'Scanning Before Footprinting',desc:'Running Nmap before performing OSINT is a rookie mistake. It instantly alerts the target\'s SOC and burns your IP address.',fix:'Always exhaust passive footprinting before sending a single packet to the target. Active scanning should be highly targeted based on footprinting results.'},
    {icon:'\U0001f534',title:'Assuming Un-Pingable Means Dead',desc:'Many firewalls block ICMP Echo Requests (ping). If a ping sweep shows a host is down, students often assume there is no server there.',fix:'Never rely solely on ICMP for host discovery. Use TCP ACK ping (nmap -PA) or TCP SYN ping (nmap -PS) to bypass firewalls that block ICMP.'},
    {icon:'\u26d4',title:'Scanning Fragile Systems Aggressively',desc:'Running intense, full-port vulnerability scans against IoT devices, medical equipment, or SCADA systems can cause them to crash or reboot, disrupting business operations.',fix:'Identify fragile systems early. Exclude them from automated scanning or use highly targeted, slow, TCP connect scans instead of aggressive SYN scans.'},
    {icon:'\U0001f3ad',title:'Ignoring UDP Ports',desc:'Scanning all 65,535 TCP ports takes time, so testers often skip UDP scanning entirely. UDP hosts critical services like DNS, SNMP, and TFTP.',fix:'Always include UDP scanning (nmap -sU) for at least the top 100 ports. SNMP (UDP 161) is often a goldmine for information.'}
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
    {f:'Host Discovery',b:'The first phase of scanning \u2014 identifying which IP addresses are alive on the network.'},
    {f:'Port Scanning',b:'The second phase of scanning \u2014 probing a live host to see which TCP/UDP ports are open.'},
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
    'Scanning is active \u2014 you are sending packets to the target and they can log your IP.',
    'Methodology order: Host Discovery -> Port Scanning -> Service/OS Detection -> Vulnerability Scan.',
    'Never assume a host is down just because it doesn\'t respond to ping (ICMP). Firewalls block ICMP by default.',
    'Use alternative discovery (TCP ACK, TCP SYN, ARP) to bypass basic ICMP blocking.',
    'Aggressive scanning crashes fragile systems (SCADA/IoT) and triggers SOC alerts.',
    'Masscan is for speed/scale; Nmap is for accuracy and deep enumeration.',
    'Vulnerability scanning maps the discovered services to known CVEs for exploitation.'
  ]
};

CONTENT['tcp-ip-scanning'] = {
  module:'Module 03 \u00b7 Scanning Networks',
  title:'TCP/IP & Port Scanning',
  sub:'Understanding the protocols behind the packets to manipulate network responses.',
  killchain:{phase:'Scanning',mitre:'T1046 \u2014 Network Service Discovery',desc:'Port scanning relies entirely on manipulating the TCP 3-way handshake and analyzing how target systems respond to unexpected flags.'},
  learn:{
    simple:'Port scanning works by sending specific TCP or UDP packets to a target port and analyzing the response. To understand port scanning, you must perfectly understand the TCP 3-way handshake (SYN, SYN-ACK, ACK) and the TCP flags.',
    analogy:'TCP is like making a phone call: You say "Hello?" (SYN). They reply "Hello, who is this?" (SYN-ACK). You say "It\'s me, let\'s talk." (ACK). Port scanning is calling every extension in a building. If they answer (SYN-ACK), the port is open. If you get a disconnected tone (RST), the port is closed. If it rings forever (no response), a firewall dropped the call.',
    why:'Different types of scans (Full Connect, Stealth SYN, XMAS, FIN) manipulate these TCP flags differently to bypass firewalls or avoid logging. If you don\'t understand TCP/IP, you are just blindly running tools without understanding why they work or why they fail.',
    architecture:'A TCP packet header contains 6 crucial flags: URG (Urgent), ACK (Acknowledgment), PSH (Push), RST (Reset), SYN (Synchronize), FIN (Finish). Mnemonic: Unskilled Attackers Pester Real Security Folk. The state of these flags determines how firewalls and operating systems handle the packet.'
  },
  diagram:{
    title:'The TCP 3-Way Handshake vs Port Scanning',
    steps:[
      {icon:'\U0001f91d',label:'Normal Connection',desc:'1. Attacker sends SYN. 2. Target replies SYN-ACK. 3. Attacker replies ACK. Connection established. (Logged by target).'},
      {icon:'\U0001f513',label:'TCP Connect Scan',desc:'Completes the full 3-way handshake. Reliable, but creates a full connection log on the target system (Noisy).'},
      {icon:'\U0001f977',label:'Stealth SYN Scan',desc:'1. Attacker sends SYN. 2. Target replies SYN-ACK. 3. Attacker sends RST to tear it down before connecting. (Often avoids application logs).'},
      {icon:'\u26d4',label:'Closed Port Response',desc:'If an attacker sends a SYN to a closed port, the target OS complies with RFC 793 and replies with an RST (Reset).'},
      {icon:'\U0001f6e1\ufe0f',label:'Filtered (Firewall)',desc:'If a firewall blocks the port, it drops the packet. The attacker receives no response (timeout), marking the port "Filtered".'},
      {icon:'\U0001f384',label:'XMAS Scan',desc:'Sends a packet with FIN, PSH, and URG flags set (lit up like a Christmas tree). Bypasses some stateless firewalls. Windows ignores it; Linux replies RST if closed, no response if open.'}
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
    {icon:'\u26a0\ufe0f',title:'Confusing "Closed" with "Filtered"',desc:'Students often think a firewall sends an RST packet. Usually, a firewall drops the packet entirely (Filtered/Timeout). A target operating system sends the RST when a port is closed but reachable.',fix:'Understand the difference: RST = Reached the server, but port is closed. Timeout = Blocked by a firewall along the way (Filtered).'},
    {icon:'\U0001f534',title:'Assuming SYN Scans are Invisible',desc:'SYN scans ("stealth" scans) do not complete the 3-way handshake, so the application (like Apache) doesn\'t log the connection. However, modern Firewalls and IDS/IPS log SYN scans easily.',fix:'Do not assume "stealth" in Nmap means undetectable. It only bypasses application-level logging, not network-level detection.'},
    {icon:'\u26d4',title:'Using XMAS/FIN Scans on Windows Targets',desc:'XMAS and FIN scans rely on RFC 793 behavior where a closed port replies with RST to an unexpected flag, and an open port ignores it. Windows does not follow this RFC strictly and replies RST to everything.',fix:'Never use XMAS, FIN, or NULL scans against Windows targets. They will incorrectly report all ports as closed. Use SYN scans.'},
    {icon:'\U0001f3ad',title:'Not Knowing the 6 TCP Flags',desc:'You cannot pass the CEH or analyze network traffic without knowing the TCP flags and the 3-way handshake by heart.',fix:'Memorize: URG, ACK, PSH, RST, SYN, FIN (Unskilled Attackers Pester Real Security Folk).'}
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
  module:'Module 03 \u00b7 Scanning Networks',
  title:'Nmap Scanning Techniques',
  sub:'Mastering the industry-standard network mapper.',
  killchain:{phase:'Scanning',mitre:'T1046 \u2014 Network Service Discovery',desc:'Nmap is the definitive tool for the scanning phase. Mastery of its flags is non-negotiable for penetration testing.'},
  learn:{
    simple:'Nmap (Network Mapper) is the Swiss Army knife of network scanning. It discovers hosts, scans ports, detects service versions, identifies operating systems, and even runs vulnerability scripts. Learning Nmap is learning the language of network reconnaissance.',
    analogy:'If a network is a neighborhood, Nmap is a drone that flies over, maps every house, checks which doors are unlocked, looks through the windows to see what brand of TV they have, and reads the manufacturer\'s label on the security system.',
    why:'You cannot pass the CEH exam or work in cybersecurity without knowing Nmap syntax. It is universally used by attackers to find vulnerabilities and by defenders to audit their own networks. Different scenarios require different Nmap flags to balance speed, stealth, and accuracy.',
    architecture:'Nmap operates in phases: 1. Target resolution (DNS), 2. Host discovery (Ping sweep), 3. Port scanning (SYN/Connect), 4. Service/Version detection, 5. OS detection, 6. Nmap Scripting Engine (NSE) execution. You control these phases using command-line flags.'
  },
  diagram:{
    title:'Essential Nmap Flags Anatomy',
    steps:[
      {icon:'\U0001f4e1',label:'Discovery: -sn',desc:'Ping sweep (No port scan). Just tells you which IP addresses are online.'},
      {icon:'\U0001f513',label:'Scan Type: -sS / -sT / -sU',desc:'-sS (Stealth SYN, requires root), -sT (TCP Connect, no root), -sU (UDP scan).'},
      {icon:'\U0001f3af',label:'Ports: -p',desc:'-p 80,443 (specific), -p 1-1000 (range), -p- (all 65,535 ports). Default is top 1,000.'},
      {icon:'\U0001f4c4',label:'Version & OS: -sV / -O',desc:'-sV (Service Version detection), -O (OS Fingerprinting).'},
      {icon:'\u26a1',label:'Timing: -T',desc:'-T0 (Paranoid/Slow/Stealthy) to -T5 (Insane/Fast/Aggressive). Default is -T3.'},
      {icon:'\U0001f4dc',label:'Scripts & All: -sC / -A',desc:'-sC (Default NSE scripts), -A (Aggressive: implies -sV, -O, -sC, and traceroute).'}
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
    {icon:'\u26a0\ufe0f',title:'Using -A (Aggressive) Automatically',desc:'Students love nmap -A because it does everything. In the real world, -A is incredibly noisy, triggers every alarm in the SOC, and can disrupt network services.',fix:'Use specific flags (-sV, -sC, -O) instead of -A to understand exactly what traffic you are generating. Reserve -A for CTFs or explicit permission.'},
    {icon:'\U0001f534',title:'Forgetting to Scan All Ports',desc:'By default, Nmap only scans the top 1,000 most common ports. Attackers deliberately hide services on high ports (e.g., a backdoor on port 44444).',fix:'When doing a thorough assessment, always use -p- to scan all 65,535 ports. It takes longer but guarantees you don\'t miss hidden services.'},
    {icon:'\u26d4',title:'Not Saving Output',desc:'Running a 2-hour scan and forgetting to save the output means you have to run it again, generating twice the noise and wasting time.',fix:'Always use -oA [filename] or -oN [filename] to output results to a file immediately. -oA saves in Normal, XML, and Grepable formats.'},
    {icon:'\U0001f3ad',title:'Running SYN Scans Without Root/Admin',desc:'A TCP SYN scan (-sS) crafts custom raw packets to tear down the connection. This requires root/administrator privileges.',fix:'If you run Nmap as a normal user, it automatically defaults to a TCP Connect scan (-sT), which is noisier. Always use sudo nmap -sS on Linux.'}
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
  module:'Module 03 \u00b7 Scanning Networks',
  title:'Hping3 & Packet Crafting',
  sub:'Custom packet generation for firewall evasion and granular network testing.',
  killchain:{phase:'Scanning',mitre:'T1046 \u2014 Network Service Discovery',desc:'When standard Nmap scans are blocked by firewalls, packet crafting allows attackers to manually manipulate TCP/IP headers to slip past rules.'},
  learn:{
    simple:'Hping3 is a command-line packet assembler and analyzer. While Nmap sends predefined scan types, Hping3 allows you to manually construct a TCP/IP packet, specifying exactly which flags are set, the packet size, the fragmentation, and the source IP.',
    analogy:'If Nmap is buying a pre-built sports car, Hping3 is ordering individual car parts and building a custom vehicle in your garage. You have total control over every single piece (packet header), allowing you to build a vehicle specifically designed to bypass the target\'s security gate.',
    why:'Firewalls and IDS systems easily recognize standard Nmap scans. Hping3 allows penetration testers to craft malformed or fragmented packets that bypass poorly configured firewalls, test firewall rule sets precisely, or execute Denial of Service (DoS) testing.',
    architecture:'Hping3 operates at the command line, taking arguments that directly map to TCP/IP header fields. You can set the TCP flags (-S for SYN, -A for ACK, -F for FIN), spoof the source IP (-a), fragment packets (-f), and specify the destination port (-p).'
  },
  diagram:{
    title:'Hping3 Packet Crafting Capabilities',
    steps:[
      {icon:'\U0001f3f9',label:'Targeted Port Probing',desc:'Send a specific flag to a specific port to test firewall rules. E.g., Send an ACK packet to see if a stateful firewall is blocking it.'},
      {icon:'\U0001f6e1\ufe0f',label:'Firewall Evasion (Fragmentation)',desc:'Split a TCP header across multiple tiny packets using the -f flag. Some firewalls cannot reassemble them and let them pass.'},
      {icon:'\U0001f3ad',label:'Source IP Spoofing',desc:'Change the source IP (-a) to make the scan appear as if it is coming from a trusted internal machine or a decoy.'},
      {icon:'\U0001f4a5',label:'Denial of Service (SYN Flood)',desc:'Flood a target with SYN packets (--flood) from random source IPs (--rand-source) to test DoS resilience.'},
      {icon:'\U0001f4e6',label:'Custom Data Payload',desc:'Attach custom data files to ICMP or TCP packets for covert channel data exfiltration testing.'}
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
    {icon:'\u26a0\ufe0f',title:'Using Hping3 for General Scanning',desc:'Hping3 is incredibly slow and tedious for mapping a whole network compared to Nmap. It requires manual analysis of the output.',fix:'Use Nmap for general discovery and scanning. Only switch to Hping3 when you encounter a specific firewall block and need to surgically craft packets to bypass it.'},
    {icon:'\U0001f534',title:'Misunderstanding IP Spoofing Responses',desc:'If you spoof your IP address using hping3 -a [fake_ip], the target will send the response (SYN-ACK) to the fake IP, not to you.',fix:'IP spoofing is useful for DoS (hiding your identity) or Decoy scanning. It is NOT useful if you actually need to see the response to know if the port is open (unless you control the spoofed IP).'},
    {icon:'\u26d4',title:'Accidentally Causing a DoS',desc:'Adding the --flood flag to an Hping3 command sends packets as fast as your network interface allows, without waiting for replies.',fix:'Never use --flood on a production network without explicit authorization for DoS testing. It will overwhelm network equipment and servers quickly.'}
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
  module:'Module 03 \u00b7 Scanning Networks',
  title:'Banner Grabbing & OS Fingerprinting',
  sub:'Identifying exactly what you are attacking.',
  killchain:{phase:'Scanning',mitre:'T1046 \u2014 Network Service Discovery',desc:'Knowing a port is open is useless if you don\'t know what software is running on it. Banner grabbing turns an open port into an exploitable target.'},
  learn:{
    simple:'Banner grabbing (Service Enumeration) is connecting to an open port and reading the text the service sends back to identify the software name and version. OS Fingerprinting analyzes how the target responds to weird packets to guess the operating system (Windows vs Linux).',
    analogy:'Port scanning tells you a store\'s door is unlocked. Banner grabbing is reading the sign above the door that says "Bank of America, Branch 42". OS Fingerprinting is looking at the building\'s architecture to determine if it was built by Windows Construction or Linux Builders.',
    why:'Exploits are highly specific. An exploit for Apache 2.2 will fail against Apache 2.4, and an exploit for Windows Server 2012 will crash a Linux server. You must accurately identify the exact service version and OS before launching an exploit, otherwise you risk failing or crashing the system.',
    architecture:'Active banner grabbing connects to the port (e.g., Telnet or Netcat) and reads the response. Passive banner grabbing uses Wireshark to read traffic without sending new packets. OS fingerprinting sends malformed packets (e.g., a SYN-FIN-URG packet) and compares the unique response (the "fingerprint") to a database of known OS behaviors.'
  },
  diagram:{
    title:'Service & OS Identification Methods',
    steps:[
      {icon:'\U0001f4e3',label:'Active Banner Grabbing',desc:'Using Netcat or Telnet to connect to a port (e.g., port 22). The server replies with a banner: "SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8".'},
      {icon:'\U0001f575\ufe0f\u200d\u2642\ufe0f',label:'Passive Banner Grabbing',desc:'Sniffing network traffic with Wireshark to capture banners as legitimate users connect. Undetectable by the target.'},
      {icon:'\U0001f4c4',label:'Nmap Version Detection (-sV)',desc:'Nmap sends specific, malformed probes (not just a basic connection) to force stubborn services to reveal their version.'},
      {icon:'\U0001f5fa\ufe0f',label:'Active OS Fingerprinting (-O)',desc:'Nmap sends malformed TCP/IP packets. Windows, Linux, and Cisco iOS all respond slightly differently to rule violations. Nmap compares the response to its database.'},
      {icon:'\U0001f310',label:'Passive OS Fingerprinting',desc:'Analyzing packet TTL (Time To Live) and TCP Window Size in Wireshark. E.g., Windows default TTL is 128, Linux is 64.'}
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
    {icon:'\u26a0\ufe0f',title:'Trusting Fake Banners',desc:'Security administrators often change banners to confuse attackers (e.g., configuring an Apache server to return an "IIS 10" banner).',fix:'Do not rely solely on the raw banner text. Use Nmap\'s -sV, which sends complex probes and analyzes behavior, not just the text string, making it harder to fool.'},
    {icon:'\U0001f534',title:'Active Fingerprinting on Fragile Networks',desc:'OS Fingerprinting (Nmap -O) sends heavily malformed packets (like FIN-URG-PSH). Legacy mainframes, IoT devices, or old printers often crash when receiving these packets.',fix:'Use Passive OS Fingerprinting (p0f or Wireshark TTL analysis) when dealing with highly fragile SCADA or medical environments.'},
    {icon:'\u26d4',title:'Assuming Port 80 is Always HTTP',desc:'Attackers often run SSH on port 80 or 443 to bypass outbound firewalls. Just because port 80 is open doesn\'t mean a web server is running.',fix:'Always use banner grabbing or -sV to verify the actual service protocol. Never assume the service based solely on the port number.'}
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
"""

if INJECT_BEFORE in html:
    pos = html.find(INJECT_BEFORE)
    html = html[:pos] + MODULE03_CONTENT + '\n\n' + html[pos:]
    ok.append('Module 03 (network-scanning-overview, tcp-ip-scanning, nmap-techniques, hping3-scanning, banner-grabbing) injected')
else:
    fail.append('INJECT_BEFORE marker missing for Module 03')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print()
print('=' * 55)
print('MODULE 03 CONTENT INJECTION COMPLETE')
print('=' * 55)
for s in ok: print(f'  [OK]  {s}')
for s in fail: print(f'  [FAIL] {s}')
print()
print(f'New size: {len(html):,} bytes / {html.count(chr(10)):,} lines')
