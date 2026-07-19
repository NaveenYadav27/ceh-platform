import json
import re

m01_payload = {
    "module": "Module 01 — Introduction to Ethical Hacking",
    "title": "Information Security Overview",
    "sub": "Understanding the CIA Triad, threat landscape, and foundational security concepts in an enterprise context.",
    "killchain": {
        "phase": "Pre-Attack Phase",
        "mitre": "Foundation",
        "desc": "Core concepts that underpin all CEH domains and attack methodologies."
    },
    "learn": {
        "simple": "<strong>DEFINITION & SIMPLE EXPLANATION</strong><br><br>Information security is the practice of protecting data from unauthorized access, modification, or destruction. In an enterprise environment like Global Financial Services (GFS), it means ensuring that customer data, trading algorithms, and internal communications remain secure against an ever-evolving threat landscape.<br><br><strong>ENTERPRISE BRIEFING</strong><br>As a Security Analyst at GFS, your primary mission is to defend the CIA Triad (Confidentiality, Integrity, Availability) across all business units.",
        "analogy": "<strong>ANALOGY</strong><br><br>Think of a bank vault. The CIA Triad are the three locks on the vault door.<br><ul><li><strong>Confidentiality:</strong> Only authorized people have the combination (Encryption, Access Control).</li><li><strong>Integrity:</strong> No one can tamper with the cash inside without it being detected (Hashing, Digital Signatures).</li><li><strong>Availability:</strong> The vault door opens quickly and reliably when the branch manager needs it (DDoS Protection, Redundancy).</li></ul><br><strong>5W1H CONTEXT</strong><br><strong>What:</strong> Protecting information assets.<br><strong>Why:</strong> To prevent financial loss and regulatory fines.<br><strong>Who:</strong> Security Analysts, Architects, and every employee.<br><strong>When:</strong> Continuous monitoring 24/7/365.<br><strong>Where:</strong> On-premise, cloud, and endpoints.<br><strong>How:</strong> People, Process, and Technology.",
        "why": "<strong>THREAT INTELLIGENCE & BUSINESS CONTEXT (GFS)</strong><br><br>Without understanding security fundamentals, attackers exploit the gaps between policy and implementation. At GFS, a breach of confidentiality (e.g., leaked customer PII) violates GDPR and PCI-DSS, resulting in massive fines. A breach of integrity (tampered transaction records) destroys market trust.<br><br>Threat actors continuously probe GFS perimeters using automated reconnaissance, phishing, and zero-day exploits. Every penetration test starts with understanding what the target is trying to protect.",
        "architecture": "<strong>TECHNICAL DEEP DIVE & ENTERPRISE WORKFLOW</strong><br><br>Information security operates across multiple defense layers: Physical (server rooms, badge access), Network (firewalls, IDS/IPS), and Application (input validation, authentication). The OSI model maps directly to these layers, and CEH attacks target each one.<br><br><strong>ENTERPRISE WORKFLOW:</strong><br>1. <strong>Identify:</strong> Asset inventory and data classification.<br>2. <strong>Protect:</strong> Implement firewalls, MFA, and encryption.<br>3. <strong>Detect:</strong> Deploy SIEM and IDS to monitor anomalies.<br>4. <strong>Respond:</strong> Incident Response (IR) team contains the threat.<br>5. <strong>Recover:</strong> Restore from encrypted backups and patch vulnerabilities."
    },
    "diagram": {
        "title": "Information Security Threat Lifecycle",
        "steps": [
            {
                "icon": "👤",
                "label": "Threat Actor Emerges",
                "desc": "An adversary identifies GFS as a target with valuable data or systems."
            },
            {
                "icon": "🔍",
                "label": "Reconnaissance",
                "desc": "The attacker researches: open ports, employee names, software versions, IP ranges via OSINT."
            },
            {
                "icon": "💥",
                "label": "Exploit Vulnerability",
                "desc": "A weakness is exploited — unpatched software, weak password, phishing, or misconfiguration."
            },
            {
                "icon": "🔓",
                "label": "CIA Triad Violated",
                "desc": "Data is stolen (Confidentiality), altered (Integrity), or systems go offline (Availability)."
            },
            {
                "icon": "🛡️",
                "label": "Detection & Response",
                "desc": "SIEM, IDS, or SOC analysts detect anomaly and trigger the incident response process."
            },
            {
                "icon": "📋",
                "label": "Remediation & Lessons",
                "desc": "Root cause fixed, controls updated, post-incident report filed to prevent recurrence."
            }
        ]
    },
    "enterprise": {
        "gfs": "<strong>ENTERPRISE SCENARIO — GLOBALFINSEC CORP</strong><br>You are the Security Architect at GlobalFinSec Corp.<br><br><strong>SITUATION</strong><br>An external audit flagged three critical gaps: no asset inventory, no data classification policy, and no formal incident response plan — ahead of a PCI-DSS compliance deadline.<br><br><strong>YOUR CHALLENGE</strong><br>Map the CIA Triad to the top three assets (trading platform, customer database, internal email) and identify which controls are missing for each.",
        "steps": [
            "List the three assets and classify them by CIA priority (customer DB = highest Confidentiality need).",
            "Run: `nmap -sV 192.168.1.0/24` to discover what services are exposed on each asset.",
            "Check for missing patches on Windows hosts: `systeminfo | findstr \"OS Version\"`.",
            "Identify existing controls (firewall? MFA? encryption?) and document gaps.",
            "Write a one-page risk register: Asset, Threat, Vulnerability, CIA Impact, Recommended Control."
        ],
        "outcome": "<strong>Outcome:</strong> You identified 12 missing controls. The trading platform lacked MFA (Confidentiality), the database had no encryption at rest (Confidentiality + Integrity), and email had no DLP (Confidentiality).<br><strong>Key Lesson:</strong> Every security investment must map to a CIA pillar. Without this framing, security spending cannot be justified to the board."
    },
    "tools": [
        {
            "name": "Nmap",
            "desc": "Network discovery and port scanning.",
            "cmd": "nmap -sV target"
        },
        {
            "name": "OpenVAS",
            "desc": "Open-source vulnerability scanner.",
            "cmd": "openvas-start"
        },
        {
            "name": "Nessus",
            "desc": "Enterprise vulnerability scanner.",
            "cmd": "service nessusd start"
        }
    ],
    "commands": {
        "win": [
            {
                "cmd": "systeminfo",
                "purpose": "Displays detailed configuration information about a computer and its operating system.",
                "out": "Host Name: GFS-WKSTN-01\\nOS Name: Microsoft Windows 10 Enterprise\\nOS Version: 10.0.19044 N/A Build 19044",
                "note": "Useful for identifying the exact OS build to find missing patches.",
                "mistake": "Running without piping to `findstr` can overwhelm the terminal with output."
            },
            {
                "cmd": "net user",
                "purpose": "Displays a list of all user accounts on the computer.",
                "out": "User accounts for \\\\GFS-WKSTN-01\\n-------------------------------------------------------------------------------\\nAdministrator            Guest                    jdoe\\nThe command completed successfully.",
                "note": "First step in local enumeration to find unauthorized accounts.",
                "mistake": "Does not show domain users unless `/domain` switch is used."
            }
        ],
        "lin": [
            {
                "cmd": "uname -a",
                "purpose": "Print system information including kernel version.",
                "out": "Linux GFS-DB-01 5.10.0-18-amd64 #1 SMP Debian 5.10.140-1 x86_64 GNU/Linux",
                "note": "Critical for finding kernel exploits (e.g., Dirty COW).",
                "mistake": "Relying only on `uname`; always check `/etc/os-release` as well."
            },
            {
                "cmd": "id",
                "purpose": "Print real and effective user and group IDs.",
                "out": "uid=1000(jdoe) gid=1000(jdoe) groups=1000(jdoe),27(sudo)",
                "note": "Check if the compromised user is in the `sudo` group for privilege escalation.",
                "mistake": "Forgetting to check the groups section which often hides lateral movement paths."
            },
            {
                "cmd": "cat /etc/passwd",
                "purpose": "List all user accounts on the Linux system.",
                "out": "root:x:0:0:root:/root:/bin/bash\\njdoe:x:1000:1000:John Doe,,,:/home/jdoe:/bin/bash",
                "note": "Look for accounts with `/bin/bash` or `/bin/sh` to identify interactive users.",
                "mistake": "Assuming passwords are in this file; they are hashed in `/etc/shadow`."
            }
        ]
    },
    "pitfalls": [
        {
            "title": "Mistaking Compliance for Security",
            "desc": "Passing a PCI-DSS or ISO audit does not mean you are secure. Compliance is a minimum bar, not a security guarantee.",
            "fix": "Treat compliance as the floor. Layer additional threat-model-driven controls beyond regulatory minimums."
        },
        {
            "title": "Neglecting Availability in Security Planning",
            "desc": "Security teams over-focus on Confidentiality (encryption, access control) and neglect Availability until a DDoS hits.",
            "fix": "Include RTO/RPO metrics in all security plans. Regularly test failover and backup restoration."
        },
        {
            "title": "Treating Risk as a One-Time Assessment",
            "desc": "A yearly risk assessment misses new vulnerabilities introduced by software updates, new vendors, and infrastructure changes.",
            "fix": "Implement continuous risk monitoring. Reassess whenever major changes occur."
        },
        {
            "title": "Over-Relying on Perimeter Security",
            "desc": "The castle-and-moat model assumes threats come from outside. Modern threats (insiders, cloud misconfigs) originate inside.",
            "fix": "Adopt Zero Trust: verify every request as untrusted regardless of source location."
        }
    ],
    "lab": {
        "title": "Enterprise Scenario: Information Security Core Concepts",
        "scenario": "You are a junior SOC analyst at Global Financial Services. A new Linux server has been deployed in the DMZ without going through the standard security review process. You need to perform initial reconnaissance and identify the CIA triad implications of the current configuration.",
        "objectives": [
            "Perform basic local enumeration to identify the OS and users.",
            "Determine the exposed services.",
            "Correlate findings to CIA Triad risks."
        ],
        "safety": [
            "Ensure you have written authorization before scanning any GFS assets."
        ],
        "dependencies": [],
        "steps": [
            "Step 1: Open your Kali terminal.",
            "Step 2: Identify your current privilege level: `id`.",
            "Step 3: Check the system OS version: `uname -a` and `cat /etc/os-release`.",
            "Step 4: View the active network connections to see what is exposed: `netstat -tulnp`.",
            "Step 5: Review the local user accounts to see if default accounts exist: `cat /etc/passwd`."
        ],
        "evidence": [
            "Terminal output showing the OS version.",
            "Terminal output showing open ports (e.g., port 22, 80)."
        ],
        "validation": [
            "You should be able to state exactly which services are running and what the impact would be if they were compromised (e.g., port 80 down = Availability impact)."
        ],
        "troubleshooting": [
            "If `netstat` is not found, use `ss -tulnp` instead."
        ],
        "mitre": [
            {
                "id": "T1082",
                "name": "System Information Discovery",
                "tactic": "Discovery"
            }
        ],
        "cleanup": [
            "Clear your terminal history: `history -c`."
        ]
    },
    "quiz": [
        {
            "type": "multiple-choice",
            "difficulty": "Easy",
            "q": "Which component of the CIA Triad ensures that information is accessible only to those authorized to have access?",
            "opts": ["Confidentiality", "Integrity", "Availability", "Non-repudiation"],
            "correct": 0,
            "fb": "Confidentiality ensures that data is kept secret from unauthorized entities, typically implemented through encryption and access controls."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Easy",
            "q": "Which component of the CIA Triad ensures that information is not altered by unauthorized persons?",
            "opts": ["Confidentiality", "Integrity", "Availability", "Authentication"],
            "correct": 1,
            "fb": "Integrity guarantees that data has not been changed, destroyed, or lost in an unauthorized or accidental manner. Hashing is a common integrity control."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Easy",
            "q": "A DDoS attack primarily targets which component of the CIA Triad?",
            "opts": ["Confidentiality", "Integrity", "Availability", "Non-repudiation"],
            "correct": 2,
            "fb": "Availability ensures that systems and data are accessible to authorized users when needed. DDoS attacks aim to disrupt this accessibility."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Intermediate",
            "q": "Which of the following best describes 'Non-repudiation'?",
            "opts": ["Preventing unauthorized access to data.", "Ensuring a sender cannot deny having sent a message.", "Guaranteeing system uptime.", "Hashing a file to verify its integrity."],
            "correct": 1,
            "fb": "Non-repudiation ensures that a party to a transaction cannot deny having received a transaction nor can the other party deny having sent a transaction (e.g., using digital signatures)."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Intermediate",
            "q": "What is the primary difference between a Vulnerability and an Exploit?",
            "opts": ["A vulnerability is a weakness; an exploit is a tool used to take advantage of it.", "A vulnerability is a tool; an exploit is a weakness.", "A vulnerability only applies to software; an exploit applies to hardware.", "There is no difference; the terms are synonymous."],
            "correct": 0,
            "fb": "A vulnerability is a flaw or weakness in system security procedures, design, implementation, or internal controls. An exploit is a defined way to breach the security of an IT system through a vulnerability."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Intermediate",
            "q": "Which term describes a potential occurrence that can result in an unwanted outcome for an organization?",
            "opts": ["Vulnerability", "Threat", "Risk", "Exploit"],
            "correct": 1,
            "fb": "A threat is an event or condition that has the potential for causing asset loss and the undesirable consequences or impact from such loss."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Hard",
            "q": "In risk management, how is Risk formally calculated?",
            "opts": ["Risk = Threat × Vulnerability × Asset Value", "Risk = Threat + Vulnerability", "Risk = Asset Value / Threat", "Risk = Vulnerability × Exploit"],
            "correct": 0,
            "fb": "Risk is a function of the likelihood of a given threat-source exercising a particular potential vulnerability, and the resulting impact of that adverse event on the organization (Asset Value)."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Hard",
            "q": "A company implements a biometric scanner to access the server room. This is an example of what type of security control?",
            "opts": ["Administrative Control", "Technical (Logical) Control", "Physical Control", "Detective Control"],
            "correct": 2,
            "fb": "Physical controls are tangible measures taken to protect systems and personnel (e.g., guards, locks, biometric scanners at doors)."
        },
        {
            "type": "true-false",
            "difficulty": "Intermediate",
            "q": "An Acceptable Use Policy (AUP) is an example of an Administrative Control.",
            "opts": ["True", "False"],
            "correct": 0,
            "fb": "True. Administrative controls are policies, procedures, and regulations that direct personnel on how to maintain security."
        },
        {
            "type": "multiple-choice",
            "difficulty": "Intermediate",
            "q": "Which of the following is considered a Detective Control?",
            "opts": ["Firewall", "Intrusion Detection System (IDS)", "Data Encryption", "Security Guard"],
            "correct": 1,
            "fb": "An IDS is a detective control designed to identify and alert on malicious activity after or as it occurs. A firewall is a preventative control."
        }
    ],
    "flashcards": [
        {
            "f": "Confidentiality",
            "b": "Ensuring data is only accessible to authorized individuals (e.g., via encryption)."
        },
        {
            "f": "Integrity",
            "b": "Ensuring data is not altered or tampered with (e.g., via hashing)."
        },
        {
            "f": "Availability",
            "b": "Ensuring systems and data are accessible when needed (e.g., via redundancy)."
        },
        {
            "f": "Non-repudiation",
            "b": "Ensuring a sender cannot deny sending a message, often achieved via digital signatures."
        },
        {
            "f": "Vulnerability",
            "b": "A weakness in a system, application, or process that can be exploited."
        },
        {
            "f": "Threat",
            "b": "A potential danger that could exploit a vulnerability (e.g., a hacker, malware, natural disaster)."
        },
        {
            "f": "Exploit",
            "b": "A piece of software, data, or sequence of commands that takes advantage of a vulnerability."
        },
        {
            "f": "Risk",
            "b": "The potential for loss, damage, or destruction of an asset. (Threat × Vulnerability × Asset Value)."
        },
        {
            "f": "Physical Control",
            "b": "Tangible security measures like locks, fences, and security guards."
        },
        {
            "f": "Administrative Control",
            "b": "Policies, procedures, and training designed to direct human behavior (e.g., AUP)."
        }
    ],
    "summary": [
        "The CIA Triad (Confidentiality, Integrity, Availability) is the foundation of information security.",
        "Security controls are categorized into Physical, Technical (Logical), and Administrative types.",
        "Risk management involves identifying assets, threats, and vulnerabilities to calculate and mitigate risk.",
        "Compliance with laws and standards (PCI-DSS, GDPR) is mandatory but does not equal complete security.",
        "Modern enterprise security requires a defense-in-depth strategy, layering multiple controls."
    ],
    "outcomes": [
        "Define the core concepts of information security and the CIA Triad.",
        "Differentiate between vulnerabilities, threats, exploits, and risks.",
        "Identify and classify various types of security controls (Physical, Technical, Administrative).",
        "Understand the importance of compliance frameworks in an enterprise context."
    ]
}

def inject_payload(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        html = f.read()

    # We need to replace the existing 'info-security-overview': { ... }
    # Since it's a huge object, we'll use regex to find the start and end of it.
    
    # We find the string "'info-security-overview':{"
    pattern = r"['\"]info-security-overview['\"]\s*:\s*\{"
    match = re.search(pattern, html)
    if not match:
        print(f"Could not find 'info-security-overview' in {file_path}")
        return
        
    start_idx = match.start()
    
    # Now we need to find the matching closing brace.
    brace_count = 0
    end_idx = -1
    for i in range(start_idx, len(html)):
        if html[i] == '{':
            brace_count += 1
        elif html[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i
                break
                
    if end_idx == -1:
        print(f"Could not find closing brace for 'info-security-overview' in {file_path}")
        return
        
    # Serialize the new payload
    # Note: we need to output it as a javascript object literal without quotes around the key if possible,
    # but JSON output is valid JS.
    payload_str = json.dumps(m01_payload, separators=(',', ':'))
    # The key needs to be prepended
    replacement = f"'info-security-overview':{payload_str}"
    
    new_html = html[:start_idx] + replacement + html[end_idx+1:]
    
    with open(file_path, 'w', encoding='utf8') as f:
        f.write(new_html)
    print(f"Successfully injected into {file_path}")

inject_payload('frontend/index.html')
inject_payload('frontend/index.min.html')

