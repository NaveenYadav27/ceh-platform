import re

def inject_m07_m10(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # PHASE 07: Malware Threats (Malware Analyst)
    m07_content = """
    topics: [
      {
        id: "t07_01",
        title: "Malware Concepts & Analysis",
        scenario: "GFS Threat Intel has flagged a suspicious email attachment received by our CFO. Your task is to safely analyze this payload, identify its behavior, and determine if it's a trojan, ransomware, or spyware.",
        commands: [
          { os: "Windows", cmd: "certutil -hashfile suspicious_invoice.exe SHA256" },
          { os: "Linux", cmd: "strings suspicious_invoice.exe | grep -i http" },
          { os: "Linux", cmd: "file suspicious_invoice.exe" }
        ],
        summary: [
          "Static Analysis: Examining the file without executing it (hashes, strings).",
          "Dynamic Analysis: Running malware in a sandbox to observe behavior.",
          "Identify malware types (Trojans, Viruses, Ransomware, Worms)."
        ],
        flashcards: [
          { q: "What is an APT?", a: "Advanced Persistent Threat - long-term, stealthy attack." },
          { q: "What tool extracts readable text from binaries?", a: "strings command." }
        ],
        ctf: {
          scenario: "You have extracted the hash of the suspicious file: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855. Submit this to VirusTotal to find the malware family name.",
          flag: "TrickBot",
          points: 50,
          hint: "Search the hash on VirusTotal. Look at the popular threat label."
        }
      },
      {
        id: "t07_02",
        title: "Fileless Malware",
        scenario: "The EDR triggered an alert for anomalous PowerShell execution on a GFS workstation. We suspect fileless malware leveraging Living off the Land (LotL) techniques. Investigate the memory footprint.",
        commands: [
          { os: "Windows", cmd: "Get-Process | Where-Object {$_.Name -eq 'powershell'}" },
          { os: "Linux", cmd: "volatility -f memory.dmp --profile=Win10x64 pslist" }
        ],
        summary: [
          "Fileless malware resides only in RAM, leaving no disk footprint.",
          "Often leverages PowerShell, WMI, or legitimate system tools.",
          "Memory forensics is required to detect and analyze these threats."
        ],
        flashcards: [
          { q: "What is LotL?", a: "Living off the Land - using built-in system tools for malicious purposes." },
          { q: "Why is fileless malware hard to detect?", a: "It has no file signature for traditional AV to scan." }
        ],
        ctf: {
          scenario: "Analyze the base64 encoded PowerShell payload found in the registry: 'ZWNobyAiR0ZTX01FTV9DT01QUk9NSVNFRCI='. Decode it to find the flag.",
          flag: "GFS_MEM_COMPROMISED",
          points: 50,
          hint: "Use echo 'string' | base64 -d in your Linux terminal."
        }
      }
    ]
"""

    # PHASE 08: Sniffing (Network Security Analyst)
    m08_content = """
    topics: [
      {
        id: "t08_01",
        title: "Network Sniffing Concepts",
        scenario: "A rogue device has been plugged into the GFS Datacenter switch. We need you to perform packet capture (PCAP) to identify what traffic this device is intercepting. Assume an active sniffing scenario.",
        commands: [
          { os: "Linux", cmd: "tcpdump -i eth0 -w gfs_capture.pcap" },
          { os: "Linux", cmd: "wireshark gfs_capture.pcap" }
        ],
        summary: [
          "Active vs Passive Sniffing (Hubs vs Switches).",
          "MAC Flooding can force a switch into hub mode (fail-open).",
          "Promiscuous mode allows a NIC to read all traffic."
        ],
        flashcards: [
          { q: "What happens in a CAM table overflow?", a: "The switch acts like a hub, broadcasting all traffic." },
          { q: "What is Promiscuous Mode?", a: "NIC accepts all packets, regardless of MAC address." }
        ],
        ctf: {
          scenario: "In the provided PCAP, filter for HTTP traffic and extract the plaintext password sent to the legacy internal portal.",
          flag: "p4ssw0rd_admin!",
          points: 50,
          hint: "Use the filter 'http.request.method == POST' in Wireshark."
        }
      },
      {
        id: "t08_02",
        title: "Spoofing & MITM Attacks",
        scenario: "An analyst reported an invalid certificate error when accessing the GFS internal payroll site. Investigate the network segment for ARP poisoning or DHCP spoofing indicating a Man-in-the-Middle attack.",
        commands: [
          { os: "Linux", cmd: "arp -a" },
          { os: "Linux", cmd: "arpspoof -i eth0 -t 10.0.0.5 10.0.0.1" }
        ],
        summary: [
          "ARP Poisoning maps the attacker's MAC to the gateway's IP.",
          "DHCP Spoofing involves a rogue server issuing malicious network configurations.",
          "Defenses include Dynamic ARP Inspection (DAI) and DHCP Snooping."
        ],
        flashcards: [
          { q: "What does ARP do?", a: "Resolves IP addresses to MAC addresses." },
          { q: "How do you prevent ARP spoofing?", a: "Dynamic ARP Inspection (DAI) on the switch." }
        ],
        ctf: {
          scenario: "You captured the MAC address of the device performing ARP spoofing: 00:1A:2B:3C:4D:5E. Identify the manufacturer using a MAC vendor lookup tool.",
          flag: "Cisco Systems",
          points: 50,
          hint: "Search the first 3 octets (OUI) online."
        }
      }
    ]
"""

    # PHASE 09: Social Engineering (Security Awareness Officer)
    m09_content = """
    topics: [
      {
        id: "t09_01",
        title: "Phishing & Spear-Phishing",
        scenario: "Multiple GFS employees received urgent emails claiming to be from HR regarding 'Q3 Bonus Adjustments'. As the Security Awareness Officer, analyze the email headers to identify the true sender and domain.",
        commands: [
          { os: "Linux", cmd: "cat suspicious_email.eml | grep 'Received:'" },
          { os: "Linux", cmd: "whois gfs-hr-bonus.com" }
        ],
        summary: [
          "Spear-phishing targets specific individuals or departments.",
          "Email header analysis reveals the true origin IP and routing path.",
          "Look for SPF, DKIM, and DMARC failures."
        ],
        flashcards: [
          { q: "What is Whaling?", a: "Phishing highly privileged targets (e.g., CEO, CFO)." },
          { q: "What DNS record specifies authorized mail servers?", a: "SPF (Sender Policy Framework)." }
        ],
        ctf: {
          scenario: "The phishing email links to a malicious domain. Extract the hidden domain from this obfuscated HTML: <a href='http://10.10.14.5%2Flogin.php'>Click Here</a>",
          flag: "10.10.14.5/login.php",
          points: 50,
          hint: "URL decode the %2F."
        }
      },
      {
        id: "t09_02",
        title: "Physical & Psychological Manipulation",
        scenario: "A physical breach occurred at the GFS London branch. An unauthorized individual gained access by carrying a large box and having an employee hold the door. Review security footage and log the attack vectors.",
        commands: [
          { os: "Windows", cmd: "Get-EventLog -LogName Security -InstanceId 4624" }
        ],
        summary: [
          "Tailgating / Piggybacking: Following an authorized person into a restricted area.",
          "Dumpster Diving: Searching trash for sensitive information.",
          "Pretexting: Creating a fabricated scenario to obtain information."
        ],
        flashcards: [
          { q: "What is Piggybacking?", a: "Following someone through a secured door with their consent." },
          { q: "What is the best defense against Social Engineering?", a: "Comprehensive user security awareness training." }
        ],
        ctf: {
          scenario: "The attacker dropped a USB drive in the parking lot (Baiting). You plug it into a sandbox and find an autorun.inf file. What executable is it attempting to run? [Action: Open autorun.inf]",
          flag: "payload.exe",
          points: 50,
          hint: "Look for the 'open=' parameter in the autorun.inf structure."
        }
      }
    ]
"""

    # PHASE 10: Denial of Service (Network Defense Analyst)
    m10_content = """
    topics: [
      {
        id: "t10_01",
        title: "DoS & DDoS Concepts",
        scenario: "The GFS trading API is experiencing extreme latency. Telemetry shows a massive influx of SYN packets from random IPs. As the Network Defense Analyst, identify the attack type and implement a mitigation strategy.",
        commands: [
          { os: "Linux", cmd: "netstat -n | grep SYN_RECV" },
          { os: "Linux", cmd: "iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP" }
        ],
        summary: [
          "SYN Flood: Exhausts server resources by leaving half-open connections.",
          "Volumetric Attacks: Consumes all available bandwidth (e.g., UDP amplification).",
          "Application Layer Attacks: Exhausts application resources (e.g., Slowloris)."
        ],
        flashcards: [
          { q: "What mitigates a SYN flood?", a: "SYN Cookies." },
          { q: "What is an Amplification Attack?", a: "Using spoofed requests to vulnerable services (DNS, NTP) to send massive responses to the victim." }
        ],
        ctf: {
          scenario: "Analyze the apache access.log. An attacker is sending partial HTTP requests very slowly to tie up threads. What is this attack called?",
          flag: "Slowloris",
          points: 50,
          hint: "It's an application-layer DoS named after a slow primate."
        }
      },
      {
        id: "t10_02",
        title: "Botnets & Mitigation",
        scenario: "The DDoS attack was traced back to a Mirai-variant botnet. We need to identify the Command & Control (C2) server communicating with the infected IoT devices on our guest network.",
        commands: [
          { os: "Linux", cmd: "ss -antp | grep ESTAB" },
          { os: "Linux", cmd: "tcpdump -i eth1 port 6667" }
        ],
        summary: [
          "Botnets consist of compromised machines (zombies) controlled by a C2 server.",
          "Often use IRC, HTTP, or P2P for communication.",
          "Mitigation includes blackholing, sinkholing, and rate limiting."
        ],
        flashcards: [
          { q: "What is a Sinkhole?", a: "Routing malicious traffic to a controlled IP for analysis." },
          { q: "What port does IRC commonly use for C2?", a: "Port 6667." }
        ],
        ctf: {
          scenario: "You intercepted C2 traffic. The botmaster issued a command: '!ddos target=10.10.50.5 port=443 time=3600'. What is the target IP address?",
          flag: "10.10.50.5",
          points: 50,
          hint: "Read the target parameter in the command string."
        }
      }
    ]
"""

    html = re.sub(r'id:\s*"m07".*?topics:\s*\[.*?\]', f'id: "m07",\n    name: "Phase 07: Malware Analyst (Malware Threats)",\n{m07_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m08".*?topics:\s*\[.*?\]', f'id: "m08",\n    name: "Phase 08: Network Security Analyst (Sniffing)",\n{m08_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m09".*?topics:\s*\[.*?\]', f'id: "m09",\n    name: "Phase 09: Security Awareness Officer (Social Engineering)",\n{m09_content}', html, flags=re.DOTALL)
    html = re.sub(r'id:\s*"m10".*?topics:\s*\[.*?\]', f'id: "m10",\n    name: "Phase 10: Network Defense Analyst (Denial of Service)",\n{m10_content}', html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        print("Content for Phases 07-10 injected successfully.")

inject_m07_m10('frontend/index.html')
